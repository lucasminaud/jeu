from enum import Enum

class Player(Enum):
    RATON = 1
    TACOS = -1
    AUCUN = 0

class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other_coords):
        return Coords(self.x + other_coords.x,
                      self.y + other_coords.y)

    def outside(self, limits_x, limits_y):
        return not (limits_x[0] <= self.x <= limits_x[1]
            and limits_y[0] <= self.y <= limits_y[1])

    def get_cell(self, board):
        print(self.x , self.y)
        return board[self.y][self.x]

class P4_moteur:
    def __init__(self):
        self.current_player = Player.RATON
        self.board = [[Player.AUCUN for i in range(7)] for j in range(6)]
        self.winner = Player.AUCUN
        self.nul = 0

    def place_symb(self, player: Player, column: int) -> int:
        """Add token on lowest row with an empty space"""
        current_row=5
        for row in reversed(self.board):
            if row[column] == Player.AUCUN:
                row[column] = player
                self.nul += 1
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
        position = Coords(click_col, current_row)

        #verification de victoire VERTICAL (first methode)
        #####
        #print("click sa mere")
        #count = 1
        #for k in range(1,4):
        #    if current_row+k <=5 and self.board[current_row + k][click_col] == player:
        #        count += 1
        #if count > 3:
        #    self.winner = self.current_player
        #    return True
        #####

        #on defini les directions pour les diferentes verifs
        # verif vertical
        countV = 0
        directionV = Coords(0, 1)

        #verif horizontal
        countH = 0
        directionD = Coords(1, 0)
        directionG = Coords(-1, 0)

        #verif diagonal haut bas
        countHB = 0
        dirDiagHBD = Coords(1, -1)
        dirDiagHBG = Coords(-1, 1)

        # verif diagonal bas haut
        countBH = 0
        dirDiagBHD = Coords(1, 1)
        dirDiagBHG = Coords(-1, -1)

        # on associe a compte avec la direction
        associations = [
            [countV, directionV],
            [countH, directionD],
            [countH, directionG],
            [countHB, dirDiagHBD],
            [countHB, dirDiagHBG],
            [countBH, dirDiagBHD],
            [countBH, dirDiagBHG],
        ]
        #on applique la recursion sur toutes les associations
        for count, direction in associations:
            count += self.recursion(position + direction, direction, player)
            if count > 2:
                self.winner = self.current_player
                return True
        if self.nul > 41:
            self.winner = player.AUCUN
            return True
        return False

    def recursion(self, position: Coords, direction: Coords, player: Player) -> int:
        """permet de regarder le pion dans la direction qu'on lui indique et compte combiens sont identiques de la direction"""
        if position.outside([0, 6], [0, 5]) or position.get_cell(self.board) != player:
            return 0
        new_pos = position + direction
        return 1 + self.recursion(new_pos, direction, player)

    def reset_board(self):
        """reinitialise le plateau"""
        self.board = [[Player.AUCUN for i in range(7)] for j in range(6)]
        self.nul = 0