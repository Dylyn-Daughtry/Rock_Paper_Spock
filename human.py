from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        user_gesture = int(input())
        chosen_gesture = self.list_of_gestures[user_gesture]
        print(chosen_gesture) # print chosen gesture
        return chosen_gesture # or return chosen gesture, return might be better for comparison condition later