import tkinter as tk
import random

#funkcja zmieniajace obraz wylosowanego przedmiotu
def changeImg(self, char):
    if char == 1:
        self.computerMove.configure(image = self.rockImage)
    elif char == 2:
        self.computerMove.configure(image = self.paperImage)
    else:
        self.computerMove.configure(image = self.scissorsImage)

#funkcja sprawdzajaca czy ktos wygral
def hasSomeoneWon(obj, self):
    user = int(self.userPoints.get())
    computer = int(self.computerPoints.get())

    if user == 3:
        self.userPoints.set(0)
        self.computerPoints.set(0)

        self.infoText.set("User won the game")

    if computer == 3:
        self.userPoints.set(0)
        self.computerPoints.set(0)

        self.infoText.set("Computer won the game")

#fukcja sprawdzajaca kto zdobyl punkt
def checkResult(self):
    waepon = int(self.waepon.get())
    computerMove = random.randint(1, 3)
    points = 0

    changeImg(self, computerMove)

    if waepon == computerMove:
        self.infoText.set("Draw!")

    if waepon == (computerMove + 1) or waepon == (computerMove - 2):
        points = int(self.userPoints.get()) + 1
        self.userPoints.set(points)
        self.infoText.set("User got 1 point!")

    if computerMove == (waepon + 1) or computerMove == (waepon - 2):
        points = int(self.computerPoints.get()) + 1
        self.computerPoints.set(points)
        self.infoText.set("PC got 1 point!")

    hasSomeoneWon(self, self)
