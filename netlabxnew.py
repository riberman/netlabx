#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import Tk, Button, Label, Frame, Canvas, PhotoImage, Menu, Toplevel, Entry, END
from PIL import Image, ImageTk
# import sys
from tkinter import messagebox as tkMessageBox
import json
import os
# import model.screenelement
from model.screenelement import ScreenElement
# import model.tooltip
from model.tooltip import ToolTip
from util.constants import *
# import importlib
# importlib.reload(sys)
# sys.setdefaultencoding('utf-8')

#Load config json
with open('devices.conf') as json_file:
    data = json.load(json_file)

class Application:
    def __init__(self, master):
        #main screen
        width_dragarea = root.winfo_screenwidth()
        height_dragarea = root.winfo_screenheight()
        root.attributes('-zoomed', True)
        self.mainarea = Frame(root, bg='#CCC', width=width_dragarea, height=height_dragarea)
        self.dragarea = Canvas(self.mainarea, width=width_dragarea/2.09, height=height_dragarea, bg='white')
        self.dragarea.pack(side='left', anchor='n')
        self.mainarea.pack(expand=True, fill='both', side='right')

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

        self.imgClose = Image.open("icons/close.png")
        self.imgResizedClose = self.imgClose.resize((20, 20), Image.Resampling.LANCZOS)
        self.ptImgClose = ImageTk.PhotoImage(self.imgResizedClose)

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

        # Init Values
        self.temp = {}
        self.counter = 1
        self.menuElements = {}

        #Item in frame
        for screenElement in data['screen-elements']:
            self.menuElements[screenElement['id']] = ScreenElement(Button(self.equipment), screenElement)
            self.menuElements[screenElement['id']].element["command"] = lambda index=screenElement['id']: self.createDevice(self.menuElements[index])
        #end item
        self.equipment.pack()

        #self.mensagem = Label(self.quartoContainer, text="", font=self.defaultFont)
        #self.mensagem.pack()

        #Desenha Linha
        # self.dragarea.bind('<Button-1>', lambda event : self.draw_line(event))
        self.click_num=0
        self.line_x1=0
        self.line_y1=0
        self.connection_1=''
        self.connection_2=''
        self.connections_list={}

    def open(self):
        print("Open")

    def save(self):
        print("Save")

    def quit(self):
        prin("Quit")

    def about(self):
        tkMessageBox.showinfo("Sobre", "{} {}\n\nPatrick Ferro Ribeiro".format(APP_NAME, CODE_VERSION))

    def createDevice(self, element):
        id = self.getRandomId()
        tagGenerated = "{}-tag".format(id)
        # print(element.id)
        # print(element.element["text"])
        # button = Button(text="C")
        # button.bind("<Button-1>", self.clicked(element.id))

        # self.imgConfig = Image.open("icons/config-back.png")
        # self.imgResizedConfig = self.imgConfig.resize((25, 25), Image.Resampling.LANCZOS)
        # self.ptImgConfig = ImageTk.PhotoImage(self.imgResizedConfig)
        #
        # self.imgShell = Image.open("icons/console.png")
        # self.imgResizedShell = self.imgShell.resize((20, 20), Image.Resampling.LANCZOS)
        # self.ptImgShell = ImageTk.PhotoImage(self.imgResizedShell)
        #
        # self.imgOn = Image.open("icons/on.png")
        # self.imgResizedOn = self.imgOn.resize((20, 20), Image.Resampling.LANCZOS)
        # self.ptImgOn = ImageTk.PhotoImage(self.imgResizedOn)
        #
        # self.imgOff = Image.open("icons/off.png")
        # self.imgResizedOff = self.imgOff.resize((20, 20), Image.Resampling.LANCZOS)
        # self.ptImgOff = ImageTk.PhotoImage(self.imgResizedOff)

        # label1 = Label(image=element.photoImage, bg='white')
        # label1.bind("<B1-Motion>", lambda event, arg=tagGenerated : self.dragDevice(event, arg))
        # label1.bind('<Button-1>', lambda event, arg=tagGenerated : self.draw_line(event, arg))

        button1 = Button(width=20, height=20, command= lambda arg=element.id : self.button1(arg), image=self.ptImgShell)
        ToolTip(button1, text = 'Console')
        # button1.bind("<B1-Motion>", lambda event, arg=tagGenerated : self.dragDevice(event, arg))

        button2 = Button(width=20, height=20, command= lambda arg=element.id : self.button2(arg), image=self.ptImgConfig)
        ToolTip(button2, text = 'Configurações')
        # button2.bind("<B1-Motion>", lambda event, arg=tagGenerated : self.dragDevice(event, arg))

        button3 = Button(width=20, height=20, command= lambda arg=element.id : self.button3(arg), image=self.ptImgOn)
        ToolTip(button3, text = 'Ligar')
        # button3.bind("<B1-Motion>", lambda event, arg=tagGenerated : self.dragDevice(event, arg))

        button4 = Button(width=20, height=20, command= lambda arg=element.id : self.button4(arg), image=self.ptImgOff)
        ToolTip(button4, text = 'Desligar')
        # button4.bind("<B1-Motion>", lambda event, arg=tagGenerated : self.dragDevice(event, arg))

        buttonClose = Button(width=20, height=20, command= lambda arg=tagGenerated : self.buttonClose(arg), image=self.ptImgClose)
        ToolTip(buttonClose, text = 'Fechar')

        buttonCloseTESTE = Button(width=20, height=20, command= lambda arg=tagGenerated : self.buttonClose(arg), image=self.ptImgClose)
        ToolTip(buttonClose, text = 'Fechar')

        labelEquip = Label(self.dragarea, text=element.name + " " + id, fg='black', bg='white')
        ToolTip(labelEquip, text = 'Editar Nome')
        labelEquip.bind("<Button-1>", lambda event, labelEquip=labelEquip, element=element: self.modal_name_device(event, labelEquip))
        # buttonClose.bind("<B1-Motion>", lambda event, arg=tagGenerated : self.dragDevice(event, arg))
        # Create Line Test
        # self.generateConection()

        # button2.bind("<Button-1>", lambda arg=element.id : self.clicked(arg))
        # button2["image"] = PhotoImage(file = "icons/config-back.png")
        # self.dragarea.create_window(155, 65,window=button)
        position_x = 50
        position_y = 50

        imageBindId = self.dragarea.create_image(position_x + 35, position_y + 35, image=element.photoImage, tag=tagGenerated)
        self.dragarea.tag_bind(imageBindId, "<B1-Motion>", lambda event, arg=tagGenerated : self.dragDevice(event, arg))
        self.dragarea.tag_bind(imageBindId, '<Button-1>', lambda event, arg=tagGenerated : self.draw_line(event, arg))
        # self.dragarea.create_window(position_x + 35, position_y + 35, window=label1, tag=tagGenerated)
        self.dragarea.create_window(position_x - 15, position_y + 10, window=button1, tag=tagGenerated)
        # self.dragarea.tag_bind(imageDevice, "<B1-Motion>", lambda event, arg=tagGenerated : self.dragDevice(event, arg))
        # self.dragarea.create_window(position_x + 85, position_y + 10, window=button2, tag=tagGenerated)
        self.dragarea.create_window(position_x - 15, position_y + 40, window=button2, tag=tagGenerated)
        self.dragarea.create_window(position_x + 85, position_y + 40, window=button3, tag=tagGenerated)
        self.dragarea.create_window(position_x + 85, position_y + 70, window=button4, tag=tagGenerated)
        # self.dragarea.create_window(position_x - 10, position_y + 40, window=buttonClose, tag=tagGenerated)
        self.dragarea.create_window(position_x + 85, position_y + 10, window=buttonClose, tag=tagGenerated)

        self.dragarea.create_window(position_x - 15, position_y + 70, window=buttonCloseTESTE, tag=tagGenerated)

        self.dragarea.create_window(position_x + 35, position_y + 95, window=labelEquip, tag=tagGenerated)

        # self.dragarea.create_image(position_x + 70, position_y, image=self.newTesteImg, anchor='nw')
        # self.dragarea.create_image(position_x + 70, position_y + 25, image=self.newTesteImg, anchor='nw')
        # self.dragarea.create_image(position_x + 70, position_y + 50, image=self.newTesteImg, anchor='nw')
        # self.dragarea.create_image(position_x - 25, position_y, image=self.newTesteImg, anchor='nw')

    def clicked(self):
        print("pressed1")

    def button1(self, test):
        print("BTN1 ID: {}".format(test))

    def button2(self, test):
        container="mysql"
        print("docker inspect --format \'{{ .NetworkSettings.Networks.dev.IPAddress }}\'")
        stream = os.popen("docker inspect --format \'{{ .NetworkSettings.Networks.dev.IPAddress }}\' {}".format(container))
        output = stream.readlines()
        print(output)
        # print("BTN2 ID: {}".format(test))

    def button3(self, test):
        print("BTN3 ID: {}".format(test))

    def button4(self, test):
        print("BTN4 ID: {}".format(test))

    def buttonClose(self, tag):
        for element in self.dragarea.find_withtag("{}teste".format(tag)):
            print("Element: {}".format(element))
        self.dragarea.delete(tag)
        self.dragarea.delete(tag + "btn_close")
        self.remove_line_by_tag(tag)


    def dragDevice(self, event, tag):
        self.click_num=0
        self.dragarea.moveto(tag, event.x, event.y)
        self.update_line_by_tag(tag, event.x, event.y)

    def generateConection(self):
        self.dragarea.create_line(50, 50, 200, 200, fill='black', width=5)

    def draw_line(self, event, tag):
        # print(event.widget)
        x_widget, y_widget = self.dragarea.coords(tag)
        x_widget = x_widget + 10
        y_widget = y_widget + 10
        if self.click_num==0 or self.connection_1==tag:
            self.x1=x_widget
            self.y1=y_widget
            self.connection_1 = tag
            self.click_num=1
        else:
            x2=x_widget
            y2=y_widget
            self.connection_2 = tag
            tag_line = "{}/{}".format(self.connection_1, self.connection_2)
            print("Criada linha: {}".format(tag_line))
            print(self.x1, x2, self.y1, y2)
            print((self.x1 + x2)/2, (self.y1 + y2)/2)
            self.connections_list[tag_line] = self.dragarea.create_line(self.x1 - 15, self.y1, x2 - 15, y2, fill='black', width=5, tag=tag_line)

            buttonClose = Button(width=20, height=20, command= lambda arg=tag_line : self.buttonClose(arg), image=self.ptImgClose)
            ToolTip(buttonClose, text = 'Fechar')
            self.dragarea.create_window((self.x1 + x2)/2, (self.y1 + y2)/2, window=buttonClose, tag=tag_line + "btn_close")


            self.dragarea.tag_lower(self.connections_list[tag_line])
            self.click_num=0

    def remove_line_by_tag(self, tag):
        list_to_remove = []
        for ref in self.connections_list:
            if tag in ref:
                print("REMOVEU: {}".format(ref))
                self.dragarea.delete(self.connections_list[ref])
                self.dragarea.delete(ref + "btn_close")
                list_to_remove.append(ref)

        for key in list_to_remove:
            self.connections_list.pop(key, None)

    def update_line_by_tag(self, tag, x, y):
        # list_to_remove = []
        for ref in self.connections_list:
            if tag in ref:
                try:
                  line_tags = ref.split("/")
                  x1, y1, x2, y2 = self.dragarea.coords(self.connections_list[ref])
                  # print("REF: {} TAG: {} X: {} Y: {}".format(ref, tag, x, y))
                  # print("x1: {} y1: {} x2: {} y2: {}".format(x1, y1, x2, y2))
                  print("REF: {} TAG: {}".format(ref, tag))
                  if tag == line_tags[0]:
                      self.dragarea.coords(self.connections_list[ref], x + 35, y + 35, x2, y2)
                      self.dragarea.moveto(ref + "btn_close", (x + x2)/2, (y + y2)/2)
                  else:
                      self.dragarea.coords(self.connections_list[ref], x1, y1, x + 35, y + 35)
                      self.dragarea.moveto(ref + "btn_close", (x + x1)/2, (y + y1)/2)
                except:
                  print("An exception occurred")
                  print("****REF: {} TAG: {}".format(ref, tag))
                  # list_to_remove.append(ref)

        # for key in list_to_remove:
        #     self.connections_list.pop(key, None)

    def modal_name_device(self, event, labelDevice):
        global pop
        pop = Toplevel(root)
        pop.title("Editar Nome")
        pop.geometry("300x150")
        pop.config(bg="#f0f0f0")
        pop.resizable(False, False)

        entry= Entry(pop, width= 20)
        entry.focus_set()
        entry.pack(pady=20)
        entry.delete(0,END)
        entry.insert(0,labelDevice.cget("text"))

        frame = Frame(pop)
        frame.pack(pady=10)

        def close():
            pop.destroy()
            pop.update()

        def set_name_device():
            labelDevice.config(text=entry.get())
            close()

        button1 = Button(frame, text="Salvar", command=lambda: set_name_device())
        button2 = Button(frame, text="Fechar", command=lambda: close())
        button2.grid(row=0, column=1)
        button1.grid(row=0, column=3)


    def handle_keypress(event):
        input1.delete(0, DEL)

    def getRandomId(self):
        id = self.counter
        self.counter = self.counter + 1
        return str(id)

root = Tk(className=APP_NAME)
root.title(APP_NAME + " - " + CODE_VERSION)
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='icons/main-icon.gif'))
Application(root)
root.focus_set()
root.mainloop()
