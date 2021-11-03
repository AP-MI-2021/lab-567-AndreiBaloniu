from Domain.inventar2 import CreazaObiect, get_ID, get_Locatie, get_Descriere, get_Nume, get_Pret_Achizitie


def concatenare_string_dupa_pret_citit(lista, pret, string):
    '''
    Concatenarea unui string citit de la tastura la descrierea obiectelor cu pretul mai mare decat cel dat
    :param lista: lista obiectelor
    :param pret: pretul citit de la tastatura
    :param string: mesajul care se va concatena la descriere
    :return: lista obiectelor modificata
    '''
    result = []
    descriere = ''
    for element in lista:
        if get_Pret_Achizitie(element) > pret:
            descriere = get_Descriere(element) + string
            id = get_ID(element)
            nume = get_Nume(element)
            pret = get_Pret_Achizitie(element)
            locatie = get_Locatie(element)
            obiect = CreazaObiect(id, nume, descriere, pret, locatie)
            result.append(obiect)

        else:
            result.append(element)

    return result
