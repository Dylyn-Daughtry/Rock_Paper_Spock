from human import Human
from ai import AI
from player import Player

class Game:
    def __init__(self):
        self.player_one = Player()
        self.ai_one = AI()

    def run_game(self):
        self.display_welcome()
        self.ai_one.choose_gesture()
        self.select_gesture()

    def display_welcome(self):
        print(f'Welcome Player(s) to Rock, Paper, Scissors, Lizard, Spock \n' + 
        'Rock crushes Scissors\n' +
        'Scissors cuts Paper\n' +
        'Paper covers Rock\n' +
        'Rock crushes Lizard\n' +
        'Lizard poisons Spock\n' +
        'Spock smashes Scissors\n' + 
        'Scissors decapitates Lizard\n' + 
        'Lizard eats Paper \n' +
        'Paper disproves Spock \n' + 
        'Spock vaporizes Rock \n') 

    def number_of_players(self):
        pass

    def select_gesture(self):
        count = 0
        for gesture in self.player_one.list_of_gestures:
            print(f'Input {count} to select {self.player_one.list_of_gestures[count]}')
            count += 1