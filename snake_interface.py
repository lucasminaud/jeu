import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from snake_moteur import *
import time

class Snake_interface(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.moteur = Snake_moteur()
        self.root.title('Puissance 4')
        self.label = tk.Label(self, text='SNAKE')
        self.label.grid()
        self.board = Canvas(
            self,
            width=600,
            height=600,
            bg='ivory'
        )
        self.board.grid()
        self.snake = self.board.create_line(self.moteur.head, self.moteur.tail, width=4, fill="green")
        self.board.grid()
        self.start()

    def start(self):
        #for i in range(50):
            time.sleep(1)# Sleep for 1 seconds
            print(self.moteur.head)
            #self.moteur.place_snake()
            self.board.after(2000, self.delete_snake, self.snake)
            time.sleep(1)  # Sleep for 1 seconds
            self.snake = self.board.create_line(100, 50, 500, 400, width=4, fill="green")
        #pass


    def delete_snake(self, snake):
        self.board.delete(snake)
