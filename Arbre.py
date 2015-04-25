from programmes import *

class Arbre():
    def __init__(self):
        self.rac = self.Noeud()

    class Noeud():
        def __init__(self):
            self.mots = []
            self.fils = []
            for i in range(0, 8):
                self.fils.append(0)
    
    def trouve(self, codeT9):
        n = self.rac
        for c in codeT9:
            if n.fils[(ord(c)-ord('0'))-2] == 0:
                n.fils[(ord(c)-ord('0'))-2] = self.Noeud()
            n = n.fils[(ord(c)-ord('0'))-2]
        return n

    def ajouterMot(self, mot):
        T9Mot = motVersCode(mot)
        n = self.trouve(T9Mot)
        if n.mots.count(mot) == 0:
            n.mots.append(mot)

    def remplitArbre(self, nomDico):
        f = open(nomDico, "r")
        for mot in f:
            mot = mot[:-1]
            self.ajouterMot(mot)
        f.close()
