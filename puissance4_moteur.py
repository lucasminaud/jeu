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
        print("click sa mere")
        count = 1
        for k in range(1,4):
            if current_row+k <=5 and self.board[current_row + k][click_col] == player:
                count += 1
        if count > 3:
            self.winner = self.current_player
            return True
        #verif horizontal par recurtion
        countH = 0
        directionD = Coords(1, 0)
        directionG = Coords(-1, 0)
        position = Coords(click_col, current_row)
        countH = self.recursion(position+directionD, directionD, player)
        countH += self.recursion(position+directionG, directionG, player)
        print(countH)
        if countH > 2:
            self.winner = self.current_player
            return True
        return False

    def recursion(self, position: Coords, direction: Coords, player: Player) -> int:
        if position.outside([0, 6], [0, 5]) or position.get_cell(self.board) != player:
            return 0
        new_pos = position + direction
        return 1 + self.recursion(new_pos, direction, player)

    def reset_board(self):
        self.board = [[Player.AUCUN for i in range(7)] for j in range(6)]