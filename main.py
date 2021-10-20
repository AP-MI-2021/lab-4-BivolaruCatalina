def nr_egal_par(lista1, lista2) -> bool:
    """
    Verifica daca exista un numar egal de numere pare in lista1 si lista2.
    :param lista1: prima lista in care au fost introduse elementele
    :param lista2: a doua  lista in care au fost introduse elementele
    :return: O valoare adevarata in functie de caz
    """
    contor1 = 0
    contor2 = 0
    for element in lista1:
        if element% 2 == 0:
            contor1 += 1

    for element in lista2:
        if element%2 == 0:
            contor2 += 1

    if contor1 == contor2:
        return True
    else:
        return False


def test_nr_egal_par():
    assert nr_egal_par([12, 22, 36, 424], [22, 23, 36, 55, 56]) == False
    assert nr_egal_par([12, 21, 36, 424], [22, 23, 36, 55, 424]) == True


def intersectia_listelor(lista1, lista2) -> list[int]:
    """
    Creeaza o noua lista result_list in  care sunt puse numerele  care se gasesc in ambele liste.
    :param lista1: prima lista in care au fost introduse elementele
    :param lista2: a doua  lista in care au fost introduse elementele
    :return: Returneaza toate elementele comune ale listelor prin parameytrul result_list
    """
    result_list = []
    for element in lista1:
        if element in lista2 and not element in result_list:
            result_list.append(element)
    return result_list


def test_intersectia_listelor():
    assert intersectia_listelor([12, 22, 36, 424], [22, 23, 36, 12, 56]) == [12,22,36]
    assert intersectia_listelor([12, 21, 36, 424], [22, 23, 32, 55, 424]) == [22]


def palindroame(lista1, lista2) -> list[int]:
    """
    Creeaza palindroamele prin concatenarea elementelor din liste aflate pe aceeasi pozitie
    :param lista1: prima lista in care au fost introduse elementele
    :param lista2: a doua  lista in care au fost introduse elementele
    :return: Returneaza lista in care se afla palindraomele prin parametrul result_list.
    """
    result_list = []
    palin = 0
    if len(lista1) > len(lista2):
        lungime = len(lista2)
    else:
        lungime = len(lista1)

    for i in range(0, lungime):
            aux1 = lista2[i]
            aux2 = 0
            palin = lista1[i]
            while aux1 :
                aux2 = aux2*10+aux1%10
                aux1 = aux1//10
            while aux2:
                palin = palin*10+aux2%10
                aux2 = aux2//10
            if is_palindrome(palin):
                result_list.append(palin)
    return result_list


def test_palindroame():
    assert palindroame([12, 22, 36, 11], [21, 23, 63, 11, 55]) == [1221, 3663, 1111]
    assert palindroame([12, 22, 36, 11], [12, 23, 63, 55, 424]) == [3663]

def is_palindrome(n) -> bool:
    """
    Verifica daca n este palindrom.
    :param n: elementul din lista ca urmeaza sa fie verificat
    :return:  O valoare adevarata in functie de caz
    """
    aux1 = n
    aux2 = 0
    while aux1:
        aux2 = aux2*10+aux1%10
        aux1 = aux1//10
    if aux2 == n:
        return True
    else:
        return False


def inlocuire_lista1(lista1, lista3) -> list[int]:
    """
    Inlocuieste elementele din lista cu oglinditele daca respecta conditiile mentionate.
    :param lista1: prima lista in care au fost introduse elementele
    :param lista3: a treia lista in care au fost introduse elementele
    :return: lista1 cu elementele inlocuite prin result_list
    """
    result_lst = []
    for element in lista1:
         if divi_cu_toate(lista3, element):
             string = str(element)
             string = string[::-1]
             result_lst.append(int(string))
         else:
             result_lst.append(element)
    return result_lst


def test_inlocuire_lista1():
    assert palindroame([12, 22, 24, 363], [1, 2, 3, 4]) == [21, 22, 42, 363]
    assert palindroame([12, 36, 24, 363], [1, 2, 3, 4]) == [21, 63, 42, 363]



def inlocuire_lista2(lista2, lista3) -> list[int]:
    """
    Inlocuieste elementele din lista cu oglinditele daca respecta conditiile mentionate.
    :param lista2: a doua lista in care au fost introduse elementele
    :param lista3: a treia lista in care au fost introduse elementele
    :return: lista1 cu elementele inlocuite prin result_lst
    """
    result_lst = []
    string = []
    for element in lista2:
        if divi_cu_toate(lista3, element):
            string = str(element)
            string = string[::-1]
            result_lst.append(int(string))
        else:
            result_lst.append(element)
    return result_lst


def test_inlocuire_lista2():
    assert palindroame([12, 22, 24, 363], [1, 2, 3, 4]) == [21, 22, 42, 363]
    assert palindroame([12, 36, 24, 363], [1, 2, 3, 4]) == [21, 63, 42, 363]


def divi_cu_toate(lista3, element) -> bool:
    """
    Verifica daca elementul se divide cu toate numerele din lista3
    :param lista3: a treia lista in care au fost introduse elementele
    :param element: elementul ce urmeaza a fi verificat
    :return: O valoare adevarata in functie de caz
    """
    ok = 0
    for i in lista3:
        if element%i == 0:
            ok = 1
        else:
            ok = 0
    if ok == 0:
        return False
    else:
        return True


def citire_lista1() -> list[int]:
    result_list = []
    string = input('Introduceti elementele primei liste: ')
    string_elemente = string.split(sep=", ")

    for string_element in string_elemente:
        result_list.append(int(string_element))
    return result_list


def citire_lista2() -> list[int]:
    result_list = []
    string = input('Introduceti elementele celei de a doua liste: ')
    string_elemente = string.split(sep=", ")

    for string_element in string_elemente:
        result_list.append(int(string_element))
    return result_list


def citire_lista3() -> list[int]:
    result_list = []
    string = input('Introduceti elementele celei de a treia liste: ')
    string_elemente = string.split(sep=", ")

    for string_element in string_elemente:
        result_list.append(int(string_element))
    return result_list



def main():
    lista1 = []
    lista2 = []
    stop = True
    while stop:
        print("""
        1 -> Citirea listelor
        2 -> Verificare numar egale de elemente pare in listta.
        3 -> Intersectia celor doua liste.4
        4 -> Afisare palindroame.
        5 -> Afisarea numerelor care indeplinesc conditiile precizate.
        x -> Oprire program.
        """)
        command = input('Introduce comand: ')
        if command == '1':
            lista1 = citire_lista1()
            lista2 = citire_lista2()
        elif command == '2':
            if nr_egal_par(lista1, lista2):
                print(f'DA')
            else:
                print(f'NU')
        elif command == '3':
            result_list = intersectia_listelor(lista1, lista2)
            print(result_list)
        elif command == '4':
            result_list = palindroame(lista1, lista2)
            print(result_list)
        elif command == '5':
            lista3 = citire_lista3()
            result_list1 = inlocuire_lista1(lista1, lista3)
            result_list2 = inlocuire_lista2(lista2, lista3)
            print(result_list1, result_list2)
        elif command == 'x':
            stop = False
main()