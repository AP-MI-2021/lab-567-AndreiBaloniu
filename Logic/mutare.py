from Domain.inventar import get_pret_achizitie, get_new_object, get_id, get_nume, get_descriere


def mutare(lista_obiecte, new_loc):
    """
    :param lista_obiecte: obiectele din inventarul institutiei
    :param initial_loc:locatia initiala a obiectului
    :param new_loc:locatia noua, in care va fi mutat obiectul
    :return:lista cu obiectele din inventarul institutiei, actualizata
    """
    if len(new_loc) != 4:
        raise ValueError('Trebuie sa aiba 4 caractere!')
    new_list = []
    for obiect in lista_obiecte:
        new_list.append(get_new_object(get_id(obiect), get_nume(obiect),
                                       get_descriere(obiect), get_pret_achizitie(obiect), new_loc))
    return new_list
