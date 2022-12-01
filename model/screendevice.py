from tkinter import PhotoImage, Toplevel, Entry, Label, END, Frame, Button, Checkbutton, IntVar, Text
from util.constants import SCREEN_ICON_SIZE
from util.functions import copy_all_text_in_input
from model.tooltip import ToolTip
import uuid
import os
import re
import unidecode

class ScreenDevice:

    def __init__(self, device_menu_id, tk_inter_base, id, name, x_widget, y_widget, script_on, script_off, script_open, script_config, script_close, script_extra):
        self.tk_inter_base = tk_inter_base
        self.device_menu = self.tk_inter_base.menuElements[device_menu_id]
        if id is None:
            id = self.tk_inter_base.get_random_id()
            device_formated = unidecode.unidecode(self.device_menu.name)
            device_formated = device_formated.lower()
            device_formated = re.sub(r"[^a-z0-9]", "", device_formated)
            self.tagGenerated = "{}-{}".format(device_formated, id)
            self.name = "{} {}".format(self.device_menu.name, id)
            self.script_on = self.device_menu.script_on
            self.script_off = self.device_menu.script_off
            self.script_open = self.device_menu.script_open
            self.script_config = self.device_menu.script_config
            self.script_close = self.device_menu.script_close
            self.script_extra = self.device_menu.script_extra
        else:
            self.tagGenerated = id
            self.name = name
            self.script_on = script_on
            self.script_off = script_off
            self.script_open = script_open
            self.script_config = script_config
            self.script_close = script_close
            self.script_extra = script_extra
        self.is_interface = self.device_menu.is_interface
        self.x_widget = x_widget
        self.y_widget = y_widget

        if (self.is_interface):
            self.btn_interface = Button(width=20, height=20, command= lambda arg=self.device_menu.id : self.changeImage(arg), image=self.tk_inter_base.icons['PT_IMG_INTERFACE'])
            self.toolTip_btn_interface = ToolTip(self.btn_interface, text = 'Interface')
        else:
            self.btn_interface = Button(width=20, height=20, command= lambda arg=self.device_menu.id : self.changeImage(arg), image=self.tk_inter_base.icons['PT_IMG_SHELL'])
            self.toolTip_btn_interface = ToolTip(self.btn_interface, text = 'Console')

        self.btn_config = Button(width=20, height=20, command= lambda: self.modal_config_device(), image=self.tk_inter_base.icons['PT_IMG_CONFIG'])
        self.toolTip_btn_config = ToolTip(self.btn_config, text = 'Configurações')

        self.btn_on = Button(width=20, height=20, command= lambda arg=self.device_menu.id : self.run_script(self.script_on), image=self.tk_inter_base.icons['PT_IMG_ON'])
        self.toolTip_btn_on = ToolTip(self.btn_on, text = 'Ligar')

        self.btn_off = Button(width=20, height=20, command= lambda arg=self.device_menu.id : self.run_script(self.script_off), image=self.tk_inter_base.icons['PT_IMG_OFF'])
        toolTip_btn_off = ToolTip(self.btn_off, text = 'Desligar')

        self.btn_close = Button(width=20, height=20, command= lambda arg=self.tagGenerated : self.btn_close_command(arg), image=self.tk_inter_base.icons['PT_IMG_CLOSE'])
        ToolTip(self.btn_close, text = 'Fechar')

        self.btn_extra = Button(width=20, height=20, command= lambda arg=self.tagGenerated : self.run_script(self.script_extra), image=self.tk_inter_base.icons['PT_IMG_PYTHON'])
        ToolTip(self.btn_extra, text = 'Opção Extra')

        self.label_device = Label(self.tk_inter_base.drag_area, text=self.name, fg='black', bg='white')
        ToolTip(self.label_device, text = 'Editar Nome')
        self.label_device.bind("<Button-1>", lambda event: self.modal_name_device(event))

        self.draw_device()

    def __repr__(self):
        return "ScreenDevice id:% s Name:% s" % (self.id, self.name)

    def btn_close_command(self, tag):
        self.tk_inter_base.drag_area.delete(tag)
        self.tk_inter_base.drag_area.delete(tag + "btn_close")
        self.tk_inter_base.remove_line_by_tag(tag)
        self.tk_inter_base.devices_list.pop(tag, None)
        self.run_script(self.script_close)

    def dragDevice(self, event, tag):
        self.tk_inter_base.click_num=0
        self.tk_inter_base.drag_area.moveto(tag, event.x, event.y)
        self.update_line_by_tag(tag, event.x, event.y)

    def generateConection(self):
        self.tk_inter_base.drag_area.create_line(50, 50, 200, 200, fill='black', width=5)

    def draw_line(self, event, tag):
        x_widget, y_widget = self.tk_inter_base.drag_area.coords(tag)
        x_widget = x_widget + 10
        y_widget = y_widget + 10
        if self.tk_inter_base.click_num==0 or self.tk_inter_base.connection_1==tag:
            self.tk_inter_base.line_x1=x_widget
            self.tk_inter_base.line_y1=y_widget
            self.tk_inter_base.connection_1 = tag
            self.tk_inter_base.click_num=1
        else:
            x2=x_widget
            y2=y_widget
            self.tk_inter_base.connection_2 = tag
            tag_line = "{}/{}/{}".format(self.tk_inter_base.connection_1, self.tk_inter_base.connection_2, uuid.uuid4())
            self.tk_inter_base.connections_list[tag_line] = self.tk_inter_base.drag_area.create_line(self.tk_inter_base.line_x1 - 15, self.tk_inter_base.line_y1, x2 - 15, y2, fill='black', width=5, tag=tag_line)

            btn_close = Button(width=20, height=20, command= lambda arg=tag_line : self.btn_close_command(arg), image=self.tk_inter_base.icons['PT_IMG_CLOSE'])
            ToolTip(btn_close, text = 'Fechar')
            self.tk_inter_base.drag_area.create_window((self.tk_inter_base.line_x1 + x2)/2, (self.tk_inter_base.line_y1 + y2)/2, window=btn_close, tag=tag_line + "btn_close")


            self.tk_inter_base.drag_area.tag_lower(self.tk_inter_base.connections_list[tag_line])
            self.tk_inter_base.click_num=0

    def update_line_by_tag(self, tag, x, y):
        for ref in self.tk_inter_base.connections_list:
            if tag in ref:
                try:
                  line_tags = ref.split("/")
                  x1, y1, x2, y2 = self.tk_inter_base.drag_area.coords(self.tk_inter_base.connections_list[ref])
                  if tag == line_tags[0]:
                      self.tk_inter_base.drag_area.coords(self.tk_inter_base.connections_list[ref], x + 35, y + 35, x2, y2)
                      self.tk_inter_base.drag_area.moveto(ref + "btn_close", (x + x2)/2, (y + y2)/2)
                  if tag == line_tags[1]:
                      self.tk_inter_base.drag_area.coords(self.tk_inter_base.connections_list[ref], x1, y1, x + 35, y + 35)
                      self.tk_inter_base.drag_area.moveto(ref + "btn_close", (x + x1)/2, (y + y1)/2)
                except:
                  print("An exception occurred")

    def modal_name_device(self, event):
        global pop
        pop = Toplevel(self.tk_inter_base.root)
        pop.title("Editar Nome")
        pop.geometry("300x150")
        pop.config(bg="#f0f0f0")
        pop.resizable(False, False)

        frameForm = Frame(pop)
        frameForm.config(bg="#f0f0f0")
        frameForm.pack(pady=35)

        label_name=Label(frameForm, text="Nome: ", bg="#f0f0f0")
        entry_name= Entry(frameForm, width= 20)
        entry_name.focus_set()
        # entry_name.pack(pady=20)
        entry_name.delete(0,END)
        entry_name.insert(0,self.label_device.cget("text"))
        entry_name.bind('<Control-KeyRelease-a>', copy_all_text_in_input)
        label_name.grid(row=0, column=1)
        entry_name.grid(row=0, column=2)

        def close():
            pop.destroy()
            pop.update()

        def set_name_device():
            self.name = entry_name.get()
            self.label_device.config(text=self.name)
            close()

        frame = Frame(pop)
        frame.config(bg="#f0f0f0")
        frame.pack(pady=10)

        button1 = Button(frame, text="Salvar", command=lambda: set_name_device())
        button2 = Button(frame, text="Fechar", command=lambda: close())
        button2.grid(row=1, column=1)
        button1.grid(row=1, column=2)
        pop.wait_visibility()
        pop.grab_set()
        pop.wm_transient(self.tk_inter_base.drag_area)


    def modal_config_device(self):
        global pop
        pop = Toplevel(self.tk_inter_base.root)
        pop.title("Configuração {}".format(self.name))
        pop.geometry("750x700")
        pop.config(bg="#f0f0f0")
        pop.resizable(False, False)
        is_interface = self.is_interface

        def set_string_in_text(text, value):
            if not value is None:
                text.delete(1.0, END)
                text.insert(END, value)

        def get_string_from_text(text):
            return text.get("1.0","end")

        def close():
            pop.destroy()
            pop.update()

        def set_device_config():
            update_interface_button()
            self.label_device.config(text=entry_name.get())
            self.name = entry_name.get()
            self.script_on = get_string_from_text(text_script_on)
            self.script_off = get_string_from_text(text_script_off)
            self.script_open = get_string_from_text(text_script_open)
            self.script_config = get_string_from_text(text_script_config)
            self.script_close = get_string_from_text(text_script_close)
            self.script_extra = get_string_from_text(text_script_extra)
            self.run_script(self.script_config)
            close()

        def update_interface_button():
            self.is_interface = self.checked_interface.get() == 1
            if (self.is_interface):
                self.btn_interface.config(image = self.tk_inter_base.icons['PT_IMG_INTERFACE'])
                self.toolTip_btn_interface.text = 'Interface'
            else:
                self.btn_interface.config(image = self.tk_inter_base.icons['PT_IMG_SHELL'])
                self.toolTip_btn_interface.text = 'Console'

        frameConfigs = Frame(pop)
        frameConfigs.config(bg="#f0f0f0")
        frameConfigs.pack(pady=10)

        label_name=Label(frameConfigs, text="Nome: ", bg="#f0f0f0")
        entry_name= Entry(frameConfigs, width= 50)
        entry_name.delete(0,END)
        entry_name.insert(0,self.label_device.cget("text"))
        entry_name.bind('<Control-KeyRelease-a>', copy_all_text_in_input)
        label_name.grid(row=0, column=1)
        entry_name.grid(row=0, column=2)

        label_configs=Label(frameConfigs, text="Configurações: ", bg="#f0f0f0")
        self.checked_interface = IntVar(frameConfigs)
        self.checked_interface.set(self.is_interface)
        check_interface= Checkbutton(frameConfigs, text='Interface Gráfica', variable=self.checked_interface, onvalue=1, offvalue=0, bg="#f0f0f0")
        label_configs.grid(row=1, column=1)
        check_interface.grid(row=1, column=2)

        label_script_on=Label(frameConfigs, text="Script Ligar: ", bg="#f0f0f0")
        text_script_on=Text(frameConfigs, height = 5, width = 52)
        set_string_in_text(text_script_on, self.script_on)
        # text_script_on.delete(0,END)
        # text_script_on.insert(0, self.script_on)
        text_script_on.bind('<Control-KeyRelease-a>', copy_all_text_in_input)
        label_script_on.grid(row=2, column=1)
        text_script_on.grid(row=2, column=2)

        label_script_off=Label(frameConfigs, text="Script Desligar: ", bg="#f0f0f0")
        text_script_off=Text(frameConfigs, height = 5, width = 52)
        set_string_in_text(text_script_off, self.script_off)
        text_script_off.bind('<Control-KeyRelease-a>', copy_all_text_in_input)
        label_script_off.grid(row=3, column=1)
        text_script_off.grid(row=3, column=2)

        label_script_open=Label(frameConfigs, text="Script Abrir: ", bg="#f0f0f0")
        text_script_open=Text(frameConfigs, height = 5, width = 52)
        set_string_in_text(text_script_open, self.script_open)
        text_script_open.bind('<Control-KeyRelease-a>', copy_all_text_in_input)
        label_script_open.grid(row=4, column=1)
        text_script_open.grid(row=4, column=2)

        label_script_config=Label(frameConfigs, text="Script Configuração: ", bg="#f0f0f0")
        text_script_config=Text(frameConfigs, height = 5, width = 52)
        set_string_in_text(text_script_config, self.script_config)
        text_script_config.bind('<Control-KeyRelease-a>', copy_all_text_in_input)
        label_script_config.grid(row=5, column=1)
        text_script_config.grid(row=5, column=2)

        label_script_close=Label(frameConfigs, text="Script Fechar: ", bg="#f0f0f0")
        text_script_close=Text(frameConfigs, height = 5, width = 52)
        set_string_in_text(text_script_close, self.script_close)
        text_script_close.bind('<Control-KeyRelease-a>', copy_all_text_in_input)
        label_script_close.grid(row=6, column=1)
        text_script_close.grid(row=6, column=2)

        label_script_extra=Label(frameConfigs, text="Script Extra: ", bg="#f0f0f0")
        text_script_extra=Text(frameConfigs, height = 5, width = 52)
        set_string_in_text(text_script_extra, self.script_extra)
        text_script_extra.bind('<Control-KeyRelease-a>', copy_all_text_in_input)
        label_script_extra.grid(row=7, column=1)
        text_script_extra.grid(row=7, column=2)

        frame = Frame(pop)
        frame.pack(pady=10)

        button1 = Button(frame, text="Salvar", command=lambda: set_device_config())
        button2 = Button(frame, text="Fechar", command=lambda: close())
        button2.grid(row=2, column=1)
        button1.grid(row=2, column=2)
        pop.wait_visibility()
        pop.grab_set()
        pop.wm_transient(self.tk_inter_base.drag_area)

    def button2(self, arg):
        self.device_menu.name = "Alterado"
        # stream = os.popen("docker inspect {}".format(command))
        # output = stream.readlines()
        # print(output)

    def run_script(self, script):
        if script != "":
            try:
                script_replaced = script.replace("DEVICEID", self.tagGenerated)
                for command in script_replaced.split(";"):
                    print("{}:".format(command))
                    stream = os.popen(command)
                    output = stream.readlines()
                    for line in output:
                        print(line)
            except Exception as error:
                print("command error: {}".format(error))


    def draw_device(self):
        self.imageDeviceBindId = self.tk_inter_base.drag_area.create_image(self.x_widget + 35, self.y_widget + 35, image=self.device_menu.photoImage, tag=self.tagGenerated)
        self.tk_inter_base.drag_area.tag_bind(self.imageDeviceBindId, "<B1-Motion>", lambda event, arg=self.tagGenerated : self.dragDevice(event, arg))
        self.tk_inter_base.drag_area.tag_bind(self.imageDeviceBindId, '<Button-1>', lambda event, arg=self.tagGenerated : self.draw_line(event, arg))
        self.tk_inter_base.drag_area.create_window(self.x_widget - 15, self.y_widget + 10, window=self.btn_interface, tag=self.tagGenerated)
        self.tk_inter_base.drag_area.create_window(self.x_widget - 15, self.y_widget + 40, window=self.btn_config, tag=self.tagGenerated)
        self.tk_inter_base.drag_area.create_window(self.x_widget + 85, self.y_widget + 40, window=self.btn_on, tag=self.tagGenerated)
        self.tk_inter_base.drag_area.create_window(self.x_widget + 85, self.y_widget + 70, window=self.btn_off, tag=self.tagGenerated)
        self.tk_inter_base.drag_area.create_window(self.x_widget + 85, self.y_widget + 10, window=self.btn_close, tag=self.tagGenerated)
        self.tk_inter_base.drag_area.create_window(self.x_widget - 15, self.y_widget + 70, window=self.btn_extra, tag=self.tagGenerated)
        self.tk_inter_base.drag_area.create_window(self.x_widget + 35, self.y_widget + 95, window=self.label_device, tag=self.tagGenerated)

    def to_dict(self):
        dict_device = {}
        x_widget, y_widget = self.tk_inter_base.drag_area.coords(self.tagGenerated)
        dict_device["id"] = self.tagGenerated
        dict_device["name"] = self.name
        dict_device["device-id"] = self.device_menu.id
        dict_device["is-interface"] = self.is_interface
        dict_device["script-on"] = self.script_on
        dict_device["script-off"] = self.script_off
        dict_device["script-open"] = self.script_open
        dict_device["script-config"] = self.script_config
        dict_device["script-close"] = self.script_close
        dict_device["script-extra"] = self.script_extra
        dict_device["x-widget"] = x_widget
        dict_device["y-widget"] = y_widget
        return dict_device
