from Random_word.Domain import Word


class Game():
    def __init__(self):
        self.word = Word()
        self.mistakes = 0
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.first_instance()
        #self.round()

    def first_instance(self):
        first_letter = self.word.word_to_play[0]
        last_letter = self.word.word_to_play[-1]

        for i in self.alphabet:
            if i == first_letter or i == last_letter:
                self.alphabet = self.alphabet.replace(i, "")

    def guess_letter(self):
        letter = input("Enter a letter: ")

        if isinstance(letter, str) == False:
            raise ValueError("You must enter a letter")



        if letter not in self.alphabet:
            raise ValueError("You already guessed this letter")

        if letter in self.word.word_to_play:
            for i in range(len(self.word.word_to_play)):
                if self.word.word_to_play[i] == letter:
                    self.word.display_positions[i] = 1
        else:
            self.mistakes += 1
        self.alphabet = self.alphabet.replace(letter, "")
        print(self.word)
        print(self.alphabet)
        print("Mistakes: ", self.mistakes)

    def check_if_won_or_lost(self):
        if self.mistakes == 6:
            print("You lost" + "\n" + "The word was: " + self.word.word_to_play)
            return True
        if 0 not in self.word.display_positions:
            print("You won")
            return True
        return False

    def round(self):
        print(self.word)
        while True:
            try:
                self.guess_letter()
                if self.check_if_won_or_lost():
                    break
            except ValueError as ve:
                print(ve)
                continue

#test = Game()