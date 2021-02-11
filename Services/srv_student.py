import Repository.repo_student as repo
import Repository.repo_asignare as repo_asignare

from Validators.validators import ValidatorStudent

from Domain.student import Student

from Exceptions.exceptions import *

import random
import string
######################################################################################################################


class ServiceStudent:
    def srv_adaugare_student(self, intrare):
        """
        Functia primeste un sir de caractere, il valideaza, si daca este totul in regula, prelucreaza datele si
        le trimite in repo pentru adaugare.

        :param intrare: Un sir de caractere care ar trebui sa fie datele de intrare pentru student.
        """

        validator_student = ValidatorStudent()

        try:
            validator_student.validare_student(intrare)

            param = intrare.split(", ")
            repo.lista_stud.validare_unicitate_stud_id(-1, param[0])

            stud_id, nume, grupa = param[0], param[1], param[2]
            student = Student(0, 0, 0)

            student.set_stud_id(stud_id)
            student.set_nume(nume)
            student.set_grupa(grupa)

            repo.lista_stud.adaugare_student_file(student)

        except IDError:
            raise IDError("ID-ul studentului este invalid! Introduceti alte date de intrare:")

        except NumeError:
            raise NumeError("Numele studentului este invalid! Introduceti alte date de intrare:")

        except GrupaError:
            raise GrupaError("Grupa studentului este invalida! Introduceti alte date de intrare:")

        except IDUnicError:
            raise IDUnicError("Exista deja un student cu acest ID! Introduceti alte date de intrare:")

        except ParamError:
            raise ParamError("Parametri insuficienti! Introduceti alte date de intrare:")

    def srv_stergere_student(self, stud_id):
        """
        Functia primeste un sir de caractere, il valideaza, si daca este totul in regula, prelucreaza datele si
        le trimite in repo pentru stergere.

        :param stud_id: Un sir de caractere, care ar trebui sa reprezinte ID-ul studentului ce trebuie eliminat.
        """

        validator_student = ValidatorStudent()

        try:
            validator_student.validare_stud_id(stud_id)

            stud_id = int(stud_id)
            index_student_gasit = repo.lista_stud.cautare_student(len(repo.lista_stud.get_content()) - 1, stud_id)

            if index_student_gasit == -1:
                raise ExistentaError

            repo_asignare.lista_asignari.stergere_asignare_file(repo.lista_stud.get_content()[index_student_gasit], 1)
            repo.lista_stud.stergere_student_file(index_student_gasit)

        except ValueError:
            raise IDError("ID invalid! Introduceti altul:")

        except IDError:
            raise IDError("ID invalid! Introduceti altul:")

        except ExistentaError:
            raise ExistentaError("Nu exista un student cu acest ID! Introduceti altul:")

    def srv_pre_modificare_student(self, stud_id):
        """
        Functia primeste un sir de caractere si il valideaza, pregatind ID-ul studentului pt modificare.

        :param stud_id: Un sir de caractere, care ar trebui sa reprezinte ID-ul studentului ce trebuie modificat.
        """

        validator_student = ValidatorStudent()

        try:
            validator_student.validare_stud_id(stud_id)

            stud_id = int(stud_id)
            try:
                repo.lista_stud.validare_unicitate_stud_id(-1, stud_id)
                raise ExistentaError

            except IDUnicError:
                pass

        except IDError:
            raise IDError("ID invalid! Introduceti altul:")

        except ExistentaError:
            raise ExistentaError("Nu exista un student cu acest ID! Introduceti altul:")

    def srv_modificare_student(self, stud_id, intrare):
        """
        Functia primeste ID-ul studentului ce trebuie modificat si noile date de intrare. Dupa ce se asigura validitatea
        datelor de intrare, functia prelucreaza datele si le trimite in repo pentru a fi modificate.

        :param stud_id: ID-ul studentului ce trebuie modificat, validat de functia de mai sus.
        :param intrare: Un sir de caractere ce ar trebui sa reprezinte noile date ale studentului.
        """

        validator_student = ValidatorStudent()
        stud_id = int(stud_id)

        try:
            validator_student.validare_student(intrare)

            param = intrare.split(", ")

            index_student_gasit = repo.lista_stud.cautare_student(len(repo.lista_stud.get_content()) - 1, stud_id)
            repo.lista_stud.validare_unicitate_stud_id(index_student_gasit, param[0])

            stud_id, nume, grupa = param[0], param[1], param[2]
            student = Student(0, 0, 0)

            student.set_stud_id(stud_id)
            student.set_nume(nume)
            student.set_grupa(grupa)

            repo_asignare.lista_asignari.modificare_asignare_file(repo.lista_stud.get_content()[index_student_gasit],
                                                                  student, 1)
            repo.lista_stud.modificare_student_file(index_student_gasit, student)

        except IDError:
            raise IDError("Noul ID al studentului este invalid! Introduceti alte date de intrare:")

        except NumeError:
            raise NumeError("Noul nume al studentului este invalid! Introduceti alte date de intrare:")

        except GrupaError:
            raise GrupaError("Noua grupa a studentului este invalida! Introduceti alte date de intrare:")

        except IDUnicError:
            raise IDUnicError("Exista deja un student cu acest ID! Introduceti alte date de intrare:")

        except ParamError:
            raise ParamError("Parametri insuficienti! Introduceti alte date de intrare:")

    def srv_cautare_student(self, intrare):
        """
        Functia primeste un sir de caractere, asigura validarea si daca totul este in regula, il prelucreaza si
        returneaza sub forma de tuple datele studentului din repo.

        :param intrare: Un sir de caractere ce ar trebui sa reprezinte ID-ul studentului cautat.
        """

        validator_student = ValidatorStudent()

        try:
            validator_student.validare_stud_id(intrare)

            stud_id = int(intrare)
            index_student_gasit = repo.lista_stud.cautare_student(len(repo.lista_stud.get_content()) - 1, stud_id)

            if index_student_gasit == -1:
                raise ExistentaError("Nu exista un student cu acest ID! Introduceti altul:")

            return repo.lista_stud.get_content()[index_student_gasit].get_all()

        except IDError:
            raise IDError("ID-ul introdus este invalid! Introduceti altul:")

    def srv_generare_student(self):
        """
        Functia genereaza datele unui student, ce sunt returnate mai departe functiei de jos (pt. validare).
        """

        stud_id = random.randint(1, 999)

        lista_litere = string.ascii_lowercase
        prenume = ''.join(random.choice(lista_litere) for i in range(10))
        nume_familie = ''.join(random.choice(lista_litere) for i in range(10))
        nume_intreg = str(prenume + " " + nume_familie)

        grupa = random.randint(100, 999)

        student = Student(stud_id, nume_intreg, grupa)

        return student

    def srv_solve_generare_student(self, intrare):
        """
        Functia primeste numarul de studenti ce trebuie generate, il valideaza, apoi apeleaza funciile de generare si
        validare de studenti, pana cand s-au generat destui studenti valizi, trimitand studentii valizi in repo pentru
        a fi adaugati.

        :param intrare: Un sir de caractere ce ar trebui sa reprezinte numarul de studenti ce trebuie sa fie generate.
        """

        validator_student = ValidatorStudent()

        try:
            intrare = int(intrare)
            if intrare < 1:
                raise ValueError

            studenti_corecti = 0
            while studenti_corecti < intrare:
                try:
                    student = self.srv_generare_student()

                    validator_student.validare_student_object(student)
                    repo.lista_stud.validare_unicitate_stud_id(-1, student.get_stud_id())

                    repo.lista_stud.adaugare_student_file(student)

                    studenti_corecti += 1

                except:
                    pass

        except ValueError:
            raise ValueError("Numarul de studenti ce trebuie generati este invalid! Introduceti altul: ")
