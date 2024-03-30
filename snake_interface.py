import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from snake_moteur import *
import random
import time




class Snake_interface(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.moteur = Snake_moteur()
        self.root.title('Puissance 4')
        self.label = tk.Label(self, text='SNAKE')
        self.label.grid()
        self.WIDTH = 500
        self.HEIGHT = 500
        self.board = Canvas(
            self,
            width=self.WIDTH,
            height=self.HEIGHT,
            bg='white'
        )
        self.root.update()
        self.board.bind("<Key-Up>", lambda: self.moteur.move())
        self.board.bind("<Key-Left>", lambda event: self.moteur.move)
        self.board.bind("<Key-Right>", lambda event: self.moteur.move)
        self.board.bind("<Key-Down>", lambda event: self.moteur.move)
        self.board.grid()
        self.start()



    def start(self):

        snake = Snake(self)
        fruit = Fruit(self)
        self.next_move(snake, fruit)

    def next_move(self, snake, fruit):
        x, y = self.moteur.next_move(snake, fruit)
        snake.coords.insert(0, (x, y))
        body = self.board.create_rectangle(
            x, y, x + 10, y + 10, fill="blue"
        )
        print(snake.coords, 'coordinates')
        print(body, 'body')
        snake.bodys.insert(0, body)
        print("test")

        del snake.coords[-1]

        self.board.delete(snake.bodys[-1])

        del snake.bodys[-1]

        self.root.after(2000, self.next_move, snake, fruit)



    def delete_snake(self, snake):
        self.board.delete(snake)

class Fruit:
    def __init__(self,plateau: Snake_interface):
        self.plateau = plateau

        x = random.randint(0,
                           self.plateau.WIDTH - 1)
        y = random.randint(0,
                           self.plateau.HEIGHT - 1)
        self.coords = [x, y]
        self.plateau.board.create_oval(
            x, y, x + 10, y + 10, fill="red"
        )

class Snake:
    def __init__(self, plateau: Snake_interface):

        self.plateau = plateau
        self.body_count = 2
        self.coords = []
        self.bodys = []

        for i in range(0, self.body_count):
            self.coords.append([0, 0])
        for x, y in self.coords:
            body = self.plateau.board.create_rectangle(
                x, y, x + 10, y + 10, fill="blue"
            )
            self.bodys.append(body)