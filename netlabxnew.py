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
        self.name = data['name']
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
        tkMessageBox.showinfo("About", APP_NAME + " " + CODE_VERSION + "\n\nPatrick Ferro Ribeiro")

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
        CreateToolTipOptions(button1, text = 'Console')
        # button1.bind("<B1-Motion>", lambda event, arg=tagGenerated : self.dragDevice(event, arg))

        button2 = Button(width=20, height=20, command= lambda arg=element.id : self.button2(arg), image=self.ptImgConfig)
        CreateToolTipOptions(button2, text = 'Configurações')
        # button2.bind("<B1-Motion>", lambda event, arg=tagGenerated : self.dragDevice(event, arg))

        button3 = Button(width=20, height=20, command= lambda arg=element.id : self.button3(arg), image=self.ptImgOn)
        CreateToolTipOptions(button3, text = 'Ligar')
        # button3.bind("<B1-Motion>", lambda event, arg=tagGenerated : self.dragDevice(event, arg))

        button4 = Button(width=20, height=20, command= lambda arg=element.id : self.button4(arg), image=self.ptImgOff)
        CreateToolTipOptions(button4, text = 'Desligar')
        # button4.bind("<B1-Motion>", lambda event, arg=tagGenerated : self.dragDevice(event, arg))

        buttonClose = Button(width=20, height=20, command= lambda arg=tagGenerated : self.buttonClose(arg), image=self.ptImgClose)
        CreateToolTipOptions(buttonClose, text = 'Fechar')

        labelEquip = Label(self.dragarea, text=element.name + " " + id, fg='black', bg='white')
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
        self.dragarea.create_window(position_x - 10, position_y + 10, window=button1, tag=tagGenerated)
        # self.dragarea.tag_bind(imageDevice, "<B1-Motion>", lambda event, arg=tagGenerated : self.dragDevice(event, arg))
        # self.dragarea.create_window(position_x + 85, position_y + 10, window=button2, tag=tagGenerated)
        self.dragarea.create_window(position_x - 10, position_y + 40, window=button2, tag=tagGenerated)
        self.dragarea.create_window(position_x + 85, position_y + 40, window=button3, tag=tagGenerated)
        self.dragarea.create_window(position_x + 85, position_y + 70, window=button4, tag=tagGenerated)
        # self.dragarea.create_window(position_x - 10, position_y + 40, window=buttonClose, tag=tagGenerated)
        self.dragarea.create_window(position_x + 85, position_y + 10, window=buttonClose, tag=tagGenerated)
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
        print("BTN2 ID: {}".format(test))

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
        print("\n")

    def generateConection(self):
        self.dragarea.create_line(50, 50, 200, 200, fill='black', width=5)

    def draw_line(self, event, tag):
        if self.click_num==0 or self.connection_1==tag:
            self.x1=event.x_root - 55
            self.y1=event.y_root - 55
            self.connection_1 = tag
            self.click_num=1
        else:
            x2=event.x_root - 55
            y2=event.y_root - 55
            self.connection_2 = tag
            tag_line = "{}/{}".format(self.connection_1, self.connection_2)
            print("Criada linha: {}".format(tag_line))
            print(self.x1, x2, self.y1, y2)
            print((self.x1 + x2)/2, (self.y1 + y2)/2)
            self.connections_list[tag_line] = self.dragarea.create_line(self.x1 - 15, self.y1, x2 - 15, y2, fill='black', width=5, tag=tag_line)

            buttonClose = Button(width=20, height=20, command= lambda arg=tag_line : self.buttonClose(arg), image=self.ptImgClose)
            CreateToolTipOptions(buttonClose, text = 'Fechar')
            self.dragarea.create_window((self.x1 + x2)/2, (self.y1 + y2)/2, window=buttonClose, tag=tag_line + "btn_close")


            self.dragarea.tag_lower(self.connections_list[tag_line])
            self.click_num=0

    def remove_line_by_tag(self, tag):
        list_to_remove = []
        for ref in self.connections_list:
            if tag in ref:
                print(self.connections_list[ref])
                list_to_remove.append(self.connections_list[ref])
                self.dragarea.delete(ref + "btn_close")

        for element in list_to_remove:
            self.dragarea.delete(element)
            self.connections_list.pop(element, None)

    def update_line_by_tag(self, tag, x, y):
        for ref in self.connections_list:
            if tag in ref:
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



    def handle_keypress(event):
        input1.delete(0, tk.DEL)

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
