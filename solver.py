def ResudreSlitherlinkRecursive(indices, etat, sommet):
    # on vérifier d'abord si la boucle est fermé
    if longueur_boucle(etat, next(iter(etat))) is not None:
        # si oui, on vérifier alors si tt les indices sont satisfis
        if Grill_satisfait(Indices, etat):
            return etat
        else:
            return None
    # si la boucle n'est pas ancore fermée, on vérifie alors s'il y un indice qui depasse ses limites
    if Existe_un_indice_deppase(indices, etat):
        return None
    # si c'est non, alors on continue de tester le chemin
    dernier_seg = list(etat.keys())[-1]  # get le dernier segment
    segment_suiv = Segments_suivant(indices.__len__(), Indices[0].__len__(), AutreSommet(dernier_seg, sommet), sommet)
    for seg_sv in segment_suiv:
        if est_vierge(etat, seg_sv):
            tracer_segment(etat, seg_sv)
            nouveau_etat = ResudreSlitherlinkRecursive(indices, etat, AutreSommet(seg_sv, sommet))
            if nouveau_etat is not None:
                return nouveau_etat
            effacer_segment(etat, seg_sv)
    return None