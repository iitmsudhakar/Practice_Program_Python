class Word:
    count = 0

    def __init__(self, word, pos):
        Word.count += 1
        self.word = word
        self.pos = pos

    def print_info(self):
        print(f'The word is "{self.word}" and its part of speech is "{self.pos}".')


input_1 = input()
input_2 = input()
word = Word(input_1, input_2)
word.print_info()

