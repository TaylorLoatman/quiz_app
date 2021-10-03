from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.create_text(150, 125, text="The text here", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        correct_img = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=correct_img)
        self.correct_button.grid(column=0, row=2)

        wrong_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_img)
        self.wrong_button.grid(column=1, row=2)


        self.window.mainloop()
