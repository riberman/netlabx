from tkinter import Label, Toplevel
class ToolTip(object):
    def __init__(self, widget, x_pading=25, y_pading=25, text='dica de ferramenta'):
        self.widget = widget
        self.text = text
        self.x_pading = x_pading
        self.y_pading = y_pading
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.close)

    def enter(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + self.x_pading
        y += self.widget.winfo_rooty() + self.y_pading
        # creates a toplevel window
        self.tw = Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(self.tw, text=self.text, justify='left',
                       background='#3498db', relief='solid', borderwidth=1,
                       font=("times", "9", "normal"))
        label.pack(ipadx=1)

    def close(self, event=None):
        if self.tw:
            self.tw.destroy()
