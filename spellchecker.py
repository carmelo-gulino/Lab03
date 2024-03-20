import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.multiDict = md.MultiDictionary()

    def aggiungiLingua(self, lingua, path):
        self.multiDict.addDict(lingua, path)

    def handleSentence(self, txtIn, language):
        text = replaceChars(txtIn)
        t1 = time.time()
        wrong = [w for w in self.multiDict.searchWord(text, language) if w.corretta==False]
        t2 = time.time()
        self.printWrong(wrong, t2-t1, "contains")
        t1 = time.time()
        wrong = [w for w in self.multiDict.searchWordLinear(text, language) if w.corretta==False]
        t2 = time.time()
        self.printWrong(wrong, t2 - t1, "Linear search")
        t1 = time.time()
        wrong = [w for w in self.multiDict.searchWordDichotomic(text, language) if w.corretta==False]
        t2 = time.time()
        self.printWrong(wrong, t2 - t1, "Dcchotomic search")

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________")

    def printWrong(self, wrong, t, metodo):
        print("______________________________")
        print(f"Using {metodo}")
        for w in wrong:
            print(w)
        print(f"Time elapsed {t}")
        print("______________________________")

def replaceChars(text):
    chars = "\\',*_{}[]()>#+-.!$%&^;.=_~?"
    for c in chars:
        text = text.replace(c, "")
    return text.lower()