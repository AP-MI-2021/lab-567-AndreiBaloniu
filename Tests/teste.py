from Domain.inventar import get_locatie, get_descriere
from Logic.crud import create, read
from Logic.concatenare import concatenate_strings
from Logic.ccm_pret_pt_fiecare_locatie import cmm_pret_pt_fiecare_locatie
from Logic.suma_preturilor_pt_fiecare_locatie import  suma_preturilor_fiecare_locatie
from Logic.mutare import mutare
from Logic.ordonare import ordonare_obiecte


def test_mutare():
    lista = []
    lista = create(lista, 1, "masa", "lemn", 300, "cluj")
    lista = create(lista, 2, "birou", "lemn", 200, "cluj")
    lista = create(lista, 3, "scaune", "tapitate", 100, "cluj")

    lista = mutare(lista, "home")

    assert get_locatie(read(lista, 1)) == "home"
    assert get_locatie(read(lista, 2)) == "home"
    assert get_locatie(read(lista, 3)) == "home"


def test_concatenate_strings():
    lista = []
    lista = create(lista, 1, "masa", "lemn", 300, "cluj")
    lista = create(lista, 2, "birou", "lemn", 200, "cluj")
    lista = create(lista, 3, "scaune", "tapitate", 100, "cluj")
    lista = concatenate_strings(lista, "mobilier", 150)

    assert get_descriere(read(lista, 1)) == "lemnmobilier"
    assert get_descriere(read(lista, 2)) == "lemnmobilier"
    assert get_descriere(read(lista, 3)) == "tapitate"


def test_ordonare_obiecte():
    lista = []
    lista = create(lista, 1, "masa", "lemn", 300, "cluj")
    lista = create(lista, 2, "birou", "lemn", 200, "cluj")
    lista = create(lista, 3, "scaune", "tapitate", 100, "cluj")
    lista_noua = ordonare_obiecte(lista)

    assert lista not in lista_noua


def test_cmm_pret_pt_fiecare_locatie():
    lista = []
    lista = create(lista, 1, "tabla", "alba", 300, "IKEA")
    lista = create(lista, 2, "birou", "lemn", 200, "IKEA")

    lista = cmm_pret_pt_fiecare_locatie(lista)




def test_suma_preturilor_fiecare_locatie():
    lista = []
    lista = create(lista, 1, "masa", "lemn", 300, "cluj")
    lista = create(lista, 2, "birou", "lemn", 200, "cluj")
    rezult = suma_preturilor_fiecare_locatie(lista)
    assert rezult == {"cluj": 500}

test_suma_preturilor_fiecare_locatie()
test_ordonare_obiecte()
test_cmm_pret_pt_fiecare_locatie()
test_concatenate_strings()
test_mutare()