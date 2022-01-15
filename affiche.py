from init import *
from colored import *





pieces = {
    "b" : {
        'r': '♔',
        'd': '♕',
        't': '♖',
        'f': '♗',
        'c': '♘',
        'p': '♙'
    },
    "n": {
        'r': '♚',
        'd': '♛',
        't': '♜',
        'f': '♝',
        'c': '♞',
        'p': '♟'
    }
}

def typeDePiece(case): 
    valeurDesPieces = {"r": 6, "d": 5, "c": 3, "f": 4, "p": 1, "t": 2}

    case = abs(case)
    
    valeurs = list(valeurDesPieces.values())
    types = list(valeurDesPieces) 
    
    i = 0
    
    while i < len(valeurs):
        if valeurDesPieces[types[i]] == case: 
                return types[i]
        i+=1

def printLettres(blanc): 
    color = fg(15) + bg(0)
    res = attr('reset')
    lettres = color + "   " + res
    if blanc: 
        i = 0
        while i < 8: 
            lettres += color + "    " + chr(97 + i) + "   "  + res 
            i+=1
    else:
        i = 0
        while i < 8: 
            lettres += color + "    " + chr(104 - i) + "   "  + res 
            i+=1


    print(lettres)
        




def pieceDansLaCase(case, pieces, valeurDesPieces): 
    if case < 0: 
        return pieces["n"][typeDePiece(case)]
    else:  
        return pieces["b"][typeDePiece(case)]


i = 0
def afficheEchiquier(blanc, ech, pieces, valeurDesPieces): 
    s = ""
    j = 0
    vide = ""
    
    
    if not(blanc):
        k = 0
        l = 0
        i = 8
        while i <= len(ech) +7: 
            l-=1
            if j%2 == 0: 
                color = fg(0) + bg('#EBEBD0')
                res = attr('reset')
            else: 
                color = fg(0) + bg('#779455')
                res = attr('reset')
            if ech[i+l] != 0:
                case = "   " + pieceDansLaCase(ech[l+i], pieces, valeurDesPieces) + "    "
            else: 
                case = "        "

            vide += color + "        " + res
            s+= color  +  case  + res
            
            if l == -8: 
                i+= 8
                l = 0
                k +=1 
                j+=1
                color = fg(15) + bg(0)
                res = attr('reset')
                
                print(color + "   " + res + vide)
                
                print(color + " " + str(k) + " " + res+ s)
                
                
                print(color + "   " + res + vide)

                s = ""
                vide = ""
            
            j+=1
        printLettres(False)
    else:
        k = 8
        l = 0
        i = len(ech) - 1 - 8
        while i >= -8: 
            l+=1
            if j%2 == 0: 
                color = fg(0) + bg('#EBEBD0')
                res = attr('reset')
            else: 
                color = fg(0) + bg('#779455')
                res = attr('reset')
            if ech[i+l] != 0:
                case = "   " + pieceDansLaCase(ech[l+i], pieces, valeurDesPieces) + "    "
            else: 
                case = "        "

            vide += color + "        " + res
            s+= color  +  case  + res
            
            if l%8 == 0: 
                i-= 8
                l = 0
                
                j+=1
                color = fg(15) + bg(0)
                res = attr('reset')
                
                print(color + "   " + res + vide)
                
                print(color + " " + str(k) + " " + res+ s)
                
                
                print(color + "   " + res + vide)
                k-= 1
                s = ""
                vide = ""
            
            j+=1
        printLettres(True)

if __name__ == '__main__':
    afficheEchiquier(True, ech, pieces, valeurDesPieces)