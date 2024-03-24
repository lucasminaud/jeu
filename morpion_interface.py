import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from morpion_moteur import *


class Morpion_interface(tk.Frame):

    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.moteur = Morpion_moteur()
        self.root.title('Morpion')

        self.board: list[list[ttk.Button]] = []
        self.label = tk.Label(self, text='Morpion')
        self.label.grid(column=1)

        # integration des images
        image_attente = Image.open("./assets/blanc.png").resize((30, 40), Image.NEAREST)
        imageR = Image.open("./assets/raton.jpg").resize((30, 40), Image.NEAREST)
        imageT = Image.open("./assets/tacos.jpg").resize((30, 40), Image.NEAREST)
        self.root.blanc = ImageTk.PhotoImage(image=image_attente)
        self.root.raton = ImageTk.PhotoImage(imageR)
        self.root.tacos = ImageTk.PhotoImage(imageT)

        self.create_buttons()

    def get_corresponding_image(self, player) -> ImageTk.PhotoImage:
        """Donne la correspondance entre un joueur et son image"""
        if player == Player.AUCUN:
            return self.root.blanc
        elif player == Player.RATON:
            return self.root.raton
        else:  # player == Player.TACOS
            return self.root.tacos

    def empty_board(self):
        """Vide le plateau"""
        for row in self.board:
            for button in row:
                button.destroy()

    def jouer_coup(self, player, column, row):
        self.moteur.jouer_coup(player, column, row)
        if self.moteur.jouer_coup(player, column, row) == 2:
            print(self.moteur.jouer_coup)
        elif self.moteur.jouer_coup(player, column, row) == 0:
            pass
        else:
            self.create_buttons()

    def win(self):
        self.empty_board()
        image = self.get_corresponding_image(self.moteur.current_player)
        button = ttk.Button(
            self,
            text='moncul',
            padding=15,
            image=image,
        )

    def create_buttons(self):
        """(Ré)génère tout le plateau de jeu"""
        self.empty_board()
        for i, row in enumerate(self.moteur.board):
            column = []
            for j, case_ in enumerate(row):
                image = self.get_corresponding_image(case_)
                button = ttk.Button(
                    self,
                    text='moncul',
                    padding=15,
                    image=image,
                    command=lambda column_index=j, row_index=i : self.jouer_coup(self.moteur.current_player, column_index , row_index),
                )
                column.append(button)
                button.grid(row=i+1, column=j)
            self.board.append(column)
