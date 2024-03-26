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
        self.current_row = 7

    def place_symb(self, player: Player, column: int) -> None:
        """Add token on lowest row with an empty space"""
        self.current_row=7
        for row in reversed(self.board):
            if row[column] == Player.AUCUN:
                row[column] = player
                print('placer')
                break
            else:
                self.current_row -= 1

    def jouer_coup(self, player: Player, column: int) -> bool:
        """Ajoute un pion et vérifie la victoire"""
        self.place_symb(player, column)
        self.switch_player()
        print(self.current_row, self.board)
        return self.verif_win(player, column)

    def switch_player(self):
        """Change le joueur courant"""
        self.current_player = Player.TACOS if self.current_player == Player.RATON else Player.RATON

    def verif_win(self, player: Player, click_col) -> bool:
        """verifie si le pion poser créé une ligne gagnante"""
        #verification de victoire VERTICAL
        verifV = []
        for k in range(1,4):
            print(click_col)
            if self.board[self.current_row + k][click_col] == player and self.current_row-k<7 :
                print(k)
                verifV.append(k)
        n1=len(verifV)
        if n1 > 2:
            self.switch_player()
            self.winner = self.current_player
            print("bordel")
            return True
        else:
            print ('tamere')
            return False

    def reset_board(self):
        self.board = [[Player.AUCUN for i in range(7)] for j in range(6)]