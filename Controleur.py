from Texte import *

class Controleur():
    def __init__(self):
        self.txt = Texte()

    def clicNum(self, num):
        self.txt.setCodeT9(self.txt.codeT9 + chr(num+ord('0')))
        self.txt.majTexte()
        return self.txt.texteCour
    def clicSelect(self):
        self.txt.texteMotSuiv()
        return self.txt.texteCour
    def clicReset(self):
        self.txt.reset()
        return self.txt.texteCour
    def clicDel(self):
        self.txt.delete()
        return self.txt.texteCour
    def getCodeT9(self):
        return self.txt.codeT9
