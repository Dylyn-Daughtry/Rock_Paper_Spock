from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        user_gesture_choice = int(input()) - 1
        self.chosen_gesture = self.list_of_gestures[user_gesture_choice]
        while user_gesture_choice not in range(-1, len(self.list_of_gestures)):
            print('Selection not available please choose a number from the list')
        return self.chosen_gesture 
        

    def get_gesture(self):
        return self.chosen_gesture

    def get_gesture_list(self):
        return self.list_of_gestures