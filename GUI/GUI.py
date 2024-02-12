from Game_unfolding.Game_unfold import Game
import tkinter as tk

game = Game()

screen = tk.Tk()
screen.geometry("800x600")
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
hangman_label.grid(row=0, column=0)

def update_hangman(mistake):
    hangman_label.config(text = hangman_art[mistake])

for i in range(len(game.word.word_to_play)):
    if game.word.display_positions[i] == 1:
        word_label = tk.Label(screen, text = game.word.word_to_play[i], font = ("Times new roman",16),bg="red", fg="white")
    else:
        word_label = tk.Label(screen, text = "_", font = ("Times new roman",16),bg="red", fg="white")
    word_label.grid(row=1, column=i)

guess_entry = tk.Entry(screen, width=3, font = ("Times new roman",14),bg="red", fg="white")
guess_entry.grid(row=2, column=0)
guess_button = tk.Button(screen, text = "Guess", font = ("Times new roman",14))
guess_button.grid(row=2, column=1)

update_hangman(game.mistakes) # first display of hangman



screen.mainloop()
