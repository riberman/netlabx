from tkinter import PhotoImage, Toplevel, Entry, Label, END, Frame, Button
from util.constants import SCREEN_ICON_SIZE
from model.tooltip import ToolTip
class ScreenDeviceMenu:
    def __init__(self, device, data):
        self.device = device
        self.id = data['id']
        self.name = data['name']
        try:
            self.is_interface = data['interface']
        except:
            self.is_interface = False
        self.photoImage = PhotoImage(file = data['logo'])
        self.device["width"] = SCREEN_ICON_SIZE
        self.device["height"] = SCREEN_ICON_SIZE
        self.device["image"] = self.photoImage
        self.device["text"] = data['name']
        self.device.image = self.photoImage
        self.device.pack()
        ToolTip(self.device, x_pading=SCREEN_ICON_SIZE, y_pading=SCREEN_ICON_SIZE, text="Criar {}".format(self.device["text"]))

    def __repr__(self):
        return "ScreenDeviceMenu id:% s elementText:% s" % (self.id, self.device["text"])
