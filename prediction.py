from Arbre import *

def preditMots(ab, codeT9, indexDebut, nbMots):
    indexFin = indexDebut
    while (indexFin < len(codeT9) and codeT9[indexFin] != "0"
           and codeT9[indexFin] != "1"):
        indexFin += 1
    indexFin += 1
    n = ab.trouve(codeT9[indexDebut:indexFin])
    return motsSuiv(n, nbMots)

def motsSuiv(n, nbMots):
    mots = []
    mots.extend(n.mots)
    couche = 1
    while len(mots) < nbMots and couche <= 25:
        mots.extend(rechercheCouche(n, couche))
        couche += 1
    if len(mots) > nbMots:
        mots = mots[:-(len(mots)-nbMots)]
    return mots

def rechercheCouche(rac, couche):
    mots = []
    if couche == 1:
        return trouveMotsDansFils(rac)
    i = 0
    while i < len(rac.fils):
        if rac.fils[i] != 0:
            mots.extend(rechercheCouche(rac.fils[i], couche-1))
        i += 1
    return mots

def trouveMotsDansFils(rac):
    mots = []
    i = 0
    while i < len(rac.fils):
        if rac.fils[i] != 0:
            mots.extend(rac.fils[i].mots)
        i += 1
    return mots
