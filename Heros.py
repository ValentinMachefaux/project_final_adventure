from character.Character import *
import pygame as pg
import sys
import os
import pytmx

vec = pg.math.Vector2

PLAYER_SPEED = 300



class Heros(Character,pg.sprite.Sprite):
    def __init__(self):
        super().__init__(self)
        self.vel = vec(0, 0)

    def get_keys(self):
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_q]:
            self.vel.x = -PLAYER_SPEED
            self.walk.play()
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vel.x = PLAYER_SPEED
            self.walk.play()
        if keys[pg.K_UP] or keys[pg.K_z]:
            self.vel.y = -PLAYER_SPEED
            self.walk.play()
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel.y = PLAYER_SPEED
            self.walk.play()
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071

    # TO DO : recup les mouvements, get le menu, get les interactions