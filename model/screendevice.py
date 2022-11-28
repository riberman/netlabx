from tkinter import PhotoImage, Toplevel, Entry, Label, END, Frame, Button, Checkbutton, IntVar
from util.constants import SCREEN_ICON_SIZE
from model.tooltip import ToolTip
import uuid
import os

POSITION_X = 80
POSITION_Y = 50

class ScreenDevice:

    def __init__(self, deviceMenu, tkInterBase, id):
        self.tagGenerated = "{}-tag".format(id)
        self.name = "{} {}".format(deviceMenu.name, id)
        self.tkInterBase = tkInterBase
        self.deviceMenu = deviceMenu
        self.is_interface = self.deviceMenu.is_interface

        if (self.is_interface):
            self.btn_left1 = Button(width=20, height=20, command= lambda arg=self.deviceMenu.id : self.changeImage(arg), image=self.tkInterBase.icons['PT_IMG_INTERFACE'])
            self.toolTip_btn_left1 = ToolTip(self.btn_left1, text = 'Interface')
        else:
            self.btn_left1 = Button(width=20, height=20, command= lambda arg=self.deviceMenu.id : self.changeImage(arg), image=self.tkInterBase.icons['PT_IMG_SHELL'])
            self.toolTip_btn_left1 = ToolTip(self.btn_left1, text = 'Console')

        self.btn_left2 = Button(width=20, height=20, command= lambda: self.modal_config_device(), image=self.tkInterBase.icons['PT_IMG_CONFIG'])
        self.toolTip_btn_left2 = ToolTip(self.btn_left2, text = 'Configurações')

        self.btn_right1 = Button(width=20, height=20, command= lambda arg=self.deviceMenu.id : self.button3(arg), image=self.tkInterBase.icons['PT_IMG_ON'])
        self.toolTip_btn_right1 = ToolTip(self.btn_right1, text = 'Ligar')

        self.btn_right2 = Button(width=20, height=20, command= lambda arg=self.deviceMenu.id : self.button4(arg), image=self.tkInterBase.icons['PT_IMG_OFF'])
        toolTip_btn_right2 = ToolTip(self.btn_right2, text = 'Desligar')

        self.btn_close = Button(width=20, height=20, command= lambda arg=self.tagGenerated : self.buttonClose(arg), image=self.tkInterBase.icons['PT_IMG_CLOSE'])
        ToolTip(self.btn_close, text = 'Fechar')

        self.buttonCloseTESTE = Button(width=20, height=20, command= lambda arg=self.tagGenerated : self.buttonClose(arg), image=self.tkInterBase.icons['PT_IMG_CLOSE'])
        ToolTip(self.btn_close, text = 'Fechar')

        self.labelDevice = Label(self.tkInterBase.dragarea, text=self.name, fg='black', bg='white')
        ToolTip(self.labelDevice, text = 'Editar Nome')
        self.labelDevice.bind("<Button-1>", lambda event: self.modal_name_device(event))

        self.draw_device()

    def __repr__(self):
        return "ScreenDevice id:% s Name:% s" % (self.id, self.name)

    def buttonClose(self, tag):
        self.tkInterBase.dragarea.delete(tag)
        self.tkInterBase.dragarea.delete(tag + "btn_close")
        self.remove_line_by_tag(tag)

    def dragDevice(self, event, tag):
        self.tkInterBase.click_num=0
        self.tkInterBase.dragarea.moveto(tag, event.x, event.y)
        self.update_line_by_tag(tag, event.x, event.y)

    def generateConection(self):
        self.tkInterBase.dragarea.create_line(50, 50, 200, 200, fill='black', width=5)

    def draw_line(self, event, tag):
        # print(event.widget)
        x_widget, y_widget = self.tkInterBase.dragarea.coords(tag)
        x_widget = x_widget + 10
        y_widget = y_widget + 10
        if self.tkInterBase.click_num==0 or self.tkInterBase.connection_1==tag:
            self.tkInterBase.line_x1=x_widget
            self.tkInterBase.line_y1=y_widget
            self.tkInterBase.connection_1 = tag
            self.tkInterBase.click_num=1
        else:
            x2=x_widget
            y2=y_widget
            self.tkInterBase.connection_2 = tag
            tag_line = "{}/{}/{}".format(self.tkInterBase.connection_1, self.tkInterBase.connection_2, uuid.uuid4())
            print("Criada linha: {}".format(tag_line))
            self.tkInterBase.connections_list[tag_line] = self.tkInterBase.dragarea.create_line(self.tkInterBase.line_x1 - 15, self.tkInterBase.line_y1, x2 - 15, y2, fill='black', width=5, tag=tag_line)

            buttonClose = Button(width=20, height=20, command= lambda arg=tag_line : self.buttonClose(arg), image=self.tkInterBase.icons['PT_IMG_CLOSE'])
            ToolTip(buttonClose, text = 'Fechar')
            self.tkInterBase.dragarea.create_window((self.tkInterBase.line_x1 + x2)/2, (self.tkInterBase.line_y1 + y2)/2, window=buttonClose, tag=tag_line + "btn_close")


            self.tkInterBase.dragarea.tag_lower(self.tkInterBase.connections_list[tag_line])
            self.tkInterBase.click_num=0

    def remove_line_by_tag(self, tag):
        list_to_remove = []
        for ref in self.tkInterBase.connections_list:
            if tag in ref:
                print("REMOVEU: {}".format(ref))
                self.tkInterBase.dragarea.delete(self.tkInterBase.connections_list[ref])
                self.tkInterBase.dragarea.delete(ref + "btn_close")
                list_to_remove.append(ref)

        for key in list_to_remove:
            self.tkInterBase.connections_list.pop(key, None)

    def update_line_by_tag(self, tag, x, y):
        for ref in self.tkInterBase.connections_list:
            if tag in ref:
                try:
                  line_tags = ref.split("/")
                  x1, y1, x2, y2 = self.tkInterBase.dragarea.coords(self.tkInterBase.connections_list[ref])
                  if tag == line_tags[0]:
                      self.tkInterBase.dragarea.coords(self.tkInterBase.connections_list[ref], x + 35, y + 35, x2, y2)
                      self.tkInterBase.dragarea.moveto(ref + "btn_close", (x + x2)/2, (y + y2)/2)
                  if tag == line_tags[1]:
                      self.tkInterBase.dragarea.coords(self.tkInterBase.connections_list[ref], x1, y1, x + 35, y + 35)
                      self.tkInterBase.dragarea.moveto(ref + "btn_close", (x + x1)/2, (y + y1)/2)
                except:
                  print("An exception occurred")
                  print("****REF: {} TAG: {}".format(ref, tag))

    def modal_name_device(self, event):
        global pop
        pop = Toplevel(self.tkInterBase.root)
        pop.title("Editar Nome")
        pop.geometry("300x150")
        pop.config(bg="#f0f0f0")
        pop.resizable(False, False)

        entry= Entry(pop, width= 20)
        entry.focus_set()
        entry.pack(pady=20)
        entry.delete(0,END)
        entry.insert(0,self.labelDevice.cget("text"))

        frame = Frame(pop)
        frame.pack(pady=10)

        def close():
            pop.destroy()
            pop.update()

        def set_name_device():
            self.name = entry.get()
            self.labelDevice.config(text=self.name)
            close()

        button1 = Button(frame, text="Salvar", command=lambda: set_name_device())
        button2 = Button(frame, text="Fechar", command=lambda: close())
        button2.grid(row=0, column=1)
        button1.grid(row=0, column=3)

    def modal_config_device(self):
        global pop
        pop = Toplevel(self.tkInterBase.root)
        pop.title("Configuração {}".format(self.name))
        pop.geometry("450x250")
        pop.config(bg="#f0f0f0")
        pop.resizable(False, False)
        is_interface = self.is_interface

        def close():
            pop.destroy()
            pop.update()

        def set_device_config():
            update_interface_button()
            self.labelDevice.config(text=entry_name.get())
            self.name = entry_name.get()
            close()

        def update_interface_button():
            self.is_interface = self.var.get() == 1
            if (self.is_interface):
                self.btn_left1.config(image = self.tkInterBase.icons['PT_IMG_INTERFACE'])
                self.toolTip_btn_left1.text = 'Interface'
            else:
                self.btn_left1.config(image = self.tkInterBase.icons['PT_IMG_SHELL'])
                self.toolTip_btn_left1.text = 'Console'

        frameConfigs = Frame(pop)
        frameConfigs.pack(pady=10)

        label_name=Label(frameConfigs, text="Nome")

        entry_name= Entry(frameConfigs, width= 20)
        entry_name.delete(0,END)
        entry_name.insert(0,self.labelDevice.cget("text"))

        label_name.grid(row=0, column=1)
        entry_name.grid(row=0, column=2)

        label_interface=Label(frameConfigs, text="Interface")

        self.var = IntVar(frameConfigs)
        self.var.set(self.is_interface )
        check_interface= Checkbutton(frameConfigs, text='', variable=self.var, onvalue=1, offvalue=0)

        label_interface.grid(row=1, column=1)
        check_interface.grid(row=1, column=2)

        frame = Frame(pop)
        frame.pack(pady=10)

        button1 = Button(frame, text="Salvar", command=lambda: set_device_config())
        button2 = Button(frame, text="Fechar", command=lambda: close())
        button2.grid(row=2, column=1)
        button1.grid(row=2, column=2)

    def button2(self, arg, command):
        stream = os.popen("docker inspect {}".format(command))
        output = stream.readlines()
        print(output)

    def draw_device(self):
        self.imageDeviceBindId = self.tkInterBase.dragarea.create_image(POSITION_X + 35, POSITION_Y + 35, image=self.deviceMenu.photoImage, tag=self.tagGenerated)
        self.tkInterBase.dragarea.tag_bind(self.imageDeviceBindId, "<B1-Motion>", lambda event, arg=self.tagGenerated : self.dragDevice(event, arg))
        self.tkInterBase.dragarea.tag_bind(self.imageDeviceBindId, '<Button-1>', lambda event, arg=self.tagGenerated : self.draw_line(event, arg))
        self.tkInterBase.dragarea.create_window(POSITION_X - 15, POSITION_Y + 10, window=self.btn_left1, tag=self.tagGenerated)
        self.tkInterBase.dragarea.create_window(POSITION_X - 15, POSITION_Y + 40, window=self.btn_left2, tag=self.tagGenerated)

        self.tkInterBase.dragarea.create_window(POSITION_X + 85, POSITION_Y + 40, window=self.btn_right1, tag=self.tagGenerated)
        self.tkInterBase.dragarea.create_window(POSITION_X + 85, POSITION_Y + 70, window=self.btn_right2, tag=self.tagGenerated)

        self.tkInterBase.dragarea.create_window(POSITION_X + 85, POSITION_Y + 10, window=self.btn_close, tag=self.tagGenerated)

        self.tkInterBase.dragarea.create_window(POSITION_X - 15, POSITION_Y + 70, window=self.buttonCloseTESTE, tag=self.tagGenerated)

        self.tkInterBase.dragarea.create_window(POSITION_X + 35, POSITION_Y + 95, window=self.labelDevice, tag=self.tagGenerated)
