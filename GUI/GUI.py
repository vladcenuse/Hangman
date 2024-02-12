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


def check_guess(guess):
    if guess in word.word_to_play:
        for i in range(len(word.word_to_play)):
            if word.word_to_play[i] == guess:
                word.display_positions[i] = 1
        for i in range(len(word.word_to_play)):
            if word.display_positions[i] == 1:
                word_label = tk.Label(screen, text = word.word_to_play[i], font = ("Times new roman",16),bg="black", fg="white")
                word_label.grid(row=1, column=i)
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
screen.geometry("300x300")
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



hangman_label = tk.Label(screen, font = ("Times new roman",12),bg="red", fg="white")
hangman_label.grid(row=0, column=9)


for i in range(len(word.word_to_play)):
    if word.display_positions[i] == 1:
        word_label = tk.Label(screen, text = word.word_to_play[i], font = ("Times new roman",16),bg="black", fg="white")
    else:
        word_label = tk.Label(screen, text = "_", font = ("Times new roman",16),bg="black", fg="white")
    word_label.grid(row=1, column=i)

guess_entry = tk.Entry(screen, width=3, font = ("Times new roman",14),bg="red", fg="white")
guess_entry.grid(row=2, column=0)
guess_button = tk.Button(screen, text = "Guess", font = ("Times new roman",14),command=lambda: check_guess(guess_entry.get()),bg="red", fg="white")
guess_button.grid(row=2, column=1)


result_label = tk.Label(screen, font = ("Times new roman",16),bg="black", fg="white")
result_label.grid(row=3, column=0)

#initialise the game
update_hangman(word.mistakes)


screen.mainloop()
