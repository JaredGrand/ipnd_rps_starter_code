#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    def __init__(self):
        self.wins = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

    def score(self):
        self.wins += 1

class RandomPlayer(Player):
    def __init__(self):
        self.wins = 0

    def move(self):
        outcomes = ['rock', 'paper', 'scissors']
        return random.choice(outcomes)

class HumanPlayer(Player):

    def move(self):
        throw = input("Throw rock, paper, or scissors? ")
        while throw not in ['rock', 'paper', 'scissors']:
            throw = input("Throw rock, paper, or scissors? ")
        return throw

class ReflectPlayer(Player):

    def __init__(self):
        self.their_move = ''


    def learn(self, my_move, their_move):
        self.their_move = their_move
        return self.their_move

    def move(self):
        if self.their_move == '':
            throw = random.choice(['rock', 'paper', 'scissor'])
        else:
            throw = self.their_move
        return throw


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.wins = 0



    def play_round(self):
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
    game = Game(Player(), Player())
    game.play_game()
