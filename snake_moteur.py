import time

class Snake_moteur:
    def __init__(self):
        self.x_head= 170
        self.y_head= 300
        self.x_tail= 100
        self.x_tail= 300
        self.head = self.x_head, self.y_head
        self.tail = self.x_tail, self.x_tail

    def place_snake(self):
        self.move()
        pass
    def move(self):
        """fait avancer le serpent"""
        self.x_tail += 10
        self.x_head += 10
        self.head = self.x_head, self.y_head
        self.tail = self.x_tail, self.x_tail
    def grow_up(self):
        """fait grandir le serpent si il mange une pomme"""
        pass


    #savoir si une fonction pour tout mouv ou une fonction par mouvement
    def turn(self):#or def turn_left(self) ... def turn_right(self)
        """faire tourner le serpent de la direction demandé"""
        pass

    def place_apple(self):
        """pose une pomme aleatoirement sur le plateau apres que le serpent est manger une pomme"""
        pass
