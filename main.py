import tkinter as tk
from tkinter import ttk
import morpion_interface as morp_UI
#import puissance4  # TODO: delete
import puissance4_interface as p4_UI
import snake
import solitaire


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.boutons = []
        # configure the root window
        self.title('My Awesome App')

        self.delete_button_worker(self.boutons),
        self.main()

    def main(self):
        #nettoyage de la page
        self.delete_button_worker(self.boutons)
        self.grid()
        # label pour menu
        self.label = ttk.Label(self, text='Bienvenue')
        self.label.grid()
        # creation des boutons menu
        associations = [
            # Shhh, c'est notre petit secret ( ͡° ͜ʖ ͡°)
            ["morpion", self.display_morpion],
            ["puissance 4", self.display_p4],
            #["puissance 4", puissance4.Puissance],  # TODO: del
            ["snake", snake.Snake],
            ["solitaire", solitaire.Solitaire],
            ["quiter", self.quite]
        ]
        for name, function in associations:
            self.button = ttk.Button(
                self,
                text=name,
                padding=20,
                command=lambda x=function: self.lance_jeu(x)
            )
            # affichage des boutons du menu
            self.button.grid()
            # memorisation des boutons pour action
            self.boutons.append(self.button)

    def lance_jeu(self, fonction):
        self.delete_button_worker(self.boutons)
        self.label.destroy()
        self.grid()
        fonction(self)

    def display_morpion(self, monculv2):
        morp = morp_UI.Morpion_interface(self)
        morp.grid()
    def display_p4(self, moncul):
        p4 = p4_UI.P4_interface(self)
        p4.grid()

    def delete_button_worker(self, cursed_data_structure):
        if isinstance(cursed_data_structure, ttk.Button):
            cursed_data_structure.destroy()
        else:
            for cursed_container in cursed_data_structure:
                self.delete_button_worker(cursed_container)

    def solitaire(self):
        pass

    def quite(self, fictif):
        fictif = fictif
        self.destroy()


if __name__ == '__main__':
    root = App()
    root.mainloop()
