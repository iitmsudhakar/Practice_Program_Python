'''
Create a class named StringManipulation that has the following specification:
Attributes
words: list of strings, all of which will be in lower case
Methods
(1) __init__: accept a list words as argument and assign it to the corresponding attribute
(2) total_words: return the total number of words in words
(3) count: accept an argument named some_word and return the number of times this word occurs in the list words
(4) words_of_length: accept a positive integer length as argument and return a list of all the words in the list words
that have a length equal to length
(5) words_start_with: accept a character char as argument and return the list of all the words in words that start with char
(6) longest_word: return the longest word in the list words; if there are multiple words that satisfy this condition,
return the first such occurrence
(7) palindromes: return a list of all the words that are palindromes in words
'''


class StringManipulation:
    def __init__(self, words):
        self.words = words

    def total_words(self):
        return len(self.words)

    def count(self, some_word):
        return self.words.count(some_word)

    def words_of_length(self, n):
        L = []
        for i in self.words:
            if len(i) == n:
                L.append(i)
        return L

    def words_start_with(self, c):
        L = []
        for i in self.words:
            if i[0] == c:
                L.append(i)
        return L

    def longest_word(self):
        max_w = len(self.words[0])
        for i in self.words:
            if len(i) > max_w:
                max_w = i
        return max_w

    def palindromes(self):
        L = []
        for i in self.words:
            reverse = ''
            for c in i:
                reverse = c + reverse
            if reverse == i:
                L.append(i)
        return L


L = ["apple", "mango", "peaches", "apple"]

print(L.count("apple"))
