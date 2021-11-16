from Domain.inventar import get_pret_achizitie, get_new_object, get_id, get_locatie, get_nume, get_descriere


def concatenate_strings(lista, string, valoare):
    """
    :param lista: Aceasta functie primeste o lista de obiecte
    :param string: Aceasta functie primeste un string
    :param valoare: Aceasta functie primeste o valoare
    :return: Aceasta functie returneaza aceeasi lista, iar in cazul in care
    exista valori mai mari decat cea data o lista in care obiectele au atasate stringuri la descriere
    """
    new_list = []
    for obiect in lista:
        if valoare < get_pret_achizitie(obiect):
            new_list.append(get_new_object(get_id(obiect), get_nume(obiect),
                                           get_descriere(obiect) + string, get_pret_achizitie(obiect), get_locatie(obiect)))
        else:
            new_list.append(obiect)
    return new_list
