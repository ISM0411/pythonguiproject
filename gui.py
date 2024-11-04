import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in to-do")
input_box = sg.InputText(tooltip="enter todo", key="todosi")
add_button = sg.Button("add")

windows = sg.Window('My To-Do App',
                    layout=[[label, input_box], [add_button]],
                    font=('Helvetica', 15))

while True:
    event, values = windows.read()
    match event:
        case "add":
            todos = functions.get_readfile()
            new_todos = values['todosi'] + "\n"
            todos.append(new_todos)
            functions.get_writefile(todos)
        case sg.WINDOW_CLOSED:
            break


windows.close()