
from tkinter import *
import tkinter as tk
import time
from enum import Enum



class Coords:
    def __init__(self, x, y=0):
        if isinstance(x, (list, tuple)):
            y = x[1]
        self.x = x
        self.y = y

    def __add__(self, other_coords):
        return Coords(self.x + other_coords.x,
                      self.y + other_coords.y)

    def outside(self, limits_x, limits_y):
        return not (limits_x[0] <= self.x <= limits_x[1]
            and limits_y[0] <= self.y <= limits_y[1])

class Direction(Enum):
    HAUT = Coords(0, -10)
    BAS = Coords(0, 10)
    GAUCHE = Coords(-10, 0)
    DROITE = Coords(10, 0)
class Snake_moteur:
    def __init__(self):
        self.direction = Direction.BAS

    def next_move(self, snake, fruit):
        x, y = snake.coords[0]
        x, y = x + self.direction.value.x, y + self.direction.value.y
        print(self.direction.name)
        return x, y
    def move(self, direction):
        """fait avancer le serpent"""
        if direction == 1:
            print("test1")
            self.direction = Direction.HAUT
        elif direction == 2:
            print("test1")
            self.direction = Direction.GAUCHE
        elif direction == 3:
            print("test1")
            self.direction = Direction.DROITE
        elif direction == 4:
            print("test1")
            self.direction = Direction.BAS
    def grow_up(self, snake, fruit) -> bool:
        """fait grandir le serpent si il mange une pomme"""
        xs, ys = snake.coords[0]
        xf = fruit.coords[0]
        yf = fruit.coords[1]
        if xs-xf == 0 and ys-yf == 0:
            print("MIAMMMMMM")
            return True



    #savoir si une fonction pour tout mouv ou une fonction par mouvement
    def turn(self):#or def turn_left(self) ... def turn_right(self)
        """faire tourner le serpent de la direction demandé"""
        pass

    def place_apple(self):
        """pose une pomme aleatoirement sur le plateau apres que le serpent est manger une pomme"""
        pass
