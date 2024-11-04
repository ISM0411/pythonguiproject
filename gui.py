import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in to-do")
input_box = sg.InputText(tooltip="enter todo", key="todosi")
list_box = sg.Listbox(values=functions.get_readfile(), key="todos",
                      enable_events=True, size=[45, 10])
                   #   size=[45, 20])
edit_button = sg.Button("Edit")
add_button = sg.Button("add")

windows = sg.Window('My To-Do App',
                    layout=[[label], [input_box, add_button],[list_box, edit_button]],
                             font=('Helvetica', 15))

while True:
    event, values = windows.read()
    print(event)
    print(values)
    match event:
        case "add":
            todos = functions.get_readfile()
            new_todos = values['todosi'] + "\n"
            todos.append(new_todos)
            functions.get_writefile(todos)
            windows['todos'].update(values=todos)
        case "Edit":
            list_to_update = values['todos'][0]
            new_todos = values['todosi']

            todos = functions.get_readfile()
            index = todos.index(list_to_update)
            todos[index] = new_todos
            functions.get_writefile(todos)
            windows['todos'].update(values=todos)  #updating the value of list box with value of todossss file which is reading the file throughh function
        case "todos":
            windows['todosi'].update(value=values['todos'][0])

        case sg.WINDOW_CLOSED:
            break


windows.close()