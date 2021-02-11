import Repository.repo_student as repo_student
import Repository.repo_problema as repo_problema
import Repository.repo_asignare as repo_asignare

from Domain.student import Student
from Domain.problema import Problema
from Domain.asignare import Asignare

from Exceptions.exceptions import *

import unittest


######################################################################################################################


class ETestRepoStudenti(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_Aadaugare_student(self):
        # White-box testing pentru adaugarea studentilor in repository.

        student = Student(1, "Pop Ana", 213)
        repo_student.lista_stud.adaugare_student_file(student)
        content = repo_student.lista_stud.readFromFile()
        assert content == [Student(1, "Pop Ana", 213)]

        student = Student(2, "Popescu Ion", 215)
        repo_student.lista_stud.adaugare_student_file(student)
        content = repo_student.lista_stud.readFromFile()
        assert content == [Student(1, "Pop Ana", 213), Student(2, "Popescu Ion", 215)]

        student = Student(3, "Georgescu George", 4)
        repo_student.lista_stud.adaugare_student_file(student)
        content = repo_student.lista_stud.readFromFile()
        assert content == [Student(1, "Pop Ana", 213), Student(2, "Popescu Ion", 215),
                           Student(3, "Georgescu George", 4)]

        student = Student(130, "Enescu Ionel", 217)
        repo_student.lista_stud.adaugare_student_file(student)
        content = repo_student.lista_stud.readFromFile()
        assert content == [Student(1, "Pop Ana", 213), Student(2, "Popescu Ion", 215),
                           Student(3, "Georgescu George", 4),
                           Student(130, "Enescu Ionel", 217)]

        student = Student(164, "Margineanu Manuela", 415)
        repo_student.lista_stud.adaugare_student_file(student)
        content = repo_student.lista_stud.readFromFile()
        assert content == [Student(1, "Pop Ana", 213), Student(2, "Popescu Ion", 215),
                           Student(3, "Georgescu George", 4),
                           Student(130, "Enescu Ionel", 217), Student(164, "Margineanu Manuela", 415)]

    def test_Dstergere_student(self):
        # White-box testing pentru stergerea studentilor din repository.

        repo_student.lista_stud.stergere_student_file(0)
        content = repo_student.lista_stud.readFromFile()
        assert content == [Student(10, 'Popescu Alex', 214), Student(3, 'Georgescu George', 4),
                           Student(15, 'Ionescu Ioana', 319), Student(5, 'Codreanu Mihai', 213)]

        repo_student.lista_stud.stergere_student_file(3)
        content = repo_student.lista_stud.readFromFile()
        assert content == [Student(10, 'Popescu Alex', 214), Student(3, 'Georgescu George', 4),
                           Student(15, 'Ionescu Ioana', 319)]

        repo_student.lista_stud.stergere_student_file(2)
        content = repo_student.lista_stud.readFromFile()
        assert content == [Student(10, 'Popescu Alex', 214), Student(3, 'Georgescu George', 4)]

        repo_student.lista_stud.stergere_student_file(1)
        content = repo_student.lista_stud.readFromFile()
        assert content == [Student(10, 'Popescu Alex', 214)]

        repo_student.lista_stud.stergere_student_file(0)
        assert repo_student.lista_stud.get_list() == []

    def test_Cmodificare_student(self):
        # White-box testing pentru modificarea studentilor din repository.

        student_nou = Student(10, "Popescu Alex", 214)
        repo_student.lista_stud.modificare_student_file(1, student_nou)
        content = repo_student.lista_stud.readFromFile()
        assert content == [Student(1, "Pop Ana", 213), Student(10, "Popescu Alex", 214),
                           Student(3, "Georgescu George", 4),
                           Student(130, "Enescu Ionel", 217), Student(164, "Margineanu Manuela", 415)]

        student_nou = Student(15, "Ionescu Ioana", 319)
        repo_student.lista_stud.modificare_student_file(3, student_nou)
        content = repo_student.lista_stud.readFromFile()
        assert content == [Student(1, "Pop Ana", 213), Student(10, "Popescu Alex", 214),
                           Student(3, "Georgescu George", 4),
                           Student(15, "Ionescu Ioana", 319), Student(164, "Margineanu Manuela", 415)]

        student_nou = Student(130, "Grigorescu Stefan", 222)
        repo_student.lista_stud.modificare_student_file(4, student_nou)
        content = repo_student.lista_stud.readFromFile()
        assert content == [Student(1, "Pop Ana", 213), Student(10, "Popescu Alex", 214),
                           Student(3, "Georgescu George", 4),
                           Student(15, "Ionescu Ioana", 319), Student(130, "Grigorescu Stefan", 222)]

        student_nou = Student(5, "Codreanu Mihai", 213)
        repo_student.lista_stud.modificare_student_file(4, student_nou)
        content = repo_student.lista_stud.readFromFile()
        assert content == [Student(1, "Pop Ana", 213), Student(10, "Popescu Alex", 214),
                           Student(3, "Georgescu George", 4),
                           Student(15, "Ionescu Ioana", 319), Student(5, "Codreanu Mihai", 213)]

    def test_Bvalidare_unicitate_id(self):
        # White-box testing pentru a valida daca exista deja un student cu acelasi ID in repository.

        self.assertRaises(IDUnicError, repo_student.lista_stud.validare_unicitate_stud_id, -1, 1)
        self.assertRaises(IDUnicError, repo_student.lista_stud.validare_unicitate_stud_id, -1, 3)
        self.assertRaises(IDUnicError, repo_student.lista_stud.validare_unicitate_stud_id, 3, 2)
        self.assertRaises(IDUnicError, repo_student.lista_stud.validare_unicitate_stud_id, 2, 130)


######################################################################################################################

dl1 = repo_problema.Data("05.11.2020")
dl2 = repo_problema.Data("22.12.2020")
dl3 = repo_problema.Data("01.01.2021")
dl4 = repo_problema.Data("17.06.2021")
dl5 = repo_problema.Data("20.11.2020")


class FTestRepoProblema(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_Aadaugare_problema(self):
        # White-box testing pentru adaugarea problemelor in repository.

        problema = Problema(1, 1, "Baza de date", dl1)

        repo_problema.lista_prob.adaugare_problema_file(problema)
        content = repo_problema.lista_prob.readFromFile()
        assert content == [Problema(1, 1, "Baza de date", dl1)]

        problema = Problema(1, 2, "Management biblioteca", dl2)

        repo_problema.lista_prob.adaugare_problema_file(problema)
        content = repo_problema.lista_prob.readFromFile()
        assert content == [Problema(1, 1, "Baza de date", dl1), Problema(1, 2, "Management biblioteca", dl2)]

        problema = Problema(2, 1, "Concurs de informatica", dl3)

        repo_problema.lista_prob.adaugare_problema_file(problema)
        content = repo_problema.lista_prob.readFromFile()
        assert content == [Problema(1, 1, "Baza de date", dl1), Problema(1, 2, "Management biblioteca", dl2),
                           Problema(2, 1, "Concurs de informatica", dl3)]

        problema = Problema(2, 2, "Catalog studenti", dl4)

        repo_problema.lista_prob.adaugare_problema_file(problema)
        content = repo_problema.lista_prob.readFromFile()
        assert content == [Problema(1, 1, "Baza de date", dl1), Problema(1, 2, "Management biblioteca", dl2),
                           Problema(2, 1, "Concurs de informatica", dl3), Problema(2, 2, "Catalog studenti", dl4)]

        problema = Problema(2, 3, "Management cont bancar", dl5)

        repo_problema.lista_prob.adaugare_problema_file(problema)
        content = repo_problema.lista_prob.readFromFile()
        assert content == [Problema(1, 1, "Baza de date", dl1), Problema(1, 2, "Management biblioteca", dl2),
                           Problema(2, 1, "Concurs de informatica", dl3), Problema(2, 2, "Catalog studenti", dl4),
                           Problema(2, 3, "Management cont bancar", dl5)]

    def test_Dstergere_problema(self):
        # White-box testing pentru stergerea problemelor din repository.

        dl6 = repo_problema.Data("05.04.2021")

        repo_problema.lista_prob.stergere_problema_file(3)
        content = repo_problema.lista_prob.readFromFile()
        assert content == [Problema(1, 1, "Baza de date studenti", dl1), Problema(1, 3, "Management biblioteca", dl2),
                           Problema(2, 1, "Concurs de informatica", dl3),
                           Problema(3, 1, "Management cinematograf", dl6)]

        repo_problema.lista_prob.stergere_problema_file(0)
        content = repo_problema.lista_prob.readFromFile()
        assert content == [Problema(1, 3, "Management biblioteca", dl2), Problema(2, 1, "Concurs de informatica", dl3),
                           Problema(3, 1, "Management cinematograf", dl6)]

        repo_problema.lista_prob.stergere_problema_file(1)
        content = repo_problema.lista_prob.readFromFile()
        assert content == [Problema(1, 3, "Management biblioteca", dl2), Problema(3, 1, "Management cinematograf", dl6)]

        repo_problema.lista_prob.stergere_problema_file(1)
        content = repo_problema.lista_prob.readFromFile()
        assert content == [Problema(1, 3, "Management biblioteca", dl2)]

        repo_problema.lista_prob.stergere_problema_file(0)
        content = repo_problema.lista_prob.readFromFile()
        assert content == []

    def test_Cmodificare_problema(self):
        # White-box testing pentru modificarea problemelor din repository.

        problema_noua = Problema(1, 1, 'Baza de date studenti', dl1)
        repo_problema.lista_prob.modificare_problema_file(0, problema_noua)
        content = repo_problema.lista_prob.readFromFile()
        assert content == [Problema(1, 1, "Baza de date studenti", dl1), Problema(1, 2, "Management biblioteca", dl2),
                           Problema(2, 1, "Concurs de informatica", dl3), Problema(2, 2, "Catalog studenti", dl4),
                           Problema(2, 3, "Management cont bancar", dl5)]

        problema_noua = Problema(1, 3, "Management biblioteca", dl2)
        repo_problema.lista_prob.modificare_problema_file(1, problema_noua)
        content = repo_problema.lista_prob.readFromFile()
        assert content == [Problema(1, 1, "Baza de date studenti", dl1), Problema(1, 3, "Management biblioteca", dl2),
                           Problema(2, 1, "Concurs de informatica", dl3), Problema(2, 2, "Catalog studenti", dl4),
                           Problema(2, 3, "Management cont bancar", dl5)]

        dl6 = repo_problema.Data("05.04.2021")
        problema_noua = Problema(3, 1, "Management cinematograf", dl6)
        repo_problema.lista_prob.modificare_problema_file(4, problema_noua)
        content = repo_problema.lista_prob.readFromFile()
        assert content == [Problema(1, 1, "Baza de date studenti", dl1), Problema(1, 3, "Management biblioteca", dl2),
                           Problema(2, 1, "Concurs de informatica", dl3), Problema(2, 2, "Catalog studenti", dl4),
                           Problema(3, 1, "Management cinematograf", dl6)]

        problema_noua = Problema(2, 3, "Catalog studenti", dl5)
        repo_problema.lista_prob.modificare_problema_file(3, problema_noua)
        content = repo_problema.lista_prob.readFromFile()
        assert content == [Problema(1, 1, "Baza de date studenti", dl1), Problema(1, 3, "Management biblioteca", dl2),
                           Problema(2, 1, "Concurs de informatica", dl3), Problema(2, 3, "Catalog studenti", dl5),
                           Problema(3, 1, "Management cinematograf", dl6)]

        problema_noua = Problema(2, 2, "Mersul trenurilor", dl4)
        repo_problema.lista_prob.modificare_problema_file(3, problema_noua)
        content = repo_problema.lista_prob.readFromFile()
        assert content == [Problema(1, 1, "Baza de date studenti", dl1), Problema(1, 3, "Management biblioteca", dl2),
                           Problema(2, 1, "Concurs de informatica", dl3), Problema(2, 2, "Mersul trenurilor", dl4),
                           Problema(3, 1, "Management cinematograf", dl6)]

    def test_Bvalidare_unicitate_nr_prob(self):
        # White-box testing pentru a valida daca deja exista exista o problema cu acel nr. lab si nr. prob.

        self.assertRaises(NrProbUnicError, repo_problema.lista_prob.validare_unicitate_nr_prob, -1, 1, 1)
        self.assertRaises(NrProbUnicError, repo_problema.lista_prob.validare_unicitate_nr_prob, -1, 2, 3)
        self.assertRaises(NrProbUnicError, repo_problema.lista_prob.validare_unicitate_nr_prob, 1, 2, 1)
        self.assertRaises(NrProbUnicError, repo_problema.lista_prob.validare_unicitate_nr_prob, 3, 2, 3)


######################################################################################################################


class GTestRepoAsignare(unittest.TestCase):
    def setUp(self):
        student1 = Student(15, "Pop Ion", 213)
        student2 = Student(3, "Alexandrescu Mihai", 917)
        student3 = Student(5, "Ionescu Malina", 316)

        new_content = [student1, student2, student3]
        repo_student.lista_stud.set_content(new_content)

        problema1 = Problema(1, 1, "Management baza de date", dl1)
        problema2 = Problema(3, 1, "Cheltuieli de familie", dl2)
        problema3 = Problema(2, 1, "Cheltuieli service auto", dl3)
        problema4 = Problema(1, 3, "Baza de date studenti", dl4)

        new_content = [problema1, problema2, problema3, problema4]
        repo_problema.lista_prob.set_content(new_content)

        self.a1 = Asignare(repo_student.lista_stud.get_content()[0], repo_problema.lista_prob.get_content()[0])
        self.a2 = Asignare(repo_student.lista_stud.get_content()[0], repo_problema.lista_prob.get_content()[1])
        self.a3 = Asignare(repo_student.lista_stud.get_content()[1], repo_problema.lista_prob.get_content()[1])
        self.a4 = Asignare(repo_student.lista_stud.get_content()[1], repo_problema.lista_prob.get_content()[2])

    def tearDown(self):
        pass

    def test_Aadaugare_asignare(self):
        # White-box testing pentru adaugarea asignarilor in repository.

        repo_asignare.lista_asignari.adaugare_asignare_file(self.a1)
        content = repo_asignare.lista_asignari.readFromFile()
        assert content == [Asignare(Student(15, 'Pop Ion', 213), Problema(1, 1, 'Management baza de date', dl1))]

        repo_asignare.lista_asignari.adaugare_asignare_file(self.a2)
        content = repo_asignare.lista_asignari.readFromFile()
        assert content == [Asignare(Student(15, 'Pop Ion', 213), Problema(1, 1, 'Management baza de date', dl1)),
                           Asignare(Student(15, 'Pop Ion', 213), Problema(3, 1, 'Cheltuieli de familie', dl2))]

        repo_asignare.lista_asignari.adaugare_asignare_file(self.a3)
        content = repo_asignare.lista_asignari.readFromFile()
        assert content == [Asignare(Student(15, 'Pop Ion', 213), Problema(1, 1, 'Management baza de date', dl1)),
                           Asignare(Student(15, 'Pop Ion', 213), Problema(3, 1, 'Cheltuieli de familie', dl2)),
                           Asignare(Student(3, 'Alexandrescu Mihai', 917),
                                    Problema(3, 1, 'Cheltuieli de familie', dl3))]

        repo_asignare.lista_asignari.adaugare_asignare_file(self.a4)
        content = repo_asignare.lista_asignari.readFromFile()
        assert content == [Asignare(Student(15, 'Pop Ion', 213), Problema(1, 1, 'Management baza de date', dl1)),
                           Asignare(Student(15, 'Pop Ion', 213), Problema(3, 1, 'Cheltuieli de familie', dl2)),
                           Asignare(Student(3, 'Alexandrescu Mihai', 917),
                                    Problema(3, 1, 'Cheltuieli de familie', dl3)),
                           Asignare(Student(3, 'Alexandrescu Mihai', 917),
                                    Problema(2, 1, 'Cheltuieli service auto', dl4))]

    def test_Bvalidare_asignare_problema(self):
        # White-box testing pentru validarea unicitatii asignarii in repository.

        s1, p1 = repo_student.lista_stud.get_content()[0], repo_problema.lista_prob.get_content()[1]
        s2, p2 = repo_student.lista_stud.get_content()[1], repo_problema.lista_prob.get_content()[1]
        s3, p3 = repo_student.lista_stud.get_content()[1], repo_problema.lista_prob.get_content()[2]
        s4, p4 = repo_student.lista_stud.get_content()[0], repo_problema.lista_prob.get_content()[0]

        self.assertRaises(UnicitateAsignareError, repo_asignare.lista_asignari.validare_asignare_problema, s1, p1)
        self.assertRaises(UnicitateAsignareError, repo_asignare.lista_asignari.validare_asignare_problema, s2, p2)
        self.assertRaises(UnicitateAsignareError, repo_asignare.lista_asignari.validare_asignare_problema, s3, p3)
        self.assertRaises(UnicitateAsignareError, repo_asignare.lista_asignari.validare_asignare_problema, s4, p4)

    def test_Cvalidare_cautare_problema_asignata(self):
        # White-box testing pentru validarea posibilitatii notarii asignarilor in repository.

        s1 = repo_student.lista_stud.get_content()[0]
        s2 = repo_student.lista_stud.get_content()[1]

        self.assertRaises(NotareError, repo_asignare.lista_asignari.validare_cautare_problema_asignata, s1, "1 10")
        self.assertRaises(NotareError, repo_asignare.lista_asignari.validare_cautare_problema_asignata, s1, "2 9")
        self.assertRaises(NotareError, repo_asignare.lista_asignari.validare_cautare_problema_asignata, s2, "1 7")
        self.assertRaises(NotareError, repo_asignare.lista_asignari.validare_cautare_problema_asignata, s2, "3 4")

    def test_Dmodificare_asignare(self):
        # White-box testing pentru modificarea asignarilor din repository.

        p1, d1 = repo_problema.lista_prob.get_content()[0], repo_problema.lista_prob.get_content()[0].get_deadline
        p2, d2 = repo_problema.lista_prob.get_content()[1], repo_problema.lista_prob.get_content()[1].get_deadline
        p3, d3 = repo_problema.lista_prob.get_content()[2], repo_problema.lista_prob.get_content()[2].get_deadline

        d4, d5 = repo_problema.Data("06.07.2021"), repo_problema.Data("02.12.2020")
        d6 = repo_problema.Data("09.01.2021")

        p4 = Problema(1, 7, "Programare dinamica", d4)
        p5 = Problema(2, 3, "Management baza de date", d5)
        p6 = Problema(4, 1, "Cont bancar", d6)

        repo_asignare.lista_asignari.modificare_asignare_file(p1, p4, 0)
        content = repo_asignare.lista_asignari.readFromFile()
        assert content == [Asignare(Student(15, 'Pop Ion', 213), Problema(1, 7, 'Programare dinamica', d4)),
                           Asignare(Student(15, 'Pop Ion', 213), Problema(3, 1, 'Cheltuieli de familie', d2)),
                           Asignare(Student(3, 'Alexandrescu Mihai', 917), Problema(3, 1, 'Cheltuieli de familie', d2)),
                           Asignare(Student(3, 'Alexandrescu Mihai', 917),
                                    Problema(2, 1, 'Cheltuieli service auto', d3))]

        repo_asignare.lista_asignari.modificare_asignare_file(p2, p5, 0)
        content = repo_asignare.lista_asignari.readFromFile()
        assert content == [Asignare(Student(15, 'Pop Ion', 213), Problema(1, 7, 'Programare dinamica', d4)),
                           Asignare(Student(15, 'Pop Ion', 213), Problema(2, 3, "Management baza de date", d5)),
                           Asignare(Student(3, 'Alexandrescu Mihai', 917),
                                    Problema(2, 3, "Management baza de date", d5)),
                           Asignare(Student(3, 'Alexandrescu Mihai', 917),
                                    Problema(2, 1, 'Cheltuieli service auto', d3))]

        repo_asignare.lista_asignari.modificare_asignare_file(p3, p6, 0)
        content = repo_asignare.lista_asignari.readFromFile()
        assert content == [Asignare(Student(15, 'Pop Ion', 213), Problema(1, 7, 'Programare dinamica', d4)),
                           Asignare(Student(15, 'Pop Ion', 213), Problema(2, 3, "Management baza de date", d5)),
                           Asignare(Student(3, 'Alexandrescu Mihai', 917),
                                    Problema(2, 3, "Management baza de date", d5)),
                           Asignare(Student(3, 'Alexandrescu Mihai', 917), Problema(4, 1, "Cont bancar", d6))]

        s1 = repo_student.lista_stud.get_content()[0]
        s4 = Student(30, "Marin Stefania", 717)

        repo_asignare.lista_asignari.modificare_asignare_file(s1, s4, 1)
        content = repo_asignare.lista_asignari.readFromFile()
        assert content == [Asignare(Student(30, "Marin Stefania", 717), Problema(1, 7, 'Programare dinamica', d4)),
                           Asignare(Student(30, "Marin Stefania", 717), Problema(2, 3, "Management baza de date", d5)),
                           Asignare(Student(3, 'Alexandrescu Mihai', 917),
                                    Problema(2, 3, "Management baza de date", d5)),
                           Asignare(Student(3, 'Alexandrescu Mihai', 917), Problema(4, 1, "Cont bancar", d6))]

    def test_Fstergere_asignare(self):
        # White-box testing pentru stergerea asignarilor din repository.

        p4 = Problema(1, 7, "Programare dinamica", repo_problema.Data("06.07.2021"))
        p5 = Problema(2, 3, "Management baza de date", repo_problema.Data("02.12.2020"))
        p6 = Problema(4, 1, "Cont bancar", repo_problema.Data("09.01.2021"))

        d4, d5 = repo_problema.Data("06.07.2021"), repo_problema.Data("02.12.2020")
        d6 = repo_problema.Data("09.01.2021")

        repo_asignare.lista_asignari.stergere_asignare_file(p4, 0)
        content = repo_asignare.lista_asignari.readFromFile()
        assert content == [Asignare(Student(30, "Marin Stefania", 717), Problema(2, 3, "Management baza de date", d5)),
                           Asignare(Student(3, 'Alexandrescu Mihai', 917),
                                    Problema(2, 3, "Management baza de date", d5)),
                           Asignare(Student(3, 'Alexandrescu Mihai', 917), Problema(4, 1, "Cont bancar", d6))]

        repo_asignare.lista_asignari.stergere_asignare_file(p5, 0)
        content = repo_asignare.lista_asignari.readFromFile()
        assert content == [Asignare(Student(3, 'Alexandrescu Mihai', 917), Problema(4, 1, "Cont bancar", d6))]

        repo_asignare.lista_asignari.stergere_asignare_file(p6, 0)
        content = repo_asignare.lista_asignari.readFromFile()
        assert content == []

    def test_Enotare_asignare(self):
        # White-box testing pentru stergerea asignarilor din repository.

        s4 = Student(30, "Marin Stefania", 717)

        p4 = Problema(1, 7, "Programare dinamica", repo_problema.Data("06.07.2021"))
        p5 = Problema(2, 3, "Management baza de date", repo_problema.Data("02.12.2020"))
        p6 = Problema(4, 1, "Cont bancar", repo_problema.Data("09.01.2021"))

        repo_asignare.lista_asignari.notare_problema_file(s4, p4, 10)
        nota = repo_asignare.lista_asignari.readFromFile()[0].get_nota()
        assert nota == 10

        repo_asignare.lista_asignari.notare_problema_file(s4, p5, 7)
        nota = repo_asignare.lista_asignari.readFromFile()[1].get_nota()
        assert nota == 7

        repo_asignare.lista_asignari.notare_problema_file(repo_student.lista_stud.get_content()[1], p5, 9)
        nota = repo_asignare.lista_asignari.readFromFile()[2].get_nota()
        assert nota == 9

        repo_asignare.lista_asignari.notare_problema_file(repo_student.lista_stud.get_content()[1], p6, 3)
        nota = repo_asignare.lista_asignari.readFromFile()[3].get_nota()
        assert nota == 3


######################################################################################################################


def repo_main():
    unittest.main()
