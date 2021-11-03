from Logic.crud import AdaugaObiectLista, ModificareObiectLista, StergereObiectLista
from Domain.inventar2 import get_str, get_Descriere, get_Pret_Achizitie, get_Locatie
from Logic.mutare import mutare_obiecte_alta_locatie
from Logic.locuri import loc_sep
from Logic.concatenare import concatenare_string_dupa_pret_citit
from Logic.ordonare import ordonare_obiecte


def show_menu():
    print("2.1 Adăugare / ștergere / modificare obiect")
    print("2.2 Mutarea tuturor obiectelor dintr-o locație în alta.")
    print("2.3 Concatenarea unui string citit la  descrierile obiectelor cu prețul mai mare decât o valoare citită.")
    #print("2.4 Determinarea celui mai mare preț pentru fiecare locație.")
    print("2.4 Ordonarea obiectelor crescător după prețul de achiziție.")
    print("a. Afisare")
    print("x. Iesire")


def UI_SubMenu(obiecte):
    while True:
        print("1. Adauga obiect.")
        print("2. Modifica obiect.")
        print("3. Sterge obiect.")
        print("b. Revenire.")
        optiune = input('Optiune aleasa: ')
        if optiune == '1':
            obiecte = UI_AdaugaObiect(obiecte)
        elif optiune == '2':
            obiecte = UI_ModificaObiect(obiecte)
        elif optiune == '3':
            obiecte = UI_StergereObiect(obiecte)
        elif optiune == 'b':
            return obiecte
        else:
            print('Optiune invalida.')


def UI_AdaugaObiect(lista):
    try:
        id = int(input("Scrie id-ul: "))
        nume = input("Scrie numele obiectului: ")
        descriere = input("Scrie descrierea obiectului: ")
        pret = float(input("Scrie pretul achizitiei obectului: "))
        locatie = input("Scrie locatia obiectului: ")
        return AdaugaObiectLista(id, nume, descriere, pret, locatie, lista)
    except ValueError as ve:
        print('Eroare: ', ve)


def UI_ModificaObiect(lista):
    try:
        id = int(input("Scrie id-ul obiectului de modificat: "))
        nume = input("Scrie noul nume al obiectului: ")
        descriere = input("Scrie noua descriere al obiectului: ")
        pret = float(input("Scrie noul pret al obectului: "))
        locatie = input("Scrie noua locatia a obiectului: ")
        return ModificareObiectLista(id, nume, descriere, pret, locatie, lista)
    except ValueError as ve:
        print('Eroare: ', ve)


def UI_StergereObiect(lista):
    try:
        id = int(input("Scrie id-ul obiectului de sters: "))
        return StergereObiectLista(id, lista)
    except ValueError as ve:
        print('Eroare: ', ve)


def UI_ShowAll(lista):
    print("Obiectele din inventar sunt: ")
    for obiect in lista:
        print(get_str(obiect))


def UI_Concatenare(obiecte):
    try:
        pret = int(input("Dati pretul unui obiect: "))
        string = input("Dati mesajul pe care-l doriti la descriere: ")
        obiecte = concatenare_string_dupa_pret_citit(obiecte, pret, string)
        print("Concatenarea stringurilor s-a realizat.")
    except ValueError as ve:
        print('Eroare: ', ve)
    return obiecte


def UI_Mutare_Obiect(obiecte):
    try:
        old_location = input("Locatia initiala a obiectului: ")
        new_location = input("Noua locatia a obiectului: ")
        obiecte = mutare_obiecte_alta_locatie(obiecte, old_location, new_location)
        print("Obiectul a fost mutat in noua locatie.")
    except ValueError as ve:
        print('Eroare: ', ve)
    return obiecte


def UI_cel_mai_mare_pret_din_ficare_loc(obiecte):
    '''
    O sa calculeze cel mai mai mare pret din fiecare locatie.
    :param obiecte: lista de obiecte
    :return:
    '''
    lista = loc_sep(obiecte)
    for i in lista:
        pret_maxim = -1
        for obiect in obiecte:
            if get_Locatie(obiect) == i:
                if pret_maxim < get_Pret_Achizitie(obiect):
                    pret_maxim = get_Pret_Achizitie(obiect)

        print(f'Pretul cel mai mare din {i} este {pret_maxim}')

def UI_Ordonare_dupa_pret(obiecte):
    pass


def UI_afisare_sumelor_pret_pentru_fiecare_loc(obiecte):
    '''
    Afiseaza suma preturilor obiectelor din fiecare loc.
    :param obiecte: lista de obiecte.
    :return:
    '''
    list = loc_sep(obiecte)
    for i in list:
        suma = 0
        for obiect in obiecte:
            if get_Locatie(obiect) == i:
                suma = suma + get_Pret_Achizitie(obiect)

        print(f'Suma tutror obiectelor din zona {i} este {suma}')


def run_UI(lista):
    while True:
        show_menu()
        optiune = input("Alege o optiune: ")
        if optiune == '2.1':
            lista = UI_SubMenu(lista)
        elif optiune == '2.2':
            lista = UI_Mutare_Obiect(lista)
        elif optiune == '2.3':
            lista = UI_Concatenare(lista)
        #elif optiune == '2.4':
            #lista = UI_cel_mai_mare_pret_din_ficare_loc(lista)
        elif optiune == '2.4':
            lista = UI_Ordonare_dupa_pret(lista)
            print('Ordonarea obiectelor dupa pret a avut loc cu succes.')
        elif optiune == '2.6':
            lista = UI_afisare_sumelor_pret_pentru_fiecare_loc(lista)
        elif optiune == 'a':
            UI_ShowAll(lista)
        elif optiune == 'x':
            print("Program incheiat.")
            break
        else:
            print("Ai ales o optiune inexistenta, incearca din nou: ")
