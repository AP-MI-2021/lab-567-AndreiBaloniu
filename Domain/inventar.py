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


def get_str(obiect):
    return f'Obiectul cu id-ul {get_ID(obiect)}, denumit {get_Nume(obiect)}, cu descrierea {get_Descriere(obiect)},care costa {get_Pret_Achizitie(obiect)},avand locul achiztionarii {get_Locatie(obiect)}'





