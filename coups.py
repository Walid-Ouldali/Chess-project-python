from affiche import *

ech[35] = 2
def caseDePiece(i):
    print(i)
    if (i+1) %8 == 0: 
        return chr(8 - 1 + ord('a')) + str((i + 1)//8)
    else:
        return chr((i+1)%8-1+ord('a')) + str((i + 1)//8 + 1)

print(caseDePiece(0))

def deplacements(typeP, i, ech): 
    pos = i
    repetition = ['t', 'd', 'f']
    tab = []
    if typeP == 'p' and i >= 56 and i <= 63 and ech[i]>0: 
        typeP = 'd'
        ech[i] = 5
    if typeP == 'p' and i >= 0 and i <= 7 and ech[i]<0: 
        typeP = 'd'
        ech[i] = -5

    if typeP  == 't': 
        tab = [8, -8, 1, -1]
    elif typeP == 'c': 
        tab = [15, 17, -15, -17, 10, 6, -10, -6]
    elif typeP == 'f': 
        tab = [7, 9, -9, -7]
    elif typeP == 'd': 
        tab = [8, -8, 1, -1, 7, 9, -9, -7]
    elif typeP == 'r': 
        tab = [8, -8, 1, -1, 7, 9, -9, -7]
    else:
        tab = [8]
    if ech[i] < 0: 
        i = 0
        while i < len(tab): 
            tab[i] = -tab[i]
            i+=1
    coups = []


    
    if typeP in repetition: 
        j = 0
        while j < len(tab):
            val = tab[j]
            
            while tab[j] + i <= 63 and tab[j] + i>= 0 :
                
                print(val)
                if ech[tab[j] + i]*ech[i] < 0 or ech[tab[j] + i +1]%8 == 0: 
                    coups.append(caseDePiece(tab[j] + i))
                    break
                if ech[tab[j] + i]*ech[i] <= 0:
                    coups.append(caseDePiece(tab[j] + i))
                print(tab[j])
                tab[j]+=val
            
            
            j+=1
        

    else: 
        j = 0
        while j < len(tab): 
            coups.append(caseDePiece(i+tab[j]))
            j+=1

        

    
    return coups




print(deplacements("t", 35, ech))





    
    


#['d6', 'd7', 'd4', 'd3', 'e5', 'f5', 'g5', 'h5', 'a6', 'c5', 'b5']
#print(coups("c", 'h8', 63, ech))

def actu(ech): 
    i = 0
    piecesBlanches = []
    piecesNoires = []





    while i < len(ech): 
        if ech[i] > 0: 
            piecesBlanches.append({})
            typePiece = typeDePiece(ech[i]) 
            piecesBlanches[i]["type"] = typePiece
            piecesBlanches[i]["position"] = caseDePiece(i)
            piecesBlanches[i]["coups"] = deplacements(piecesBlanches[i]["type"], i, ech)
















""""
def coups(typeP, position, i, ech):
    pos = i
    tab = []
    if typeP == 'p': 
        if ech[i]>0: 
            if int(position[1]) == 8: 
                typeP = 'd'
                ech[i] = 5
            else:
                if  i+8 <= len(ech) - 1  and ech[i+8] == 0:
                    tab.append(position[0] + str(int(position[1]) + 1))
                if position[1] == '2': 
                    tab.append(position[0] + str(int(position[1]) + 2))
                if i+8 <= len(ech) - 1 and ech[i+7] < 0  : 
                    tab.append(chr(ord(position[0]) -1) + position[1])
                if i+9 <= len(ech) - 1 and ech[i+9] < 0 : 
                    tab.append(chr(ord(position[0]) +1) + position[1])
        else:
            if int(position[1]) == 1: 
                typeP = 'd'
                ech[i] = -5
            else:
                if ech[i-8] == 0 and i-8 >= 0:
                    tab.append(position[0] + str(int(position[1]) - 1))
                if position[1] == '7': 
                    tab.append(position[0] + str(int(position[1]) - 2))
                if ech[i-7] > 0 and i-8>= 0: 
                    tab.append(chr(ord(position[0]) +1) + position[1])
                if ech[i-9] > 0 and i-9 >= 0: 
                    tab.append(chr(ord(position[0]) -1) + position[1])
    elif typeP == 't': 
        if ech[i] > 0: 
            while i + 8 <= len(ech) - 1 and ech[i+8] <= 0: 
                if ech[i+8] == 0:
                    tab.append(caseDePiece(i+8))
                if ech[i+8] * ech[pos] < 0: 
                    tab.append(caseDePiece(i+8))
                    break

                i+=8
            i = pos
            while i - 8 >= 0 and ech[i-8] <= 0: 
                if ech[i-8] == 0:
                    tab.append(caseDePiece(i-8))
                if ech[i-8] * ech[pos] < 0: 
                    tab.append(caseDePiece(i-8))
                    break
                i-=8

            i = pos
            while (i+1)%8 != 0 and ech[i+1] <= 0 :
                if ech[i+1] == 0: 
                    tab.append(caseDePiece(i+1))
                elif ech[i+1] < 0: 
                    tab.append(caseDePiece(i+1))
                    break
                i+=1
            
            i = pos - 2
            while i%8 != 0 and ech[i+1] <= 0 and i +1 <= len(ech)-1:
                if ech[i+1] == 0: 
                    tab.append(caseDePiece(i+1))
                elif ech[i+1] < 0: 
                    tab.append(caseDePiece(i+1))
                    break
                
                
                i-=1 
            if i%8 == 0: 
                tab.append(caseDePiece(i+1))
                tab.append(caseDePiece(i))

            i = pos
        elif ech[i] < 0: 
            while i + 8 <= len(ech) - 1 and ech[i+8] >= 0: 
                if ech[i+8] == 0:
                    tab.append(caseDePiece(i+8))
                if ech[i+8] > 0: 
                    tab.append(caseDePiece(i+8))
                    break
                i+=8
            i = pos
            while i - 8 >= 0 and ech[i-8] >= 0: 
                if ech[i-8] == 0:
                    tab.append(caseDePiece(i-8))
                if ech[i-8] > 0: 
                    tab.append(caseDePiece(i-8))
                    break
                i-=8

            i = pos
            while (i+1)%8 != 0 and ech[i+1] >= 0 :
                if ech[i+1] == 0: 
                    tab.append(caseDePiece(i+1))
                elif ech[i+1] > 0: 
                    tab.append(caseDePiece(i+1))
                    break
                i+=1
            
            i = pos - 2
            while i%8 != 0 and ech[i+1] >= 0 and i +1 <= len(ech)-1:
                if ech[i+1] == 0: 
                    tab.append(caseDePiece(i+1))
                elif ech[i+1] > 0: 
                    tab.append(caseDePiece(i+1))
                    break
                
                i-=1 
            if i%8 == 0: 
                tab.append(caseDePiece(i+1))
                tab.append(caseDePiece(i))

            i = pos

    elif typeP == 'c':
            if  i+15<len(ech)-1 and ech[i+15]*ech[i] <= 0: 
                tab.append(caseDePiece(i+15))
            if  i+17 < len(ech)-1 and ech[i+17]*ech[i] <= 0: 
                tab.append(caseDePiece(i+17))
            if i+10< len(ech) - 1 and  ech[i+10]*ech[i] <= 0 : 
                tab.append(caseDePiece(i+10))
            if i+6 < len(ech)-1 and ech[i+6] * ech[i] <= 0: 
                tab.append(caseDePiece(i+6))
            if  i-15 >= 0 and ech[i-15]*ech[i] <= 0: 
                tab.append(caseDePiece(i-15))
            if  i-17 >= 0 and ech[i-17]*ech[i] <= 0: 
                tab.append(caseDePiece(i-17))
            if i-10 >= 0  and  ech[i-10]*ech[i] <= 0 : 
                tab.append(caseDePiece(i-10))
            if i-6 >= 0 and ech[i-6] * ech[i] <= 0: 
                tab.append(caseDePiece(i-6))
"""