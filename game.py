import random


class mechanics():

    #funkcja zmieniajace obraz wylosowanego przedmiotu
    def changeImg(self, char):
        if char == 1:
            self.computer_move.configure(image = self.rock_image)
        elif char == 2:
            self.computer_move.configure(image = self.paper_image)
        else:
            self.computer_move.configure(image = self.scissors_image)

    #funkcja sprawdzajaca czy ktos wygral
    def hasSomeoneWon(obj, self):
        user = int(self.user_points.get())
        computer = int(self.computer_points.get())

        if user == 3:
            self.user_points.set(0)
            self.computer_points.set(0)

            self.info_text.set("User won the game")

        if computer == 3:
            self.user_points.set(0)
            self.computer_points.set(0)

            self.info_text.set("Computer won the game")

    #fukcja sprawdzajaca kto zdobyl punkt
    @staticmethod
    def checkResult(self):
        waepon = int(self.waepon.get())
        computer_move = random.randint(1, 3)
        points = 0

        mechanics.changeImg(self, computer_move)

        if waepon == computer_move:
            self.info_text.set("Draw!")

        if waepon == (computer_move + 1) or waepon == (computer_move - 2):
            points = int(self.user_points.get()) + 1
            self.user_points.set(points)
            self.info_text.set("User got 1 point!")

        if computer_move == (waepon + 1) or computer_move == (waepon - 2):
            points = int(self.computer_points.get()) + 1
            self.computer_points.set(points)
            self.info_text.set("PC got 1 point!")

        mechanics.hasSomeoneWon(self, self)
