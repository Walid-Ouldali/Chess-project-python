from case import *




def remplacePositionDepart(position): 
    """
    Fonction permettant de placer les pièces dans les positions saisies par l'utilisateur
    
    Arguments: 
    position -- Chaîne de charachtère contenant la position d'une pièce 
        exemples: rg1, h1, tf6
    """
    valeurDesPions = {"r": 6, "d": 5, "c": 3, "f": 4, "p": 1, "t": 2}
    if len(position) == 2: 
        ech[((int(position[1])*8) - (8 - (ord(position[0]) - 97 + 1)) - 1)] = -1
    else:
        ech[((int(position[2])*8) - (8 - (ord(position[1]) - 97 + 1)) - 1)] = -valeurDesPions[position[0]]


#1ère Fonction: saisie_pieces()
def saisie_pieces(): 
    """
    Cette fonction permet à l’utilisateur de saisir une position de départ.

    Exemple: 
    la chaîne 'rg1 f2 g2 h2' pour un roi en g1, des pions en f2, g2, h2    
    Arguments :
    Aucun
    """

    print("Entrez votre couleur (N/B):")
    couleur = input()

    while couleur.upper() != 'N' and couleur.upper() != 'B': 
        print("Saisie invalide")
        print("Entrez votre couleur (N/B):")
        couleur = input()

    if couleur == 'N': 
        print("Saisissez une position de départ:")
        positionDepart = input()
        #((nb * 8) - (8 - (ord(lettre) + 1))) - 1
        #["rg1"]
        tableauDeRemplissage = positionDepart.split()   
        i = 0
        while i < len(tableauDeRemplissage): 
            position = tableauDeRemplissage[i]#rg1
            remplacePositionDepart(position)
            i+=1
    else: 
        print("\nSaisissez une position de départ:")
        positionDepart = input()


        tableauDeRemplissage = positionDepart.split()
        i = 0
        while i < len(tableauDeRemplissage) : 
            position = tableauDeRemplissage[i]#a8
            remplacePositionDepart(position)
            i+=1
    print("\n\nL'échiquier après le remplissage:")
    print(ech)


#saisie_pieces()


#help(saisie_pieces) #aka/ ?saisie_pieces


#2ème Fonction: posit()
def posit(echiquier): 
    """
    Fonction permettant de placer toutes les pièces dans la position initiale standard.
    
    Arguments: Aucun
    """

    ech = echiquier.copy()
    return ech
ech = posit(echiquier)