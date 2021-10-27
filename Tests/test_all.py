from Logic.crud import AdaugaObiectLista, StergereObiectLista, ModificareObiectLista, GetById
from Domain.inventar import CreazaObiect, get_ID, get_Locatie, get_Descriere, get_Nume, get_Pret_Achizitie


def testAdaugaObiect():
    lista = []

    lista = AdaugaObiectLista(1, "monitor", "UHD", 1700, "cluj", lista)

    assert len(lista) == 1
    assert get_ID(GetById(1, lista)) == 1
    assert get_Nume(GetById(1, lista)) == "monitor"
    assert get_Descriere(GetById(1, lista)) == "UHD"
    assert get_Pret_Achizitie(GetById(1, lista)) == 1700
    assert get_Locatie(GetById(1, lista)) == "cluj"


def testModificareObiect():
    lista = []
    lista = AdaugaObiectLista(1, "monitor", "UHD", 1700, "cluj", lista)
    lista = AdaugaObiectLista(2, "congelator", "A++", 900, "cluj", lista)

    lista = ModificareObiectLista(2, "congelator", "10 sertare", 1000, "cluj", lista)
    obiect = GetById(1, lista)

    assert get_ID(obiect) == 1
    assert get_Nume(obiect) == "monitor"
    assert get_Descriere(obiect) == "UHD"
    assert get_Pret_Achizitie(obiect) == 1700
    assert get_Locatie(obiect) == "cluj"

    obiect = GetById(2, lista)

    assert get_ID(obiect) == 2
    assert get_Nume(obiect) == "congelator"
    assert get_Descriere(obiect) == "10 sertare"
    assert get_Pret_Achizitie(obiect) == 1000
    assert get_Locatie(obiect) == "cluj"


def testStergereObiect():
    lista = []
    lista = AdaugaObiectLista(1, "monitor", "UHD", 1700, "cluj", lista)
    lista = AdaugaObiectLista(2, "congelator", "A++", 900, "cluj", lista)

    lista = StergereObiectLista(1, lista)
    assert len(lista) == 1

    assert GetById(1, lista) is None
    assert GetById(2, lista) is not None

    lista = StergereObiectLista(3, lista)

    assert len(lista) == 1
    assert GetById(1, lista) is None
    assert GetById(2, lista) is not None


def testObiect():
    obiect = CreazaObiect(1, "monitor", "UHD", 1700, "cluj")

    assert get_ID(obiect) == 1
    assert get_Nume(obiect) == "monitor"
    assert get_Descriere(obiect) == "UHD"
    assert get_Pret_Achizitie(obiect) == 1700
    assert get_Locatie(obiect) == "cluj"


def run_all_tests():
    testObiect()
    testAdaugaObiect()
    testModificareObiect()
    testStergereObiect()
