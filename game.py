from human import Human
from ai import AI
from player import Player

class Game:
    def __init__(self):
        self.player_one = Player()
        self.human_one = Human()
        self.ai_one = AI()

    def run_game(self):
        self.display_welcome()
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
        # need display message to ask for number of players
        # if condition may be needed to create player objects in Player file if more than two
        # if condition may be needed for whether the player(s) are human or ai
        pass

    def select_gesture(self):
        count = 0
        for gesture in self.player_one.list_of_gestures:
            print(f'Input {count} to select {gesture}')
            count += 1
        self.human_one.choose_gesture() # can call user gesture method here instead of in run game
        self.ai_one.choose_gesture() # may need to place ai gesture here too

    def user_gesture_capture(self):
        user_gesture = int(input())
        chosen_gesture = self.human_one.choose_gesture(user_gesture)
        print(chosen_gesture) # print chosen gesture
        # return chosen_gesture # or return chosen gesture, return might be better for comparison condition later

    def determine_winner(self):
        if self.human_one.get_gesture() == self.ai_one.chosen_gesture:
            print(f'Its a Tie!')
        elif self.player_one.chosen_gesture == 'Rock':
            if self.ai_one.chosen_gesture == 'Scissors':
                print('Rock crushes scissors!')
            elif self.ai_one.chosen_gesture == 'Paper':
                print('Paper covers Rock!')
            elif self.ai_one.chosen_gesture == 'Lizard':
                print('Rock crushes Lizard!')
            elif self.ai_one.chosen_gesture == 'Spock':
                print('Spock Vaporizes Rock')