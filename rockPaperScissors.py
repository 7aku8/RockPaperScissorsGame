import tkinter as tk
import random

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        #nazwa aplikacji
        self.winfo_toplevel().title("RockPaperScissors")

        #zmienna przechowujaca wybrana opcje [kamien, papier, nozyce]
        self.waepon = tk.StringVar()

        #pobranie obrazow
        self.rockImage = tk.PhotoImage(file = ".\\rock.png")
        self.paperImage = tk.PhotoImage(file = ".\\paper.png")
        self.scissorsImage = tk.PhotoImage(file = ".\\scissors.png")

        #przyciski do wyboru opcji
        self.rock = tk.Radiobutton(self, image = self.rockImage, variable = self.waepon, value = 1).grid(row = 0, column = 0)
        self.paper = tk.Radiobutton(self, image = self.paperImage, variable = self.waepon, value = 2).grid(row = 0, column = 1)
        self.scissors = tk.Radiobutton(self, image = self.scissorsImage, variable = self.waepon, value = 3).grid(row = 0, column = 2)

        self.warButton = tk.Button(self, text = "Battle!", command = self.checkResult).grid(row = 1, column = 1)

        self.ctext = tk.Label(self, text = "Computer's Move").grid(row = 2, column = 1)

        #pole wyswietlajace wylosowany przedmiot przez komputer
        self.computerMove = tk.Label(self)
        self.computerMove.grid(row = 3, column = 1)

        #pole wyswietlajace wynik
        self.infoText = tk.StringVar()
        self.infoText.set("Waiting for move...")
        self.info = tk.Label(self, textvariable = self.infoText).grid(row = 1, column = 3)
        self.rtext = tk.Label(self, text = "Result:").grid(row = 2, column = 3)
        self.userPoints = tk.StringVar()
        self.userPoints.set(0)
        self.computerPoints = tk.StringVar()
        self.computerPoints.set(0)
        self.userResult = tk.Label(self, textvariable = self.userPoints).grid(row = 3, column = 3)
        self.computerResult = tk.Label(self, textvariable = self.computerPoints).grid(row = 3, column = 4)

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

        self.changeImg(computerMove)

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

        self.hasSomeoneWon(self)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
