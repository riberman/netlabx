from tkinter import PhotoImage, Toplevel, Entry, Label, END, Frame, Button
from util.constants import SCREEN_ICON_SIZE
from model.tooltip import ToolTip
class ScreenDeviceMenu:
    def __init__(self, frame_equipment, screen_frame_equipment_menu):
        self.frame_equipment = frame_equipment
        self.id = screen_frame_equipment_menu['id']
        self.name = screen_frame_equipment_menu['name']
        self.script_on = screen_frame_equipment_menu['script-on']
        self.script_off = screen_frame_equipment_menu['script-off']
        self.script_open = screen_frame_equipment_menu['script-open']
        self.script_config = screen_frame_equipment_menu['script-config']
        self.script_close = screen_frame_equipment_menu['script-close']
        self.script_extra = screen_frame_equipment_menu['script-extra']
        try:
            self.is_interface = screen_frame_equipment_menu['interface']
        except:
            self.is_interface = False
        self.photoImage = PhotoImage(file = screen_frame_equipment_menu['logo'])
        self.frame_equipment["width"] = SCREEN_ICON_SIZE
        self.frame_equipment["height"] = SCREEN_ICON_SIZE
        self.frame_equipment["image"] = self.photoImage
        self.frame_equipment["text"] = screen_frame_equipment_menu['name']
        self.frame_equipment.image = self.photoImage
        self.frame_equipment.pack()
        ToolTip(self.frame_equipment, x_pading=SCREEN_ICON_SIZE, y_pading=SCREEN_ICON_SIZE, text="Criar {}".format(self.frame_equipment["text"]))

    def __repr__(self):
        return "ScreenDeviceMenu id:% s elementText:% s" % (self.id, self.frame_equipment["text"])
