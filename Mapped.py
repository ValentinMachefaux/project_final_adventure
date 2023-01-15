import sys
from Mappy import *


class Mapped:
    def __init__(self, height, width, coo_x, coo_y, path):
        self.height = height
        self.width = width
        self.x = coo_x
        self.y = coo_y
        self.path = path

    # def quest(self):
    #   Ajouter une quête sur

    def move(self, dir):

        # Check pour la disponibilité d'aller au nord en fonction du path
        if dir == 1:
            if ((self.x, self.y-1), (self.x, self.y)) not in self.path:
                print("Vous ne pouvez pas allez plus au nord")
            else:
                self.y -= 1
        # Check pour la disponibilité d'aller au sud en fonction du path
        if dir == 2:
            if ((self.x, self.y), (self.x, self.y+1)) not in self.path:
                print("Vous ne pouvez pas allez plus au sud")
            else:
                self.y += 1
        # Check pour la disponibilité d'aller à l'est en fonction du path
        if dir == 3:
            if ((self.x, self.y), (self.x+1, self.y)) not in self.path:
                print("Vous ne pouvez pas allez plus à l'est")
            else:
                self.x += 1
        # Check pour la disponibilité d'aller à l'ouest en fonction du path
        if dir == 4:
            if ((self.x-1, self.y), (self.x, self.y)) not in self.path:
                print("Vous ne pouvez pas allez plus à l'ouest")
            else:
                self.x -= 1
        if dir == 5:
            return 5

    def draw_map(self):
        for y in range(0, self.height):
            for x in range(0, self.width):
                if self.x == x and self.y == y:
                    sys.stdout.write(" ✧ ")  # Place du joueur
                else:
                    if ((x, y), (x, y+1)) in self.path or ((x, y-1), (x, y)) in self.path or ((x-1, y), (x, y)) in self.path:
                        sys.stdout.write(" ▢ ")  # Place vide
                    else:
                        sys.stdout.write(" ▨ ")  # Chemin

                if ((x, y), (x+1, y)) in self.path:
                    sys.stdout.write("-")  # Chemin
                else:
                    sys.stdout.write(" ")  # Chemin vide

            print("")
            # ▢▨▨▨

            for x in range(0, self.width):
                sys.stdout.write(" ")
                if ((x, y), (x, y+1)) in self.path:
                    sys.stdout.write("|  ")
                else:
                    sys.stdout.write("   ")
            print("")

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


# Map du village detruit
DREENSHGARD = [
    ((2, 1), (2, 2)),
    ((1, 2), (2, 2)),
    ((1, 1), (1, 2)),
    ((1, 0), (1, 1)),
    ((0, 2), (1, 2)),
    ((0, 2), (0, 3)),
    ((0, 3), (1, 3)),
    ((1, 3), (2, 3)),
    ((2, 3), (2, 4)),
    ((1, 3), (1, 4)),
    ((0, 0), (0, 1)),
    ((0, 1), (0, 2)),
    ((2, 2), (3, 2)),
    ((2, 3), (3, 3)),
]

FOREST = [
    ((2, 4), (3, 4)),
    ((1, 4), (2, 4)),
    ((2, 3), (2, 4)),
    ((1, 3), (2, 3)),
    ((1, 2), (1, 3)),
    ((0, 2), (1, 2)),
    ((0, 2), (0, 3)),
    ((0, 3), (1, 3)),
    ((1, 3), (1, 4)),
    ((0, 4), (1, 4)),
    ((1, 1), (1, 2)),
    ((0, 1), (1, 1)),
    ((0, 0), (0, 1)),
    ((0, 0), (1, 0)),
    ((1, 0), (2, 0)),
    ((2, 0), (3, 0)),
    ((3, 0), (3, 1)),
    ((2, 1), (3, 1)),
    ((2, 1), (2, 2)),
    ((2, 2), (3, 2)),
]
# Initialisation de la map
# 2, 1 là où on doit commencer le jeu
dreenshgard = Mapped(5, 4, 1, 1, DREENSHGARD)
forest = Mapped(5, 4, 3, 4, FOREST)

coordinate = str(dreenshgard.get_x()) + "," + str(dreenshgard.get_y())
m = Mappy(json_map(str(coordinate)))

# while True:
#     dreenshgard.draw_map()
#     dir = input("Quelle direction souhaitez vous prendre ?\n[1] - Nord\n[2] - Sud\n[3] - Est\n[4] - Ouest\n")
#     dreenshgard.move(dir)
