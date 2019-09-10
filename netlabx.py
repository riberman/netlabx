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
CODE_VERSION = "1.0.0"

class Application:
    def __init__(self, master):
        #main screen
        #width_dragarea = root.winfo_screenwidth() - 70
        #height_dragarea = root.winfo_screenheight()
        self.mainarea = Frame(root, bg='#CCC', width=1024, height=720)
        self.dragarea = Canvas(self.mainarea, width=1000, height=500, bg='white')
        self.dragarea.pack(side='left', anchor='n')
        #self.dragarea.create_oval(175,175,100,100,fill='red',width=1)
        self.mainarea.pack(expand=True, fill='both', side='right')

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
        #Item in frame
        desktopIcon = PhotoImage(file = "icons/desktop-back.png")
        self.desktop = Button(self.equipment)
        self.desktop["font"] = ("Calibri", "8")
        self.desktop["width"] = 65
        self.desktop["height"] = 65
        self.desktop["image"] = desktopIcon
        self.desktop["text"] = "Desktop"
        self.desktop["command"] = self.test
        self.desktop.image = desktopIcon
        self.desktop.pack()

        laptopIcon = PhotoImage(file = "icons/laptop-back.png")
        self.laptop = Button(self.equipment)
        self.laptop["font"] = ("Calibri", "8")
        self.laptop["width"] = 65
        self.laptop["height"] = 65
        self.laptop["image"] = laptopIcon
        self.laptop["text"] = "Laptop"
        self.laptop["command"] = self.test
        self.laptop.image = laptopIcon
        self.laptop.pack()

        dnsIcon = PhotoImage(file = "icons/dns-back.png")
        self.dns = Button(self.equipment)
        self.dns["font"] = ("Calibri", "8")
        self.dns["width"] = 65
        self.dns["height"] = 65
        self.dns["image"] = dnsIcon
        self.dns["text"] = "DNS Server"
        self.dns["command"] = self.test
        self.dns.image = dnsIcon
        self.dns.pack()

        webIcon = PhotoImage(file = "icons/web-back.png")
        self.web = Button(self.equipment)
        self.web["font"] = ("Calibri", "8")
        self.web["width"] = 65
        self.web["height"] = 65
        self.web["image"] = webIcon
        self.web["text"] = "Web Server"
        self.web["command"] = self.test
        self.web.image = webIcon
        self.web.pack()

        routerIcon = PhotoImage(file = "icons/router-back.png")
        self.router = Button(self.equipment)
        self.router["font"] = ("Calibri", "8")
        self.router["width"] = 65
        self.router["height"] = 65
        self.router["image"] = routerIcon
        self.router["text"] = "Router"
        self.router["command"] = self.test
        self.router.image = routerIcon
        self.router.pack()

        switchIcon = PhotoImage(file = "icons/switch-back.png")
        self.switch = Button(self.equipment)
        self.switch["font"] = ("Calibri", "8")
        self.switch["width"] = 65
        self.switch["height"] = 65
        self.switch["image"] = switchIcon
        self.switch["text"] = "Switch"
        self.switch["command"] = self.test
        self.switch.image = switchIcon
        self.switch.pack()

        wiresharkIcon = PhotoImage(file = "icons/wireshark-back.png")
        self.wireshark = Button(self.equipment)
        self.wireshark["font"] = ("Calibri", "8")
        self.wireshark["width"] = 65
        self.wireshark["height"] = 65
        self.wireshark["image"] = wiresharkIcon
        self.wireshark["text"] = "Wireshark"
        self.wireshark["command"] = self.test
        self.wireshark.image = wiresharkIcon
        self.wireshark.pack()
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
        tkMessageBox.showinfo("About", APP_NAME + " v." + CODE_VERSION + "\n\nPatrick Ferro Ribeiro")

    def test(self):
        print "test button"


root = Tk(className=APP_NAME)
root.title(APP_NAME + " - " +CODE_VERSION)
imgicon = PhotoImage(file='icons/main-icon.gif')
root.tk.call('wm', 'iconphoto', root._w, imgicon)
Application(root)
root.mainloop()
