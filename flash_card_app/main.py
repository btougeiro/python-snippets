from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
CARD_TITLE_FONT = ("Ariel", 40, "italic")
CARD_TEXT_FONT = ("Ariel", 60, "bold")
current_card = {}
to_learn = {}

# importing csv file
try:
    data_frame = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data_frame.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn) # {"French": "word_in_french", "English":"word_in_english"}
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_text, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# creating window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window_icon = PhotoImage(file="images/flash-cards.png")
window.iconphoto(False, window_icon)

flip_timer = window.after(3000, func=flip_card)

# importing images
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

## canvas
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 526
canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, image=card_front)
card_title = canvas.create_text(400, 150, text="", font=CARD_TITLE_FONT)
card_text = canvas.create_text(400, 263, text="", font=CARD_TEXT_FONT)
canvas.grid(row=0, column=0, columnspan=2)

# creating button
button_wrong = Button(image=wrong, highlightthickness=0, command=next_card)
button_wrong.grid(row=1, column=0)
button_right = Button(image=right, highlightthickness=0, command=is_known)
button_right.grid(row=1, column=1)

# calling the card due the first execution
next_card()

# set resizable to off
window.resizable(False, False)

# loop the window
window.mainloop()
