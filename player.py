#!/usr/bin/env python3
import os
import pygame

from deck import Deck
from playerStatus import PlayerStatus


class Player(object):
    def __init__(self):
        print('Welcome to Blackjack!')
        self.money = 1000
        self.cards = []
        self.handScore = 0
        self.bet = 0
        self.deck = Deck()
        self.stat = PlayerStatus()

    def draw(self):
        auxCard = self.deck.draw()
        if auxCard[1] == 1:
            if self.handScore <= 10:
                auxCard = ('A', 11)

        self.cards.append(auxCard[0])
        self.handScore += auxCard[1]

    def placeBet(self):
        print('You have: $' + str(self.money))
        print('Place bet: ')
        while True:
            try:
                self.bet = int(input())

            except:
                print('Please type in an integer as the bet')
                continue
            else:
                self.money -= self.bet
                break

        self.draw()
        self.printHand()

    def checkScore(self, comm):
            self.printHand()
            if self.handScore < 16:
                if comm == 's':
                    print('Bet lost')
                    self.stat.losses += 1
                    self.cards = []
                    self.handScore = 0
                    return 1
                else:
                    return 0
            elif 16 < self.handScore <= 21:
                print('Bet won')
                self.money += (self.bet * 2)
                self.stat.wins += 1
                self.cards = []
                self.handScore = 0
            elif self.handScore == 16:
                print('Draw bet')
                self.money += self.bet
                self.stat.draws += 1
                self.cards = []
                self.handScore = 0
            elif self.handScore > 21:
                print('BUST')
                self.stat.busts += 1
                self.cards = []
                self.handScore = 0

            return 1

    def printHand(self):
        print(self.cards)
        print()
        print('Score: ' + str(self.handScore))
        print()

    def restart(self):
        if os.name == 'nt':

            os.system('cls')
        else:
            os.system('clear')

        print("Welcome to BlackJack!")
        self.money = 1000
        self.cards = []
        self.handScore = 0
        self.bet = 0
        self.deck.restart()
        self.stat.restart()

        self.game()
        #self.game()

    def gameRound(self):
        while True:
            # self.printHand()
            print('Choose action:- d - draw; s - stand; r - restart: ')
            option = input()
            if option == 'd':
                if len(self.cards) < 5:
                    self.draw()
                    return self.checkScore('d')

            elif option == 's':
                return self.checkScore('s')
            elif option == 'r':
                self.restart()
                continue
                #break
            else:
                print('No such command, please retry')
                input()
                continue

        self.deck.restart()

    def checkMoney(self):
        self.showStatus()
        if self.money <= 0:
            print('YOU LOST')
            return 1
        elif self.money >= 3000:
            print('YOU WON')
            return 1
        else:
            return 0

    def showStatus(self):
        print('Money: $' + str(self.money))
        self.stat.printStatus()

    def game(self):
        while True:
            self.placeBet()
            while self.gameRound() == 0:
                continue

            if self.checkMoney():
                print('Want to play again?(y/n) ')
                if input() == 'y':
                    self.restart()
                    continue
                else:
                    return False


player = Player()
player.game()
pygame.init()
green = (0, 200, 150)
moneyColor = (0, 255, 0)
white = (255, 255, 255)
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('pyBlackJack')

lead_x = 350
lead_y = 350
x_change = 0
y_change = 0

clock = pygame.time.Clock()

gameExit = False
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

pygame.display.update()
pygame.quit()
quit()
