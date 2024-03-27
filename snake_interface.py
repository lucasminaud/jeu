import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from snake_moteur import *

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
        self.start()

    def start(self):
        pass