from Services.srv_student import ServiceStudent
from Services.srv_problema import ServiceProblema
from Services.srv_asignari import ServiceAsignare
from Services.srv_statistici import ServiceStatistici

from Domain.student import Student
from Domain.problema import Problema

from Exceptions.exceptions import *

import Repository.repo_student as repo_student
import Repository.repo_problema as repo_problema
import Repository.repo_asignare as repo_asignare

import unittest

from Misc.utils import *


######################################################################################################################


class ATestServiceStudent(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_Asrv_adaugare_student(self):
        # White-box testing pentru service-ul de adaugare a studentilor.

        srv_student = ServiceStudent()
        srv_student.srv_adaugare_student("1, Popescu Alexandru, 213")
        assert repo_student.lista_stud.get_list() == [(1, 'Popescu Alexandru', 213)]

        srv_student.srv_adaugare_student("2, Antonovici Traian, 917")
        assert repo_student.lista_stud.get_list() == [(1, 'Popescu Alexandru', 213), (2, 'Antonovici Traian', 917)]

        srv_student.srv_adaugare_student("1024, Stefanescu Daniel, 319")
        assert repo_student.lista_stud.get_list() == [(1, 'Popescu Alexandru', 213), (2, 'Antonovici Traian', 917),
                                                      (1024, 'Stefanescu Daniel', 319)]

        self.assertRaises(IDError, srv_student.srv_adaugare_student, "-1, Alexandrescu Mihai, 918")
        self.assertRaises(NumeError, srv_student.srv_adaugare_student, "10, Alexandre7689scu t*tMihai, 218")
        self.assertRaises(GrupaError, srv_student.srv_adaugare_student, "18, Alautomotostivuitoresei Andrei, 0")
        self.assertRaises(IDUnicError, srv_student.srv_adaugare_student, "1, Alexandrovici Alexandru, 813")
        self.assertRaises(ParamError, srv_student.srv_adaugare_student, "1, Clarkson Jeremy")

    def test_Csrv_pre_modificare_student(self):
        srv_student = ServiceStudent()

        self.assertRaises(ExistentaError, srv_student.srv_pre_modificare_student, "10")
        self.assertRaises(IDError, srv_student.srv_pre_modificare_student, "0")
        self.assertRaises(IDError, srv_student.srv_pre_modificare_student, "-1")
        self.assertRaises(IDError, srv_student.srv_pre_modificare_student, "a")
        self.assertRaises(IDError, srv_student.srv_pre_modificare_student, "145atwe")

    def test_Dsrv_modificare_student(self):
        # White-box testing pentru service-ul de modificare a studentilor.

        srv_student = ServiceStudent()
        srv_student.srv_modificare_student(2, "3, Dna. Dr. Madalina Adam, 888")
        assert repo_student.lista_stud.get_list() == [(1, 'Popescu Alexandru', 213), (3, 'Dna. Dr. Madalina Adam', 888),
                                                      (1024, 'Stefanescu Daniel', 319)]

        srv_student.srv_modificare_student(1, "4, Amotostivuitoresei George, 991")
        assert repo_student.lista_stud.get_list() == [(4, 'Amotostivuitoresei George', 991),
                                                      (3, 'Dna. Dr. Madalina Adam', 888),
                                                      (1024, 'Stefanescu Daniel', 319)]

        srv_student.srv_modificare_student(1024, "100, Cabral, 100")
        assert repo_student.lista_stud.get_list() == [(4, 'Amotostivuitoresei George', 991),
                                                      (3, 'Dna. Dr. Madalina Adam', 888), (100, 'Cabral', 100)]

        self.assertRaises(IDError, srv_student.srv_modificare_student, 1, "-1, Alexandrescu Mihai, 918")
        self.assertRaises(NumeError, srv_student.srv_modificare_student, 1, "10, Alexandre7689scu t*tMihai, 218")
        self.assertRaises(GrupaError, srv_student.srv_modificare_student, 1, "18, Alautomotostivuitoresei Andrei, 0")
        self.assertRaises(IDUnicError, srv_student.srv_modificare_student, 1024, "4, Alexandrovici Alexandru, 813")
        self.assertRaises(ParamError, srv_student.srv_modificare_student, 100, "Hammond Richard, 715")

    def test_Esrv_stergere_student(self):
        # White-box testing pentru service-ul de stergere a studentilor.

        srv_student = ServiceStudent()

        self.assertRaises(IDError, srv_student.srv_stergere_student, -1)
        self.assertRaises(IDError, srv_student.srv_stergere_student, "a")
        self.assertRaises(IDError, srv_student.srv_stergere_student, 0)
        self.assertRaises(ExistentaError, srv_student.srv_stergere_student, 39)

        srv_student.srv_stergere_student(3)
        assert repo_student.lista_stud.get_list() == [(4, 'Amotostivuitoresei George', 991), (100, 'Cabral', 100)]

        srv_student.srv_stergere_student(4)
        assert repo_student.lista_stud.get_list() == [(100, 'Cabral', 100)]

        srv_student.srv_stergere_student(100)
        assert repo_student.lista_stud.get_list() == []

    def test_Bsrv_cautare_student_Black_Box(self):
        # Black-box testing pentru service-ul de cautare a problemelor: adaug cateva probleme, pentru
        # a putea cauta indiferent de problemele introduse mai sus, in white-box testing.

        repo_student.lista_stud.set_content([])

        srv_student = ServiceStudent()
        srv_student.srv_adaugare_student("1, Ionescu Alexandru, 213")
        srv_student.srv_adaugare_student("18, Popescu Andrei, 317")
        srv_student.srv_adaugare_student("420, Popovici Mihai, 919")

        assert srv_student.srv_cautare_student("1") == (1, "Ionescu Alexandru", 213)
        assert srv_student.srv_cautare_student("18") == (18, "Popescu Andrei", 317)
        assert srv_student.srv_cautare_student("420") == (420, "Popovici Mihai", 919)

        self.assertRaises(IDError, srv_student.srv_cautare_student, "-1")
        self.assertRaises(IDError, srv_student.srv_cautare_student, "b")
        self.assertRaises(IDError, srv_student.srv_cautare_student, "0")
        self.assertRaises(ExistentaError, srv_student.srv_cautare_student, "15")
        self.assertRaises(ExistentaError, srv_student.srv_cautare_student, "2")

        # Refacem content-ul dinaintea adaugarilor mele, pentru a merge restul testelor white-box.

        repo_student.lista_stud.set_content([Student(1, 'Popescu Alexandru', 213), Student(2, 'Antonovici Traian', 917),
                                             Student(1024, 'Stefanescu Daniel', 319)])


######################################################################################################################

class BTestServiceProblema(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_Asrv_adaugare_problema(self):
        # White-box testing pentru service-ul de adaugare a problemelor.

        srv_problema = ServiceProblema()

        srv_problema.srv_adaugare_problema("1, 1, Management cont bancar, 18.12.2020")
        dl1 = repo_problema.Data("18.12.2020")
        assert repo_problema.lista_prob.get_list() == [(1, 1, 'Management cont bancar', dl1)]

        srv_problema.srv_adaugare_problema("1, 2, Mersul trenurilor, 30.04.2021")
        dl2 = repo_problema.Data("30.04.2021")
        assert repo_problema.lista_prob.get_list() == [(1, 1, 'Management cont bancar', dl1),
                                                       (1, 2, 'Mersul trenurilor', dl2)]

        srv_problema.srv_adaugare_problema("2, 1, Problema grafuri, 24.11.2020")
        dl3 = repo_problema.Data("24.11.2020")
        assert repo_problema.lista_prob.get_list() == [(1, 1, 'Management cont bancar', dl1),
                                                       (1, 2, 'Mersul trenurilor', dl2),
                                                       (2, 1, 'Problema grafuri', dl3)]

        self.assertRaises(NrLabError, srv_problema.srv_adaugare_problema, "-3, 1, Management cont bancar, 18.12.2020")
        self.assertRaises(NrProbError, srv_problema.srv_adaugare_problema, "4, 0, Management cont bancar, 18.12.2020")
        self.assertRaises(DescrError, srv_problema.srv_adaugare_problema, "5, 4, , 18.12.2020")
        self.assertRaises(ParamError, srv_problema.srv_adaugare_problema, "6, 3,")
        self.assertRaises(ParamError, srv_problema.srv_adaugare_problema, "6, 3, Programare dinamica, 06.12.2020, aaa")
        self.assertRaises(ZiError, srv_problema.srv_adaugare_problema, "6, 3, Management cont bancar, 33.10.2021")
        self.assertRaises(LunaError, srv_problema.srv_adaugare_problema, "6, 3, Management cont bancar, 05.16.2020")
        self.assertRaises(AnError, srv_problema.srv_adaugare_problema, "6, 3, Management cont bancar, 30.10.1105")
        self.assertRaises(NrProbUnicError, srv_problema.srv_adaugare_problema, "2, 1, Mersul trenurilor, 05.04.2020")

    def test_Bsrv_cautare_problema_Black_Box(self):
        # Black-box testing pentru service-ul de cautare a problemelor: adaug cateva probleme, pentru
        # a putea cauta indiferent de problemele introduse mai sus, in white-box testing.

        repo_problema.lista_prob.set_content([])

        srv_problema = ServiceProblema()
        srv_problema.srv_adaugare_problema("1, 1, Cheltuieli de familie, 09.12.2020")
        srv_problema.srv_adaugare_problema("1, 2, Catalog studenti, 31.01.2021")
        srv_problema.srv_adaugare_problema("16, 27, Mersul trenurilor, 28.02.2021")

        assert srv_problema.srv_cautare_problema("1 1") == \
               (1, 1, 'Cheltuieli de familie', repo_problema.Data("09.12.2020"))

        assert srv_problema.srv_cautare_problema("1 2") == (1, 2, "Catalog studenti", repo_problema.Data("31.01.2021"))

        assert srv_problema.srv_cautare_problema("16 27") == \
               (16, 27, "Mersul trenurilor", repo_problema.Data("28.02.2021"))

        self.assertRaises(NrLabError, srv_problema.srv_cautare_problema, "-16 27")
        self.assertRaises(NrLabError, srv_problema.srv_cautare_problema, "0 27")
        self.assertRaises(NrLabError, srv_problema.srv_cautare_problema, "n 27")
        self.assertRaises(NrProbError, srv_problema.srv_cautare_problema, "16 -27")
        self.assertRaises(NrProbError, srv_problema.srv_cautare_problema, "16 0")
        self.assertRaises(NrProbError, srv_problema.srv_cautare_problema, "16 l")
        self.assertRaises(ParamError, srv_problema.srv_cautare_problema, "16")
        self.assertRaises(ParamError, srv_problema.srv_cautare_problema, "16 27 8")
        self.assertRaises(ParamError, srv_problema.srv_cautare_problema, "")
        self.assertRaises(ExistentaError, srv_problema.srv_cautare_problema, "4 5")
        self.assertRaises(ExistentaError, srv_problema.srv_cautare_problema, "7 5")

        # Refacem content-ul dinaintea adaugarilor mele, pentru a merge restul testelor white-box.

        repo_problema.lista_prob.set_content([Problema(1, 1, 'Management cont bancar',
                                                       repo_problema.Data("18.12.2020")),
                                              Problema(1, 2, 'Mersul trenurilor', repo_problema.Data("30.04.2021")),
                                              Problema(2, 1, 'Problema grafuri', repo_problema.Data("24.11.2020"))])

    def test_Csrv_pre_modificare_problema(self):
        srv_problema = ServiceProblema()

        self.assertRaises(ParamError, srv_problema.srv_pre_modificare_problema, "1")
        self.assertRaises(ParamError, srv_problema.srv_pre_modificare_problema, "1 5 6")
        self.assertRaises(NrLabError, srv_problema.srv_pre_modificare_problema, "-1 1")
        self.assertRaises(NrLabError, srv_problema.srv_pre_modificare_problema, "a 1")
        self.assertRaises(NrProbError, srv_problema.srv_pre_modificare_problema, "1 0")
        self.assertRaises(NrProbError, srv_problema.srv_pre_modificare_problema, "1 f")

    def test_Dsrv_modificare_problema(self):
        # White-box testing pentru service-ul de modificare a problemelor.

        srv_problema = ServiceProblema()
        dl1 = repo_problema.Data("18.12.2020")
        dl2 = repo_problema.Data("30.04.2021")

        srv_problema.srv_modificare_problema(2, 1, "2, 2, Algoritmica, 30.11.2020")
        dl3 = repo_problema.Data("30.11.2020")
        assert repo_problema.lista_prob.get_list() == [(1, 1, 'Management cont bancar', dl1),
                                                       (1, 2, 'Mersul trenurilor', dl2),
                                                       (2, 2, 'Algoritmica', dl3)]

        srv_problema.srv_modificare_problema(1, 1, "1, 17, Management biblioteca, 31.05.2021")
        dl4 = repo_problema.Data("31.05.2021")
        assert repo_problema.lista_prob.get_list() == [(1, 17, 'Management biblioteca', dl4),
                                                       (1, 2, 'Mersul trenurilor', dl2),
                                                       (2, 2, 'Algoritmica', dl3)]

        srv_problema.srv_modificare_problema(1, 2, "3, 4, Cheltuieli service auto, 06.06.2021")
        dl5 = repo_problema.Data("06.06.2021")
        assert repo_problema.lista_prob.get_list() == [(1, 17, 'Management biblioteca', dl4),
                                                       (3, 4, 'Cheltuieli service auto', dl5),
                                                       (2, 2, 'Algoritmica', dl3)]

        self.assertRaises(NrLabError, srv_problema.srv_modificare_problema, 2, 2, "-3, 1, Catalog studenti, 18.12.2020")
        self.assertRaises(NrProbError, srv_problema.srv_modificare_problema, 2, 2, "4, 0, Catalog studenti, 18.12.2020")
        self.assertRaises(DescrError, srv_problema.srv_modificare_problema, 2, 2, "5, 4, , 18.12.2020")
        self.assertRaises(ParamError, srv_problema.srv_modificare_problema, 2, 2, "6, 3,")
        self.assertRaises(ParamError, srv_problema.srv_modificare_problema, 2, 2, "6, 3, Algoritmica, 06.12.2020, aaa")
        self.assertRaises(ZiError, srv_problema.srv_modificare_problema, 2, 2, "6, 3, Catalog studenti, 33.10.2021")
        self.assertRaises(LunaError, srv_problema.srv_modificare_problema, 2, 2, "6, 3, Catalog studenti, 05.16.2020")
        self.assertRaises(AnError, srv_problema.srv_modificare_problema, 2, 2, "6, 3, Catalog studenti, 30.10.1105")
        self.assertRaises(NrProbUnicError, srv_problema.srv_modificare_problema, 2, 2, "3, 4, Algoritmica, 05.04.2020")

    def test_Esrv_stergere_problema(self):
        # White-box testing pentru service-ul de stergere a problemelor.

        srv_problema = ServiceProblema()

        self.assertRaises(NrLabError, srv_problema.srv_stergere_problema, "-2 3")
        self.assertRaises(NrProbError, srv_problema.srv_stergere_problema, "2 0")
        self.assertRaises(ParamError, srv_problema.srv_stergere_problema, "4257")
        self.assertRaises(ParamError, srv_problema.srv_stergere_problema, "4agh7")
        self.assertRaises(ExistentaError, srv_problema.srv_stergere_problema, "1 1")

        dl1 = repo_problema.Data("31.05.2021")
        dl2 = repo_problema.Data("06.06.2021")

        srv_problema.srv_stergere_problema("2 2")
        assert repo_problema.lista_prob.get_list() == [(1, 17, 'Management biblioteca', dl1),
                                                       (3, 4, 'Cheltuieli service auto', dl2)]

        srv_problema.srv_stergere_problema("3 4")
        assert repo_problema.lista_prob.get_list() == [(1, 17, 'Management biblioteca', dl1)]

        srv_problema.srv_stergere_problema("1 17")
        assert repo_problema.lista_prob.get_list() == []


######################################################################################################################


class CTestServiceAsignare(unittest.TestCase):

    def setUp(self):
        file = open("Date/test_asignari.txt", "w")
        file.write("")
        file.close()

        srv_student, srv_problema = ServiceStudent(), ServiceProblema()
        srv_student.srv_adaugare_student("1, Popescu Alexandru, 213")
        srv_student.srv_adaugare_student("2, Antonovici Traian, 917")

        srv_problema.srv_adaugare_problema("1, 1, Management cont bancar, 18.12.2020")
        srv_problema.srv_adaugare_problema("1, 2, Mersul trenurilor, 03.02.2021")
        srv_problema.srv_adaugare_problema("2, 1, Problema grafuri, 05.04.2021")

    def tearDown(self):
        file = open("Date/test_studenti.txt", "w")
        file.write("")
        file.close()

        file = open("Date/test_probleme.txt", "w")
        file.write("")
        file.close()

        repo_student.lista_stud.set_content([])
        repo_problema.lista_prob.set_content([])

    def test_Asrv_asignare_student(self):
        # White-box testing pentru service-ul de adaugare a asignarilor.

        srv_asignare = ServiceAsignare()

        srv_asignare.srv_asignare_problema(repo_student.lista_stud.get_content()[0], "1 1")
        asignare = repo_asignare.lista_asignari.get_content()[0]
        assert asignare.get_student().get_all() == (1, 'Popescu Alexandru', 213) \
               and asignare.get_problema().get_all_dl() == (1, 1, "Management cont bancar")

        srv_asignare.srv_asignare_problema(repo_student.lista_stud.get_content()[1], "1 2")
        asignare = repo_asignare.lista_asignari.get_content()[1]
        assert asignare.get_student().get_all() == (2, 'Antonovici Traian', 917) \
               and asignare.get_problema().get_all_dl() == (1, 2, 'Mersul trenurilor')

        srv_asignare.srv_asignare_problema(repo_student.lista_stud.get_content()[0], "2 1")
        asignare = repo_asignare.lista_asignari.get_content()[2]
        assert asignare.get_student().get_all() == (1, 'Popescu Alexandru', 213) \
               and asignare.get_problema().get_all_dl() == (2, 1, "Problema grafuri")

        srv_asignare.srv_asignare_problema(repo_student.lista_stud.get_content()[1], "1 1")
        asignare = repo_asignare.lista_asignari.get_content()[3]
        assert asignare.get_student().get_all() == (2, "Antonovici Traian", 917) \
               and asignare.get_problema().get_all_dl() == (1, 1, "Management cont bancar")

        studenti = repo_student.lista_stud.get_content()
        self.assertRaises(NrLabError, srv_asignare.srv_asignare_problema, studenti[1], "-1 1")
        self.assertRaises(NrProbError, srv_asignare.srv_asignare_problema, studenti[1], "1 0")
        self.assertRaises(ParamError, srv_asignare.srv_asignare_problema, studenti[1], "64")
        self.assertRaises(UnicitateAsignareError, srv_asignare.srv_asignare_problema, studenti[1], "1 2")

    def test_Bsrv_notare_student(self):
        # White-box testing pentru service-ul de notare a asignarilor.

        srv_asignare = ServiceAsignare()

        srv_asignare.srv_notare_problema(repo_student.lista_stud.get_content()[0], "1 1", 7)
        asignare = repo_asignare.lista_asignari.get_content()[0]
        assert asignare.get_nota() == 7

        srv_asignare.srv_notare_problema(repo_student.lista_stud.get_content()[1], "1 2", 9)
        asignare = repo_asignare.lista_asignari.get_content()[1]
        assert asignare.get_nota() == 9

        srv_asignare.srv_notare_problema(repo_student.lista_stud.get_content()[0], "2 1", 8)
        asignare = repo_asignare.lista_asignari.get_content()[2]
        assert asignare.get_nota() == 8

        srv_asignare.srv_notare_problema(repo_student.lista_stud.get_content()[1], "1 1", 3)
        asignare = repo_asignare.lista_asignari.get_content()[3]
        assert asignare.get_nota() == 3

        studenti = repo_student.lista_stud.get_content()
        self.assertRaises(NotaError, srv_asignare.srv_notare_problema, studenti[0], "1 1", 11)
        self.assertRaises(NotaError, srv_asignare.srv_notare_problema, studenti[0], "1 1", "aa")


######################################################################################################################

class DTestServiceStatistici(unittest.TestCase):

    def setUp(self):
        srv_student = ServiceStudent()
        srv_problema = ServiceProblema()
        srv_asignare = ServiceAsignare()

        file = open("Date/test_studenti.txt", "w")
        file.write("")
        file.close()

        file = open("Date/test_probleme.txt", "w")
        file.write("")
        file.close()

        file = open("Date/test_asignari.txt", "w")
        file.write("")
        file.close()

        repo_student.lista_stud.set_content([])
        repo_problema.lista_prob.set_content([])
        repo_asignare.lista_asignari.set_content([])

        srv_student.srv_adaugare_student("1, Popescu Alexandru, 213")
        srv_student.srv_adaugare_student("2, Antonovici Traian, 917")
        srv_student.srv_adaugare_student("3, Popovici Alina, 311")

        srv_problema.srv_adaugare_problema("1, 1, Management cont bancar, 18.12.2020")
        srv_problema.srv_adaugare_problema("1, 2, Mersul trenurilor, 03.02.2021")
        srv_problema.srv_adaugare_problema("2, 1, Problema grafuri, 05.04.2021")

        srv_asignare.srv_asignare_problema(repo_student.lista_stud.get_content()[0], "1 1")
        srv_asignare.srv_asignare_problema(repo_student.lista_stud.get_content()[0], "1 2")
        srv_asignare.srv_asignare_problema(repo_student.lista_stud.get_content()[1], "1 2")
        srv_asignare.srv_asignare_problema(repo_student.lista_stud.get_content()[1], "2 1")
        srv_asignare.srv_asignare_problema(repo_student.lista_stud.get_content()[2], "1 2")

        srv_asignare.srv_notare_problema(repo_student.lista_stud.get_content()[0], "1 1", 3)
        srv_asignare.srv_notare_problema(repo_student.lista_stud.get_content()[0], "1 2", 9)
        srv_asignare.srv_notare_problema(repo_student.lista_stud.get_content()[1], "1 2", 2)
        srv_asignare.srv_notare_problema(repo_student.lista_stud.get_content()[1], "2 1", 6)
        srv_asignare.srv_notare_problema(repo_student.lista_stud.get_content()[2], "1 2", 7)

        srv_asignare.srv_notare_problema(repo_student.lista_stud.get_content()[0], "1 2", 6)
        srv_asignare.srv_asignare_problema(repo_student.lista_stud.get_content()[0], "2 1")
        srv_asignare.srv_notare_problema(repo_student.lista_stud.get_content()[0], "2 1", 3)

    def tearDown(self):
        file = open("Date/test_asignari.txt", "w")
        file.write("")
        file.close()

        file = open("Date/test_studenti.txt", "w")
        file.write("")
        file.close()

        file = open("Date/test_probleme.txt", "w")
        file.write("")
        file.close()

        repo_student.lista_stud.set_content([])
        repo_problema.lista_prob.set_content([])
        repo_asignare.lista_asignari.set_content([])

    def test_srv_studenti_ordonat(self):
        srv_statistici = ServiceStatistici()

        stat = srv_statistici.srv_studenti_ordonati("1 2", 'cresc', 'a', 1)
        stud1, nota1, stud2, nota2 = stat[0].get_student(), stat[0].get_nota(), stat[1].get_student(), stat[
            1].get_nota()
        stud3, nota3 = stat[2].get_student(), stat[2].get_nota()

        assert stud1 == Student(2, "Antonovici Traian", 917) and nota1 == 2
        assert stud2 == Student(1, "Popescu Alexandru", 213) and nota2 == 6
        assert stud3 == Student(3, "Popovici Alina", 311) and nota3 == 7

        stat = srv_statistici.srv_studenti_ordonati("1 2", 'desc', 'n', 1)
        stud1, nota1, stud2, nota2 = stat[0].get_student(), stat[0].get_nota(), stat[1].get_student(), stat[
            1].get_nota()
        stud3, nota3 = stat[2].get_student(), stat[2].get_nota()

        assert stud3 == Student(2, 'Antonovici Traian', 917)
        assert nota3 == 2
        assert stud2 == Student(1, 'Popescu Alexandru', 213)
        assert nota2 == 6
        assert stud1 == Student(3, 'Popovici Alina', 311)
        assert nota1 == 7

        self.assertRaises(ParamError, srv_statistici.srv_studenti_ordonati, "34", 'desc', 'n', 1)
        self.assertRaises(NrLabError, srv_statistici.srv_studenti_ordonati, "a 4", 'desc', 'n', 1)
        self.assertRaises(NrProbError, srv_statistici.srv_studenti_ordonati, "3 -4", 'cresc', 'n', 1)
        self.assertRaises(ExistentaError, srv_statistici.srv_studenti_ordonati, "3 4", 'cresc', 'n', 1)

    def test_srv_medie_mica(self):
        srv_student = ServiceStudent()
        srv_statistici = ServiceStatistici()

        stat = srv_statistici.srv_medie_mica(1)
        stud1, nota1, stud2, nota2 = stat[0][0], stat[0][1], stat[1][0], stat[1][1]

        assert stud1 == Student(1, 'Popescu Alexandru', 213)
        assert nota1 == 4.0
        assert stud2 == Student(2, 'Antonovici Traian', 917)
        assert nota2 == 4.0

        srv_student.srv_stergere_student(2)
        srv_student.srv_stergere_student(1)
        stat = srv_statistici.srv_medie_mica(1)

        assert stat == []

    def test_srv_grupe_ordonate(self):
        srv_student = ServiceStudent()
        srv_statistici = ServiceStatistici()
        srv_asignare = ServiceAsignare()

        assert srv_statistici.srv_grupe_ordonate("cresc") == [(917, 2), (213, 3)]

        srv_student.srv_adaugare_student("4, Domnu Istvan, 917")
        srv_asignare.srv_asignare_problema(repo_student.lista_stud.get_content()[2], "1 1")
        srv_asignare.srv_notare_problema(repo_student.lista_stud.get_content()[2], "1 1", 3)

        assert srv_statistici.srv_grupe_ordonate("cresc") == [(311, 1), (917, 2), (213, 3)]

        srv_student.srv_stergere_student(1)
        assert srv_statistici.srv_grupe_ordonate("desc") == [(917, 2), (311, 1)]


######################################################################################################################


def srv_main():
    unittest.main()
