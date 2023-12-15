import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
Input_box = sg.InputText(tooltip="Enter a Todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window('My todo App',
                   layout=[[label, Input_box,add_button]],
                   font=('Mulish', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WINDOW_CLOSED:
            break

window.close()