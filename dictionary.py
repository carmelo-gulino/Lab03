class Dictionary:
    def __init__(self, path):
        self.parole = []
        self.loadDictionary(path)

    def loadDictionary(self,path):
        with open(path, "r", encoding="utf-8") as d:
            for riga in d:
                riga = riga.rstrip()
                self.parole.append(riga)

    def printAll(self):
        for word in self.parole:
            print(word)

    @property
    def dict(self):
        return self._dict
