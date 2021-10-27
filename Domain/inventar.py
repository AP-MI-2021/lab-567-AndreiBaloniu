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
    return {
        'id': ID,
        'nume': nume,
        'descriere': descriere,
        'pret': pret_achizitie,
        'locatie': locatie,
    }


def get_ID(obiect):
    return obiect["id"]


def get_Nume(obiect):
    return obiect["nume"]


def get_Descriere(obiect):
    return obiect["descriere"]


def get_Pret_Achizitie(obiect):
    return obiect["pret"]


def get_Locatie(obiect):
    return obiect["locatie"]


def toString(obiect):
    return "ID: {}, Nume: {}, Descriere: {}, Pret_Achizitie: {}, Locatie: {}".format(
        get_ID(obiect),
        get_Nume(obiect),
        get_Descriere(obiect),
        get_Pret_Achizitie(obiect),
        get_Locatie(obiect)
    )
