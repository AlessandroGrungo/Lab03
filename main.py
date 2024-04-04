import spellchecker

sc = spellchecker.SpellChecker()

def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text

while(True):

    sc.printMenu()

    txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input()
        txtIn = replaceChars(txtIn)
        sc.handleSentence(txtIn,"italiano")
        continue

    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input()
        txtIn = replaceChars(txtIn)
        sc.handleSentence(txtIn,"english")
        continue

    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input()
        txtIn = replaceChars(txtIn)
        sc.handleSentence(txtIn,"spanish")
        continue

    if int(txtIn) == 4:
        print("Grazie per aver scelto noi, alla prossima!")
        break

    else:
        print("Selezione non vaida, sei pregato di inserire un numero intero da 1 a 4")
