#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    """Player class that only throws rock"""

    def __init__(self):
        self.wins = 0

    def move(self):
        """Move that throws rock"""
        return 'rock'

    def learn(self, my_move, their_move):
        """Player class passes on learn method"""
        pass

    def score(self):
        """Instance level variable for a players score"""
        self.wins += 1


class RandomPlayer(Player):
    """Subclass that plays randomly"""

    def __init__(self):
        self.wins = 0

    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    """Subclass for a human player"""

    def move(self):
        throw = input("Throw rock, paper, or scissors? ")
        while throw.lower() not in ['rock', 'paper', 'scissors']:
            throw = input("Throw rock, paper, or scissors? ")
        return throw


class ReflectPlayer(Player):
    """Subclass that 1st plays randomly and then the opponents previous move"""

    def __init__(self):
        self.their_move = ''

    def learn(self, my_move, their_move):
        self.their_move = their_move
        return self.their_move

    def move(self):
        if self.their_move == '':
            throw = random.choice(moves)
        else:
            throw = self.their_move
        return throw


class CyclePlayer(Player):
    """Subclass that 1st plays randomly and then cycles throw moves"""

    def __init__(self):
        self.my_move = ''

    def learn(self, my_move, their_move):
        self.my_move = my_move
        return self.my_move

    def move(self):
        if self.my_move == '':
            throw = random.choice(moves)
        elif self.my_move == 'rock':
            throw = 'paper'
        elif self.my_move == 'paper':
            throw = 'scissors'
        else:
            throw = 'rock'
        return throw


def beats(one, two):
    """Function that returns True when one beats two"""
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def define_players(name):
    """Function to define which styles are playing"""
    str1 = f"Player {name}: (H)uman, (Ro)ck, (Ra)ndom, (Re)flect, or (C)ycle? "
    ans1 = input(str1).upper()
    while ans1 not in ['H', 'RO', 'RA', 'RE', 'C']:
        ans1 = input(str1).upper()
    if ans1 == 'H':
        p1 = HumanPlayer()
    elif ans1 == 'RA':
        p1 = RandomPlayer()
    elif ans1 == 'RE':
        p1 = ReflectPlayer()
    elif ans1 == 'RO':
        p1 = Player()
    else:
        p1 = CyclePlayer()
    return p1


class Game:
    """Class for gameplay"""
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.wins = 0

    def play_round(self):
        """Function for a single round"""
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if move1 == move2:
            print("The players tied!")
        elif beats(move1, move2):
            self.p1.score()
            print("Player 1 wins!")
        else:
            self.p2.score()
            print("Player 2 wins!")
        print(f"Score: Player 1: {self.p1.wins}  Player 2: {self.p2.wins}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        """Function for a game of multiple rounds"""
        self.p1.wins = 0
        self.p2.wins = 0
        rounds = int(input("How many rounds? "))
        print("Game start!")
        print("")
        for round in range(rounds):
            print(f"Round {round + 1}:")
            self.play_round()
            print(" ")
        print("Game over!")
        if self.p1.wins > self.p2.wins:
            print("Player 1 wins!")
        elif self.p1.wins < self.p2.wins:
            print("Player 2 wins!")
        else:
            print("The players tied!")


if __name__ == '__main__':
    p1 = define_players(1)
    p2 = define_players(2)
    game = Game(p1, p2)
    game.play_game()
