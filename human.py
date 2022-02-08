from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        user_gesture_choice = int(input())
        self.chosen_gesture = self.list_of_gestures[user_gesture_choice]
        print(f'You chose {self.chosen_gesture}.') # prints chosen gesture
        return self.chosen_gesture # or return chosen gesture, return might be better for comparison condition later