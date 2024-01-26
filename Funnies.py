try: # Checks if Kivy is installed
    from kivy.app import App # Imports the Kivy module, a cross-platform GUI-framework for creating programs using Python
    from kivy.uix.widget import Widget
except ImportError: # If Kivy isn't installed, it raises an ImportError that it's isn't installed and gives instructions how to install
    raise ImportError('Kivy not installed. Please run:\npip -r requirements.txt\n(Recommended to use venv or conda.)')


class RecommenderApp(App):
    pass

if __name__ == "__main__":
    RecommenderApp().run()
