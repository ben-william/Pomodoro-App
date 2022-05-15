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

def reset():
    window.after_cancel(timer) # after_cancel method needs to reference a variable,
    # so global 'timer' defined above and timer in count_down() saved as this variable
    label.config(text='Timer', fg=GREEN)
    global reps
    reps = 0
    checkmark.config(text='')
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        print('long break')
        count_down(LONG_BREAK_MIN * 60)
        label.config(text="Long Break!", fg=RED)
    elif reps % 2 == 0:
        print('short break')
        count_down(SHORT_BREAK_MIN * 60)
        label.config(text="Short Break!", fg=PINK)
    else:
        print('work timer')
        count_down(WORK_MIN * 60)
        label.config(text="Time to Work!", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(time):
    minutes_remaining = math.floor(time / 60)
    seconds_remaining = time % 60
    if seconds_remaining < 10:
        seconds_remaining = f"0{seconds_remaining}"
    canvas.itemconfig(timer_text, text=f"{minutes_remaining}:{seconds_remaining}")
    if time > 0:
        global timer
        timer = window.after(1000, count_down, time - 1)
    else: # When timer reaches 0
        start_timer()
        checks = ''
        for i in range(0,math.floor(reps/2)):   # floor used because dividing by 2 makes it a float
            checks += '✅'
        checkmark.config(text=checks)

    # ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text='00:00', font=(FONT_NAME, 33, 'bold'))
canvas.grid(row=1,column=1)


label = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, 'bold'))
label.grid(row=0, column=1)

start_button = Button(text="Start Timer", highlightbackground=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset)
reset_button.grid(row=2, column=2)

checkmark = Label(bg=YELLOW)
checkmark.grid(row=3, column=1)

window.mainloop()