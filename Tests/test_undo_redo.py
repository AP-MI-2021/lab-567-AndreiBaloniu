from Logic.crud import create
from UserInterface.console import handle_new_list, handle_undo, handle_redo


def testare_undo_redo():
    lista_obiecte = []
    list_version = [lista_obiecte]
    current_version = 0
    lista_obiecte = create(lista_obiecte, 1, 'masa', 'lemn', 300, 'IKEA')
    list_version, current_version = handle_new_list(list_version, current_version, lista_obiecte)
    lista_obiecte = create(lista_obiecte, 2, 'cana', 'albastru', 10, 'IKEA')
    list_version, current_version = handle_new_list(list_version, current_version, lista_obiecte)
    lista_obiecte = create(lista_obiecte, 3, 'boxa', 'JBL', 250, 'EMAG')
    list_version, current_version = handle_new_list(list_version, current_version, lista_obiecte)
    lista_obiecte, current_version = handle_undo(list_version, current_version)
    assert len(lista_obiecte) == 2
    lista_obiecte, current_version = handle_undo(list_version, current_version)
    assert len(lista_obiecte) == 1
    lista_obiecte, current_version = handle_undo(list_version, current_version)
    assert len(lista_obiecte) == 0
    lista_obiecte, current_version = handle_undo(list_version, current_version)
    assert len(lista_obiecte) == 0
    lista_obiecte = create(lista_obiecte, 1, 'masa', 'lemn', 300, 'IKEA')
    list_version, current_version = handle_new_list(list_version, current_version, lista_obiecte)
    lista_obiecte = create(lista_obiecte, 2, 'cana', 'albastru', 10, 'IKEA')
    list_version, current_version = handle_new_list(list_version, current_version, lista_obiecte)
    lista_obiecte = create(lista_obiecte, 3, 'boxa', 'JBL', 250, 'EMAG')
    list_version, current_version = handle_new_list(list_version, current_version, lista_obiecte)
    lista_obiecte, current_version = handle_redo(list_version, current_version)
    assert len(lista_obiecte) == 3
    lista_obiecte, current_version = handle_undo(list_version, current_version)
    lista_obiecte, current_version = handle_undo(list_version, current_version)
    assert len(lista_obiecte) == 1
    lista_obiecte, current_version = handle_redo(list_version, current_version)
    assert len(lista_obiecte) == 2
    lista_obiecte, current_version = handle_redo(list_version, current_version)
    assert len(lista_obiecte) == 3
    lista_obiecte, current_version = handle_undo(list_version, current_version)
    lista_obiecte, current_version = handle_undo(list_version, current_version)
    assert len(lista_obiecte) == 1
    lista_obiecte = create(lista_obiecte, 4, 'lampa', 'de birou', 100, 'IKEA')
    list_version, current_version = handle_new_list(list_version, current_version, lista_obiecte)
    lista_obiecte, current_version = handle_redo(list_version, current_version)
    assert len(lista_obiecte) == 2
    lista_obiecte, current_version = handle_undo(list_version, current_version)
    assert len(lista_obiecte) == 1
    lista_obiecte, current_version = handle_undo(list_version, current_version)
    assert len(lista_obiecte) == 0
    lista_obiecte, current_version = handle_redo(list_version, current_version)
    lista_obiecte, current_version = handle_redo(list_version, current_version)
    assert len(lista_obiecte) == 2
    lista_obiecte, current_version = handle_redo(list_version, current_version)
    assert len(lista_obiecte) == 2


testare_undo_redo()