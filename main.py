__author__ = 'kurt'

import sys
from book import Book
from wordlist import WordList
from word import Word

def main():
    '''The main funciton, calls upon all other classes to make this work'''
    try:
        text = Book(sys.argv[1])
    except IndexError:
        print("Need EXACTLY 1 Command Line Argument")
        exit(1)

    try:
        sys.argv[2]
        print("Need EXACTLY 1 Command Line Argument")
        exit(1)
    except IndexError:
        pass

    word_list = WordList()

    while True :
        word = text.readWord()
        if word == '':
            break
        word_list.add(Word(word,1))

    print(word_list.maximum())
    print(word_list.minimum())
    word_list.save('result1.txt')
    word_list.order()
    word_list.save('result2.txt')


if __name__ == "__main__":
    main()