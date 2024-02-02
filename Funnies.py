try:
    import kivy
except ImportError: # If Kivy isn't installed, it raises an ImportError that it's isn't installed and gives instructions how to install
    raise ImportError('Kivy not installed. Please read the README.md to properly run the program. ')
try:
    from kivy.app import App
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.button import Button
    from kivy.uix.image import Image
    from kivy.uix.label import Label
    from kivy.graphics.texture import Texture

    import cv2
    import numpy as np
    from kivy.clock import Clock
    from deepface import DeepFace
    import threading
    import tempfile
except ImportError:
    raise ImportError('Necessary modules not installed. Please read the READEME.md to properly run the program. ')

class MoodDetectionApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        # Button to capture mood
        self.capture_button = Button(text="Capture Mood", on_press=self.capture_mood)
        self.layout.add_widget(self.capture_button)

        # Image widget for displaying the processed frame
        self.processed_image = Image(size=(640, 480))
        self.layout.add_widget(self.processed_image)

        # Label widget for displaying the detected emotion
        self.emotion_label = Label(text='', font_size=20, markup=True)
        self.layout.add_widget(self.emotion_label)

        # Load pre-trained emotion detection model (DeepFace)
        self.detected_emotion = None

        # Flag to ensure mood is captured only once per face
        self.mood_captured = False

        # Initialize OpenCV Haarcascades for face detection
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Capture frame from the default camera
        self.cap = cv2.VideoCapture(0)

        # Clock to schedule face detection
        Clock.schedule_interval(self.detect_face, 1.0 / 30.0)  # Every 33 milliseconds (30 FPS)

        return self.layout

    def capture_mood(self, instance):
        if self.detected_emotion and not self.mood_captured:
            print(f"Detected Mood: {self.detected_emotion}")
            self.mood_captured = True
        elif not self.detected_emotion:
            print("No face detected. Please try again.")
        elif self.mood_captured:
            print("Mood already captured. Wait for the next face.")

    def detect_face(self, dt):
        # Read frame from the camera
        ret, frame = self.cap.read()

        if ret:
            # Resize the frame for faster processing
            frame = cv2.resize(frame, (640, 480))

            # Convert the frame to grayscale for face detection
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Perform face detection
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

            for (x, y, w, h) in faces:
                # Extract the region of interest (ROI) for emotion detection
                roi_gray = gray[y:y + h, x:x + w]

                # Perform emotion analysis on the face in a separate thread
                threading.Thread(target=self.analyze_emotion_async, args=(roi_gray,), daemon=True).start()

                # Draw a rectangle around the detected face
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Display the processed frame using the Image widget
            texture = self.create_texture(frame)
            self.processed_image.texture = texture

    def analyze_emotion_async(self, face_image):
        detected_emotion = self.analyze_emotion(face_image)
        Clock.schedule_once(lambda dt: self.update_detected_emotion(detected_emotion))

    def analyze_emotion(self, face_image):
        # Save the ROI as a temporary image file
        temp_img_path = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False).name
        cv2.imwrite(temp_img_path, face_image)

        try:
            # Perform emotion prediction using the DeepFace model
            result = DeepFace.analyze(img_path=temp_img_path, actions=['emotion'], enforce_detection=False)

            if isinstance(result, list):
                # For older versions of DeepFace that return a list
                detected_emotion = result[0]['dominant_emotion']
            elif isinstance(result, dict):
                # For newer versions of DeepFace that return a dictionary
                detected_emotion = result['dominant_emotion']
            else:
                raise ValueError("Unexpected result type from DeepFace")

            return detected_emotion
        finally:
            # Remove the temporary image file
            import os
            os.remove(temp_img_path)

    def update_detected_emotion(self, emotion):
        self.detected_emotion = emotion
        self.emotion_label.text = f"[b]{emotion}[/b]"

    def create_texture(self, cv_frame):
        # Rotate the frame by 180 degrees
        rotated_frame = cv2.rotate(cv_frame, cv2.ROTATE_180)

        # Convert OpenCV BGR frame to Kivy texture
        texture = Texture.create(size=(rotated_frame.shape[1], rotated_frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(rotated_frame.tobytes(), colorfmt='bgr', bufferfmt='ubyte')

        return texture

    def on_stop(self):
        # Release the camera when the app is stopped
        self.cap.release()
        super().on_stop()

if __name__ == '__main__':  # Checks if file is being run, if it is, then it runs the App, or if it's being used as a module, doesn't run
    MoodDetectionApp().run()
