import json


class Save:

    def save(data):
        with open("save.json","w") as file:
            json.dump(data,file)
        # pass

    def load():
        # json load
        pass