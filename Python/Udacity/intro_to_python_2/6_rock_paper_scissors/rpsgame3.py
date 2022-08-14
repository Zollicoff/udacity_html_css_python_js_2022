import random
import time

ROCK = 0
PAPER = 1
SCISSORS = 2


# Repurposed Print Pause Function
def print_pause(message):
    print(message)
    time.sleep(2)


# Repurposed Valid Input Function
def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause(f'Sorry, the option "{option}" is invalid. Try again!')


# Repurposed Play Again Function
def play_again():
    play_again = valid_input("Would you like to play again?"
                             "(y/n) \n", ["y", "n"])
    if play_again == "y":
        print_pause("Excellent! Restarting the game ...")
        game.play_game()
    elif play_again == "n":
        print_pause("Thanks for playing! See you next time.")
        time.sleep(2)
        exit()


class Player:
    def move(self):
        return ROCK

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move():
        return random.choice([ROCK, PAPER, SCISSORS])


class CyclingPlayer(Player):
    memory = []

    def move(self):
        if not self.memory:
            return random.choice([ROCK, PAPER, SCISSORS])
        else:
            return (self.memory[(-1)] + 1) % 3

    def learn(self, my_move, their_move):
        self.memory.append(my_move)


class Imitator(CyclingPlayer):
    def learn(self, my_move, their_move):
        self.memory.append(their_move)


class HumanPlayer(Player):
    MOVES = {'rock': ROCK, 'paper': PAPER, 'scissors': SCISSORS}
    INV_MOVES = {ROCK: 'rock', PAPER: 'paper', SCISSORS: 'scissors'}

    def move(self):
        moved = None
        while moved not in self.MOVES:
            moved = input('Choose rock, paper, or scissors.\n').lower()

        return self.MOVES[moved]

    def learn(self, my_move, their_move):
        print_pause(f"You played {self.INV_MOVES[my_move]}.")
        print_pause(f"Opponent played {self.INV_MOVES[their_move]}.")


class Game:
    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two
        self.score_one = 0
        self.score_two = 0

    @staticmethod
    def beats(x, y):
        """Does x beat y?"""
        return x == (y + 1) % 3

    def play_round(self):
        move_one = self.player_one.move()
        move_two = self.player_two.move()
        self.player_one.learn(move_one, move_two)
        self.player_two.learn(move_two, move_one)
        if self.beats(move_one, move_two):
            print_pause("PLAYER ONE WINS THE ROUND!")
            self.score_one += 1
        else:
            if self.beats(move_two, move_one):
                print_pause("PLAYER TWO WINS THE ROUND!")
                self.score_two += 1
            else:
                print_pause("THE ROUND ENDS IN A TIE!")
        print_pause(f"Player One's Score: {self.score_one}, "
                    f"Player Two's Score: {self.score_two}")

    def play_game(self):
        print_pause("Welcome to Rock Paper Scissors (Built in Python)")
        for round in range(3):
            print_pause(f"Round {round + 1}:")
            self.play_round()
        if self.beats(self.score_one, self.score_two):
            print_pause(f"PLAYER ONE WINS THE GAME "
                        "WITH A SCORE OF {self.score_one}!")
        elif self.beats(self.score_two, self.score_one):
            print_pause(f"PLAYER TWO WINS THE GAME "
                        "WITH A SCORE OF {self.score_two}!")
        else:
            print_pause(f"THE GAME ENDS IN A TIE!")
        play_again()


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclingPlayer())
    game.play_game()
