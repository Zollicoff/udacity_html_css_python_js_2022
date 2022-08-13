# Necessary module imports
import random
import time

# Global variable for moves
moves = ['rock', 'paper', 'scissors']


# Repurposed pause function
def print_pause(message):
    print(message)
    time.sleep(2)


# Repurposed input validation function
def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause(f'Sorry, "{option}" is an invalid input. Try again!')


# Win condition function
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


# The Player class is the parent class for all of the Players in this game
class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        return my_move, their_move


# Random Player subclass
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


# Human player subclass with validation
class HumanPlayer(Player):
    def move(self):
        hp = valid_input("Enter rock, paper, or scissors.\n",
                         ['rock', 'paper', 'scissors'])
        return hp


# Remembers what move the opponent played last round and plays this round **** NEEDS WORK ****
class ReflectPlayer(Player):
    def move(self):
        pass


# Remembers what move IT played last round and cycles through the list **** NEEES WORK ****
class CyclingPlayer(Player):
    def move(self):
        return moves


# Create score keeper, announce winner, report scores each round
class Game:


    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print_pause(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2) == True:
            p1_score.append(+1)
            print_pause("Player 1 wins the round!")
        elif beats(move1, move2) == False:
            p2_score.append(+1)
            print_pause("Player 2 wins the round!")
        
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        # match move 1 with move 2 using win condition beats function

    def play_game(self):
        print_pause("Welcome to Rock Paper Scissors!")
        print_pause("Lets start the game!")
        for round in range(3):
            print_pause(f"Round {round + 1}:")
            self.play_round()
        print_pause("Game over!")


# Calls the program, choose which player to use (Player 1, Player 2)
if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
