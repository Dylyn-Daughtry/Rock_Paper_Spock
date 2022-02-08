from human import Human
from ai import AI
from player import Player
import os
clear = lambda: os.system('cls')



class Game:
    def __init__(self):
        self.player_one = Player()
        self.human_one = Human()
        self.human_two = Human()
        self.ai_one = AI()

    def run_game(self):
        self.display_welcome()
        self.number_of_players()
    
    def display_welcome(self):
        print(f'Welcome Player(s) to Rock, Paper, Scissors, Lizard, Spock \n' + 
        '\n' +
        'The rules are as follows:\n' +
        '\n' +
        '   -Rock crushes Scissors\n' +
        '   -Scissors cuts Paper\n' +
        '   -Paper covers Rock\n' +
        '   -Rock crushes Lizard\n' +
        '   -Lizard poisons Spock\n' +
        '   -Spock smashes Scissors\n' + 
        '   -Scissors decapitates Lizard\n' + 
        '   -Lizard eats Paper \n' +
        '   -Paper disproves Spock \n' + 
        '   -Spock vaporizes Rock \n') 

    def number_of_players(self):
        # need display message to ask for number of players
        # if condition may be needed to create player objects in Player file if more than two
        # if condition may be needed for whether the player(s) are human or ai
        print('Choose game mode:\n')
        print('Press 1 for single player\n' +
        'Press 2 for mutliplayer')
        choose_game_mode = input()

        if choose_game_mode == '1':
            self.human_vs_ai()
        elif choose_game_mode == '2':
            self.human_vs_human()

    def display_gesture_options(self):
        count = 0
        for gesture in self.human_one.get_gesture_list():
            print(f'Input {count + 1} to select {gesture}')
            count += 1
        #self.human_one.choose_gesture() # can call user gesture method here instead of in run game
        #self.ai_one.choose_gesture() # may need to place ai gesture here too
    
    def singleplayer(self):
        self.display_gesture_options()
        self.human_one.choose_gesture()
        self.ai_one.choose_gesture()

    def multiplayer(self):
        self.display_gesture_options()
        self.human_one.choose_gesture()

        self.display_gesture_options()
        self.human_two.choose_gesture()

    def human_vs_ai(self):
        player_one_wins = self.player_one.wins
        player_two_wins = self.player_one.wins
        
        while player_one_wins != 2 and player_two_wins != 2:
            self.singleplayer()
            if self.human_one.get_gesture() == self.ai_one.chosen_gesture:
                print(f'Its a Tie!')
            elif self.human_one.get_gesture() == self.player_one.list_of_gestures[0]:
                if self.ai_one.chosen_gesture == self.player_one.list_of_gestures[1]:
                    print('Rock crushes scissors!')
                    player_one_wins += 1
                elif self.ai_one.chosen_gesture == self.player_one.list_of_gestures[2]:
                    print('Paper covers Rock!')
                    player_two_wins += 1
                elif self.ai_one.chosen_gesture == self.player_one.list_of_gestures[3]:
                    print('Rock crushes Lizard!')
                    player_one_wins += 1
                elif self.ai_one.chosen_gesture == self.player_one.list_of_gestures[4]:
                    print('Spock Vaporizes Rock!')
                    player_two_wins += 1
            elif self.human_one.get_gesture() == self.player_one.list_of_gestures[1]:
                if self.ai_one.chosen_gesture == self.player_one.list_of_gestures[0]:
                    print('Paper covers Rock')
                    player_one_wins += 1
                elif self.ai_one.chosen_gesture == self.player_one.list_of_gestures[2]:
                    print('Scissors cut Paper')
                    player_two_wins += 1
                elif self.ai_one.chosen_gesture == self.player_one.list_of_gestures[3]:
                    print('Lizard eats Paper')
                    player_one_wins += 1
                elif self.ai_one.chosen_gesture == self.player_one.list_of_gestures[4]:
                    print('Paper disproves Spock')
                    player_one_wins += 1
            elif self.human_one.get_gesture() == self.player_one.list_of_gestures[2]:
                if self.ai_one.chosen_gesture == self.player_one.list_of_gestures[0]:
                    print('Rock crushes Scissors')
                    player_two_wins += 1
                elif self.ai_one.chosen_gesture == self.player_one.list_of_gestures[1]:
                    print('Scissors cut Paper')
                    player_one_wins += 1
                elif self.ai_one.chosen_gesture == self.player_one.list_of_gestures[3]:
                    print('Scissors decapitates Lizard')
                    player_one_wins += 1
                elif self.ai_one.chosen_gesture == self.player_one.list_of_gestures[4]:
                    print('Spock Smashes Scissors')
                    player_two_wins += 1
            elif self.human_one.get_gesture() == self.player_one.list_of_gestures[3]:
                if self.ai_one.chosen_gesture == self.player_one.list_of_gestures[0]:
                    print('Rock crushes Lizard')
                    player_two_wins += 1
                elif self.ai_one.chosen_gesture == self.player_one.list_of_gestures[1]:
                    print('Lizard eats Paper')
                    player_one_wins += 1
                elif self.ai_one.chosen_gesture == self.player_one.list_of_gestures[2]:
                    print('Scissors decapiates Lizard')
                    player_two_wins += 1
                elif self.ai_one.chosen_gesture == self.player_one.list_of_gestures[4]:
                    print('Lizard poisons Spock')
                    player_one_wins += 1
            elif self.human_one.get_gesture() == self.player_one.list_of_gestures[4]:
                if self.ai_one.chosen_gesture == self.player_one.list_of_gestures[0]:
                    print('Spock vaporizes Rock')
                    player_one_wins += 1
                elif self.ai_one.chosen_gesture == self.player_one.list_of_gestures[1]:
                    print('Paper disproves Spock')
                    player_two_wins += 1
                elif self.ai_one.chosen_gesture == self.player_one.list_of_gestures[2]:
                    print('Spock smashes Scissors')
                    player_one_wins += 1
                elif self.ai_one.chosen_gesture == self.player_one.list_of_gestures[3]:
                    print('Lizard poisons Spock')
                    player_two_wins += 1
            
        if player_one_wins > player_two_wins:
            print('You win!')
        elif player_two_wins > player_one_wins:
            print('AI two wins!')

    def human_vs_human(self):
        player_one_wins = self.player_one.wins
        player_two_wins = self.player_one.wins
        
        while player_one_wins != 2 and player_two_wins != 2:
            self.multiplayer()
            #self.select_gesture()
            if self.human_one.get_gesture() == self.human_two.get_gesture():
                print(f'Its a Tie!')
            elif self.human_one.get_gesture() == self.player_one.list_of_gestures[0]:
                if self.human_two.chosen_gesture == self.player_one.list_of_gestures[1]:
                    print('Rock crushes scissors!')
                    player_one_wins += 1
                elif self.human_two.chosen_gesture == self.player_one.list_of_gestures[2]:
                    print('Paper covers Rock!')
                    player_two_wins += 1
                elif self.human_two.chosen_gesture == self.player_one.list_of_gestures[3]:
                    print('Rock crushes Lizard!')
                    player_one_wins += 1
                elif self.human_two.chosen_gesture == self.player_one.list_of_gestures[4]:
                    print('Spock Vaporizes Rock!')
                    player_two_wins += 1
            elif self.human_one.get_gesture() == self.player_one.list_of_gestures[1]:
                if self.human_two.chosen_gesture == self.player_one.list_of_gestures[0]:
                    print('Paper covers Rock')
                    player_one_wins += 1
                elif self.human_two.chosen_gesture == self.player_one.list_of_gestures[2]:
                    print('Scissors cut Paper')
                    player_two_wins += 1
                elif self.human_two.chosen_gesture == self.player_one.list_of_gestures[3]:
                    print('Lizard eats Paper')
                    player_one_wins += 1
                elif self.human_two.chosen_gesture == self.player_one.list_of_gestures[4]:
                    print('Paper disproves Spock')
                    player_one_wins += 1
            elif self.human_one.get_gesture() == self.player_one.list_of_gestures[2]:
                if self.human_two.chosen_gesture == self.player_one.list_of_gestures[0]:
                    print('Rock crushes Scissors')
                    player_two_wins += 1
                elif self.human_two.chosen_gesture == self.player_one.list_of_gestures[1]:
                    print('Scissors cut Paper')
                    player_one_wins += 1
                elif self.human_two.chosen_gesture == self.player_one.list_of_gestures[3]:
                    print('Scissors decapitates Lizard')
                    player_one_wins += 1
                elif self.human_two.chosen_gesture == self.player_one.list_of_gestures[4]:
                    print('Spock Smashes Scissors')
                    player_two_wins += 1
            elif self.human_one.get_gesture() == self.player_one.list_of_gestures[3]:
                if self.human_two.chosen_gesture == self.player_one.list_of_gestures[0]:
                    print('Rock crushes Lizard')
                    player_two_wins += 1
                elif self.human_two.chosen_gesture == self.player_one.list_of_gestures[1]:
                    print('Lizard eats Paper')
                    player_one_wins += 1
                elif self.human_two.chosen_gesture == self.player_one.list_of_gestures[2]:
                    print('Scissors decapiates Lizard')
                    player_two_wins += 1
                elif self.human_two.chosen_gesture == self.player_one.list_of_gestures[4]:
                    print('Lizard poisons Spock')
                    player_one_wins += 1
            elif self.human_one.get_gesture() == self.player_one.list_of_gestures[4]:
                if self.human_two.chosen_gesture == self.player_one.list_of_gestures[0]:
                    print('Spock vaporizes Rock')
                    player_one_wins += 1
                elif self.human_two.chosen_gesture == self.player_one.list_of_gestures[1]:
                    print('Paper disproves Spock')
                    player_two_wins += 1
                elif self.human_two.chosen_gesture == self.player_one.list_of_gestures[2]:
                    print('Spock smashes Scissors')
                    player_one_wins += 1
                elif self.human_two.chosen_gesture == self.player_one.list_of_gestures[3]:
                    print('Lizard poisons Spock')
                    player_two_wins += 1
            

        if player_one_wins > player_two_wins:
            print('Player one wins!')
        elif player_two_wins > player_one_wins:
            print('Player two wins!')

        
       
    
        