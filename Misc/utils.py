def cmp_generic_nota(a1, a2, rev):
    """

    Functia este are rolul de comparator pentru doua elemente a1 si a2, in functie de nota.
    :param a1: Primul obiect ce trebuie comparat (de tip Asignare()).
    :param a2: Al doilea obiect ce trebuie comparat (de tip Asignare()).
    :param rev: Ordonarea crescatoare sau descrescatoare (cresc sau desc).
    :return: Functia returneaza -1 daca elemenele nu sunt in ordine, 1 daca sunt si 0 daca sunt egale.

    """

    if not rev:
        ordine = -1

    else:
        ordine = 1

    if a1.get_nota() < a2.get_nota():
        return (-1) * ordine
    elif a1.get_nota() > a2.get_nota():
        return 1 * ordine
    else:
        return 0


def cmp_generic_nume(a1, a2, rev):
    """

    Functia este are rolul de comparator pentru doua elemente a1 si a2, in functie de nume.
    :param a1: Primul obiect ce trebuie comparat (de tip Asignare()).
    :param a2: Al doilea obiect ce trebuie comparat (de tip Asignare()).
    :param rev: Ordonarea crescatoare sau descrescatoare (cresc sau desc).
    :return: Functia returneaza -1 daca elemenele nu sunt in ordine, 1 daca sunt si 0 daca sunt egale.

    """

    if not rev:
        ordine = -1

    else:
        ordine = 1

    if a1.get_student().get_nume() < a2.get_student().get_nume():
        return (-1) * ordine
    elif a1.get_student().get_nume() > a2.get_student().get_nume():
        return 1 * ordine
    else:
        return 0


def cmp_generic_nr_probleme(d1, d2, rev):
    """

    Functia este are rolul de comparator pentru doua elemente d1 si d2, in functie de nume.
    :param d1: Primul obiect ce trebuie comparat.
    :param d2: Al doilea obiect ce trebuie comparat.
    :param rev: Ordonarea crescatoare sau descrescatoare (cresc sau desc).
    :return: Functia returneaza -1 daca elemenele nu sunt in ordine, 1 daca sunt si 0 daca sunt egale.

    """
    if not rev:
        ordine = -1

    else:
        ordine = 1

    if d1[1] < d2[1]:
        return (-1) * ordine
    elif d1[1] > d2[1]:
        return 1 * ordine
    else:
        return 0


def qSort_generic(lst, cmp=cmp_generic_nota, rev=False):
    """

    Functia recursiva pentru qSort primeste o lista, o functie de comparatie si un parametru optional rev
    (care determina daca se va ordona crescator sau descrescator) si returneaza lista sortata.

    :param lst: Lista ce trebuie sortata.
    :param cmp: Comparatorul, in functie de campul clasei.
    :param rev: Un parametru optional care, by default, este False.
                (True == sortare descrescatoare, False == sortare crescatoare)
    :return: Functia returneaza lista sortata.

    Complexitate caz defavorabil: Theta(n^2) (lista este in ordine inversa)
    Complexitate caz favorabil: Theta(n * log(n)) (lista este ordonata deja)
    Complexitate caz mediu: Theta(n * log(n))
    Complexitate generala: O(n * log(n))

    """

    if len(lst) <= 1:
        return lst

    pivot = lst.pop()
    mic = qSort_generic([x for x in lst if cmp(x, pivot, rev) == 1], cmp, rev)
    mare = qSort_generic([x for x in lst if cmp(x, pivot, rev) <= 0], cmp, rev)
    return mic + [pivot] + mare


def qSort_generic_nou(lst, cmp1=cmp_generic_nota, cmp2=cmp_generic_nume, rev=False):
    if len(lst) <= 1:
        return lst

    pivot = lst.pop()

    mic = qSort_generic_nou([x for x in lst if (cmp1(x, pivot, rev) == 1) or
                             (cmp1(x, pivot, rev) == 0 and cmp2(x, pivot, rev) == 1)], cmp1, cmp2, rev)

    mare = qSort_generic_nou([x for x in lst if (cmp1(x, pivot, rev) == -1) or
                              (cmp1(x, pivot, rev) == 0 and cmp2(x, pivot, rev) <= 0)], cmp1, cmp2, rev)

    return mic + [pivot] + mare


def gnome_sort_generic(lst, cmp=cmp_generic_nota, rev=False):
    """

    Gnome Sort, supranumit si "stupid sort", este un algoritm de sortare similar cu Insertion Sort
    (in sensul ca lucreaza cu cate un element odata). Algoritmul gaseste prima pozitie unde doua elemente sunt nesortate
    si le interschimba si decrementeaza pozitia. Altfel, avanseaza.

    Complexitate caz defavorabil: Theta(n^2) (lista ordonata descrescator)
    Complexitate caz favorabil: Theta(n) (lista ordonata deja crescator)
    Complexitate caz mediu: Theta(n^2)
    Complexitate generala: O(n^2)

    :param lst: Lista ce trebuie sortata.
    :param cmp: Comparatorul, in functie de campul clasei.
    :param rev: Un parametru optional care, by default, este False.
                (True == sortare descrescatoare, False == sortare crescatoare)
    :return: Functia returneaza lista sortata.

    """

    pos = 0

    while pos <= len(lst) - 1:

        if pos == 0 or cmp(lst[pos - 1], lst[pos], rev) >= 0:
            pos += 1
        else:
            lst[pos], lst[pos - 1] = lst[pos - 1], lst[pos]
            pos -= 1

    return lst


def gnome_sort_generic_nou(lst, cmp1=cmp_generic_nota, cmp2=cmp_generic_nume, rev=False):
    pos = 0

    while pos <= len(lst) - 1:

        if pos == 0 or cmp1(lst[pos - 1], lst[pos], rev) == 1 or (cmp1(lst[pos - 1], lst[pos], rev) == 0 and
                                                                  cmp2(lst[pos - 1], lst[pos], rev) == 1):
            pos += 1

        elif cmp1(lst[pos - 1], lst[pos], rev) == -1 or (cmp1(lst[pos - 1], lst[pos], rev) == 0 and
                                                         cmp2(lst[pos - 1], lst[pos], rev) == -1):
            lst[pos], lst[pos - 1] = lst[pos - 1], lst[pos]
            pos -= 1

    return lst
