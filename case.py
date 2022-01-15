#Tableau représentant l'échiquier
ech = [
#   a, b, c, d, e, f, g, h
    0, 0, 0, 0, 0, 0, 0, 0, #1
    0, 0, 0, 0, 0, 0, 0, 0, #2
    0, 0, 0, 0, 0, 0, 0, 0, #3
    0, 0, 0, 0, 0, 0, 0, 0, #4
    0, 0, 0, 0, 0, 0, 0, 0, #5
    0, 0, 0, 0, 0, 0, 0, 0, #6
    0, 0, 0, 0, 0, 0, 0, 0, #7
    0, 0, 0, 0, 0, 0, 0, 0, #8
]



#Échiquier d'initialisation
echiquier = [
    2, 3, 4, 5, 6, 4, 3, 2,
    1, 1, 1, 1, 1, 1, 1, 1,
    0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 
   -1,-1,-1,-1,-1,-1,-1,-1, 
   -2,-3,-4,-5,-6,-4,-3,-2
]

#Tableau de pièces blanches (début de partie)
piecesBlanches = [
#Pions
    {"type" : 'p', "position": 'a2', "destination": ['a3', 'a4']},
    {"type" : 'p', "position": 'b2', "destination": ['b3', 'b4']},
    {"type" : 'p', "position": 'c2', "destination": ['c3', 'c4']},
    {"type" : 'p', "position": 'd2', "destination": ['d3', 'd4']},
    {"type" : 'p', "position": 'e2', "destination": ['e3', 'e4']},
    {"type" : 'p', "position": 'f2', "destination": ['f3', 'f4']},
    {"type" : 'p', "position": 'g2', "destination": ['g3', 'g4']},
    {"type" : 'p', "position": 'h2', "destination": ['h3', 'h4']},
#Tours
    {"type" : 't', "position": 'a1', "destination": []},
    {"type" : 't', "position": 'h1', "destination": []},
#Cavaliers
    {"type" : 'c', "position": 'b1', "destination": ['a3', 'c3']},
    {"type" : 'c', "position": 'g1', "destination": ['h3', 'f3']},
#Fou
    {"type" : 'f', "position": 'c1', "destination": []},
    {"type" : 'f', "position": 'f1', "destination": []},
#Dame
    {"type" : 'd', "position": 'd1', "destination": []},
#Roi
    {"type" : 'r', "position": 'e1', "destination": []},
]


#Tableau de pièces noires (début de partie)
piecesNoires = [
#Pions
    {"type" : 'p', "position": 'a7', "destination": ['a6', 'a5']},
    {"type" : 'p', "position": 'b7', "destination": ['b6', 'b5']},
    {"type" : 'p', "position": 'c7', "destination": ['c6', 'c5']},
    {"type" : 'p', "position": 'd7', "destination": ['d6', 'd5']},
    {"type" : 'p', "position": 'e7', "destination": ['e6', 'e5']},
    {"type" : 'p', "position": 'f7', "destination": ['f6', 'f5']},
    {"type" : 'p', "position": 'g7', "destination": ['g6', 'g5']},
    {"type" : 'p', "position": 'h7', "destination": ['h6', 'h5']},
#Tours
    {"type" : 't', "position": 'a8', "destination": []},
    {"type" : 't', "position": 'h8', "destination": []},
#Cavaliers
    {"type" : 'c', "position": 'b8', "destination": ['a6', 'c6']},
    {"type" : 'c', "position": 'g8', "destination": ['h6', 'f6']},
#Fou
    {"type" : 'f', "position": 'c8', "destination": []},
    {"type" : 'f', "position": 'f8', "destination": []},
#Dame
    {"type" : 'd', "position": 'd8', "destination": []},
#Roi
    {"type" : 'r', "position": 'e8', "destination": []},
]

def caseExiste(case):#a13 
    if case[0].lower() >= 'a' and case[0].lower() <= 'h' and int(case[1]) >= 1 and int(case[1]) <= 8 and len(case) == 2: 
        return True
    else:
        return False


def caseVide(case): 
    if caseExiste(case) == True: 
        if ech[numeroDeCase(case)] != 0:
            return False
        else: 
            return True
    else: 
        print(f"La case {case} n'existe pas")

def occupeCase(case):
    if caseExiste(case)  == True: 
        if caseVide(case) == False: 
            if ech[numeroDeCase(case)] < 0: 
                return -1
            else:
                return 1
    
    

def numeroDeCase(case): #a7
    return ((int(case[1])*8) - (8 - (ord(case[0]) - 97 + 1)) - 1)


valeurDesPieces = {"r": 6, "d": 5, "c": 3, "f": 4, "p": 1, "t": 2}