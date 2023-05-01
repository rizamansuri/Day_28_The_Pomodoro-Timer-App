# Bismillahir-rahmanir-rahim
from tkinter import *
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
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer", fg=GREEN)
    checkmark.config(text=" ")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = " "
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Riza's Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)
# Label
label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
label.grid(row=0, column=1)

# Canvas and Image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, fill="white", text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Start Button
start_button = Button(text="Start", font=(FONT_NAME, 11, "bold"), command=start_timer)
start_button.grid(row=2, column=0)

# Reset Button
reset_button = Button(text="Reset", font=(FONT_NAME, 11, "bold"), command=reset_timer)
reset_button.grid(row=2, column=2)

# Checkmarks
checkmark = Label(bg=YELLOW, fg=GREEN, font=(60))
checkmark.grid(row=3, column=1)

window.mainloop()
