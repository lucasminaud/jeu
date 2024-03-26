from enum import Enum

class Player(Enum):
    RATON = 1
    TACOS = -1
    AUCUN = 0

class P4_moteur:
    def __init__(self):
        self.current_player = Player.RATON
        self.board = [[Player.AUCUN for i in range(7)] for j in range(6)]
        self.winner = Player.AUCUN

    def place_symb(self, player: Player, column: int) -> int:
        """Add token on lowest row with an empty space"""
        current_row=5
        for row in reversed(self.board):
            if row[column] == Player.AUCUN:
                row[column] = player
                print('placer')
                break
            else:
                current_row -= 1
        return current_row

    def jouer_coup(self, player: Player, column: int) -> bool:
        """Ajoute un pion et vérifie la victoire"""
        row = self.place_symb(player, column)
        win = self.verif_win(player, column, row)
        self.switch_player()
        return win

    def switch_player(self):
        """Change le joueur courant"""
        self.current_player = Player.TACOS if self.current_player == Player.RATON else Player.RATON

    def verif_win(self, player: Player, click_col : int, current_row : int) -> bool:
        """verifie si le pion poser créé une ligne gagnante"""
        #verification de victoire VERTICAL
        count = 1
        if current_row >2:
            return False
        for k in range(1,4):
            if self.board[current_row + k][click_col] == player:
                count += 1
            else:
                return False
        if not count > 2:
            return False
        self.winner = self.current_player
        return True
    def reset_board(self):
        self.board = [[Player.AUCUN for i in range(7)] for j in range(6)]