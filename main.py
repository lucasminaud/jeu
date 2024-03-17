import tkinter as tk
from tkinter import ttk
import morpion
import puissance4

class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.boutons = []
        # configure the root window
        self.title('My Awesome App')

        self.main()

    def main(self):
        # label pour menu
        self.label = ttk.Label(self, text='Bienvenue')
        self.label.grid()
        #creation des boutons menu
        associations = [
            ["morpion", morpion.Morpion],
            ["puissance 4", puissance4.Puissance],
            ["snake", self.snake],
            ["solitaire", self.solitaire],
            ["quiter", self.quite]
        ]
        for name, function in associations:
            self.button = ttk.Button(
                self,
                text=name,
                padding=20,
                command=lambda x=function: self.lance_jeu(x)
            )
            #affichage des boutons du menu
            self.button.grid()
            #memorisation des boutons pour action
            self.boutons.append(self.button)
    def lance_jeu(self, fonction):
        print(self.boutons)
        self.label.destroy()
        self.grid()
        fonction()

    def delete_button_worker(self, cursed_data_structure):
        if isinstance(cursed_data_structure, ttk.Button):
            cursed_data_structure.destroy()
        else:
            for cursed_container in cursed_data_structure:
                self.delete_button_worker(cursed_container)

    def snake(self):
        pass

    def solitaire(self):
        pass
    def quite(self):
        self.destroy()



if __name__ == '__main__':
    root = App()
    root.mainloop()