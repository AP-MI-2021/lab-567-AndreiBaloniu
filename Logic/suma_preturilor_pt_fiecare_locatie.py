from Domain.inventar import get_locatie, get_pret_achizitie


def suma_preturilor_fiecare_locatie(lista_obiecte):
    """
    Aceasta functie returneaza suma preturilor pentru fiecare locatie
    :param lista_obiecte: lista
    :return: suma
    """
    new_list = {}
    for obiect in lista_obiecte:
        locatie = get_locatie(obiect)
        pret = float(get_pret_achizitie(obiect))
        if locatie in new_list:
            new_list[locatie] = new_list[locatie] + pret
        else:
            new_list[locatie]= pret
    return new_list