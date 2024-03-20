import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
        self.md = {}

    def addDict(self, lingua, path):
        lang = d.Dictionary(path)
        self.md = {lingua: lang}

    def printDic(self, language):
        try:
            self.md = d.Dictionary(language).printAll()
        except KeyError:
            print("Lingua non presente")

    def searchWord(self, words, language):
        r_words = []
        words = words.split()
        for word in words:
            if self.md[language].parole.__contains__(word):
                r_word = rw.RichWord(word)
                r_word.corretta = True
            else:
                r_word = rw.RichWord(word)
                r_word.corretta = False
            r_words.append(r_word)
        return r_words

    def searchWordLinear(self, words, language):
        r_words = []
        words = words.split()
        for word in words:
            ok=False
            for p in self.md[language].parole:
                if p==word:
                    ok=True
                    break
            r_word = rw.RichWord(word)
            if ok==True:
                r_word.corretta = True
            else:
                r_word.corretta = False
            r_words.append(r_word)
        return r_words

    def searchWordDichotomic(self, words, language):
        r_words = []
        words = words.split()
        for word in words:
            r_word = rw.RichWord(word)
            l = len(self.md[language].parole)
            dict = self.md[language].parole
            try:
                while(True):
                    l = int(l/2)
                    mid_word = dict[l]
                    if word==mid_word:
                        ok=True
                        break
                    elif word<mid_word:
                        dict = dict[:l]
                    elif word>mid_word:
                        dict = dict[l+1:]
                r_word.corretta = True
                r_words.append(r_word)
            except IndexError:
                r_word.corretta = False
                r_words.append(r_word)
        return r_words

