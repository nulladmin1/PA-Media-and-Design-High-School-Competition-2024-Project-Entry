try:
    import flet as ft # Don't forget to pip
except ImportError:
    raise ImportError('Flet not installed. ')

def main(page): #kinda ovious 
    def add_clicked(e): #button comand
        page.add(ft.Checkbox(label=new_task.value)) #adds a checkbox gui
        new_task.value = "" # Clears the text in the new_task text field
        new_task.focus() #This means that after clicking the "Add" button, the cursor focus is moved to the new_task
        new_task.update() #upate page

    new_task = ft.TextField(hint_text="Whats needs to be done?", width=300) #basicly prints on the screen
    page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)])) #button command

ft.app(target=main)# setting as app