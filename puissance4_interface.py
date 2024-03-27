import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from puissance4_moteur import *


class P4_interface(tk.Frame):

    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.moteur = P4_moteur()
        self.root.title('Puissance 4')
        self.winner = Player.AUCUN

        self.board: list[list[ttk.Button]] = []
        self.label = tk.Label(self, text='Puissance 4')
        self.label.grid(column=3)

        # integration des images
        #image pour Victoire
        image_attente = Image.open("./assets/blanc.png").resize((150, 180), Image.NEAREST)
        imageR = Image.open("./assets/raton.jpg").resize((150, 180), Image.NEAREST)
        imageT = Image.open("./assets/tacos.jpg").resize((150, 180), Image.NEAREST)
        self.root.blancV = ImageTk.PhotoImage(image=image_attente)
        self.root.ratonV = ImageTk.PhotoImage(imageR)
        self.root.tacosV = ImageTk.PhotoImage(imageT)
        #image pour plateau
        image_attente = image_attente.resize((30, 40), Image.NEAREST)
        imageR = imageR.resize((30, 40), Image.NEAREST)
        imageT = imageT.resize((30, 40), Image.NEAREST)
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

    def get_corresponding_imageWIN(self, player) -> ImageTk.PhotoImage:
        """Donne la correspondance entre un joueur et son image"""
        if player == Player.AUCUN:
            return self.root.blancV
        elif player == Player.RATON:
            return self.root.ratonV
        else:  # player == Player.TACOS
            return self.root.tacosV

    def empty_board(self):
        """Vide le plateau"""
        for row in self.board:
            for button in row:
                button.destroy()

    def jouer_coup(self, player, column):
        if self.moteur.jouer_coup(player, column) == True:
            self.win()
        else:
            self.create_buttons()



    def win(self):
        """création de l'interface de victoire"""
        self.empty_board()
        self.label.destroy()
        self.label = tk.Label(self, text='le Gagnant est ' + self.moteur.winner.name + '!')
        self.label.grid(column=1)

        image = self.get_corresponding_imageWIN(self.moteur.winner)
        self.afficheWIN = Canvas(
            self,
            width=170,
            height=200,
            bg='ivory'
        )
        self.afficheWIN.create_image(10, 10, anchor=NW, image=image)

        self.afficheWIN.grid(column=1)

        self.rejouer = ttk.Button(
            self,
            text="REJOUER",
            padding=20,
            command=lambda x= 1: self.end_game(x)
        )
        # affichage des boutons du menu
        self.rejouer.grid(column=0, row=2)

        self.menu = ttk.Button(
            self,
            text="MENU",
            padding=20,
            command=lambda x= 2: self.end_game(x)
        )
        # affichage des boutons du menu
        self.menu.grid(column=2, row=2)

    def end_game(self, choix):
        self.moteur.reset_board()
        self.afficheWIN.destroy()
        self.rejouer.destroy()
        self.menu.destroy()
        self.label.destroy()
        self.empty_board()
        if choix == 1:
            self.label = tk.Label(self, text='Puissance 4')
            self.label.grid(column=3)
            self.create_buttons()
        else: #egal à 2
            self.root.main()
            self.destroy()



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
                    command=lambda column_index=j,: self.jouer_coup(self.moteur.current_player, column_index),
                )
                column.append(button)
                button.grid(row=i+1, column=j)
            self.board.append(column)
