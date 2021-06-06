from fltk import *
from utilities import *
import fltk


#dimentions = [400, 600]
#h = int(dimentions[0]/50)
#l = int(dimentions[1]/50)

ax = {}     # definition des axes pour pouvoir reperer les sommets et les cases par des coordonnes
ay = {}
etat = {}

def libre(etat,segment) :
    if segment in list(etat.keys()):
        return False
    return True

def est_interdit(etat,segment) :
    if segment in list(etat.keys()):
        print("Interdit!")


def arete(pt1, pt2, couleure="black", tag=""):

    if pt1[0] != pt2[0] and pt1[1] != pt2[1]:
        return
    #add condition sur
    if len(tag)==0:
        tag = "({},{}),({},{})".format(pt1[0],pt1[1],pt2[0], pt2[1])
    rectangle((pt1[0] * 50) + 3, (pt1[1] * 50) + 3, (pt2[0] * 50) - 3, (pt2[1] * 50) - 3, remplissage=couleure, tag=tag)
    #print(tag)


if __name__ == "__main__":

    txtfile = "grille1.txt"
    checkdata(txtfile)
    #hna koun ghi tzid dik la partie read text
    #bach yloadi l indices
    #khass tkoun l matrice f nfss dim li dkhlna f l w h
    indices =chargegrille(txtfile)
    l = len(indices[0])
    h = len(indices)
    dimentions = [l * 50, h * 50]
    cree_fenetre(dimentions[0]+100, dimentions[1]+100)
    for i in range(l+1):
        ax[i] = i * 50
    for j in range(h+1):
        ay[j] = j * 50
    for i in range(l):
        for j in range(h):
            cercle(ax[i]+50, ay[j]+50, 3, remplissage="red")
            texte(ax[i]+20+50, ay[j]+10+50, str(indices[j][i]), taille=17)
    print(ax)
    for i in range(l):
        cercle(ax[i] + 50, ay[h] + 50, 3, remplissage="red")

    for j in range(h):
        cercle(ax[l] + 50, ay[j] + 50, 3, remplissage="red")


    cercle(ax[l] + 50, ay[h] + 50, 3, remplissage="red")

    attend_ev()
    #print(l,h)

    while   cond1victoire(indices,etat):

        #print(indices)
        ev = donne_ev()
        tev = type_ev(ev)
        print(statut(indices, etat, (0,1)))
        for i,j in zip(range(l),range(h)):
            if statut(indices, etat, (i,j)) == None :
                texte(ax[i] + 20 + 50, ay[j] + 10 + 50, str(indices[i][j]), taille=10)
            elif statut(indices, etat, (i,j)) > 0 :
                tag = "({},{})".format(i,j)
                efface(str(indices[i][j]))
                texte(ax[i] + 20 + 50, ay[j] + 10 + 50, str(indices[i][j]), taille=10)

        #print(indices[1])
        # Action dépendant du type d'événement reçu :

        if tev == 'Touche':
            print('Appui sur la touche', touche(ev))

        elif tev == "ClicDroit":
            # need to add a condition to stay in the game field(la brkto 3liiiimn ga3 wla 3liisr ga3 wakha machi bin 2 points rah ayrsmolk)
            if abscisse(ev) % 50 <= 10  and abscisse(ev) < 50*l :
                if libre(etat, ((int((abscisse(ev)+3)/50), int((ordonnee(ev))/50)), (int((abscisse(ev)+3)/50), int((ordonnee(ev))/50) + 1))):
                    arete([int((abscisse(ev)+3)/50), int((ordonnee(ev))/50)],
                          [int((abscisse(ev)+3)/50), int((ordonnee(ev))/50) + 1], "black")
                    traceseg (etat, ((int((abscisse(ev)+3)/50), int((ordonnee(ev))/50)), (int((abscisse(ev)+3)/50), int((ordonnee(ev))/50) + 1)) )
                    print(etat)
                else:
                    pt1_eff=[int((abscisse(ev) + 3) / 50), int((ordonnee(ev)) / 50)]
                    pt2_eff=[int((abscisse(ev) + 3) / 50) , int((ordonnee(ev)) / 50) + 1]
                    efface("({},{}),({},{})".format(pt1_eff[0],pt1_eff[1],pt2_eff[0], pt2_eff[1]))
                    print("({},{}),({},{})".format(pt1_eff[0],pt1_eff[1],pt2_eff[0], pt2_eff[1]))
                    del etat[tuple(pt1_eff),tuple(pt2_eff)]
                    print(etat)
                    print("effacé")
                    mise_a_jour()
            if ordonnee(ev) % 50 <= 3:
                if libre(etat, ((int((abscisse(ev)) / 50), int((ordonnee(ev) + 3) / 50)),
                                (int((abscisse(ev)) / 50) + 1, int((ordonnee(ev) + 3) / 50)))):
                    arete([int((abscisse(ev)) / 50), int((ordonnee(ev) + 3) / 50)],
                          [int((abscisse(ev)) / 50) + 1, int((ordonnee(ev) + 3) / 50)], "black")
                    etat[((int((abscisse(ev)) / 50), int((ordonnee(ev) + 3) / 50)),
                          (int((abscisse(ev)) / 50) + 1, int((ordonnee(ev) + 3) / 50)))] = 1
                else:
                    pt1_eff=[int((abscisse(ev)) / 50),
                                         int((ordonnee(ev) + 3) / 50)]
                    pt2_eff = [int((abscisse(ev)) / 50) + 1, int((ordonnee(ev) + 3) / 50)]
                    print("({},{}),({},{})".format(pt1_eff[0],pt1_eff[1],pt2_eff[0], pt2_eff[1]))
                    efface("({},{}),({},{})".format(pt1_eff[0],pt1_eff[1],pt2_eff[0], pt2_eff[1]))
                    del etat[((int((abscisse(ev)) / 50), int((ordonnee(ev) + 3) / 50)), (int((abscisse(ev)) / 50) + 1, int((ordonnee(ev) + 3) / 50)))]
                    print("effacé")
                    attend_ev()

        elif tev == "ClicGauche":
            if abscisse(ev) % 50 <= 3:
                arete([int((abscisse(ev) + 3) / 50), int((ordonnee(ev)) / 50)],
                      [int((abscisse(ev) + 3) / 50), int((ordonnee(ev)) / 50) + 1], "red")
                etat[((int((abscisse(ev) + 3) / 50), int((ordonnee(ev)) / 50)),
                      (int((abscisse(ev) + 3) / 50), int((ordonnee(ev)) / 50) + 1))] = -1
                print(etat)
            #same as above
            if ordonnee(ev) % 50 <= 3:
                arete([int((abscisse(ev)) / 50), int((ordonnee(ev) + 3) / 50)],
                      [int((abscisse(ev)) / 50) + 1, int((ordonnee(ev) + 3) / 50)], "red")
                etat[((int((abscisse(ev)) / 50), int((ordonnee(ev) + 3) / 50)),
                      (int((abscisse(ev)) / 50) + 1, int((ordonnee(ev) + 3) / 50)))] = -1
            # same as above

        elif tev == 'Quitte':  # on sort de la boucle
            break

        else:  # dans les autres cas, on ne fait rien
            pass

        mise_a_jour()
    ferme_fenetre()
