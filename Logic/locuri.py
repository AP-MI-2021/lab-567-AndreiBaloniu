from Logic.repetare import ver_rep
from Domain.inventar import get_Locatie

def loc_sep(obiecte):
    '''
    Returneaza o lista de locatii distincte.
    :param obiecte: lista de obiecte
    :return: o lista cu locatii diferite in care se afla obiectele
    '''
    lista = []
    for obiect in obiecte:
        lista.append(get_Locatie(obiect))

    result = []
    for i in range(0, len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                if len(result) > 0:
                    if ver_rep(result, lista[i]):
                        result.append(lista[i])

                else:
                    result.append(lista[i])


    return result