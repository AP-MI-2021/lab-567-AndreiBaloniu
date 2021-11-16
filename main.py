from Tests.teste import test_mutare, test_concatenate_strings, test_ordonare_obiecte, \
    test_suma_preturilor_fiecare_locatie, test_cmm_pret_pt_fiecare_locatie
from Tests.teste_crud import test_crud
from Tests.test_undo_redo import testare_undo_redo
from UserInterface.console import run_console
from UserInterface.console2 import console2


def main():
    lista = []
    obiecte = []
    console2(obiecte)
    run_console(lista)


if __name__ == '__main__':
    test_crud()
    test_mutare()
    test_concatenate_strings()
    test_suma_preturilor_fiecare_locatie()
    test_cmm_pret_pt_fiecare_locatie()
    test_ordonare_obiecte()
    testare_undo_redo()
    main()
