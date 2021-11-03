from Logic.crud import AdaugaObiectLista
from Logic.locuri import loc_sep


def test_loc_sep():
    obiecte = []
    obiecte = AdaugaObiectLista(obiecte, 1, 'a', 'aa', 1, 'aaa')
    obiecte = AdaugaObiectLista(obiecte, 2, 'b', 'bb', 2, 'b')
    obiecte = AdaugaObiectLista(obiecte, 3, 'c', 'cc', 3, 'aaa')
    obiecte = AdaugaObiectLista(obiecte, 4, 'd', 'dd', 4, 'b')

    lista = loc_sep(obiecte)
    assert len(lista) == 2
    assert lista[0] == 'adad'
    assert lista[1] == 'sdai'
