try: # Checks if Flet is installed
    import flet as ft # Imports the flet module, a framework for creating programs using Python in the flutter SDK
except ImportError: # If flet isn't installed, it raises an ImportError that it's isn't installed and gives instructions how to install
    raise ImportError('Flet not installed. Please run:\npip -r requirements.txt\n(Recommended to use venv or conda.)')

def main(page): # Creates a main function; needed for flet
    def add_clicked(e): # Button comand
        page.add(ft.Checkbox(label=new_task.value)) # Adds a checkbox in the GUI
        new_task.value = "" # Clears the text in the new_task text field
        new_task.focus() # This means that after clicking the "Add" button, the cursor focus is moved to the new_task
        new_task.update() # Updates the page

    new_task = ft.TextField(hint_text="Whats needs to be done?", width=300) #basicly prints on the screen
    page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)])) #button command

ft.app(target=main)# Sets the main function as a Flet app