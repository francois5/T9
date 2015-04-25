from tkinter    import *
from Arbre      import *
from prediction import *
from programmes import *

class Texte(): 
    def __init__(self):
        self.codeT9 = ""
        self.texteCour = ""
        self.debutPhrase = True
        self.numMot = 0
        self.ab = Arbre()
        self.ab.remplitArbre("dico.txt")

    def setCodeT9(self, nouvCode):
        self.codeT9 = nouvCode

    def mots(self, index):
        if self.codeT9 == "":
            return ""
        else:
            return preditMots(self.ab, self.codeT9, index, 8)

    def espaceOuPoint(self):
        if self.codeT9[len(self.codeT9)-1] == "0":
            self.debutPhrase = False
            return self.texteCour + " "
        elif self.codeT9[len(self.codeT9)-1] == "1":
            self.debutPhrase = True
            return self.texteCour + ". "
        else:
            return ""

    def debutMotCode(self):
        res=len(self.codeT9)-1
        while res >= 0 and self.codeT9[res] != "0" and self.codeT9[res] != "1":
            res-=1
        res+=1
        return res

    def debutMotTexte(self):
        res = len(self.texteCour)-1
        while res >= 0 and self.texteCour[res] != " ":
            res-=1
        res+=1
        return res

    # Retourne le texte + le mot que l'utilisateur est en train de saisir
    # ("lettre" parce que le code T9 se termine par une lettre et non un espace ou un point)
    def lettre(self):
        if len(self.mots(self.debutMotCode())) <= self.numMot:
            self.numMot = 0 # gestion de l'exeption ou l'utilisateur clic sur le bouton select et qu'il y a moins de 8 mots
        if self.debutPhrase == False:
            return self.texteCour[0:self.debutMotTexte()] + self.mots(self.debutMotCode())[self.numMot]
        else:
            if len(self.mots(self.debutMotCode())) > 0:
                return self.texteCour[0:self.debutMotTexte()] + self.mots(self.debutMotCode())[self.numMot].capitalize()
        return self.texteCour[0:self.debutMotTexte()].capitalize()

    def texte(self):
        if self.codeT9 == "":
            return ""
        if self.espaceOuPoint() != "":
            return self.espaceOuPoint()
        else:
            return self.lettre()

    def majTexte(self, resetNumMot = True):
        if resetNumMot:
            self.numMot = 0
        self.texteCour = self.texte()

    def majDebutPhrase(self):
        if not contient(self.texteCour, " "):
            self.debutPhrase = True

    def reset(self):
        self.codeT9 = ""
        self.debutPhrase = True
        self.majTexte()

    def delete(self):
        if self.codeT9[len(self.codeT9)-1] == '0':
            self.texteCour = self.texteCour[:-1]
        elif self.codeT9[len(self.codeT9)-1] == '1':
            self.texteCour = self.texteCour[:-2]
            self.debutPhrase = False
        self.codeT9 = self.codeT9[:-1]
        if len(self.codeT9) > 0 and self.codeT9[len(self.codeT9)-1] != '0' and self.codeT9[len(self.codeT9)-1] != '1':
            self.majDebutPhrase()
            self.majTexte()
        else:
            self.texteCour = self.texteCour[:-1]
    
    def texteMotSuiv(self):
        if self.numMot > 6:
            self.numMot = 0
        else:
            self.numMot += 1
        self.majTexte(False)
