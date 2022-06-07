#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from PIL import Image, ImageTk
# import sys
from tkinter import messagebox as tkMessageBox
# import Tkinter as tk
import tkinter as tk
import json
# import importlib
# importlib.reload(sys)
# sys.setdefaultencoding('utf-8')

#Default Values
APP_NAME = "NetLabX"
CODE_VERSION = "v1.0.0"
SCREEN_ICON_SIZE = 65

#Load config json
with open('devices.conf') as json_file:
    data = json.load(json_file)

#Menu Button Object
class ScreenElement:
    def __init__(self, element, data):
        self.element = element
        self.id = data['id']
        self.photoImage = PhotoImage(file = data['logo'])
        self.element["width"] = SCREEN_ICON_SIZE
        self.element["height"] = SCREEN_ICON_SIZE
        self.element["image"] = self.photoImage
        self.element["text"] = data['name']
        #self.element["command"] = lambda: self.test(data)
        self.element.image = self.photoImage
        self.element.pack()
        CreateToolTip(self.element, text = 'Criar novo ' + self.element["text"])

    def __repr__(self):
        return "ScreenElement id:% s elementText:% s" % (self.id, self.element["text"])

#CreateToolTip
class CreateToolTip(object):
    '''
    create a tooltip for a given widget
    '''
    def __init__(self, widget, text='widget info'):
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.close)

    def enter(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + SCREEN_ICON_SIZE
        y += self.widget.winfo_rooty() + SCREEN_ICON_SIZE
        # creates a toplevel window
        self.tw = tk.Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',
                       background='#3498db', relief='solid', borderwidth=1,
                       font=("times", "9", "normal"))
        label.pack(ipadx=1)

    def close(self, event=None):
        if self.tw:
            self.tw.destroy()

#CreateToolTipOption
class CreateToolTipOptions(object):
    '''
    create a tooltip for a given widget
    '''
    def __init__(self, widget, text='widget info'):
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.close)

    def enter(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25
        # creates a toplevel window
        self.tw = tk.Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',
                       background='#3498db', relief='solid', borderwidth=1,
                       font=("times", "9", "normal"))
        label.pack(ipadx=1)

    def close(self, event=None):
        if self.tw:
            self.tw.destroy()

class Application:
    def __init__(self, master):
        #main screen
        #width_dragarea = root.winfo_screenwidth() - 70
        #height_dragarea = root.winfo_screenheight()
        self.mainarea = Frame(root, bg='#CCC', width=1024, height=720)
        self.dragarea = Canvas(self.mainarea, width=1000, height=500, bg='white')
        self.dragarea.pack(side='left', anchor='n')
        self.mainarea.pack(expand=True, fill='both', side='right')

        # self.imgDesk = PhotoImage(file = "icons/desktop-back.png")
        # put gif image on canvas
        # pic's upper left corner (NW) on the canvas is at x=50 y=10
        # items = []
        # items.append(self.dragarea.create_image(0, 0, image=self.imgDesk, anchor='nw'))
        # self.dragarea.coords(items[0], 500, 150)

        # testeOne = self.dragarea.create_rectangle(0, 0, 100, 30, fill="grey40", outline="grey60")
        # testeTwo = self.dragarea.create_text(50, 15, text="click")
        # self.dragarea.tag_bind(testeOne, "<Button-1>", self.clicked)
        # self.dragarea.tag_bind(testeTwo, "<Button-1>", self.clicked)

        # self.dragarea.create_image(100, 100, image=self.imgDesk, anchor='nw')
        # self.dragarea.create_image(200, 200, image=self.imgDesk, anchor='nw')

        #self.dragarea.create_oval(175,175,100,100,fill='red',width=1)

        #new menubar
        self.menubar = Menu(root)

        # create a pulldown menu, and add it to the menu bar
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Open", command=self.open)
        self.filemenu.add_command(label="Save", command=self.save)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=root.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        # create a pulldown menu
        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About", command=self.about)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

        # display the menu
        root.config(menu=self.menubar)

        # set default font
        self.defaultFont = ("Arial", "10")

        # container equipments
        self.equipment = Frame(master)

        # Init Values
        self.temp = {}
        self.counter = 0
        self.menuElements = {}

        #Item in frame
        for screenElement in data['screen-elements']:
            self.menuElements[screenElement['id']] = ScreenElement(Button(self.equipment), screenElement)
            self.menuElements[screenElement['id']].element["command"] = lambda index=screenElement['id']: self.createDevice(self.menuElements[index])
        #end item
        self.equipment.pack()

        #self.mensagem = Label(self.quartoContainer, text="", font=self.defaultFont)
        #self.mensagem.pack()

    def open(self):
        print("Open")

    def save(self):
        print("Save")

    def quit(self):
        prin("Quit")

    def about(self):
        tkMessageBox.showinfo("About", APP_NAME + " " + CODE_VERSION + "\n\nPatrick Ferro Ribeiro")

    def createDevice(self, element):
        # print(element.id)
        # print(element.element["text"])
        # button = Button(text="C")
        # button.bind("<Button-1>", self.clicked(element.id))
        self.imgConfig = Image.open("icons/config-back.png")
        self.imgResizedConfig = self.imgConfig.resize((25, 25), Image.Resampling.LANCZOS)
        self.ptImgConfig = ImageTk.PhotoImage(self.imgResizedConfig)

        self.imgShell = Image.open("icons/console.png")
        self.imgResizedShell = self.imgShell.resize((20, 20), Image.Resampling.LANCZOS)
        self.ptImgShell = ImageTk.PhotoImage(self.imgResizedShell)

        self.imgOn = Image.open("icons/on.png")
        self.imgResizedOn = self.imgOn.resize((20, 20), Image.Resampling.LANCZOS)
        self.ptImgOn = ImageTk.PhotoImage(self.imgResizedOn)

        self.imgOff = Image.open("icons/off.png")
        self.imgResizedOff = self.imgOff.resize((20, 20), Image.Resampling.LANCZOS)
        self.ptImgOff = ImageTk.PhotoImage(self.imgResizedOff)

        self.testeImg = PhotoImage(width=100, height=100, file = "icons/config-back.png")
        self.testeImg.subsample(200, 200)

        button1 = Button(width=20, height=20, command= lambda arg=element.id : self.button1(arg), image=self.ptImgShell)
        CreateToolTipOptions(button1, text = 'Console')

        button2 = Button(width=20, height=20, command= lambda arg=element.id : self.button2(arg), image=self.ptImgConfig)
        CreateToolTipOptions(button2, text = 'Configurações')

        button3 = Button(width=20, height=20, command= lambda arg=element.id : self.button3(arg), image=self.ptImgOn)
        CreateToolTipOptions(button3, text = 'Ligar')

        button4 = Button(width=20, height=20, command= lambda arg=element.id : self.button4(arg), image=self.ptImgOff)
        button4.bind("<B1-Motion>", self.drag)
        CreateToolTipOptions(button4, text = 'Desligar')

        label = Label(bg='white', image=element.photoImage)
        label.bind("<B1-Motion>", self.drag)

        # button2.bind("<Button-1>", lambda arg=element.id : self.clicked(arg))
        # button2["image"] = PhotoImage(file = "icons/config-back.png")
        # self.dragarea.create_window(155, 65,window=button)
        position_x = 50
        position_y = 25
        # self.dragarea.create_image(position_x, position_y, image=element.photoImage, anchor='nw')
        self.dragarea.create_window(position_x, position_y, window=label)
        # self.TEsteIMGHow = element.photoImage
        # self.dragarea.tag_bind(test, "<B1-Motion>", self.drag(test))
        self.teste1 = self.dragarea.create_window(position_x - 10, position_y + 10, window=button1)
        self.teste2 = self.dragarea.create_window(position_x + 85, position_y + 10, window=button2)
        self.teste3 = self.dragarea.create_window(position_x + 85, position_y + 40, window=button3)
        self.teste4 = self.dragarea.create_window(position_x + 85, position_y + 70, window=button4)

        # self.dragarea.create_image(position_x + 70, position_y, image=self.newTesteImg, anchor='nw')
        # self.dragarea.create_image(position_x + 70, position_y + 25, image=self.newTesteImg, anchor='nw')
        # self.dragarea.create_image(position_x + 70, position_y + 50, image=self.newTesteImg, anchor='nw')
        # self.dragarea.create_image(position_x - 25, position_y, image=self.newTesteImg, anchor='nw')

    def clicked(self):
        print("pressed1")

    def button1(self, test):
        print("BTN1 ID: {}".format(test))

    def button2(self, test):
        print("BTN2 ID: {}".format(test))

    def button3(self, test):
        print("BTN3 ID: {}".format(test))

    def button4(self, test):
        print("BTN4 ID: {}".format(test))

    def drag(self, event):
        # print(vars(event))
        event.widget.place(x=event.x_root, y=event.y_root)
        self.teste1.place(x=event.x_root - 10, y=event.y_root + 10)
        # self.TEsteIMGHow.place(x=event.x_root, y=event.y_root,anchor=E)

    def getRandomId(self):
        id = self.counter
        self.counter = self.counter + 1
        return str(id)

root = Tk(className=APP_NAME)
root.title(APP_NAME + " - " + CODE_VERSION)
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='icons/main-icon.gif'))
Application(root)
root.mainloop()
