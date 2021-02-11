import Repository.repo_problema as repo
import Repository.repo_asignare as repo_asignare

from Exceptions.exceptions import *

from Domain.problema import Problema

from Validators.validators import ValidatorProblema

import random
import string
######################################################################################################################


class ServiceProblema:
    def to_printable_form(self, element):
        """

        :param element: Functia primeste un obiect de tip tuple si returneaza un string in
        forma printabila(user-friendly) cu datele acelui obiect.

        """

        printable_element = "(" + str(element[0]) + ", " + str(element[1]) + ", " + str(element[2]) + ", "
        printable_element += str(element[3].get_zi()) + "." + str(element[3].get_luna()) + "."
        printable_element += str(element[3].get_an()) + ")"

        return printable_element

    def srv_adaugare_problema(self, intrare):
        """
        Functia primeste un sir de caractere, il valideaza, si daca este totul in regula, prelucreaza datele si
        le trimite in repo pentru adaugare.

        :param intrare: Un sir de caractere care ar trebui sa fie datele de intrare pentru problema.
        """

        validator_problema = ValidatorProblema()

        try:
            validator_problema.validare_problema(intrare)

            param = intrare.split(", ")
            repo.lista_prob.validare_unicitate_nr_prob(-1, param[0], param[1])

            nr_lab, nr_prob, descr = param[0], param[1], param[2]
            deadline = repo.Data(param[3])
            problema = Problema(0, 0, 0, 0)

            problema.set_nr_lab(nr_lab)
            problema.set_nr_prob(nr_prob)
            problema.set_descr(descr)
            problema.set_deadline(deadline)

            repo.lista_prob.adaugare_problema_file(problema)

        except NrLabError:
            raise NrLabError("Numarul laboratorului este invalid! Introduceti alte date de intrare:")

        except NrProbError:
            raise NrProbError("Numarul problemei este invalid! Introduceti alte date de intrare:")

        except DescrError:
            raise DescrError("Descrierea problemei este invalida! Introduceti alte date de intrare:")

        except DeadlineError:
            raise DeadlineError("Formatul deadline-ului problemei este invalid! Introduceti alte date de intrare:")

        except ZiError:
            raise ZiError("Ziua deadline-ului este invalida! Introduceti alte date de intrare:")

        except LunaError:
            raise LunaError("Luna deadline-ului este invalida! Introduceti alte date de intrare:")

        except AnError:
            raise AnError("Anul deadline-ului este invalid! Introduceti alte date de intrare:")

        except NrProbUnicError:
            raise NrProbUnicError(
                "Exista deja o problema cu acest numar la laboratorul acesta! Introduceti alte date de intrare:")

        except ParamError:
            raise ParamError("Parametri insuficienti! Introduceti alte date de intrare:")

        except ValueError:
            raise ValueError("Date de intrare invalide! Introduceti altele:")

    def srv_stergere_problema(self, intrare):
        """
        Functia primeste un sir de caractere, il valideaza, si daca este totul in regula, prelucreaza datele si
        le trimite in repo pentru stergere.

        :param intrare: Un sir de caractere, care ar trebui sa reprezinte numarul laboratorului si al problemei ce
        trebuie sa fie eliminata.
        """

        validator_problema = ValidatorProblema()

        try:
            validator_problema.validare_cautare_problema(intrare)

            param = intrare.split(" ")
            nr_lab, nr_prob = int(param[0]), int(param[1])

            index_problema_gasita = repo.lista_prob.cautare_problema(len(repo.lista_prob.get_content()) - 1, nr_lab, nr_prob)

            if index_problema_gasita == -1:
                raise ExistentaError

            repo_asignare.lista_asignari.stergere_asignare_file(repo.lista_prob.get_content()[index_problema_gasita], 0)
            repo.lista_prob.stergere_problema_file(index_problema_gasita)

        except NrLabError:
            raise NrLabError("Numarul laboratorului introdus este invalid! Introduceti alte date de intrare:")

        except NrProbError:
            raise NrProbError("Numarul problemei introduse este invalid! Introduceti alte date de intrare:")

        except ParamError:
            raise ParamError("Nu s-au introdus doua numere! Introduceti alte date de intrare:")

        except ExistentaError:
            raise ExistentaError(
                "Nu exista o problema cu acest numar la laboratorul dat! Introduceti alte date de intrare:")

    def srv_pre_modificare_problema(self, intrare):
        """
        Functia primeste un sir de caractere si il valideaza, pregatind numarul laboratorului si al problemei
        pentru modificare.

        :param intrare: Un sir de caractere, care ar trebui sa reprezinte ID-ul numarul laboratorului si numarul
        problemei ce trebuie modificata.
        """

        validator_problema = ValidatorProblema()

        try:
            validator_problema.validare_cautare_problema(intrare)

            param = intrare.split(" ")
            nr_lab, nr_prob = int(param[0]), int(param[1])
            try:
                repo.lista_prob.validare_unicitate_nr_prob(-1, nr_lab, nr_prob)
                raise ExistentaError

            except NrProbUnicError:
                pass

            return nr_lab, nr_prob

        except NrLabError:
            raise NrLabError("Numarul laboratorului introdus este invalid! Introduceti alte date de intrare:")

        except NrProbError:
            raise NrProbError("Numarul problemei introduse este invalid! Introduceti alte date de intrare:")

        except ParamError:
            raise ParamError("Nu s-au introdus doua numere! Introduceti alte date de intrare:")

        except ExistentaError:
            raise ExistentaError(
                "Nu exista o problema cu acest numar la laboratorul dat! Introduceti alte date de intrare:")

    def srv_modificare_problema(self, nr_lab, nr_prob, intrare):
        """
        Functia primeste nr. laboratorlui si al problemei ce trebuie modificata si noile date de intrare. Dupa ce se
        asigura validitatea datelor de intrare, functia prelucreaza datele si le trimite in repo pentru a fi modificate.

        :param nr_lab: Numarul laboratorului din care face parte problema ce trebuie modificat, validat mai sus.
        :param nr_prob: Numarul problemei ce trebuie modificata, validat de functia de mai sus.
        :param intrare: Un sir de caractere ce ar trebui sa reprezinte noile date ale problemei.
        """

        validator_problema = ValidatorProblema()

        try:
            validator_problema.validare_problema(intrare)

            param = intrare.split(", ")

            index_problema_gasita = repo.lista_prob.cautare_problema(
                len(repo.lista_prob.get_content()) - 1, nr_lab, nr_prob)

            repo.lista_prob.validare_unicitate_nr_prob(index_problema_gasita, param[0], param[1])

            nr_lab, nr_prob, descr = param[0], param[1], param[2]
            deadline = repo.Data(param[3])
            problema = Problema(0, 0, 0, 0)

            problema.set_nr_lab(nr_lab)
            problema.set_nr_prob(nr_prob)
            problema.set_descr(descr)
            problema.set_deadline(deadline)

            repo_asignare.lista_asignari.modificare_asignare_file(repo.lista_prob.get_content()[index_problema_gasita],
                                                                  problema, 0)
            repo.lista_prob.modificare_problema_file(index_problema_gasita, problema)

        except NrLabError:
            raise NrLabError("Noul numar al laboratorului este invalid! Introduceti alte date de intrare:")

        except NrProbError:
            raise NrProbError("Noul numar al problemei este invalid! Introduceti alte date de intrare:")

        except DescrError:
            raise DescrError("Noua descriere a problemei este invalida! Introduceti alte date de intrare:")

        except DeadlineError:
            raise DeadlineError("Noul format al deadline-ului este invalid! Introduceti alte date de intrare:")

        except ZiError:
            raise ZiError("Noua zi a deadline-ului este invalida! Introduceti alte date de intrare:")

        except LunaError:
            raise LunaError("Noua luna a deadline-ului este invalida! Introduceti alte date de intrare:")

        except AnError:
            raise AnError("Noul an al deadline-ului este invalid! Introduceti alte date de intrare:")

        except NrProbUnicError:
            raise NrProbUnicError(
                "Exista deja o problema cu acest numar la laboratorul acesta! Introduceti alte date de intrare:")

        except ParamError:
            raise ParamError("Noii parametri sunt insuficienti! Introduceti alte date de intrare:")

        except ValueError:
            raise ValueError("Noile date de intrare sunt invalide! Introduceti altele:")

    def srv_cautare_problema(self, intrare):
        """
        Functia primeste un sir de caractere, asigura validarea si daca totul este in regula, il prelucreaza si
        returneaza sub forma de tuple datele problemei din repo.

        :param intrare: Un sir de caractere ce ar trebui sa reprezinte numarul laboratorului si al problemei ce
        trebuie cautata.
        """

        validator_problema = ValidatorProblema()

        try:
            validator_problema.validare_cautare_problema(intrare)

            param = intrare.split(" ")
            nr_lab, nr_prob = int(param[0]), int(param[1])

            index_problema_gasita = repo.lista_prob.cautare_problema(
                len(repo.lista_prob.get_content()) - 1, nr_lab, nr_prob)

            if index_problema_gasita == -1:
                raise ExistentaError(
                    "Nu exista o problema cu acest numar la laboratorul dat! Introduceti alte date de intrare:")

            return repo.lista_prob.get_content()[index_problema_gasita].get_all()

        except NrLabError:
            raise NrLabError("Numarul laboratorului introdus este invalid! Introduceti alte date de intrare:")

        except NrProbError:
            raise NrProbError("Numarul problemei introduse este invalid! Introduceti alte date de intrare:")

        except ParamError:
            raise ParamError("Nu s-au introdus doua numere! Introduceti alte date de intrare:")

    def srv_generare_problema(self):
        """
        Functia genereaza datele unei probleme, ce sunt returnate mai departe functiei de jos (pt. validare).
        """

        nr_lab = random.randint(1, 99)
        nr_prob = random.randint(1, 99)

        lista_litere = string.ascii_lowercase
        descriere = ''.join(random.choice(lista_litere) for i in range(20))

        zi = random.randint(1, 31)
        luna = random.randint(1, 12)
        an = random.randint(2020, 2023)

        deadline_string = ""
        if zi < 10:
            deadline_string += "0"
        deadline_string += str(zi) + "."

        if luna < 10:
            deadline_string += "0"
        deadline_string += str(luna) + "." + str(an)

        deadline = repo.Data(deadline_string)
        problema = Problema(nr_lab, nr_prob, descriere, deadline)

        return problema

    def srv_solve_generare_problema(self, intrare):
        """
        Functia primeste numarul de probleme ce trebuie generate, il valideaza, apoi apeleaza funciile de generare si
        validare de probleme, pana cand s-au generat destule probleme valide, trimitand problemele valide in repo pentru
        a fi adaugate.

        :param intrare: Un sir de caractere ce ar trebui sa reprezinte numarul de probleme ce trebuie sa fie generate.
        """
        validator_problema = ValidatorProblema()

        try:
            intrare = int(intrare)
            if intrare < 1:
                raise ValueError

            probleme_corecte = 0
            while probleme_corecte < intrare:
                try:
                    problema = self.srv_generare_problema()

                    validator_problema.validare_problema_object(problema)
                    repo.lista_prob.validare_unicitate_nr_prob(-1, problema.get_nr_lab(), problema.get_nr_prob())

                    repo.lista_prob.adaugare_problema(problema)

                    probleme_corecte += 1

                except:
                    pass

        except ValueError:
            raise ValueError("Numarul de studenti ce trebuie generati este invalid! Introduceti altul: ")
