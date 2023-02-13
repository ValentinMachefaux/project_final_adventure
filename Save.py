import json
from Character import *
from Mapped import *



class Save:

    def save(data):
        with open("save.json","w") as file:
            json.dump(data,file)
        # pass

    def load():
        # json load
        with open("save.json","r") as file:
            data = json.load(file)
            heros = data["heros"]
            lancer = data["lancer"]
            warrior = data["warrior"]
            coord_x_dreen = data["coordinate_x_dreen"]
            coord_y_dreen = data["coordinate_y_dreen"]
            coord_x_forest = data["coordinate_x_forest"]
            coord_y_forest = data["coordinate_y_forest"]
            coord_x_forest_2 = data["coordinate_x_forest_2"]
            coord_y_forest_2 = data["coordinate_y_forest_2"]
            coord_x_dungeon = data["coordinate_x_dungeon"]
            coord_y_dungeon = data["coordinate_y_dungeon"]
            
        p.set_hp(heros["hp"])
        p.set_mp(heros["mp"])
        p.set_rp(heros["rp"])
        v.set_hp(lancer["hp"])
        v.set_mp(lancer["mp"])
        v.set_rp(lancer["rp"])
        t.set_hp(warrior["hp"])
        t.set_mp(warrior["mp"])
        t.set_rp(warrior["rp"])
        dreenshgard.set_x(int(coord_x_dreen))
        dreenshgard.set_y(int(coord_y_dreen))
        forest.set_x(int(coord_x_forest))
        forest.set_y(int(coord_y_forest))
        forest_2.set_x(int(coord_x_forest_2))
        forest_2.set_y(int(coord_y_forest_2))
        dungeon.set_x(int(coord_x_dungeon))
        dungeon.set_y(int(coord_y_dungeon))

        
        # pass


