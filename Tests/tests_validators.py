import Repository.repo_problema

from Domain.student import Student
from Validators.validators import ValidatorStudent

from Domain.problema import Problema
from Validators.validators import ValidatorProblema

from Validators.validators import ValidatorAsignare

from Exceptions.exceptions import *

import unittest

######################################################################################################################


class TestValidatorStudent(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_validare_id(self):
        # White-box testing: testez toate ramurile pentru validarea ID-ului studentului
        # (ID-ul sa nu fie studentului nul, negativ sau non-intreg).

        validator_student = ValidatorStudent()

        student = Student(-1, "Pop Ion", 213)
        self.assertRaises(IDError, validator_student.validare_stud_id, student.get_stud_id())

        student = Student("1a", "Pop Ion", 2009)
        self.assertRaises(IDError, validator_student.validare_stud_id, student.get_stud_id())

        student = Student(0, "Pop Ion", 317)
        self.assertRaises(IDError, validator_student.validare_stud_id, student.get_stud_id())

        student = Student(4.5, "Pop Ion",999)
        self.assertRaises(IDError, validator_student.validare_stud_id, student.get_stud_id())

    def test_validare_nume(self):
        # White-box testing: testez toate ramurile pentru validarea numelui studentului
        # (numele sa nu fie vid, contine cifre sau e non-string).

        validator_student = ValidatorStudent()

        student = Student(3, "", 919)
        self.assertRaises(NumeError, validator_student.validare_nume, student.get_nume())

        student = Student(103, "Popescu7 Andrei008", 303)
        self.assertRaises(NumeError, validator_student.validare_nume, student.get_nume())

        student = Student(75, "157 0 rw // gds", 999)
        self.assertRaises(NumeError, validator_student.validare_nume, student.get_nume())

        student = Student(10, "154256", 777)
        self.assertRaises(NumeError, validator_student.validare_nume, student.get_nume())

        student = Student(11, 345, 790)
        self.assertRaises(NumeError, validator_student.validare_nume, student.get_nume())

    def test_validare_grupa(self):
        # White-box testing: testez toate ramurile pentru validarea grupei studentului
        # (grupa sa nu fie negativa, nula sau non-intreg).

        validator_student = ValidatorStudent()

        student = Student(53, "Pop Alex", -1)
        self.assertRaises(GrupaError, validator_student.validare_grupa, student.get_grupa())

        student = Student(103, "Popescu Andrei", 0)
        self.assertRaises(GrupaError, validator_student.validare_grupa, student.get_grupa())

        student = Student(103, "Ionescu Daniel", "213j")
        self.assertRaises(GrupaError, validator_student.validare_grupa, student.get_grupa())

        student = Student(555, "Alexandriuc Iulia", "afGj")
        self.assertRaises(GrupaError, validator_student.validare_grupa, student.get_grupa())

        student = Student(33, "Popovici Stefania", "afe*( .. //t5 yGj")
        self.assertRaises(GrupaError, validator_student.validare_grupa, student.get_grupa())

        student = Student(303, "Popovici Stefania", 8.80)
        self.assertRaises(GrupaError, validator_student.validare_grupa, student.get_grupa())

    def test_validare_student(self):
        # White-box testing pentru validarea tuturor datelor unui student.

        validator_student = ValidatorStudent()

        student = Student(-1, "Popescu Ionescu", 213)
        self.assertRaises(IDError, validator_student.validare_student_object, student)

        student = Student(0, "Popescu Ionescu", 213)
        self.assertRaises(IDError, validator_student.validare_student_object, student)

        student = Student("a", "Popescu Ionescu", 213)
        self.assertRaises(IDError, validator_student.validare_student_object, student)

        student = Student(7.5, "Popescu Ionescu", 213)
        self.assertRaises(IDError, validator_student.validare_student_object, student)

        student = Student(5, "Po53 7Acu", 213)
        self.assertRaises(NumeError, validator_student.validare_student_object, student)

        student = Student(5, "Poescu Ionesc**/.u", 213)
        self.assertRaises(NumeError, validator_student.validare_student_object, student)

        student = Student(5, "", 213)
        self.assertRaises(NumeError, validator_student.validare_student_object, student)

        student = Student(7, "Popescu Ionescu", 213.5)
        self.assertRaises(GrupaError, validator_student.validare_student_object, student)

        student = Student(7, "Popescu Ionescu", "k")
        self.assertRaises(GrupaError, validator_student.validare_student_object, student)

        student = Student(7, "Popescu Ionescu", -1)
        self.assertRaises(GrupaError, validator_student.validare_student_object, student)

        student = Student(7, "Popescu Ionescu", 0)
        self.assertRaises(GrupaError, validator_student.validare_student_object, student)

######################################################################################################################


class TestValidatorProblema(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_validare_nr_lab(self):
        # White-box testing: testez toate ramurile pentru validarea numarului laboratorului
        # (numarul sa nu fie negativ, nul sau non-intreg).

        validator_problema = ValidatorProblema()

        dl1 = Repository.repo_problema.Data("05.12.2020")
        problema = Problema(-1, 1, "Baza de date", dl1)
        self.assertRaises(NrLabError, validator_problema.validare_nr_lab, problema.get_nr_lab())

        dl2 = Repository.repo_problema.Data("19.12.2020")
        problema = Problema(0, 1, "Management Biblioteca", dl2)
        self.assertRaises(NrLabError, validator_problema.validare_nr_lab, problema.get_nr_lab())

        dl3 = Repository.repo_problema.Data("07.01.2021")
        problema = Problema("11a", 3, "Management Cinematograf", dl3)
        self.assertRaises(NrLabError, validator_problema.validare_nr_lab, problema.get_nr_lab())

        dl4 = Repository.repo_problema.Data("31.12.2020")
        problema = Problema(7.657, 7, "Mersul trenurilor", dl4)
        self.assertRaises(NrLabError, validator_problema.validare_nr_lab, problema.get_nr_lab())

    def test_validare_nr_prob(self):
        # White-box testing: testez toate ramurile pentru validarea numarului problemei
        # (numarul sa nu fie negativ, nul sau non-intreg).

        validator_problema = ValidatorProblema()

        dl1 = Repository.repo_problema.Data("18.02.2021")
        problema = Problema(1, -1, "Catalog studenti", dl1)
        self.assertRaises(NrProbError, validator_problema.validare_nr_prob, problema.get_nr_prob())

        dl2 = Repository.repo_problema.Data("31.06.2021")
        problema = Problema(2, 0, "Metoda Greedy", dl2)
        self.assertRaises(NrProbError, validator_problema.validare_nr_prob, problema.get_nr_prob())

        dl3 = Repository.repo_problema.Data("30.04.2021")
        problema = Problema(3, "33c", "Cont bancar", dl3)
        self.assertRaises(NrProbError, validator_problema.validare_nr_prob, problema.get_nr_prob())

        dl4 = Repository.repo_problema.Data("30.11.2020")
        problema = Problema(4, 9.523, "Mersul trenurilor", dl4)
        self.assertRaises(NrProbError, validator_problema.validare_nr_prob, problema.get_nr_prob())

    def test_validare_descr(self):
        # White-box testing: testez toate ramurile pentru validarea descrierii problemei
        # (descrierea sa nu fie vida sau non-string).

        dl1 = Repository.repo_problema.Data("31.12.2020")
        problema = Problema(1, 1, "", dl1)
        validator_problema = ValidatorProblema()
        self.assertRaises(DescrError, validator_problema.validare_descr, problema.get_descr())

        dl2 = Repository.repo_problema.Data("30.04.2021")
        problema = Problema(1, 1, 456, dl2)
        validator_problema = ValidatorProblema()
        self.assertRaises(DescrError, validator_problema.validare_descr, problema.get_descr())

    def test_validare_deadline(self):
        # White-box testing: testez toate ramurile pentru validarea deadline-ul problemei
        # (deadline-ul sa fie valid (adica 31 aprilie este o data invalida), ziua sa fie integer intre 1 si 31, luna sa
        # fie integer intre 1 si 12 si anul sa fie integer intre 2020 si 2023).

        validator_problema = ValidatorProblema()

        dl1 = Repository.repo_problema.Data("aa.12.2020")
        problema = Problema(1, 1, "Contabilitate", dl1)
        self.assertRaises(DeadlineError, validator_problema.validare_deadline, problema.get_deadline())

        dl2 = Repository.repo_problema.Data("12.aa.2020")
        problema = Problema(1, 1, "Cheltuieli de familie", dl2)
        self.assertRaises(DeadlineError, validator_problema.validare_deadline, problema.get_deadline())

        dl3 = Repository.repo_problema.Data("12.12.aaaa")
        problema = Problema(1, 1, "Management Service Auto", dl3)
        self.assertRaises(DeadlineError, validator_problema.validare_deadline, problema.get_deadline())

        dl4 = Repository.repo_problema.Data("-1.06.2020")
        problema = Problema(1, 1, "Cumparaturi", dl4)
        self.assertRaises(ZiError, validator_problema.validare_deadline, problema.get_deadline())

        dl5 = Repository.repo_problema.Data("72.06.2020")
        problema = Problema(1, 2, "Mersul trenurilor", dl5)
        self.assertRaises(ZiError, validator_problema.validare_deadline, problema.get_deadline())

        dl6 = Repository.repo_problema.Data("01.17.2020")
        problema = Problema(2, 1, "Cadouri de craciun", dl6)
        self.assertRaises(LunaError, validator_problema.validare_deadline, problema.get_deadline())

        dl7 = Repository.repo_problema.Data("01.-7.2020")
        problema = Problema(2, 2, "Problema de geometrie", dl7)
        self.assertRaises(LunaError, validator_problema.validare_deadline, problema.get_deadline())

        dl8 = Repository.repo_problema.Data("01.07.1990")
        problema = Problema(3, 3, "Cadouri de craciun", dl8)
        self.assertRaises(AnError, validator_problema.validare_deadline, problema.get_deadline())

        dl9 = Repository.repo_problema.Data("01.07.-1")
        problema = Problema(3, 7, "Cheltuieli reparatii automobil", dl9)
        self.assertRaises(AnError, validator_problema.validare_deadline, problema.get_deadline())

        dl10 = Repository.repo_problema.Data("38.12.-1.78.35")
        problema = Problema(3, 9, "Cheltuieli service auto", dl10)
        self.assertRaises(AnError, validator_problema.validare_deadline, problema.get_deadline())

    def test_validare_problema(self):
        # White-box testing pentru validarea tuturor datelor unei probleme.

        validator_problema = ValidatorProblema()

        dl1 = Repository.repo_problema.Data("16.12.2020")
        problema = Problema(-1, 1, "Catalog studenti", dl1)
        self.assertRaises(NrLabError, validator_problema.validare_problema_object, problema)

        problema = Problema("v", 1, "Catalog studenti", dl1)
        self.assertRaises(NrLabError, validator_problema.validare_problema_object, problema)

        problema = Problema(0, 1, "Catalog studenti", dl1)
        self.assertRaises(NrLabError, validator_problema.validare_problema_object, problema)

        problema = Problema(2, -1, "Catalog studenti", dl1)
        self.assertRaises(NrProbError, validator_problema.validare_problema_object, problema)

        problema = Problema(2, 0, "Catalog studenti", dl1)
        self.assertRaises(NrProbError, validator_problema.validare_problema_object, problema)

        problema = Problema(2, "m", "Catalog studenti", dl1)
        self.assertRaises(NrProbError, validator_problema.validare_problema_object, problema)

        problema = Problema(3, 2, "", dl1)
        self.assertRaises(DescrError, validator_problema.validare_problema_object, problema)

        problema = Problema(3, 2, 980, dl1)
        self.assertRaises(DescrError, validator_problema.validare_problema_object, problema)


######################################################################################################################


class TestValidatorAsignare(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_validare_nota(self):
        # White-box testing: testez toate ramurile pentru validarea notei asignarii
        # (nota sa fie numar, cuprins intre 1 si 10)

        validator_asignare = ValidatorAsignare()

        self.assertRaises(NotaError, validator_asignare.validare_nota, 100)
        self.assertRaises(NotaError, validator_asignare.validare_nota, "abc")
        self.assertRaises(NotaError, validator_asignare.validare_nota, "")
        self.assertRaises(NotaError, validator_asignare.validare_nota, -109538)
        self.assertRaises(NotaError, validator_asignare.validare_nota, 0)
        self.assertRaises(NotaError, validator_asignare.validare_nota, 11)


######################################################################################################################


def validators_main():
    unittest.main()
