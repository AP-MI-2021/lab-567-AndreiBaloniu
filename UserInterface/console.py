from Domain.inventar import get_new_object, get_object_string, get_locatie, get_pret_achizitie
from Logic.ccm_pret_pt_fiecare_locatie import cmm_pret_pt_fiecare_locatie
from Logic.concatenare import concatenate_strings
from Logic.crud import delete, update, create, read
from Logic.mutare import mutare
from Logic.ordonare import ordonare_obiecte
from Logic.suma_preturilor_pt_fiecare_locatie import suma_preturilor_fiecare_locatie


def handle_create(lista_obiecte):
    try:
        id_obiect = int(input("Introduceti ID-ul obiectului: "))
        if read(lista_obiecte, id_obiect) is not None:
            raise ValueError("Exista deja un obiect cu acest ID!")
        nume = input("Introduceti numele obiectului: ")
        if not nume:
            raise ValueError("Numele nu poate sa fie nul.")

        descriere = input("Introduceti descrierea obiectului: ")
        if not descriere:
            raise ValueError("Descrierea nu poate sa fie nula.")
        pret_achizitie = float(input("Introduceti pretul de achizitie al obiectlui: "))
        if pret_achizitie < 0:
            raise ValueError("Pretul nu poate fi negativ.")
        locatie = input("Introduceti locatia obiectului: ")
        return create(lista_obiecte, id_obiect, nume, descriere, pret_achizitie, locatie)
    except ValueError as ve:
        print("Eroare, nu ati introdus o valoare valida!", ve)

    return lista_obiecte


def handle_delete(lista_obiecte):
    try:
        id_obiect = int(input("Introduceti ID-ul elementului pe care doriti sa il stergeti: "))
        if read(lista_obiecte, id_obiect) is None:
            raise ValueError("Obiectul cu ID-ul introdus nu exista!")
        lista_obiecte = delete(lista_obiecte, id_obiect)
    except ValueError as ve:
        print("Eroare, nu ati introdus o valoare valida pentru ID!", ve)
    return lista_obiecte


def handle_update(lista_obiecte):
    try:
        id_obiect = int(input("Introduceti ID-ul obiectului pe care doriti sa il modificati: "))
        if read(lista_obiecte, id_obiect) is None:
            raise ValueError("Obiectul cu ID-ul introdus nu exista.")
        nume = input("Introduceti numele obiectului: ")
        if not nume:
            raise ValueError("Numele nu poate sa fie nul.")
        descriere = input("Introduceti descrierea obiectului: ")
        if not descriere:
            raise ValueError("Descrierea nu poate sa fie nula.")
        pret_achizitie = float(input("Introduceti pretul de achizitie al obiectlui: "))
        if pret_achizitie < 0:
            raise ValueError("Pretul nu poate fi negativ.")
        locatie = input("Introduceti locatia obiectului: ")
        new_object = get_new_object(id_obiect, nume, descriere, pret_achizitie, locatie)
        lista_obiecte = update(lista_obiecte, new_object)
    except ValueError as ve:
        print("Eroare, nu ati introdus o valoare valida!", ve)

    return lista_obiecte


def handle_suma_preturilor_fiecare_locatie(lista_obiecte):
    lista_sumelor_preturilor = suma_preturilor_fiecare_locatie(lista_obiecte)
    for element in lista_sumelor_preturilor:
        print(f'Suma preturilor pentru locatia {get_locatie(element)} este {get_pret_achizitie(element)}')


def handle_ordonare_obiecte(lista_obiecte):
    return ordonare_obiecte(lista_obiecte)


def handle_cmm_pret_pentru_fiecare_locatie(lista_obiecte):
    cmm_pret = cmm_pret_pt_fiecare_locatie(lista_obiecte)
    for element in cmm_pret:
        print(f'Cel mai mare pret pentru locatia {get_locatie(element)} este {get_pret_achizitie(element)}')


def handle_show_all(lista_obiecte):
    for obiect in lista_obiecte:
        print(get_object_string(obiect))


def handle_mutare(lista_obiecte):
    try:
        locatie_noua = input('Introduceti locatia noua: ')
        return mutare(lista_obiecte, locatie_noua)
    except ValueError as ve:
        print("Locatia noua introdusa este gresita:", ve)


def handle_concatenare_str(lista_obiecte):
    try:
        string = str(input("Dati stringul: "))
        valoare = float(input("Dati valoarea: "))
        return concatenate_strings(lista_obiecte, string, valoare)
    except ValueError as ve:
        print("Datele introduse sunt gresite", ve)


def handle_new_list(versions_list, curent_version, lista_obiecte):
    while curent_version < len(versions_list) - 1:
        versions_list.pop()
    versions_list.append(lista_obiecte)
    curent_version += 1
    return versions_list, curent_version


def handle_undo(list_versions, current_version):
    """
    Functia are rolul de a reface ulima modificare facuta listei inainte de ultima executare,
    respectiv o refacere a listei dupa executarea unui functionalitati.
    :param list_versions: vesriunea actuala a listei
    :param current_version: numarul care reprezinta versiunea listei
    :return: lista actualizata in urma executarii functiei
    """
    if current_version < 1:
        print("Nu se mai poate face undo.")
        return [], 0
    current_version -= 1
    return list_versions[current_version], current_version


def handle_redo(list_versions, current_version):
    """
    Functia are rolul de a reface ulima modificare facuta listei inainte de ultima executare,
    respectiv o refacere a listei dupa executarea unui Undo.
    :param list_versions: vesriunea actuala a listei
    :param current_version: numarul care reprezinta versiunea listei
    :return: lista actualizata in urma executarii functiei
    """

    if current_version == len(list_versions) - 1:
        print("Nu se mai poate face redo.")
        return list_versions[current_version], current_version
    current_version += 1
    return list_versions[current_version], current_version


def show_menu():
    print("""
            1. Adaugare obiect
            2. Stergere obiect
            3. Modificare obiect
            4. Muta toate obiectele dintr-o locatie in alta
            5. Concateneaza un string la toate descrierile obiectelor cu un pret mai mare decat o anumita valoare
            6. Determina cel mai mare pret pentru fiecare locatie
            7. Ordoneaza obiectele crescator dupa pret
            8. Determina suma preturilor pentru fiecare locatie
            u. Undo
            r. Redo
            a. Show all
            x. Iesire program
    """)


def run_console(lista_obiecte):

    current_version = 0
    list_versions = [lista_obiecte]

    while True:

        try:
            show_menu()

            optiune = input("Introduceti optiunea: ")

            if optiune == '1':

                lista_obiecte = handle_create(lista_obiecte)
                list_versions, current_version = handle_new_list(list_versions, current_version, lista_obiecte)

            elif optiune == '2':

                lista_obiecte = handle_delete(lista_obiecte)
                list_versions, current_version = handle_new_list(list_versions, current_version, lista_obiecte)

            elif optiune == '3':

                lista_obiecte = handle_update(lista_obiecte)
                list_versions, current_version = handle_new_list(list_versions, current_version, lista_obiecte)

            elif optiune == '4':

                lista_obiecte = handle_mutare(lista_obiecte)
                list_versions, current_version = handle_new_list(list_versions, current_version, lista_obiecte)

            elif optiune == '5':

                lista_obiecte = handle_concatenare_str(lista_obiecte)
                list_versions, current_version = handle_new_list(list_versions, current_version, lista_obiecte)

            elif optiune == '6':

                handle_cmm_pret_pentru_fiecare_locatie(lista_obiecte)

            elif optiune == '7':

                lista_obiecte = handle_ordonare_obiecte(lista_obiecte)
                list_versions, current_version = handle_new_list(list_versions, current_version, lista_obiecte)

            elif optiune == '8':
                handle_suma_preturilor_fiecare_locatie(lista_obiecte)

            elif optiune == 'u':

                lista_obiecte, current_version = handle_undo(list_versions, current_version)

            elif optiune == 'r':

                lista_obiecte, current_version = handle_redo(list_versions, current_version)

            elif optiune == 'a':

                handle_show_all(lista_obiecte)

            elif optiune == 'x':
                break

            else:
                print("Optiune invalida!")

        except Exception as ex:
            print("Eroare! ", ex)
