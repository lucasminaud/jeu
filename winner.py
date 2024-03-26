import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

import main
from main import *
from morpion_moteur import *

class Winner(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        self.root = root
        self.root.title("WINNER")
        self.main = main.App()
        self.moteur = Morpion_moteur()


        # integration des images
        image_attente = Image.open("./assets/blanc.png").resize((100, 120), Image.NEAREST)
        imageR = Image.open("./assets/raton.jpg").resize((100, 120), Image.NEAREST)
        imageT = Image.open("./assets/tacos.jpg").resize((100, 120), Image.NEAREST)
        self.root.blanc = ImageTk.PhotoImage(image=image_attente)
        self.root.raton = ImageTk.PhotoImage(imageR)
        self.root.tacos = ImageTk.PhotoImage(imageT)

        self.create_board()

    def create_board(self):
        image = self.get_corresponding_image(self.moteur.winner)
        afficheWIN = Canvas(
            self,
            width=500,
            height=500,
            bg='ivory'
        )
        afficheWIN.create_image(10, 10, anchor=NW, image=image)

        afficheWIN.grid()

        rejouer = ttk.Button(
            self,
            text="REJOUER",
            padding=20,
            command=main
        )
        # affichage des boutons du menu
        rejouer.grid(column=0, row=1)

        menu = ttk.Button(
            self,
            text="MENU",
            padding=20,
        )
        # affichage des boutons du menu
        menu.grid(column=1, row=1)

    def get_corresponding_image(self, player) -> ImageTk.PhotoImage:
        """Donne la correspondance entre un joueur et son image"""
        if player == Player.AUCUN:
            return self.root.blanc
        elif player == Player.RATON:
            return self.root.raton
        else:  # player == Player.TACOS
            return self.root.tacos

