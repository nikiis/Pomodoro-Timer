import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
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



# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    heading_label.config(text="Timer")
    check_mark.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    reps += 1
    work_seconds = round(WORK_MIN * 60)
    shortbr_seconds = round(SHORT_BREAK_MIN * 60)
    longbr_seconds = round(LONG_BREAK_MIN * 60)

    if reps % 8 == 0:
        countdown(longbr_seconds)
        heading_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        countdown(shortbr_seconds)
        heading_label.config(text="Short Break", fg=PINK)
    else:
        countdown(work_seconds)
        heading_label.config(text="Working Time", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    minute = math.floor(count / 60)
    seconds = count % 60

    if seconds < 10:
            seconds = f'0{seconds}'

    canvas.itemconfig(timer_text, text=f"{minute}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# creating heading title label
heading_label = tk.Label()
heading_label.config(text="Timer", font=(FONT_NAME, 35), fg=GREEN, bg=YELLOW, pady=10)
heading_label.grid(row=0, column=1)


# creating a canvas with the tomato image + timer
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(row=1, column=1)

# create text
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

# creating the buttons
start_button = tk.Button()
start_button.config(text="Start", highlightbackground=YELLOW, fg="black", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tk.Button()
reset_button.config(text="Reset", highlightbackground=YELLOW, fg="black", command=reset_timer)
reset_button.grid(row=2, column=2)


# check mark
check_mark = tk.Label()
check_mark.config(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
check_mark.grid(row=3, column=1)

window.mainloop()