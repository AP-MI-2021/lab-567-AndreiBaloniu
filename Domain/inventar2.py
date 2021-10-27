def CreazaObiect(ID, nume, descriere, pret_achizitie, locatie):
    """
    Creeaza o achizitie
    :param ID: id-ul obiectului
    :param nume: numele obiectului
    :param descriere: descrierea obiectului
    :param pret_achizitie: pretul obiectului
    :param locatie: locatia obiectului (exact 4 caractere)
    :return:
    """
    lista_obiect = [ID, nume, descriere, pret_achizitie, locatie]
    return lista_obiect


def get_ID(lista_obiect):
    return lista_obiect[0]


def get_Nume(lista_obiect):
    return lista_obiect[1]


def get_Descriere(lista_obiect):
    return lista_obiect[2]


def get_Pret_Achizitie(lista_obiect):
    return lista_obiect[3]


def get_Locatie(lista_obiect):
    return lista_obiect[4]


def toString(lista_obiect):
    return "ID: {}, Nume: {}, Descriere: {}, Pret_Achizitie: {}, Locatie: {}".format(
        get_ID(lista_obiect),
        get_Nume(lista_obiect),
        get_Descriere(lista_obiect),
        get_Pret_Achizitie(lista_obiect),
        get_Locatie(lista_obiect)
    )