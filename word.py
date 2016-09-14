__author__ = 'kurt'

class Word(object):

    def __init__(self, text, frequency):
        self.word = text
        self.frequency = frequency

    def get_word(self):
        """Gets word"""
        return str(self.word)

    def set_word(self, word):
        """Sets Word"""
        self.word = word

    def get_freq(self):
        """Gets Frequency"""
        return int(self.frequency)

    def set_freq(self, freq):
        """Sets Frequency"""
        self.frequency = freq

    def __str__(self):
        return str(self.word) + " : " + str(self.frequency) + "\n"

