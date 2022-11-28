#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import Tk, Button, Label, Frame, Canvas, PhotoImage, Menu
from PIL import Image, ImageTk
from tkinter import messagebox as tkMessageBox
import json
from model.screendevice import ScreenDevice
from model.screendevicemenu import ScreenDeviceMenu
from model.tkinterbase import TkInterBase
from model.tooltip import ToolTip
from util.constants import *
import screeninfo

#Load config json
with open('devices.conf') as json_file:
    data = json.load(json_file)

def get_screensize_primary_monitor():
    for screen in screeninfo.get_monitors():
        if screen.is_primary:
            return screen.width, screen.height

class Application:
    def __init__(self, master):
        #main screen
        width_dragarea, height_dragarea = get_screensize_primary_monitor()
        root.attributes('-zoomed', True)
        self.mainarea = Frame(root, bg='#CCC', width=width_dragarea, height=height_dragarea)
        self.dragarea = Canvas(self.mainarea, width=width_dragarea-75, height=height_dragarea, bg='white')
        self.dragarea.pack(side='left', anchor='n')
        self.mainarea.pack(expand=True, fill='both', side='right')

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

        # Init Values
        self.temp = {}
        self.menuElements = {}

        self.tkinter_base = TkInterBase(self.dragarea, root, DEFAULT_IMG_ICONS_DEVICE)

        #new menubar
        self.menubar = Menu(root)

        # create a pulldown menu, and add it to the menu bar
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Abrir", command=self.open)
        self.filemenu.add_command(label="Salvar", command=self.save)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Sair", command=root.quit)
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
        self.equipment = Frame(master)

        #Item in frame
        for screenDeviceMenu in data['screen-elements']:
            self.menuElements[screenDeviceMenu['id']] = ScreenDeviceMenu(Button(self.equipment), screenDeviceMenu)
            self.menuElements[screenDeviceMenu['id']].device["command"] = lambda index=screenDeviceMenu['id']: self.createDevice(self.menuElements[index])
        #end item
        self.equipment.pack()

    def get_random_id(self):
        id = self.tkinter_base.counter
        self.tkinter_base.counter = self.tkinter_base.counter + 1
        return str(id)

    def open(self):
        print("Open")

    def save(self):
        print("Save")

    def quit(self):
        prin("Quit")

    def about(self):
        tkMessageBox.showinfo("Sobre", "{} {}\n\nPatrick Ferro Ribeiro".format(APP_NAME, CODE_VERSION))

    def createDevice(self, deviceMenu):
        ScreenDevice(deviceMenu, self.tkinter_base, self.get_random_id())

    def handle_keypress(event):
        input1.delete(0, DEL)

root = Tk(className=APP_NAME)
root.title(APP_NAME + " - " + CODE_VERSION)
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='icons/main-icon.gif'))
Application(root)
root.focus_set()
root.mainloop()
