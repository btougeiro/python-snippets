import tkinter

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

## window

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
photo = tkinter.PhotoImage(file="tomato.png")
window.iconphoto(False, photo)

## definitions

def start_timer():
    global reps

    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))

def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
    canvas.itemconfig(timer_text, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
    check_mark.config(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
    global reps
    reps = 0

def count_down(count):

    min = count // 60
    sec = count % 60

    if sec < 10:
        sec = f"0{sec}"
    
    if min < 10:
        min = f"0{min}"

    canvas.itemconfig(timer_text, text=f"{min}:{sec}", fill="white", font=(FONT_NAME, 28, "bold"))
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(reps//2):
            mark += "✔"
        check_mark.config(text=mark)

## label

timer_label = tkinter.Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

## canvas

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(row=1, column=1)

## button

start_button = tkinter.Button(text="Start", font=(FONT_NAME, 11, "bold"), highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text="Reset", font=(FONT_NAME, 11, "bold"), highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

## check mark

check_mark = tkinter.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
check_mark.grid(row=4, column=1)

## window mainloop

window.resizable(False, False)
window.mainloop()
