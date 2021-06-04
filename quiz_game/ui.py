from tkinter import *
from question_model import Question
from data import QuestionData
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
FONT = ("Arial", 20, "italic")

class QuizInterface:

    def __init__(self):
        self.question_bank = self.create_questions()
        self.quiz_brain = QuizBrain(self.question_bank)

        # window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.quiz_icon = PhotoImage(file="images/quiz.png")
        self.window.iconphoto(False, self.quiz_icon)

        # score label
        self.score_label = Label(text="Score: 0", font=FONT, bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1, pady=10)

        # images
        img_button_true = PhotoImage(file="images/true.png")
        img_button_false = PhotoImage(file="images/false.png")
        img_button_refresh = PhotoImage(file="images/refresh.png")

        # canvas
        self.canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white", highlightthickness=0)
        self.canvas_text = self.canvas.create_text(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, width=CANVAS_WIDTH-20, fill=THEME_COLOR, font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # button
        self.button_true = Button(image=img_button_true, highlightthickness=0, command=self.true_pressed)
        self.button_true.grid(row=2, column=0, padx=46, pady=10)
        self.button_false = Button(image=img_button_false, highlightthickness=0, command=self.false_pressed)
        self.button_false.grid(row=2, column=1, padx=46, pady=10)
        self.button_refresh = Button(image=img_button_refresh, bg=THEME_COLOR, highlightthickness=0, command=self.refresh_pressed)
        self.button_refresh.config(state="disabled")
        self.button_refresh.grid(row=0, column=0, padx=46, pady=10)

        # call first question
        self.get_next_question()

        self.window.resizable(False, False)
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz_brain.score}/{QuestionData().get_num_of_questions()}")
            question_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.canvas_text, text=question_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="You've reached the end of the quiz.")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")
            self.button_refresh.config(state="active")

    def create_questions(self) -> list:
        question_bank = []
        question_data = QuestionData().get_question_data()
        for question in question_data:
            q = Question(question["question"], question["correct_answer"])
            question_bank.append(q)
        return question_bank

    def true_pressed(self):
        is_right = self.quiz_brain.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz_brain.check_answer("False")
        self.give_feedback(is_right)

    def refresh_pressed(self):
        self.button_refresh.config(state="disabled")
        self.button_true.config(state="active")
        self.button_false.config(state="active")
        self.question_bank = self.create_questions()
        self.quiz_brain = QuizBrain(self.question_bank)
        self.get_next_question()

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
