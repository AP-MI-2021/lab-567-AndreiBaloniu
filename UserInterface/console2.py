from Domain.inventar import get_new_object, get_object_string
from Logic.concatenare import concatenate_strings
from Logic.crud import create, delete, update
from Logic.mutare import mutare


def show_menu():
    print("""Adaugare: id, nume, descriere, pret, locatie   -> comanda: adaugare
                Exemplu: adaugare,1,scaun,albastru,150,IKEA
             Stergere: id obiect     -> comanda: stergere
                Exemplu: delete
             Modificare: id, nume, descriere, pret, locatie -> comanda: update
                Exemplu: update,1,scaun,albastru,100,IKEA
             Afisare lista. -> comanda: showall
             Modificarea locatiei tuturor obiectelor: locatie  -> comanda: mutare
                Exemplu: mutare, adada
             Concatenare_str: string, valoare   -> comanda: concatenare
                Exemplu: concatenare,orice,100
             Iesire. -> comanda: iesire
    """)


def show_all(obiecte):
    for obiect in obiecte:
        print(get_object_string(obiect))


def console2(obiecte):
    done = True
    while done:
        show_menu()
        comanda = input("Introduceti comenzile separate prin ';', iar detaliitle pentru fiecare comanda prin ',': ")
        serie_comanda = comanda.split(";")
        for comanda in serie_comanda:
            comanda = comanda.split(",")
            if comanda[0] == "adaugare":
                try:
                    obiecte = create(obiecte, int(comanda[1]), comanda[2], comanda[3], float(comanda[4]), comanda[5])
                except ValueError as ve:
                    print("Eroare: ", ve)
            elif comanda[0] == "stergere":
                try:
                    obiecte = delete(obiecte, int(comanda[1]))
                except ValueError as ve:
                    print("Eroare: ", ve)
            elif comanda[0] == "update":
                try:
                    obiecte = update(obiecte, get_new_object(int(comanda[1]),
                                                             comanda[2], comanda[3], float(comanda[4]), comanda[5]))
                except ValueError as ve:
                    print("Eroare: ", ve)
            elif comanda[0] == "showall":
                show_all(obiecte)
            elif comanda[0] == "mutare":
                print(mutare(obiecte, comanda[1]))
            elif comanda[0] == "concatenare":
                try:
                    print(concatenate_strings(obiecte, comanda[1], float(comanda[2])))
                except ValueError as ve:
                    print("Eroare: ", ve)
            elif comanda[0] == "iesire":
                done = False
                break
