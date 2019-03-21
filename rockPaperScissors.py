import tkinter as tk
from game import mechanics

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

        self.warButton = tk.Button(self, text = "Battle!", command = lambda: mechanics.checkResult(self)).grid(row = 1, column = 1)

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

root = tk.Tk()
app = Application(master=root)
app.mainloop()
