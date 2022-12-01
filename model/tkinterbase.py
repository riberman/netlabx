import json
class TkInterBase:
    def __init__(self, drag_area, root, icons):
        self.drag_area = drag_area
        self.root = root
        self.icons = icons
        self.menuElements = {}
        self.connections_list = {}
        self.devices_list = {}
        self.counter = 1
        self.click_num=0
        self.line_x1=0
        self.line_y1=0
        self.connection_1=''
        self.connection_2=''

    def clear(self):
        self.connections_list = {}
        self.devices_list = {}
        self.counter = 1
        self.click_num=0
        self.line_x1=0
        self.line_y1=0
        self.connection_1=''
        self.connection_2=''

    def remove_line_by_tag(self, tag):
        list_to_remove = []
        for ref in self.connections_list:
            if tag in ref:
                self.drag_area.delete(self.connections_list[ref])
                self.drag_area.delete(ref + "btn_close")
                list_to_remove.append(ref)

        for key in list_to_remove:
            self.connections_list.pop(key, None)

    def get_random_id(self):
        id = self.counter
        self.counter = self.counter + 1
        return str(id)

    def to_dict_devices_list(self):
        list_devices = []
        for device_tag in self.devices_list:
            list_devices.append(self.devices_list[device_tag].to_dict())
        return list_devices

    def to_dict_connections_list(self):
        list_connections = []
        for ref in self.connections_list:
            x_widget1, y_widget1, x_widget2, y_widget2 = self.drag_area.coords(ref)
            dict_connections = {}
            dict_connections["id"]=ref
            list_connections.append(dict_connections)
        return list_connections

    def to_dict(self):
        dict_json = {}
        dict_json["devices"] = self.to_dict_devices_list()
        dict_json["connections"] = self.to_dict_connections_list()
        # if not ( dict_json["devices"] and dict_json["connections"]):
        #     dict_json = {}
        return dict_json
