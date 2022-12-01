#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import Tk, Button, Label, Frame, Canvas, PhotoImage, Menu, Toplevel
from PIL import Image, ImageTk
from tkinter import messagebox as tkMessageBox
import json
from model.screendevice import ScreenDevice
from model.screendevicemenu import ScreenDeviceMenu
from model.tkinterbase import TkInterBase
from model.tooltip import ToolTip
from util.constants import *
from util.functions import get_file_name_from_date, get_screensize_primary_monitor, set_app_file_name
from tkinter.filedialog import asksaveasfile, askopenfilename
import sys

#Load config json
with open('devices.conf') as json_file:
    data = json.load(json_file)

class Application:
    def __init__(self, master):
        #main screen
        width_dragarea, height_dragarea = get_screensize_primary_monitor()
        root.attributes('-zoomed', True)
        self.main_area = Frame(root, bg='#CCC', width=width_dragarea, height=height_dragarea)
        self.drag_area = Canvas(self.main_area, width=width_dragarea-75, height=height_dragarea, bg='white')
        self.drag_area.pack(side='left', anchor='n')
        self.main_area.pack(expand=True, fill='both', side='right')

        DEFAULT_IMG_ICONS_DEVICE = {}

        IMG_CONFIG = Image.open("icons/config-back.png")
        IMG_RESIZED_CONFIG = IMG_CONFIG.resize((25, 25), Image.Resampling.LANCZOS)
        DEFAULT_IMG_ICONS_DEVICE['PT_IMG_CONFIG'] = ImageTk.PhotoImage(IMG_RESIZED_CONFIG)

        IMG_SHELL = Image.open("icons/console.png")
        IMG_RESIZED_SHELL = IMG_SHELL.resize((20, 20), Image.Resampling.LANCZOS)
        DEFAULT_IMG_ICONS_DEVICE['PT_IMG_SHELL'] = ImageTk.PhotoImage(IMG_RESIZED_SHELL)

        IMG_INTERFACE = Image.open("icons/interface.png")
        IMG_RESIZED_INTERFACE = IMG_INTERFACE.resize((20, 20), Image.Resampling.LANCZOS)
        DEFAULT_IMG_ICONS_DEVICE['PT_IMG_INTERFACE'] = ImageTk.PhotoImage(IMG_RESIZED_INTERFACE)

        IMG_ON = Image.open("icons/on.png")
        IMG_RESIZED_ON = IMG_ON.resize((20, 20), Image.Resampling.LANCZOS)
        DEFAULT_IMG_ICONS_DEVICE['PT_IMG_ON'] = ImageTk.PhotoImage(IMG_RESIZED_ON)

        IMG_OFF = Image.open("icons/off.png")
        IMG_RESIZED_OFF = IMG_OFF.resize((20, 20), Image.Resampling.LANCZOS)
        DEFAULT_IMG_ICONS_DEVICE['PT_IMG_OFF'] = ImageTk.PhotoImage(IMG_RESIZED_OFF)

        IMG_CLOSE = Image.open("icons/close.png")
        IMG_RESIZED_CLOSE = IMG_CLOSE.resize((20, 20), Image.Resampling.LANCZOS)
        DEFAULT_IMG_ICONS_DEVICE['PT_IMG_CLOSE'] = ImageTk.PhotoImage(IMG_RESIZED_CLOSE)

        IMG_PYTHON = Image.open("icons/python.png")
        IMG_RESIZED_PYTHON = IMG_PYTHON.resize((20, 20), Image.Resampling.LANCZOS)
        DEFAULT_IMG_ICONS_DEVICE['PT_IMG_PYTHON'] = ImageTk.PhotoImage(IMG_RESIZED_PYTHON)

        # Init main Values
        self.tkinter_base = TkInterBase(self.drag_area, root, DEFAULT_IMG_ICONS_DEVICE)

        #new menubar
        self.menubar = Menu(root)

        # create a pulldown menu, and add it to the menu bar
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Novo", command=self.new)
        self.filemenu.add_command(label="Abrir", command=self.open)
        self.filemenu.add_command(label="Salvar", command=self.save)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Sair", command=self.quit)
        root.protocol('WM_DELETE_WINDOW', self.quit)
        self.menubar.add_cascade(label="Arquivo", menu=self.filemenu)

        # create a pulldown menu
        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="Sobre", command=self.about)
        self.menubar.add_cascade(label="Ajuda", menu=self.helpmenu)

        # display the menu
        root.config(menu=self.menubar)

        # set default font
        self.defaultFont = ("Arial", "10")

        # container equipments
        self.frame_equipment = Frame(master)

        #Item in frame
        for screen_device_menu in data['screen-elements']:
            self.tkinter_base.menuElements[screen_device_menu['id']] = ScreenDeviceMenu(Button(self.frame_equipment), screen_device_menu)
            self.tkinter_base.menuElements[screen_device_menu['id']].frame_equipment["command"] = lambda device_menu_id=screen_device_menu['id']: self.create_device(device_menu_id)
        #end item
        self.frame_equipment.pack()

    def new(self):
        reponse = tkMessageBox.askquestion(title="Novo", message="O laborátorio não salvo será perdido, deseja continuar?", icon='warning')

        if reponse == "yes":
            self.tkinter_base.clear()
            self.drag_area.delete('all')

    def save(self):
        dict = self.tkinter_base.to_dict()
        if (dict["devices"]):
            file_name = "projeto{}.netlabx".format(get_file_name_from_date())
            file = asksaveasfile(initialfile = file_name, defaultextension=".netlabx",filetypes=[("Projetos NetLabX","*.netlabx")])
            if (file):
                file.write(json.dumps(dict))
                set_app_file_name(root, file_name)
        else:
            tkMessageBox.showwarning("Atenção", "Não foi possível salvar!")

    def open(self):
        self.tkinter_base.clear()
        self.drag_area.delete('all')
        file_name = askopenfilename(defaultextension=".netlabx")
        set_app_file_name(root, file_name)
        with open(file_name) as file:
            data = json.load(file)
        for device in data['devices']:
            self.create_device(device["device-id"], device["id"], device["name"], device["x-widget"], device["y-widget"], device["script-on"], device["script-off"], device["script-open"], device["script-config"], device["script-close"], device["script-extra"])
        for connection in data['connections']:
            self.draw_line(connection["id"])

    def quit(self):
        reponse = tkMessageBox.askquestion(title="Sair", message="Deseja realmente sair?")

        if reponse == "yes":
            sys.exit()

    def about(self):
        tkMessageBox.showinfo("Sobre", "{} {}\n\nPatrick Ferro Ribeiro".format(APP_NAME, CODE_VERSION))

    def create_device(self, device_menu_id, id=None, name=None, x_widget=80, y_widget=50, script_on=None, script_off=None, script_open=None, script_config=None, script_close=None, script_extra=None):
        device = ScreenDevice(device_menu_id, self.tkinter_base, id, name, x_widget, y_widget, script_on, script_off, script_open, script_config, script_close, script_extra)
        self.tkinter_base.devices_list[device.tagGenerated] = device

    def draw_line(self, tag_line):
        devices_id = tag_line.split("/")
        x_widget1, y_widget1 = self.tkinter_base.drag_area.coords(devices_id[0])
        x_widget2, y_widget2 = self.tkinter_base.drag_area.coords(devices_id[1])
        x_widget1 = x_widget1 + 10
        y_widget1 = y_widget1 + 10
        x_widget2 = x_widget2 + 10
        y_widget2 = y_widget2 + 10
        self.tkinter_base.connections_list[tag_line] = self.tkinter_base.drag_area.create_line(x_widget1 - 15, y_widget1, x_widget2 - 15, y_widget2, fill='black', width=5, tag=tag_line)

        buttonClose = Button(width=20, height=20, command= lambda arg=tag_line : self.buttonClose(arg), image=self.tkinter_base.icons['PT_IMG_CLOSE'])
        ToolTip(buttonClose, text = 'Fechar')
        self.tkinter_base.drag_area.create_window((x_widget1 + x_widget2)/2, (y_widget1 + y_widget2)/2, window=buttonClose, tag=tag_line + "btn_close")

        self.tkinter_base.drag_area.tag_lower(self.tkinter_base.connections_list[tag_line])

    def buttonClose(self, tag):
        self.tkinter_base.drag_area.delete(tag)
        self.tkinter_base.drag_area.delete(tag + "btn_close")
        self.tkinter_base.remove_line_by_tag(tag)
        self.tkinter_base.devices_list.pop(tag, None)

    def handle_keypress(event):
        input1.delete(0, DEL)

root = Tk(className=APP_NAME)
root.title(APP_NAME + " - " + CODE_VERSION)
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='icons/main-icon.gif'))
Application(root)
root.focus_set()
root.mainloop()
