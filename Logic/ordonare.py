from Domain.inventar import get_pret_achizitie


def ordonare_obiecte(lista_obiecte):
    """
    Ordoneaza crescator obiectele din inventar dupa pretul de achizitie
    :param lista_obiecte: lista care contine obiectele din inventar
    :return: lista sortata
    """

    return sorted(lista_obiecte, key=get_pret_achizitie)
