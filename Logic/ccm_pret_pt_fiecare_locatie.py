from Domain.inventar import get_locatie, get_pret_achizitie


def cmm_pret_pt_fiecare_locatie(lista) -> object:
    """
    Aceasta functie determina cel mai mare pret pentru fiecare locatie
    :param lista:Aceasta functie primeste o lista
    :return:Aceasta functie returneaza cel mai mare pret pentru fiecare locatie
    """
    new_list = {}
    for obiect in lista:
        locatie = get_locatie(obiect)
        pret = get_pret_achizitie(obiect)
        if locatie in new_list:
            if pret > get_pret_achizitie(new_list[locatie]):
                new_list[locatie] = obiect
        else:
            new_list[locatie] = obiect
    return new_list