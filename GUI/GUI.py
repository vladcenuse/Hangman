from Random_word.Domain import Word
import tkinter as tk

word = Word()
def end_game(message):
    if message == "You won":
        result_text = "You won"
    else:
        result_text = "You lost, the word was " + word.word_to_play
    result_label.config(text = result_text)
    guess_button.config(state = "disabled")
    guess_entry.config(state = "disabled")

def display_word():
    for i in range(len(word.word_to_play)):
        if word.display_positions[i] == 1:
            word_label = tk.Label(screen, text=word.word_to_play[i], font=("Times new roman", 16), bg="black",
                                  fg="white")
            word_label.grid(row=1, column=i)
def check_guess(guess):
    if guess in word.word_to_play:
        for i in range(len(word.word_to_play)):
            if word.word_to_play[i] == guess:
                word.display_positions[i] = 1
        display_word()
        if 0 not in word.display_positions:
            end_game("You won")
    else:
        word.mistakes += 1
        update_hangman(word.mistakes)
        if word.mistakes == 6:
            end_game("You lost!")

def update_hangman(mistake):
    hangman_label.config(text = hangman_art[mistake])


screen = tk.Tk()
screen.geometry("400x300")
screen.title("Hangman")
screen.configure(bg="black")

hangman_art = [
    "   +---+\n   |   |\n       |\n       |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n       |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n   |   |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|   |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n  /    |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n  / \\  |\n       |\n========="
]



hangman_label = tk.Label(screen, font = ("Arial",12),bg="black", fg="lightblue")
hangman_label.grid(row=0, column=0, columnspan=len(word.word_to_play), pady=10, padx=10)


for i in range(len(word.word_to_play)):
    if word.display_positions[i] == 1:
        word_label = tk.Label(screen, text=word.word_to_play[i], font=("Arial", 16), bg="black", fg="white")
    else:
        word_label = tk.Label(screen, text="_", font=("Arial", 16), bg="black", fg="gray")
    # Set each label directly next to each other with no horizontal padding
    word_label.grid(row=1, column=i)

guess_entry = tk.Entry(screen, width=3, font=("Arial", 14), fg="#fff", bg="#333")
guess_entry.grid(row=2, column=0, columnspan=2, pady=20, padx=(10, 0))
guess_button = tk.Button(screen, text="Guess", font=("Arial", 14), command=lambda: check_guess(guess_entry.get()), bg="#4CAF50", fg="black")  # Android green for the button
guess_entry.config(highlightbackground="gray", highlightcolor="gray", highlightthickness=1, insertbackground="white")
guess_button.grid(row=2, column=2, pady=20, padx=(0, 10))


result_label = tk.Label(screen, font = ("Arial",16),bg="black", fg="white")
result_label.grid(row=3, column=0)

#initialise the game
update_hangman(word.mistakes)


screen.mainloop()
