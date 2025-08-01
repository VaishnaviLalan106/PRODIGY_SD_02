import tkinter as tk
import random
from tkinter import messagebox
import time
root = tk.Tk()
root.title("Guess the Number!")
root.geometry("550x450")
root.config(bg="#b7e4c7")
label=tk.Label(root,text="Hello there! Can you guess the number I'm thinking of?",font=("Comic Sans MS",12),bg="#e2f3e8")
label.pack()
number_to_guess = random.randint(1, 100)
attempts = 0
def type_text(widget, message, color):
    widget.config(text="", fg=color)
    widget.update()
    def animate(i=0):
        if i < len(message):
            widget.config(text=widget.cget("text") + message[i])
            root.after(20, animate, i+1)
    animate()
def give_hint(guess):
    parity = "even" if number_to_guess % 2 == 0 else "odd"

    if guess < number_to_guess:
        direction = f"Try a number greater than {guess}."
    elif guess > number_to_guess:
        direction = f"Try a number less than {guess}."
    else:
        direction = ""

    range_start = max(1, number_to_guess - 10)
    range_end = min(100, number_to_guess + 10)
    range_hint = f"The number is between {range_start} and {range_end}."

    distance = abs(guess - number_to_guess)
    if distance <= 5:
        closeness = "You're very close!"
    elif distance <= 15:
        closeness = "You are closer."
    else:
        closeness = "You are far away."

    return f"{direction} It's an {parity} number. {range_hint} {closeness}"
def bounce_button(btn):
    btn.config(font=("Comic Sans MS", 14, "bold"))
    root.after(150, lambda: btn.config(font=("Comic Sans MS", 12)))
def check_guess():
    global attempts
    guess = entry.get()
    bounce_button(guess_btn)

    if guess.isdigit():
        guess = int(guess)
        attempts += 1

        if guess < number_to_guess:
            type_text(result_label, f"Too low!\nHINT: {give_hint(guess)}", "black")
        elif guess > number_to_guess:
            type_text(result_label, f"Too high!\nHINT: {give_hint(guess)}","black")
        else:
            type_text(result_label, f"🎉 Correct! You got it in {attempts} attempts.", "black")
            celebration_popup()
    else:
        type_text(result_label, "Please enter a valid number!", "red")
def celebration_popup():
    messagebox.showinfo("Congratulations!", f"You did it !!!\nYou guessed the number correctly!")
def reset_game():
    global number_to_guess, attempts
    bounce_button(reset_btn)
    number_to_guess = random.randint(1, 100)
    attempts = 0
    entry.delete(0, tk.END)
    type_text(result_label, "New game started! Enter your guess.","black")
def create_button(master, text, command, color):
    return tk.Button(master,text=text,command=command,bg=color,fg="black",activebackground="#dcedc8",font=("Comic Sans MS", 12),relief="flat",bd=2,padx=10,pady=5)
title = tk.Label(root, text="Guess the Number (1–100)", font=("Comic Sans MS", 16, "bold"), bg="#4EC94E")
title.pack(pady=15)
entry = tk.Entry(root, font=("Comic Sans MS", 14), justify="center", bd=3, relief="ridge", highlightthickness=2)
entry.pack(pady=10)
entry.bind("<FocusIn>", lambda e: entry.config(bg="white"))
entry.bind("<FocusOut>", lambda e: entry.config(bg="white"))
guess_btn = create_button(root, "Guess", check_guess, "#4EC94E")
guess_btn.pack(pady=6)
reset_btn = create_button(root, "Reset", reset_game, "#4EC94E")
reset_btn.pack(pady=6)
result_label = tk.Label(root,text="New game started! Enter your guess.",font=("Comic Sans MS", 12),bg="#b7e4c7",wraplength=380,justify="center")
result_label.pack(pady=25)
root.mainloop()
