from Logic.crud import AdaugaObiectLista, ModificareObiectLista, StergereObiectLista
from Domain.inventar import toString


def PrintMenu():
    print("1. Adauga obiect.")
    print("2. Modifica obiect.")
    print("3. Sterge obiect.")
    print("4. Afisare obiecte din inventar.")
    print("x. Program incheiat.")


def UI_AdaugaObiect(lista):
    id = int(input("Scrie id-ul: "))
    nume = input("Scrie numele obiectului: ")
    descriere = input("Scrie descrierea obiectului: ")
    pret = float(input("Scrie pretul achizitiei obectului: "))
    locatie = input("Scrie locatia obiectului: ")

    return AdaugaObiectLista(id, nume, descriere, pret, locatie, lista)


def UI_ModificaObiect(lista):
    id = int(input("Scrie id-ul obiectului de modificat: "))
    nume = input("Scrie noul nume al obiectului: ")
    descriere = input("Scrie noua descriere al obiectului: ")
    pret = float(input("Scrie noul pret al obectului: "))
    locatie = input("Scrie noua locatia a obiectului: ")

    return ModificareObiectLista(id, nume, descriere, pret, locatie, lista)


def UI_StergereObiect(lista):
    id = int(input("Scrie id-ul obiectului de sters: "))

    return StergereObiectLista(id, lista)


def UI_ShowAll(lista):
    print("Obiectele din inventar sunt: ")
    for obiect in lista:
        print(toString(obiect))


def run_UI(lista):
    while True:
        PrintMenu()
        optiune = input("Alege o optiune: ")
        if optiune == '1':
            lista = UI_AdaugaObiect(lista)
        elif optiune == '2':
            lista = UI_ModificaObiect(lista)
        elif optiune == '3':
            lista = UI_StergereObiect(lista)
        elif optiune == '4':
            UI_ShowAll(lista)
        elif optiune == 'x':
            print("Program incheiat.")
            break
        else:
            print("Ai ales o optiune inexistenta, incearca din nou: ")
