from Domain.student import Student
from Domain.problema import Problema
from Domain.asignare import Asignare

from Repository.repo_problema import Data

import unittest

######################################################################################################################


class TestStudenti(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_getters_student(self):
        # White-box testing: testez toate ramurile pentru getteri
        # (ID-ul studentului, numr, grupa, si toate atributele).

        student = Student(1, "Pop Ion", 213)

        assert student.get_stud_id() == 1
        assert student.get_nume() == "Pop Ion"
        assert student.get_grupa() == 213
        assert student.get_all() == (1, "Pop Ion", 213)

    def test_setters_student(self):
        # White-box testing: testez toate ramurile pentru setteri, dar si pentru getteri
        # (ID-ul studentului, numr, grupa, si toate atributele).

        student = Student(0, 0, 0)

        student.set_stud_id(101)
        student.set_nume("Pop Ion")
        student.set_grupa(213)

        assert student.get_stud_id() == 101
        assert student.get_nume() == "Pop Ion"
        assert student.get_grupa() == 213
        assert student.get_all() == (101, "Pop Ion", 213)

        student.set_all(1, "Popescu Alexandru", 913)

        assert student.get_stud_id() == 1
        assert student.get_nume() == "Popescu Alexandru"
        assert student.get_grupa() == 913
        assert student.get_all() == (1, "Popescu Alexandru", 913)


######################################################################################################################

class TestProbleme(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_getters_problema(self):
        # White-box testing: testez toate ramurile pentru getteri
        # (nr. laborator, nr. problema, descriere, deadline, toate atributele si toate atributele fara deadline).

        dl1 = Data("11.12.2020")
        problema = Problema(1, 1, "Management baza de date", dl1)

        assert problema.get_nr_lab() == 1
        assert problema.get_nr_prob() == 1
        assert problema.get_descr() == "Management baza de date"
        assert problema.get_deadline() == dl1
        assert problema.get_all() == (1, 1, "Management baza de date", dl1)
        assert problema.get_all_dl() == (1, 1, "Management baza de date")

    def test_setters_problema(self):
        # White-box testing: testez toate ramurile pentru setteri, dar si pentru getteri
        # (nr. laborator, nr. problema, descriere, deadline si toate atributele).

        dl1 = Data("04.03.2021")
        problema = Problema(0, 0, 0, 0)

        problema.set_nr_lab(2)
        problema.set_nr_prob(3)
        problema.set_descr("Mersul trenurilor")
        problema.set_deadline(dl1)

        assert problema.get_nr_lab() == 2
        assert problema.get_nr_prob() == 3
        assert problema.get_descr() == "Mersul trenurilor"
        assert problema.get_deadline() == dl1
        assert problema.get_all() == (2, 3, "Mersul trenurilor", dl1)
        assert problema.get_all_dl() == (2, 3, "Mersul trenurilor")

        dl2 = Data("28.02.2021")
        problema.set_all(7, 17, "Cont bancar", dl2)

        assert problema.get_nr_lab() == 7
        assert problema.get_nr_prob() == 17
        assert problema.get_descr() == "Cont bancar"
        assert problema.get_deadline() == dl2
        assert problema.get_all() == (7, 17, "Cont bancar", dl2)
        assert problema.get_all_dl() == (7, 17, "Cont bancar")


######################################################################################################################

class TestAsignari(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_getters_asignare(self):
        # White-box testing: testez toate ramurile pentru getteri
        # (student, problema, nota si asignarea sub forma de tuple).

        s1, p1 = Student(1, "Pop Ion", 213), Problema(1, 1, "Cont bancar", "20.12.2020")
        a1 = Asignare(s1, p1)

        assert a1.get_nota() == 0
        assert a1.get_student() == Student(1, "Pop Ion", 213)
        assert a1.get_problema() == Problema(1, 1, "Cont bancar", "20.12.2020")

        a1.set_nota(9)
        assert a1.get_nota() == 9

        assert a1.get_asignare_tuple() == (Student(1, "Pop Ion", 213), Problema(1, 1, "Cont bancar", "20.12.2020"))

    def test_setters_asignare(self):
        # White-box testing: testez toate ramurile pentru setteri, dar si pentru getteri
        # (student, problema si nota).

        s1, p1 = Student(1, "Pop Ion", 213), Problema(1, 1, "Cont bancar", "20.12.2020")
        nota = 7
        a1 = Asignare(0, 0)

        a1.set_nota(nota)
        assert a1.get_nota() == 7

        a1.set_student(s1)
        assert a1.get_student() == Student(1, "Pop Ion", 213)

        a1.set_problema(p1)
        assert a1.get_problema() == Problema(1, 1, "Cont bancar", "20.12.2020")


######################################################################################################################


def domain_main():
    unittest.main()
