from Domain.inventar import CreazaObiect, get_ID


def AdaugaObiectLista(id, nume, descriere, pret_achizitie, locatie, lista):
    """
    Adauga un obiect intr-o lista data
    :param id: id-ul obiect
    :param nume: numele obiectului
    :param descriere: descrierea obiectului
    :param pret_achizitie: pretul obiectului
    :param locatie: locatia obiectului
    :param lista: lista in care este adaugat obiectul
    :return: lista cu obiectul adaugat
    """
    obiect = CreazaObiect(id, nume, descriere, pret_achizitie, locatie)
    return lista + [obiect]


def GetById(id, lista):
    """
    Citeste un obiect cu id dat din lista
    :param id: id-ul obiectului
    :param lista: lista de obiecte
    :return: id-ul dorit
    """
    for obiect in lista:
        if get_ID(obiect) == id:
            return obiect

    return None


def StergereObiectLista(id, lista):
    """
    Sterge un obiect din lista data
    :param id: id obiect
    :param lista: lista initiala
    :return: lista noua
    """
    new_list = []
    for obiect in lista:
        if get_ID(obiect) != id:
            new_list.append(obiect)
    return new_list


def ModificareObiectLista(id, nume, descriere, pret_achizitie, locatie, lista):
    """
    Modifica un obiect cu id-ul dat din lista
    :param id: id-ul obiect
    :param nume: numele obiectului
    :param descriere: descrierea obiectului
    :param pret_achizitie: pretul obiectului
    :param locatie: locatia obiectului
    :param lista: lista in care este adaugat obiectul
    :return: lista obtinuta in urma modificarii
    """
    new_list = []
    for obiect in lista:
        if get_ID(obiect) == id:
            obiect_nou = CreazaObiect(id, nume, descriere, pret_achizitie, locatie)
            new_list.append(obiect_nou)
        else:
            new_list.append(obiect)

    return new_list
