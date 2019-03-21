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
        self.rock_image = tk.PhotoImage(file = ".\\rock.png")
        self.paper_image = tk.PhotoImage(file = ".\\paper.png")
        self.scissors_image = tk.PhotoImage(file = ".\\scissors.png")

        #przyciski do wyboru opcji
        self.rock = tk.Radiobutton(self, image = self.rock_image, variable = self.waepon, value = 1).grid(row = 0, column = 0)
        self.paper = tk.Radiobutton(self, image = self.paper_image, variable = self.waepon, value = 2).grid(row = 0, column = 1)
        self.scissors = tk.Radiobutton(self, image = self.scissors_image, variable = self.waepon, value = 3).grid(row = 0, column = 2)

        self.war_button = tk.Button(self, text = "Battle!", command = lambda: mechanics.checkResult(self)).grid(row = 1, column = 1)

        self.ctext = tk.Label(self, text = "Computer's Move").grid(row = 2, column = 1)

        #pole wyswietlajace wylosowany przedmiot przez komputer
        self.computer_move = tk.Label(self)
        self.computer_move.grid(row = 3, column = 1)

        #pole wyswietlajace wynik
        self.info_text = tk.StringVar()
        self.info_text.set("Waiting for move...")
        self.info = tk.Label(self, textvariable = self.info_text).grid(row = 1, column = 3)
        self.rtext = tk.Label(self, text = "Result:").grid(row = 2, column = 3)
        self.user_points = tk.StringVar()
        self.user_points.set(0)
        self.computer_points = tk.StringVar()
        self.computer_points.set(0)
        self.user_result = tk.Label(self, textvariable = self.user_points).grid(row = 3, column = 3)
        self.computerResult = tk.Label(self, textvariable = self.computer_points).grid(row = 3, column = 4)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
