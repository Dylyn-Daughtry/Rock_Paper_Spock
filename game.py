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
        # count = 0
        # while count < 3:
        # self.select_gesture()
        self.determine_winner()
            # count += 1
    
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
        for gesture in self.human_one.get_gesture_list():
            print(f'Input {count} to select {gesture}')
            count += 1
        self.human_one.choose_gesture() # can call user gesture method here instead of in run game
        self.ai_one.choose_gesture() # may need to place ai gesture here too

    # def user_gesture_capture(self):
    #     user_gesture = int(input())
    #     chosen_gesture = self.human_one.choose_gesture(user_gesture)
    #     print(chosen_gesture) # print chosen gesture
        # return chosen_gesture # or return chosen gesture, return might be better for comparison condition later
    # def win_counter(self):
    #     player_one_wins = 0
    #     player_two_wins = 0
    #     ai_wins = 0

    def determine_winner(self):
        player_one_wins = self.player_one.wins
        player_two_wins = self.player_one.wins
        
        
        while player_one_wins != 2 and player_two_wins != 2:
            self.select_gesture()
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
            print('Player two wins!')

        
       
    
        