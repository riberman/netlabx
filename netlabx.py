#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
from PIL import Image, ImageTk
import sys
import tkMessageBox
import Tkinter as tk
import json
reload(sys)
sys.setdefaultencoding('utf-8')

#Default Values
APP_NAME = "NetLabX"
CODE_VERSION = "v1.0.0"
SCREEN_ICON_SIZE = 65

#Load config json
with open('config.conf') as json_file:
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
        self.element.image = self.photoImage
        self.element.pack()
        CreateToolTip(self.element, text = 'Criar novo ' + self.element["text"])

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
                       background='yellow', relief='solid', borderwidth=1,
                       font=("times", "8", "normal"))
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

        self.imgDesk = PhotoImage(file = "icons/desktop-back.png")
        # put gif image on canvas
        # pic's upper left corner (NW) on the canvas is at x=50 y=10
        items = []
        items.append(self.dragarea.create_image(0, 0, image=self.imgDesk, anchor='nw'))
        self.dragarea.coords(items[0], 500, 150)

        testeOne = self.dragarea.create_rectangle(0, 0, 100, 30, fill="grey40", outline="grey60")
        testeTwo = self.dragarea.create_text(50, 15, text="click")
        self.dragarea.tag_bind(testeOne, "<Button-1>", self.clicked)
        self.dragarea.tag_bind(testeTwo, "<Button-1>", self.clicked)

        self.dragarea.create_image(100, 100, image=self.imgDesk, anchor='nw')
        self.dragarea.create_image(200, 200, image=self.imgDesk, anchor='nw')

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
            print screenElement['id']
            self.menuElements[screenElement['id']] = ScreenElement(Button(self.equipment), screenElement)
            print self.menuElements[screenElement['id']].id
            self.menuElements[screenElement['id']].element["command"] = lambda: self.test(self.menuElements[screenElement['id']])
        #end item
        self.equipment.pack()

        #self.mensagem = Label(self.quartoContainer, text="", font=self.defaultFont)
        #self.mensagem.pack()

    #Metodo verificar senha
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "patrick" and senha == "123":
            self.mensagem["text"] = "Autenticado"
        else:
            self.mensagem["text"] = "Erro na autenticação"

    def open(self):
        print "Open"

    def save(self):
        print "Save"

    def quit(self):
        print "Quit"

    def about(self):
        tkMessageBox.showinfo("About", APP_NAME + " " + CODE_VERSION + "\n\nPatrick Ferro Ribeiro")

    def test(self, element):
        print element.id
        print element.element["text"]

    def clicked(self, test):
        print "pressed"

    def getRandomId(self):
        id = self.counter
        self.counter = self.counter + 1
        return str(id)

root = Tk(className=APP_NAME)
root.title(APP_NAME + " - " + CODE_VERSION)
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='icons/main-icon.gif'))
Application(root)
root.mainloop()
