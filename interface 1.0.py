from math import sqrt
import utilities
import sys

from fltk import *

ax = {}
ay = {}
etat = {}


def action_permise(etat, indice, indices):
    nb_segemnts_around_indice = 0
    if etat(f"(({indice[0]}, {indice[1]}),({indice[0]}, {indice[1] +1}))"):
        nb_segemnts_around_indice += 1
    if etat(f"(({indice[0]}, {indice[1]}),({indice[0]+1}, {indice[1]}))"):
        nb_segemnts_around_indice += 1
    if etat(f"(({indice[0]}, {indice[1]+1}),({indice[0]+1}, {indice[1] +1}))"):
        nb_segemnts_around_indice += 1
    if etat(f"(({indice[0]+1}, {indice[1]}),({indice[0]+1}, {indice[1] +1}))"):
        nb_segemnts_around_indice += 1
    if nb_segemnts_around_indice > indices[indice[1]][indice[0]]:
        efface("tag_dia dak l'indice")
        texte("tag_bl7mr")




def libre(etat,segment):
    """
    Véérifie si lr segment est libre
    """
    if segment in list(etat.keys()):
        return False
    return True


def dessine_segment(pt1, pt2, couleur="black", tag=""):
    """
    Déssine un segment
    """
    dist = sqrt( (pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2 )
    if dist != 1:
        print("too far")
        return
    if len(tag)==0:
        tag = "({},{}),({},{})".format(pt1[0], pt1[1], pt2[0], pt2[1])
    rectangle((pt1[0] * 50) + 3, (pt1[1] * 50) + 3, (pt2[0] * 50) - 3, (pt2[1] * 50) - 3, remplissage=couleur, tag=tag)
    print(tag)


if __name__ == "__main__":
    # Vérifie si la taille et la data dans la grille est conforme
    #file = str(sys.argv[0])
    #print(sys.argv)
    file = "Grille1.txt"
    #print(file)
    if not utilities.checkdata(file):
        pass
    # charge les indices
    indices = utilities.chargegrille(file)
    # Définit les dimensions du jeu
    l = len(indices[0])
    h = len(indices)
    dimentions = [l * 50, h * 50]
    # Crée une fenetre pour le jeu
    cree_fenetre(dimentions[0]+50, dimentions[1]+50)
    # Définit les coordonées de tout les somets du jeu
    for i in range(int(dimentions[0] / 50)):
        ax[i] = i * 50
    for j in range(int(dimentions[1] / 50)):
        ay[j] = j * 50
    # Déssine les somets et les indices
    for i in range(int(dimentions[0] / 50)):
        for j in range(int(dimentions[1] / 50)):
            cercle(ax[i]+50, ay[j]+50, 3, remplissage="red")
            if i <((dimentions[0]/50)-1) and j<((dimentions[1]/50)-1):
                if indices[j][i] == "_":
                    pass
                else:
                    texte(ax[i]+20+50, ay[j]+10+50, str(indices[j][i]), taille=17)
    attend_ev()
    # Boucle du jeu
    while utilities.cond1victoire(indices,etat):
        ev = donne_ev()
        tev = type_ev(ev)

        # Action dépendant du type d'événement reçu :

        if tev == 'Touche':
            print('Appui sur la touche', touche(ev))
            utilities.solver

        elif tev == "ClicGauche":
            # Verifie si le clic est dans une zone de segment horizentale
            if (abscisse(ev) + 3) % 50 <= 6:
                # Verifie si le segment est libre
                if libre(etat, ((int((abscisse(ev)+3)/50), int((ordonnee(ev))/50)), (int((abscisse(ev)+3)/50), int((ordonnee(ev))/50) + 1))):
                    #dessine le segment noir
                    dessine_segment([int((abscisse(ev)+3)/50), int((ordonnee(ev))/50)],
                          [int((abscisse(ev)+3)/50), int((ordonnee(ev))/50) + 1], "black")
                    # ajoute l'état du segment et lui affecte 1
                    etat[((int((abscisse(ev)+3)/50), int((ordonnee(ev))/50)),
                          (int((abscisse(ev)+3)/50), int((ordonnee(ev))/50) + 1))] = 1
                else:
                    # efface le segment
                    pt1_eff = [int((abscisse(ev) + 3) / 50), int((ordonnee(ev)) / 50)]
                    pt2_eff = [int((abscisse(ev) + 3) / 50) , int((ordonnee(ev)) / 50) + 1]
                    efface("({},{}),({},{})".format(pt1_eff[0], pt1_eff[1], pt2_eff[0], pt2_eff[1]))
                    print("({},{}),({},{})".format(pt1_eff[0], pt1_eff[1], pt2_eff[0], pt2_eff[1]))
                    # Suprime l'etat du segment
                    del etat[((int((abscisse(ev)+3)/50), int((ordonnee(ev))/50)), (int((abscisse(ev)+3)/50), int((ordonnee(ev))/50) + 1))]
                    print(etat)
                    print("effacé")
                    mise_a_jour()
            # Verifie si le clic est dans une zone de segement verticale
            elif (ordonnee(ev) + 3) % 50 <= 6:
                #Verifie si le segment est libre
                if libre(etat, ((int((abscisse(ev)) / 50), int((ordonnee(ev) + 3) / 50)),
                                (int((abscisse(ev)) / 50) + 1, int((ordonnee(ev) + 3) / 50)))):
                    # Dessine le segment de cette zone
                    dessine_segment([int((abscisse(ev)) / 50), int((ordonnee(ev) + 3) / 50)],
                          [int((abscisse(ev)) / 50) + 1, int((ordonnee(ev) + 3) / 50)], "black")
                    # ajoute l'état du segment et lui affecte 1
                    etat[((int((abscisse(ev)) / 50), int((ordonnee(ev) + 3) / 50)),
                          (int((abscisse(ev)) / 50) + 1, int((ordonnee(ev) + 3) / 50)))] = 1
                    print(etat)
                else:
                    # Efface le segment
                    pt1_eff=[int((abscisse(ev)) / 50),
                                         int((ordonnee(ev) + 3) / 50)]
                    pt2_eff = [int((abscisse(ev)) / 50) + 1, int((ordonnee(ev) + 3) / 50)]
                    print("({},{}),({},{})".format(pt1_eff[0], pt1_eff[1], pt2_eff[0], pt2_eff[1]))
                    efface("({},{}),({},{})".format(pt1_eff[0], pt1_eff[1], pt2_eff[0], pt2_eff[1]))
                    del etat[((int((abscisse(ev)) / 50), int((ordonnee(ev) + 3) / 50)), (int((abscisse(ev)) / 50) + 1, int((ordonnee(ev) + 3) / 50)))]
                    attend_ev()

        elif tev == "ClicDroit":
            # Pareil que pour le clic droit sauf qu'il affecte un etat -1 et dessine des segments rouges
            if (abscisse(ev) + 3) % 50 <= 6:
                if libre(etat, ((int((abscisse(ev) + 3) / 50), int((ordonnee(ev)) / 50)),
                                (int((abscisse(ev) + 3) / 50), int((ordonnee(ev) / 50)) + 1))):
                    dessine_segment([int((abscisse(ev) + 3) / 50), int((ordonnee(ev)) / 50)],
                              [int((abscisse(ev) + 3) / 50), int((ordonnee(ev)) / 50) + 1], "red")
                    etat[((int((abscisse(ev) + 3) / 50), int((ordonnee(ev)) / 50)),
                              (int((abscisse(ev) + 3) / 50), int((ordonnee(ev)) / 50) + 1))] = -1
                    print(etat)
                else:
                    pt1_eff = [int((abscisse(ev) + 3) / 50),
                               int((ordonnee(ev)) / 50)]
                    pt2_eff = [int((abscisse(ev) + 3) / 50), int((ordonnee(ev) / 50)) + 1]
                    print("({},{}),({},{})".format(pt1_eff[0], pt1_eff[1], pt2_eff[0], pt2_eff[1]))
                    efface("({},{}),({},{})".format(pt1_eff[0], pt1_eff[1], pt2_eff[0], pt2_eff[1]))
                    del etat[((pt1_eff[0], pt1_eff[1]), (pt2_eff[0], pt2_eff[1]))]
                    print("effacé")
                    print(etat)
                    attend_ev()
            elif (ordonnee(ev) + 3) % 50 <= 6:
                if libre(etat, ((int((abscisse(ev)) / 50), int((ordonnee(ev) + 3) / 50)),
                      (int((abscisse(ev)) / 50) + 1, int((ordonnee(ev) + 3) / 50)))):
                    dessine_segment([int((abscisse(ev)) / 50), int((ordonnee(ev) + 3) / 50)],
                          [int((abscisse(ev)) / 50) + 1, int((ordonnee(ev) + 3) / 50)], "red")
                    etat[((int((abscisse(ev)) / 50), int((ordonnee(ev) + 3) / 50)),
                          (int((abscisse(ev)) / 50) + 1, int((ordonnee(ev) + 3) / 50)))] = -1
                    print(etat)
                else:
                    pt1_eff = [int((abscisse(ev)) / 50),
                               int((ordonnee(ev) + 3) / 50)]
                    pt2_eff = [int((abscisse(ev)) / 50) + 1, int((ordonnee(ev) + 3) / 50)]
                    print("({},{}),({},{})".format(pt1_eff[0], pt1_eff[1], pt2_eff[0], pt2_eff[1]))
                    efface("({},{}),({},{})".format(pt1_eff[0], pt1_eff[1], pt2_eff[0], pt2_eff[1]))
                    del etat[((pt1_eff[0], pt1_eff[1]), (pt2_eff[0], pt2_eff[1]))]
                    print("effacé")
                    print(etat)
                    attend_ev()

        elif tev == 'Quitte':  # on sort de la boucle
            break

        else:  # dans les autres cas, on ne fait rien
            pass

        mise_a_jour()
    print("You WON!")
    ferme_fenetre()