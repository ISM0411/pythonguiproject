from struct import pack_into
from unittest.mock import right
from zipfile import ZIP_DEFLATED
import os
import FreeSimpleGUI as sg
import zipfile

from FreeSimpleGUI import Window, theme, button_color_to_tuple
from numpy.ma.core import left_shift

label_1 = sg.Text("select files", s=10, justification=right, text_color="white", background_color="DarkGreen")
input_box1 = sg.InputText(tooltip="choose file", key="files")
file_select_button = sg.FilesBrowse("choose", key="file_choose", button_color="violet")

label_2 = sg.Text("target folder", s=10, justification=right, text_color="white", background_color="DarkGreen")
input_box2 = sg.InputText(tooltip="target folder to compress", key="folder")
folder_select_button = sg.FolderBrowse("choose", key="folder_choose", button_color="violet")

compress_button = sg.Button("compress", key="compress", s=7, expand_x=True, button_color="red")

default_filename = sg.InputText(tooltip="Default file name", key="dfname", pad=(88, 40), justification=right, default_text="compressed.zip", s=18)

windows = sg.Window("File Compressor",
                    layout = [[label_1, input_box1, file_select_button],
                              [label_2, input_box2, folder_select_button],
                              [sg.Exit(button_color="tomato"), default_filename, compress_button]],
                               font=('Helvetica', 12), background_color="DarkGreen")

while True:
   events, values = windows.read()
   print(events)
   print(values)

   match events:
       case "compress":
           filepath = values['files'].split(";")
           target_location = values['folder']
           target_location = f"{target_location}/compressed.zip"
           try:
               with zipfile.ZipFile(target_location, 'w', ZIP_DEFLATED) as Zipf:
                   for files in filepath:
                       Zipf.write(files, os.path.basename(files))
                       sg.popup_no_titlebar("File is compressed ! :)")
           except OSError as err:
               message = (f"Please select the correct folder Path \n"
                          f"or check for file permission: \n"
                          f"{err}")
               sg.popup_error(message, title="Error", button_color=("white", "blue"), font=("Arial", 12, "bold"))
       case sg.WINDOW_CLOSED | "Exit" :
           break




windows.close()