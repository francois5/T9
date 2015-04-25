def lettre(c):
    return ((ord(c) <= ord('z') and ord(c) >= ord('a'))
            or (ord(c) <= ord('Z') and ord(c) >= ord('A')))

# Attention c doit etre une lettre
def charVersNum(c):
    v = ['2','2','2','3','3','3','4','4','4','5','5','5','6','6','6',
         '7','7','7','7','8','8','8','9','9','9','9']
    return v[ord(c.lower()) - ord('a')]

def motVersCode(mot):
    i = 0
    T9Mot = ""
    while i < len(mot):
        if lettre(mot[i]):
            T9Mot = T9Mot + charVersNum(mot[i])
        i += 1
    return T9Mot

#attention ssch ne doit contienir qu'un caractaire
def contient(ch, ssch):
    for c in ch:
        if c == ssch:
            return True
    return False
