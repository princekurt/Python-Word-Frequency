__author__ = 'kurt'
class Book(object):
    '''Used for actually grabbing each word from the file, should be read as Book. llike to book a ticket'''
    def __init__(self, filename):
        self.filename = open(filename, "r")

    def readChar(self):
        """Reads a single Character"""
        working_char = self.filename.read(1)
        if working_char == '':
            working_char = ''
            return working_char
        # while working_char.isalpha() == False:
        #     working_char = self.filename.read(1)

        return working_char


    def readWord(self):
        """Uses readChar to read a single Word"""
        word_holder = ''
        c = self.readChar()
        while True:

            if c.isalpha() or c == '_':
                while c.isalpha() or c == '_':
                    word_holder += word_holder.join(c)
                    c = self.readChar()
                return word_holder

            else:
                while c.isalpha() == False:
                    if c == '':
                        return word_holder
                    else:
                        c = self.readChar()


