from enum import Enum

class Player(Enum):
    RATON = 1
    TACOS = -1
    AUCUN = 0

class Morpion_moteur:
    def __init__(self):
        self.current_player = Player.RATON
        self.board = [[Player.AUCUN for i in range(3)] for j in range(3)]
        self.winner = Player.AUCUN.name

    def place_symb(self, player: Player, column: int, row: int) -> None:
        """Add token on lowest row with an empty space"""
        if self.board[row][column] == Player.AUCUN:
            self.board[row][column] = player

    def jouer_coup(self, player: Player, column: int, row: int) -> int:
        """Ajoute un pion et vérifie la victoire"""
        self.place_symb(player, column, row)
        self.switch_player()
        return self.verif_win(player, column, row)

    def switch_player(self):
        """Change le joueur courant"""
        self.current_player = Player.TACOS if self.current_player == Player.RATON else Player.RATON

    def verif_win(self, player: Player, click_row, click_col) -> int:
        # detec ligne gagnante
        i = 0
        checks = (
            lambda x, y: x[y][click_row],
            lambda x, y: x[click_col][y],
            lambda x, y: x[y][y],
            lambda x, y: x[2 - y][y],
        )
        for expr in checks:
            count = 0
            for i in range(3):
                current_bouton = expr(self.board, i)
                # Si on est pas sur une série gagnante, on skip jusqu'à la suivante
                if current_bouton != player:
                    break
            else:
                self.winner = self.current_player.name
                return 1
        # Aucun gagnant de trouvé
        else:
            count = 0
            for col in range(3):
                for row in range(3):
                    current_bouton = self.board[col][row]
                    if current_bouton != player.AUCUN:
                        count += 1
            # Toutes les cases sont remplies
            if count == 9:
                print('match nul')

        return 2

