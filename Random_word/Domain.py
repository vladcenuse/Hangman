import random_word as rw

class Word():
    def __init__(self):
        self.word_class = rw.RandomWords()
        self.word_to_play = self.word_class.get_random_word()
        self.display_positions  = [0] * len(self.word_to_play)
        self.initial_instance()

        """
        1 - we show the letter
        0 - we display _
        """

    def initial_instance(self):
        first_letter =  self.word_to_play[0]
        last_letter = self.word_to_play[-1]

        self.display_positions[0] = 1
        self.display_positions[-1] = 1

        for i in range(1, len(self.word_to_play) - 1):
            if self.word_to_play[i] == first_letter or self.word_to_play[i] == last_letter:
                self.display_positions[i] = 1
            else:
                self.display_positions[i] = 0

    def __str__(self):
        for i in range(len(self.word_to_play)):
            if self.display_positions[i] == 1:
                print(self.word_to_play[i], end = " ")
            else:
                print("_", end = " ")
        return ""


