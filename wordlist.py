__author__ = 'kurt'

class WordList(object):

    def __init__(self):
        self.word_list = {}
        self.object_list = []





    def add(self, text):
        """Adds a word Object to the list"""
        for i in range(len(self.object_list)):
            if text.get_word() == self.object_list[i].get_word():
                self.object_list[i].set_freq(self.object_list[i].get_freq() + 1)
                return


        self.object_list.append(text)




    def order(self):
        """Takes the list and orders it"""
        self.object_list = sorted(self.object_list, key=lambda word: word.get_word())


    def __str__(self):
        """Tells the Prgraom how to implement the print function"""
        return "{" + "".join(map(str,self)) + "}"

    def __iter__(self):
        """A defined iterator"""
        cursor = 0
        while cursor < len(self.object_list):
            yield self.object_list[cursor]
            cursor += 1

    def maximum(self):
        """Provides the Maximum of a list of objects"""
        frequency = 0
        for i in range(len(self.object_list)):
            if self.object_list[i].get_freq() > frequency:
                frequency = self.object_list[i].get_freq()
            else:
                pass
        return frequency

    def minimum(self):
        """Provides a minimum for a list of objects"""
        frequency = len(self.object_list)
        for i in range(len(self.object_list)):
            if self.object_list[i].get_freq() < frequency:
                frequency = self.object_list[i].get_freq()
            else:
                pass
        return frequency

    def save(self, filename):
        """Saves the Files to export file locations"""
        file = open(filename, 'w')
        for i in range(len(self.object_list)):
            file.write(str(self.object_list[i].get_word()) + ":" + str(self.object_list[i].get_freq()) + "\n")
        file.close()