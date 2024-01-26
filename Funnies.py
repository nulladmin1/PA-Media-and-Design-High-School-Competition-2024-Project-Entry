try: # Checks if Kivy is installed
    from kivy.app import App # Imports from the Kivy module, a cross-platform GUI-framework for creating programs using Python
    from kivy.uix.widget import Widget
except ImportError: # If Kivy isn't installed, it raises an ImportError that it's isn't installed and gives instructions how to install
    raise ImportError('Kivy not installed. Please read the README.md to properly run the program. ')


class RecommenderApp(App): # Instantaniates Class RecommenderApp for a Kivy App
    pass

if __name__ == "__main__": # Checks if file is being run, if it is, then it runs the App, or if it's being used as a module, doesn't run
    RecommenderApp().run()
