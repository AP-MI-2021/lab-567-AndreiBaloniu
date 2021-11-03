from Domain.inventar import get_ID, CreazaObiect, get_Nume, get_Locatie, get_Pret_Achizitie, get_Descriere
from Logic.key import modif

def test_modif():
    obiect_aux = CreazaObiect(2, 'b', 'bb', 2, 'bbb')
    modif(obiect_aux, 'id', 1)
    assert get_ID(obiect_aux) == 1

    modif(obiect_aux, 'nume', 'a')
    assert get_Nume(obiect_aux) == 'a'

    modif(obiect_aux, 'desc', 'aa')
    assert get_Descriere(obiect_aux) == 'aa'

    modif(obiect_aux, 'pret', 1)
    assert get_Pret_Achizitie(obiect_aux) == 1

    modif(obiect_aux, 'locatie', 'aaa')
    assert get_Locatie(obiect_aux) == 'aaa'
