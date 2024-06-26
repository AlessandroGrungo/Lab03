import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self): # con questa definizione del multidizionario creo i dizionari
        self._english = d.Dictionary([], 'english')
        self._italiano = d.Dictionary([], 'italiano')
        self._spanish = d.Dictionary([], 'spanish')

        self._english.loadDictionary("resources/English.txt")
        self._italiano.loadDictionary("resources/Italian.txt")
        self._spanish.loadDictionary("resources/Spanish.txt")

    def searchWord(self, words, language):
        parole = []
        for word in words:
            word = word.lower()
            trovata = False
            richW = rw.RichWord(word)
            if language == 'italiano' and self._italiano.dict.__contains__(word):
                trovata = True
            elif language == 'spanish' and self._spanish.dict.__contains__(word):
                trovata = True
            elif language == 'english' and self._english.dict.__contains__(word):
                trovata = True
            if trovata:
                richW.corretta = True
            parole.append(richW)
        return parole

    def searchWordLinear(self, word, language):
        parole = []

        for word in words:
            word = word.lower()
            found = False
            richW = rw.RichWord(word)
            if language == "english":
                if self._english.dict.__contains__(word):
                    found = True
            elif language == "italian":
                if self._italian.dict.__contains__(word):
                    found = True
            elif language == "spanish":
                if self._spanish.dict.__contains__(word):
                    found = True
            if (found):
                richW.corretta = True

            parole.append(richW)

        return parole

    def searchWordLinear(self, words, language): # come prima ma cerca in tutto il dizionario anzichè usare contains
        # words is a list of strings
        parole = []

        for word in words:
            word = word.lower()
            found = False
            richW = rw.RichWord(word)
            if language == "english":
                for entry in self._english.dict:
                    if entry == word:
                        found = True
            elif language == "italian":
                for entry in self._italian.dict:
                    if entry == word:
                        found = True
            elif language == "spanish":
                for entry in self._spanish.dict:
                    if entry == word:
                        found = True
            if (found):
                richW.corretta = True

            parole.append(richW)

        return parole

    def searchWordDichotomic(self, words, language):
        # words is a list of strings
        parole = []

        for word in words:
            word = word.lower()
            found = False
            richW = rw.RichWord(word)
            if language == "english":
                currentDic = self._english.dict
                found = dichotomicSearch(word, currentDic)
            elif language == "italian":
                currentDic = self._italiano.dict
                found = dichotomicSearch(word, currentDic)
            elif language == "spanish":
                currentDic = self._spanish.dict
                found = dichotomicSearch(word, currentDic)
            if (found):
                richW.corretta = True

            parole.append(richW)

        return parole


def dichotomicSearch(word, currentDic):
    start = 0
    end = len(currentDic)

    while (start != end):
        mean = start + int((end - start) / 2)
        currentW = currentDic[mean]
        if word == currentW:
            return True
        elif word > currentW:  # in python < applied to strings gives True if the first string is before in lexicographic order
            start = mean + 1
        else:
            end = mean

    return False