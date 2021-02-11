import Repository.repo_asignare as repo
import Repository.repo_student as repo_student
import Repository.repo_problema as repo_problema

from Domain.asignare import Asignare

from Validators.validators import ValidatorStudent, ValidatorProblema

from Exceptions.exceptions import *

######################################################################################################################


class ServiceAsignare:
    def srv_pre_asignare_problema(self, intrare):
        """
        Functia primeste sirul de caractere cu ID-ul studentului, asigura validitatea lui si il trimite in repo pentru
        a fi cautat.

        :param intrare: Un sir de caractere ce ar trebui sa fie ID-ul studentului.
        """

        validator_student = ValidatorStudent()

        try:
            validator_student.validare_stud_id(intrare)
            stud_id = int(intrare)

            index_student_gasit = repo_student.lista_stud.cautare_student(
                len(repo_student.lista_stud.get_content() - 1), stud_id)

            student = repo_student.lista_stud.get_content()[index_student_gasit]
            if index_student_gasit == -1:
                raise ExistentaError

            return student

        except IDError:
            raise IDError("ID-ul introdus este invalid! Introduceti altul:")

        except ExistentaError:
            raise ExistentaError("Nu exista un student cu acest ID! Introduceti altul:")

    def srv_asignare_problema(self, student, intrare):
        """
        Functia primeste studentul deja validat si datele problemei ce trebuie sa ii fie asignata. Functia va asigura
        validitatea datelor problemei si va trimite in repo studentul si problema pentru asignare.

        :param student: Studentul caruia trebuie sa ii fie asignata problema.
        :param intrare: Un sir de caractere ce ar trebui sa reprezinte nr. laboratorului si al problemei ce trebuie
        asignata.
        """

        validator_problema = ValidatorProblema()
        try:
            validator_problema.validare_cautare_problema(intrare)

            param = intrare.split(" ")
            nr_lab, nr_prob = int(param[0]), int(param[1])

            index_problema_gasita = repo_problema.lista_prob.cautare_problema(
                len(repo_problema.lista_prob.get_content()) - 1, nr_lab, nr_prob)

            problema = repo_problema.lista_prob.get_content()[index_problema_gasita]

            repo.lista_asignari.validare_asignare_problema(student, problema)

            asignare = Asignare(student, problema)
            repo.lista_asignari.adaugare_asignare_file(asignare)

        except NrLabError:
            raise NrLabError("Numarul laboratorului introdus este invalid! Introduceti alte date de intrare:")

        except NrProbError:
            raise NrProbError("Numarul problemei introduse este invalid! Introduceti alte date de intrare:")

        except ParamError:
            raise ParamError("Nu s-au introdus doua numere! Introduceti alte date de intrare:")

        except UnicitateAsignareError:
            raise UnicitateAsignareError("Problema aceasta este deja asignata! Introduceti alte date de intrare:")

    def srv_pre_notare_problema(self, student, intrare):
        """
        Functia primeste studentul deja validat si un string ce reprezinta problema ce trebuie notata si asigura
        validitatea datelor problemei.

        :param student: Studentul care trebuie sa fie notat.
        :param intrare: Un string ce reprezinta numarul laboratorului si al problemei ce trebuie notata.
        """
        try:
            repo.lista_asignari.validare_cautare_problema_asignata(student, intrare)

        except ParamError:
            raise ParamError("Nu s-au introdus doua numere! Introduceti alte date de intrare:")

        except NotareError:
            raise NotareError("Studentul ales nu are asignata aceasta problema! Introduceti alte date de intrare:")

        except ValueError:
            raise ValueError("Datele problemei introduse sunt invalide! Introduceti alte date de intrare:")

    def srv_notare_problema(self, student, intrare, intrare2):
        """
        Functia primeste un student si string-ul cu datele problemei (deja validate) ce trebuiesc prelucrate, dar si
        nota care, dupa asigurarea validitatii, va fi asignata studentului la problema data.

        :param student: Studentul caruia trebuie sa ii fie notata problema.
        :param intrare: Datele problemei ce trebuie sa fie notata.
        :param intrare2: Nota problemei ce trebuie adaugata problemei.
        """

        validator_student = ValidatorStudent()

        try:
            validator_student.validare_nota(intrare2)
            nota = int(intrare2)

            param = intrare.split(" ")
            nr_lab, nr_prob = int(param[0]), int(param[1])
            problema = repo.lista_asignari.cautare_problema(nr_lab, nr_prob)

            repo.lista_asignari.notare_problema_file(student, problema, nota)

        except NotaError:
            raise NotaError("Nota introdusa este invalida! Introduceti alta:")

