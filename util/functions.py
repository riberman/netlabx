from tkinter import Entry, Text
from datetime import datetime
from util.constants import *
import screeninfo

def copy_all_text_in_input(event):
    if isinstance(event.widget, Entry):
        event.widget.select_range(0, 'end')
        event.widget.icursor('end')
    elif isinstance(event.widget, Text):
        event.widget.tag_add("sel","1.0","end")
    else:
        print("Não foi possível copiar o texto.")

def get_file_name_from_date():
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%d-%m-%Y-%H-%M")
    return current_time

def get_screensize_primary_monitor():
    for screen in screeninfo.get_monitors():
        if screen.is_primary:
            return screen.width, screen.height

def set_app_file_name(root, file_name):
    root.title("{} - {} | {}".format(APP_NAME, CODE_VERSION, file_name))
