
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
        rock = 'Rock'
        paper = 'Paper'
        scissors = 'Scissors'
        lizard = 'Lizard'
        spock = 'Spock'
        
        self.list_of_gestures.append(rock)
        self.list_of_gestures.append(paper)
        self.list_of_gestures.append(scissors)
        self.list_of_gestures.append(lizard)
        self.list_of_gestures.append(spock)