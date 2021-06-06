import os
from random import random

import random

def chargegrille(fichier):  # script chargement de grille à partir d'un fichier texte ===> liste de listes (indexes)
    indexes = []
    with open(fichier, 'r') as read_file:
        length = len(read_file.readline())

        for line in read_file.readlines():
            L = list(line)
            L.remove('\n')
            for index, item in enumerate(L):
                if item == '_':
                    L[index] = None
            indexes.append(L)

        return(indexes)


def checkdata(txtfile):
    global data, w, h

    # select data
    data = chargegrille(txtfile)

    # there needs to be some data
    if len(data) <= 0 or len(data[0]) <= 0:
        print("Please enter data.")
        return False

    # determine width and height
    w, h = len(data[0]), len(data)

    # check every line for its length and characters
    for y in range(h):
        if len(data[y]) != w:
            print("Incorrect data width in line %d." % y)
            return False
        else:
            for x in range(w):
                if data[y][x] not in ("_", "0", "1", "2", "3"):
                    print("Unknown character '%s' in line %d, row %d." % (data[y][x], y, x))
                    return False

    # slither should not be too small
    if w < 4 or h < 4:
        print("Slither too small, solve it yourself!")
        return False

    # data was checked
    return True



# consigne  : Afin de ne pas avoir des doublons d'informations, on choisira toujours
# de représenter les segments dans le dictionnaire en donnant en premier le sommet le plus petit
# dans l’ordre lexicographique. (somme d'indice le plus bas en premiere position)
def norepetition(dict):
    for x in dict.keys():
        if (x[0][0] + x[0][1])   >  (x[1][0] + x[1][1]) :
            x[0],x[1] = x[1],x[0]
    return dict


#chargegrille('data.txt')



#chargegrille('data.txt')

def est_trace(etat,segment) :
    if segment in list(etat.keys()):
        if(etat[segment]==-1):
            print("Tracé!")
            return True
    return False

def est_interdit(etat,segment) :
    if segment in list(etat.keys()):
        if(etat[segment]==-1):
            print("Interdit!")
            return True
    return False


def est_vierge(etat,segment) :
    if segment not in list(etat.keys()):
        return True
    else :
        return False









def traceseg(etat,segment):
    etat[segment]=1
    #return  etat

def interdireseg(etat,segment):
    etat[segment] = -1#
    #return etat

def effacer_segment(etat, segment):
    if segment in list(etat.keys()):
        etat = etat.pop(segment)
    #return etat



def segments_traces(etat, sommet) :
    Listesegmentstraces = []
    for x in etat.keys():
        if (sommet in x ) and est_trace(etat, x):
      #  if (sommet in x ) and etat[x]==1 :
            Listesegmentstraces.append(x)
    return Listesegmentstraces

def segments_interdits(etat, sommet) :
    Listesegmentsinterdits = []
    for x in etat.keys():
        if (sommet in x ) and est_interdit(etat, x):
        #if (sommet in x ) and etat[x]==-1 :
            Listesegmentsinterdits.append(x)
    return Listesegmentsinterdits



def segments_vierges(etat, sommet) :
    Listesegmentsvierges = []
    for x in etat.keys():
        if (sommet in x ) and est_vierge(etat, x):
            Listesegmentsvierges.append(x)
    return Listesegmentsvierges


def statut(indexes, etat, case):
    compteur = 0  # nombre de lignes tracés autour de la case
    x = case[0]
    y = case[1]
    if indexes[x][y] == None:
        pass
    else:
        if est_trace(etat, ((x, y), (x, y + 1))) :  # ligne a gauche
            compteur += 1
        if est_trace(etat, ((x, y + 1), (x + 1, y + 1))) :  # ligne en haut de la case
            compteur += 1
        if est_trace(etat, ((x + 1, y), (x + 1, y+1))) :  # ligne a droite
            compteur += 1
        if est_trace(etat, ((x, y), (x + 1, y))) :  # ligne en bas
            compteur += 1

        return int(indexes[x][y]) - compteur

def cond1victoire(indexes,etat) :
    for l in indexes :
        for case in l :
            if case in [0,1,2,3] :
                if statut(indexes, etat, case) != 0 :
                    return False
    return True




"""def cond1victoire(indexes,etat) :
    for case in indexes :
        if case in [None,0,1,2,3] :
            if statut(indexes, etat, case) != 0 :
                return False
    return True


for i in range (l):
    for j in range(h):
        


"""

def voisins(sommet):
    left, right, up,down = (sommet[0]-1,sommet[1]) , (sommet[0]+1,sommet[1]) , (sommet[0],sommet[1]+1) , (sommet[0],sommet[1]-1)
    return left, right, up,down



def cond2victoire(etat,segment) :
    path=[]
    depart  = segment[0]
    precedent = depart
    courant = segment[1]
    while (courant != depart) :
        path.append(courant)
        if len(segments_traces(etat, depart)) != 2 :
            return None
        else :
            adjacents = list(voisins(sommet))
            adjacents = adjacents.pop(precedent)
            precedent = courant
            courant = random.choice(adjacents)
