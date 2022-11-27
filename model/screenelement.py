from tkinter import PhotoImage
from util.constants import SCREEN_ICON_SIZE
from model.tooltip import ToolTip
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
        try:
            self.element.buttons = data['action-buttons']
        except:
            print("Dont find action-buttons")
        self.element.pack()
        ToolTip(self.element, x_pading=SCREEN_ICON_SIZE, y_pading=SCREEN_ICON_SIZE, text="Criar {}".format(self.element["text"]))

    def __repr__(self):
        return "ScreenElement id:% s elementText:% s" % (self.id, self.element["text"])
