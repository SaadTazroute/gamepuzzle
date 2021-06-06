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

            indexes.append(L)

        return(indexes)


def checkdata(txtfile):
    global data, w, h

    # select data
    data = chargegrille(txtfile)

    # there needs to be some data
    if len(data) <= 0 or len(data[0]) <= 0:
        raise Exception("Please enter correct data.")

    # determine width and height
    w, h = len(data[0]), len(data)

    # check la longueur deslignes et les caracteres non autorisés
    for y in range(h):
        if len(data[y]) != w:
            raise Exception("Incorrect data width in line %d." % y)
        else:
            for x in range(w):
                if data[y][x] not in ("_", "0", "1", "2", "3"):
                    raise Exception("Unknown character '%s' in line %d, row %d." % (data[y][x], y, x))

    # slither should not be too small
    if w < 4 or h < 4:
        raise Exception("Grid too small, you can solve it yourself! Just do it")

    print("C'est bon tu peux commencer")
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



def longueurboucle(etat,segment) :
    path=[]
    depart  = segment[0]
    precedent = depart
    courant = segment[1]
    while (courant != depart) :
        segtraces = segments_traces(etat, depart)
        path.append(courant)
        if len(segtraces) != 2 :
            return None
        else :
            precedent = courant
            courant = autrepoint(precedent,(segments_traces(etat,courant)))
    return len(path)

def cond2victoire(etat,sommet =(1,1)) :
#On démarre la boucle pour savoir si la boucle est fermé à partir du premier segment tracé du dictionnaire etat
    segs = segments_traces(etat,sommet)
    segment = segmenttracés[0]     # choix de commencer par le point 1,1
    segmenttracétotal = 0
    for x in etat.keys():
        if etat[x]==1 :
            segmenttracétotal += 1
    if longueurboucle(etat,segment) is not None :
        return longueurboucle(etat,segment) == segmenttracétotal


def AutreSommet(segment,sommet):
    if segment[0] == sommet :
        return segment[1]
    else :
        return segment[0]

def segmentssuivnats(etat,sommet1,sommet2):
    L=list()
    for x in voisins(sommet2):
        if x == sommet1 :
            pass
        else:
            for i in range(len(voisins(sommet2))):
                L.append((x,voisins(sommet2)[i]))


def Recursivesolver(indices, etat, sommet):
    # on vérifier d'abord si la boucle est fermé
    for segment in etat :
        if longueur_boucle(etat, next(iter(etat))) is not None:
            # si oui, on vérifier alors si tt les indices sont satisfis
            if cond1victoire(indices, etat):
                return etat
            else:
                return None

    # si c'est non, alors on continue de tester le chemin
    dernier_seg = list(etat.keys())[-1]  # get le dernier segment
#    segmentsuivant =
    segment_suiv = Segments_suivant(indices.__len__(), Indices[0].__len__(), AutreSommet(dernier_seg, sommet), sommet)
    for seg_sv in segment_suiv:
        if est_vierge(etat, seg_sv):
            tracer_segment(etat, seg_sv)
            nouveau_etat = Recursivesolver(indices, etat, AutreSommet(seg_sv, sommet))
            if nouveau_etat is not None:
                return nouveau_etat
            effacer_segment(etat, seg_sv)
    return None

