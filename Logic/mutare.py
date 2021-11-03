from Domain.inventar2 import CreazaObiect, get_ID, get_Locatie, get_Descriere, get_Nume, get_Pret_Achizitie

def mutare_obiecte_alta_locatie(lista, locatie, destinatie):
    '''
    Mutarea obiectelor din lista din aceeasi locatie in alta
    :param lista: lista obiectelor
    :param locatie: locatia initiala
    :param destinatie: locatia finala
    :return:lista obiectelor modificata
    '''
    if len(locatie) != 4 or len(destinatie) != 4:
        raise ValueError(f'Locatia a fost introdusa gresit! Trebuie sa aiba exact 4 caractere!')

    result = []
    for element in lista:
        if get_Locatie(element) != locatie:
            result.append(element)
        else:
            id = get_ID(element)
            nume = get_Nume(element)
            descriere = get_Descriere(element)
            pret = get_Pret_Achizitie(element)
            obiect = CreazaObiect(id, nume, descriere, pret, destinatie)
            result.append(obiect)

    return result