import json


def json_map(coordinate):
    with open('resources\\json_datas\\map.json', "r", encoding="utf-8") as f:
        # with open('json_datas\\map.json',"r",encoding="utf-8") as f:
        data = json.load(f)
    get_map = data['Dreenshgard']
    Dreenshgard = get_map[0]
    return Dreenshgard[coordinate]


class Mappy:

    def __init__(self, info_map):
        self.name = info_map["name"]
        self.description = info_map["description"]
        self.description_2 = info_map["description_2"]
        self.description_before = info_map["description_before"]

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_description_2(self):
        return self.description_2

    def get_description_before(self):
        return self.description_before


# m = Mappy(json_class("0,0"))
# print(m.get_description())
