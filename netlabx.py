#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://www.devmedia.com.br/tkinter-interfaces-graficas-em-python/33956
from Tkinter import *
from PIL import Image, ImageTk
import sys
import tkMessageBox
reload(sys)
sys.setdefaultencoding('utf-8')
APP_NAME = "NetLabX"
CODE_VERSION = "v1.0.0"

class ScreenElement:
    def __init__(self, element, id):
        self.element = element
        self.id = id

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

        self.temp["photo-image"] = PhotoImage(file = "icons/desktop-back.png")
        newElement = ScreenElement(Button(self.equipment), self.getRandomId)
        self.menuElements[newElement.id] = newElement
        self.menuElements[newElement.id].element["font"] = ("Calibri", "8")
        self.menuElements[newElement.id].element["width"] = 65
        self.menuElements[newElement.id].element["height"] = 65
        self.menuElements[newElement.id].element["image"] = self.temp["photo-image"]
        self.menuElements[newElement.id].element["text"] = "Desktop"
        self.menuElements[newElement.id].element["command"] = self.test(newElement.id)
        self.menuElements[newElement.id].element.image = self.temp["photo-image"]
        self.menuElements[newElement.id].element.pack()

        self.temp["photo-image"] = PhotoImage(file = "icons/laptop-back.png")
        self.laptop = Button(self.equipment)
        self.laptop["font"] = ("Calibri", "8")
        self.laptop["width"] = 65
        self.laptop["height"] = 65
        self.laptop["image"] = self.temp["photo-image"]
        self.laptop["text"] = "Laptop"
        self.laptop["command"] = self.test
        self.laptop.image = self.temp["photo-image"]
        self.laptop.pack()

        self.temp["photo-image"] = PhotoImage(file = "icons/dns-back.png")
        self.dns = Button(self.equipment)
        self.dns["font"] = ("Calibri", "8")
        self.dns["width"] = 65
        self.dns["height"] = 65
        self.dns["image"] = self.temp["photo-image"]
        self.dns["text"] = "DNS Server"
        self.dns["command"] = self.test
        self.dns.image = self.temp["photo-image"]
        self.dns.pack()

        self.temp["photo-image"] = PhotoImage(file = "icons/web-back.png")
        self.web = Button(self.equipment)
        self.web["font"] = ("Calibri", "8")
        self.web["width"] = 65
        self.web["height"] = 65
        self.web["image"] = self.temp["photo-image"]
        self.web["text"] = "Web Server"
        self.web["command"] = self.test
        self.web.image = self.temp["photo-image"]
        self.web.pack()

        self.temp["photo-image"] = PhotoImage(file = "icons/router-back.png")
        self.router = Button(self.equipment)
        self.router["font"] = ("Calibri", "8")
        self.router["width"] = 65
        self.router["height"] = 65
        self.router["image"] = self.temp["photo-image"]
        self.router["text"] = "Router"
        self.router["command"] = self.test
        self.router.image = self.temp["photo-image"]
        self.router.pack()

        self.temp["photo-image"] = PhotoImage(file = "icons/switch-back.png")
        self.switch = Button(self.equipment)
        self.switch["font"] = ("Calibri", "8")
        self.switch["width"] = 65
        self.switch["height"] = 65
        self.switch["image"] = self.temp["photo-image"]
        self.switch["text"] = "Switch"
        self.switch["command"] = self.test
        self.switch.image = self.temp["photo-image"]
        self.switch.pack()

        self.temp["photo-image"] = PhotoImage(file = "icons/wireshark-back.png")
        self.wireshark = Button(self.equipment)
        self.wireshark["font"] = ("Calibri", "8")
        self.wireshark["width"] = 65
        self.wireshark["height"] = 65
        self.wireshark["image"] = self.temp["photo-image"]
        self.wireshark["text"] = "Wireshark"
        self.wireshark["command"] = self.test
        self.wireshark.image = self.temp["photo-image"]
        self.wireshark.pack()

        #remove temp
        del self.temp["photo-image"]
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

    def test(self, teste):
        print self.menuElements[teste].element["text"]
        print "test button"

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
