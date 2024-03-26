from enum import Enum

class Player(Enum):
    RATON = 1
    TACOS = -1
    AUCUN = 0

class Morpion_moteur:
    def __init__(self):
        self.current_player = Player.RATON
        self.board = [[Player.AUCUN for i in range(3)] for j in range(3)]
        self.winner = Player.AUCUN

    def place_symb(self, player: Player, column: int, row: int) -> bool:
        """Add token on lowest row with an empty space"""
        print(self.board[row][column])
        if self.board[row][column] == player.AUCUN:
            self.board[row][column] = player
            return True
        else:
            return False

    def jouer_coup(self, player: Player, column: int, row: int) -> bool:
        """Ajoute un pion et vérifie la victoire"""
        if self.place_symb(player, column, row) == True:
            self.switch_player()
            return self.verif_win(player, column, row)

    def switch_player(self):
        """Change le joueur courant"""
        self.current_player = Player.TACOS if self.current_player == Player.RATON else Player.RATON
        print("Le joueur")

    def verif_win(self, player: Player, click_row, click_col) -> bool:
        """verification de la victoire"""
        # detec ligne gagnante
        i = 0
        checks = (
            lambda x, y: x[y][click_row],
            lambda x, y: x[click_col][y],
            lambda x, y: x[y][y],
            lambda x, y: x[2 - y][y],
        )
        for expr in checks:
            for i in range(3):
                current_bouton = expr(self.board, i)
                # Si on est pas sur une série gagnante, on skip jusqu'à la suivante
                if current_bouton != player:
                    break
            else:
                #si elle est bonne, on remet le bon joueur car il a switch auto et on l'enregistre dans winner
                self.switch_player()
                self.winner = self.current_player
                return True
        # Aucun gagnant de trouvé
        else:
            count = 0
            for col in range(3):
                for row in range(3):
                    current_bouton = self.board[col][row]
                    if current_bouton != player.AUCUN:
                        count += 1
            # Toutes les cases sont remplies = MATCH NUL
            if count == 9:
                print('match nul')
                return True
            else:
                #si pas de gagnant et pas de match nul, on continu la partie
                return False

    def reset_board(self):
        self.board = [[Player.AUCUN for i in range(3)] for j in range(3)]
