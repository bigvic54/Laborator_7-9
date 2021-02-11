import unittest

from Misc.utils import *

from Domain.asignare import Asignare
from Domain.student import Student
from Domain.problema import Problema
from Repository.repo_problema import Data
######################################################################################################################


class TestUtils(unittest.TestCase):
    def setUp(self):
        self.__a1 = Asignare(Student(1, "Farcasanu Stefan", 213), Problema(1, 1, "Biblioteca", Data("05.04.2021")))
        self.__a2 = Asignare(Student(2, "Dina Andrei-Const", 213), Problema(1, 1, "Biblioteca", Data("05.04.2021")))
        self.__a3 = Asignare(Student(3, "Dretcanu Mihai", 917), Problema(1, 2, "Cinema", Data("18.12.2020")))
        self.__a4 = Asignare(Student(4, "Dretcanu Mihai", 313), Problema(1, 2, "Cinema", Data("18.12.2020")))

        self.__a1.set_nota(6)
        self.__a2.set_nota(6)
        self.__a3.set_nota(10)
        self.__a4.set_nota(9)

        self.__d1 = [213, 2]
        self.__d2 = [313, 1]

    def tearDown(self):
        pass

    def test_qSort_generic(self):
        lista = [self.__a1, self.__a2, self.__a3]
        lista_ordonata = qSort_generic(lista, cmp_generic_nume, True)
        assert lista_ordonata == [self.__a1, self.__a3, self.__a2]

        lista = [self.__a3, self.__a1, self.__a2]
        lista_ordonata = qSort_generic(lista, cmp_generic_nota, True)
        assert lista_ordonata == [self.__a3, self.__a2, self.__a1]

        lista = [self.__a3, self.__a2, self.__a1]
        lista_ordonata = qSort_generic(lista, cmp_generic_nota, False)
        assert lista_ordonata == [self.__a1, self.__a2, self.__a3]

        lista = [self.__a2, self.__a1, self.__a3]
        lista_ordonata = qSort_generic(lista, cmp_generic_nume, False)
        assert lista_ordonata == [self.__a2, self.__a3, self.__a1]

        lista = [self.__d1, self.__d2]
        lista_ordonata = qSort_generic(lista, cmp_generic_nr_probleme, False)
        assert lista_ordonata == [self.__d2, self.__d1]

        lista = [self.__d2, self.__d1]
        lista_ordonata = qSort_generic(lista, cmp_generic_nr_probleme, True)
        assert lista_ordonata == [self.__d1, self.__d2]

    def test_qSort_generic_nou(self):
        lista = [self.__a1, self.__a2, self.__a3, self.__a4]
        lista_ordonata = qSort_generic_nou(lista, cmp_generic_nume, cmp_generic_nota, True)
        assert lista_ordonata == [self.__a1, self.__a3, self.__a4, self.__a2]

        lista = [self.__a4, self.__a2, self.__a3, self.__a1]
        lista_ordonata = qSort_generic_nou(lista, cmp_generic_nota, cmp_generic_nume, True)
        assert lista_ordonata == [self.__a3, self.__a4, self.__a1, self.__a2]

        lista = [self.__a2, self.__a4, self.__a3, self.__a1]
        lista_ordonata = qSort_generic_nou(lista, cmp_generic_nota, cmp_generic_nume, False)
        assert lista_ordonata == [self.__a2, self.__a1, self.__a4, self.__a3]

        lista = [self.__a1, self.__a3, self.__a2, self.__a4]
        lista_ordonata = qSort_generic_nou(lista, cmp_generic_nume, cmp_generic_nota, False)
        assert lista_ordonata == [self.__a2, self.__a4, self.__a3, self.__a1]

    def test_gnome_sort_generic(self):
        lista = [self.__a1, self.__a2, self.__a3]
        lista_ordonata = gnome_sort_generic(lista, cmp_generic_nume, True)
        assert lista_ordonata == [self.__a1, self.__a3, self.__a2]

        lista = [self.__a1, self.__a3, self.__a2]
        lista_ordonata = gnome_sort_generic(lista, cmp_generic_nota, True)
        assert lista_ordonata == [self.__a3, self.__a1, self.__a2]

        lista = [self.__a3, self.__a2, self.__a1]
        lista_ordonata = gnome_sort_generic(lista, cmp_generic_nota, False)
        assert lista_ordonata == [self.__a2, self.__a1, self.__a3]

        lista = [self.__a2, self.__a1, self.__a3]
        lista_ordonata = gnome_sort_generic(lista, cmp_generic_nume, False)
        assert lista_ordonata == [self.__a2, self.__a3, self.__a1]

        lista = [self.__d1, self.__d2]
        lista_ordonata = gnome_sort_generic(lista, cmp_generic_nr_probleme, False)
        assert lista_ordonata == [self.__d2, self.__d1]

        lista = [self.__d2, self.__d1]
        lista_ordonata = gnome_sort_generic(lista, cmp_generic_nr_probleme, True)
        assert lista_ordonata == [self.__d1, self.__d2]

    def test_gnome_sort_generic_nou(self):
        lista = [self.__a1, self.__a2, self.__a3, self.__a4]
        lista_ordonata = gnome_sort_generic_nou(lista, cmp_generic_nume, cmp_generic_nota, True)
        assert lista_ordonata == [self.__a1, self.__a3, self.__a4, self.__a2]

        lista = [self.__a4, self.__a2, self.__a3, self.__a1]
        lista_ordonata = gnome_sort_generic_nou(lista, cmp_generic_nota, cmp_generic_nume, True)
        assert lista_ordonata == [self.__a3, self.__a4, self.__a1, self.__a2]

        lista = [self.__a2, self.__a4, self.__a3, self.__a1]
        lista_ordonata = gnome_sort_generic_nou(lista, cmp_generic_nota, cmp_generic_nume, False)
        assert lista_ordonata == [self.__a2, self.__a1, self.__a4, self.__a3]

        lista = [self.__a1, self.__a3, self.__a2, self.__a4]
        lista_ordonata = gnome_sort_generic_nou(lista, cmp_generic_nume, cmp_generic_nota, False)
        assert lista_ordonata == [self.__a2, self.__a4, self.__a3, self.__a1]


######################################################################################################################


def utils_main():
    unittest.main()
