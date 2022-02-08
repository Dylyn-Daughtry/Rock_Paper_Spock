
class Player:
    def __init__(self):
        self.wins = 0
        self.name = ""
        self.chosen_gesture = ""
        self.list_of_gestures = []
        self.gestures()

    def choose_gesture(self):
        pass

    def gestures(self):
        rock = 'Rock' # index 0
        paper = 'Paper' # index 1
        scissors = 'Scissors' # index 2
        lizard = 'Lizard' # index 3
        spock = 'Spock' # index 4
        
        self.list_of_gestures.append(rock)
        self.list_of_gestures.append(paper)
        self.list_of_gestures.append(scissors)
        self.list_of_gestures.append(lizard)
        self.list_of_gestures.append(spock)