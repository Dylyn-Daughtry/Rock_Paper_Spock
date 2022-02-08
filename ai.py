from player import Player
import random

class AI(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        self.chosen_gesture = random.choice(self.list_of_gestures)
        print(f'Your opponent chose {self.chosen_gesture}.')
        return self.chosen_gesture