from tkinter    import *
from Controleur import *

class Vue(Frame): 
    def __init__(self, fenetre):
        Frame.__init__(self, fenetre, width=768, height=576)
        self.pack()
        self.ctrl = Controleur()

        cadreLabelCodeReset = Frame(self)
        cadreLabelCodeReset.pack(side = TOP)
        cadreLabelTexte = Frame(self)
        cadreLabelTexte.pack(side = TOP)
        cadre123 = Frame(self)
        cadre123.pack(side = TOP)
        cadre456 = Frame(self)
        cadre456.pack(side = TOP)
        cadre789 = Frame(self)
        cadre789.pack(side = TOP)
        cadre0 = Frame(self)
        cadre0.pack(side = TOP)

        self.labelCode = Label(cadreLabelCodeReset, text="", height=3, width=29,
                             relief = RAISED, font = (20), wraplength = 250)
        self.labelCode.pack(side ="left")
        self.labelTexte = Label(cadreLabelTexte, text="", height=7, width=36,
                             relief = RAISED, font = (20), wraplength = 290)
        self.labelTexte.pack(side = "left")

        self.boutonReset = Button(cadreLabelCodeReset, text="Reset",
                                  relief = RAISED, height=3, width=8
                                  , command=self.cliquerReset)
        self.boutonReset.pack( side="left")
        self.boutonDel = Button(cadreLabelCodeReset, text="Del", relief = RAISED
                                , command=self.cliquerDel, height=3, width=8)
        self.boutonDel.pack( side="left")
        self.boutonSelect = Button(cadreLabelTexte, text="Select", height=8, width=8
                                   , command=self.cliquerSelect)
        self.boutonSelect.pack(side="left")
        self.bouton1 = Button(cadre123, text="1 .", height=4, width=17
                              , command=self.cliquer1)
        self.bouton1.pack(side="left")
        self.bouton2 = Button(cadre123, text="2 abc", command=self.cliquer2,
                              height=4, width=18)
        self.bouton2.pack(side="left")
        self.bouton3 = Button(cadre123, text="3 def", command=self.cliquer3,
                              height=4, width=17)
        self.bouton3.pack(side="left")
        self.bouton4 = Button(cadre456, text="4 ghi", command=self.cliquer4,
                              height=4, width=17)
        self.bouton4.pack(side="left")
        self.bouton5 = Button(cadre456, text="5 jkl", command=self.cliquer5,
                              height=4, width=18)
        self.bouton5.pack(side="left")
        self.bouton6 = Button(cadre456, text="6 mno", command=self.cliquer6,
                              height=4, width=17)
        self.bouton6.pack(side="left")
        self.bouton7 = Button(cadre789, text="7 pqrs", command=self.cliquer7,
                              height=4, width=17)
        self.bouton7.pack(side="left")
        self.bouton8 = Button(cadre789, text="8 tuv", command=self.cliquer8,
                              height=4, width=18)
        self.bouton8.pack(side="left")
        self.bouton9 = Button(cadre789, text="9 wxyz", command=self.cliquer9,
                              height=4, width=17)
        self.bouton9.pack(side="left")
        self.boutonEtoile = Button(cadre0, text="*", height=4, width=17)
                                   #, command=self.cliquerEtoile)
        self.boutonEtoile.pack( side="left")
        self.bouton0 = Button(cadre0, text="0 espace", command=self.cliquer0
                              , height=4, width=18)
        self.bouton0.pack( side="left")
        self.boutonCarre = Button(cadre0, text="#", height=4, width=17)
                                  #, command=self.cliquerCarre)
        self.boutonCarre.pack( side="left")

    def cliquerReset(self):
        self.labelTexte["text"] = self.ctrl.clicReset()
        self.labelCode["text"] = self.ctrl.getCodeT9()
    def cliquerDel(self):
        self.labelTexte["text"] = self.ctrl.clicDel()
        self.labelCode["text"] = self.ctrl.getCodeT9()
    def cliquerSelect(self):
        self.labelTexte["text"] = self.ctrl.clicSelect()
        self.labelCode["text"] = self.ctrl.getCodeT9()
    def cliquer1(self):
        self.labelTexte["text"] = self.ctrl.clicNum(1)
        self.labelCode["text"] = self.ctrl.getCodeT9()
    def cliquer2(self):
        self.labelTexte["text"] = self.ctrl.clicNum(2)
        self.labelCode["text"] = self.ctrl.getCodeT9()
    def cliquer3(self):
        self.labelTexte["text"] = self.ctrl.clicNum(3)
        self.labelCode["text"] = self.ctrl.getCodeT9()
    def cliquer4(self):
        self.labelTexte["text"] = self.ctrl.clicNum(4)
        self.labelCode["text"] = self.ctrl.getCodeT9()
    def cliquer5(self):
        self.labelTexte["text"] = self.ctrl.clicNum(5)
        self.labelCode["text"] = self.ctrl.getCodeT9()
    def cliquer6(self):
        self.labelTexte["text"] = self.ctrl.clicNum(6)
        self.labelCode["text"] = self.ctrl.getCodeT9()
    def cliquer7(self):
        self.labelTexte["text"] = self.ctrl.clicNum(7)
        self.labelCode["text"] = self.ctrl.getCodeT9()
    def cliquer8(self):
        self.labelTexte["text"] = self.ctrl.clicNum(8)
        self.labelCode["text"] = self.ctrl.getCodeT9()
    def cliquer9(self):
        self.labelTexte["text"] = self.ctrl.clicNum(9)
        self.labelCode["text"] = self.ctrl.getCodeT9()
    #def cliquerEtoile(self):
    #    self.codeT9 = self.codeT9 + 'E'
    #    self.majlabels()
    def cliquer0(self):
        self.labelTexte["text"] = self.ctrl.clicNum(0)
        self.labelCode["text"] = self.ctrl.getCodeT9()
    #def cliquerCarre(self):
    #    self.codeT9 = self.codeT9 + 'C'
    #    self.majlabels()
