class TkInterBase:
    def __init__(self, dragarea, root, icons):
        self.dragarea = dragarea
        self.root = root
        self.icons = icons
        self.connections_list = {}
        self.counter = 1
        self.click_num=0
        self.line_x1=0
        self.line_y1=0
        self.connection_1=''
        self.connection_2=''
        self.connections_list={}
