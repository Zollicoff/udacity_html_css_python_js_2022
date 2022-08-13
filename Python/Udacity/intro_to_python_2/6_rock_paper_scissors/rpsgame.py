import random

moves = ['rock', 'paper', 'scissors']
memory = []


# The Player class is the parent class for all of the Players in this game
class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


# Random Player subclass *FINISHED*
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


# Validate user input **** NEEDS WORK ****
class HumanPlayer(Player):
    def move(self):
        hp = input()
        if hp in moves:
            return hp
        else:
            print("error")


# Cycling Decision Player subclass **** NEEDS WORK ****
class CyclingPlayer(Player):
    def move(self):
        return something


# Smart Player subclass **** NEEDS WORK ****
class SmartPlayer(Player):
    def move(self):
        if memory == " ":
            return random.choice(moves)
        else:
            return memory


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


# Game class **** NEEDS WORK ****
#     Create score keeper, announce winner, report scores each round
class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Welcome to RPS. Game start!")
        for round in range(3):
            print(f"Round {round + 1}:")
            self.play_round()
        print("Game over!")


# Calls the program
if __name__ == '__main__':
    game = Game(RandomPlayer(), RandomPlayer())
    game.play_game()
