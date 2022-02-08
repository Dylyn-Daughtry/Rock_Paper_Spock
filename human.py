from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        is_gesture = False
        while is_gesture != True:
            user_gesture_choice = int(input()) - 1
            if user_gesture_choice not in range(0, 5):
                print('Bad input. Please select again.')
            else:
                self.chosen_gesture = self.list_of_gestures[user_gesture_choice]
                is_gesture = True

        return self.chosen_gesture 
        

    def get_gesture(self):
        return self.chosen_gesture

    def get_gesture_list(self):
        return self.list_of_gestures