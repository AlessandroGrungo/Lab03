import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.multiDizionario = md.MultiDictionary()

    def handleSentence(self, txtIn, language):
        print('ricerca con contains---------------------------------------------')
        t1 = time.time()
        words = txtIn.split()
        parole = self.multiDizionario.searchWord(words, language)
        for p in parole:
            if not p.corretta:
                print(p)
        t2 = time.time()
        print("Time " + str(t2 - t1))
        print('ricerca linare---------------------------------------------------')
        t1 = time.time()
        words = txtIn.split()
        parole = self.multiDizionario.searchWord(words, language)
        for p in parole:
            if not p.corretta:
                print(p)
        t2 = time.time()
        print("Time " + str(t2 - t1))
        print('ricerca dicotomica---------------------------------------------------')
        t1 = time.time()
        words = txtIn.split()
        parole = self.multiDizionario.searchWord(words, language)
        for p in parole:
            if not p.corretta:
                print(p)
        t2 = time.time()
        print("Time " + str(t2 - t1))

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")
