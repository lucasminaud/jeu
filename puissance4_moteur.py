from enum import Enum

class Player(Enum):
    RATON = 1
    TACOS = -1
    AUCUN = 0

class P4_moteur:
    def __init__(self):
        self.current_player = Player.RATON
        self.board = [[Player.AUCUN for i in range(7)] for j in range(6)]

    def place_symb(self, player: Player, column: int) -> None:
        """Add token on lowest row with an empty space"""
        for row in reversed(self.board):
            if row[column] == Player.AUCUN:
                row[column] = player
                break

    def jouer_coup(self, player: Player, column: int):
        """Ajoute un pion et vérifie la victoire"""
        self.place_symb(player, column)
        self.switch_player()
        return self.verif_win()

    def switch_player(self):
        """Change le joueur courant"""
        self.current_player = Player.TACOS if self.current_player == Player.RATON else Player.RATON

    def verif_win(self) -> bool:
        return False
