from Domain.student import Student
from Domain.asignare import Asignare
from Domain.problema import Problema

from Repository.repo_problema import Data

from Exceptions.exceptions import ParamError, NotareError, UnicitateAsignareError

from Misc.utils import qSort_generic, cmp_generic_nota, cmp_generic_nume

######################################################################################################################


class ListaAsignari:
    def __init__(self, content):
        self.__content = content

    def get_content(self):
        return self.__content

    def get_length(self):
        return len(self.__content)

    def get_element(self, element):
        return self.__content[element]

    def get_nr_probleme(self, student):
        content = self.__content
        length = len(content)

        nr_probleme = 0
        for i in range(0, length):
            if content[i].get_student() == student:
                nr_probleme += 1

        return nr_probleme

    def get_probleme_from_student(self, student):
        string = ""
        content = self.__content
        length = len(content)

        for i in range(0, length):
            if content[i].get_student() == student:
                problema = content[i].get_problema()
                dl = problema.get_deadline()

                string += "(" + str(problema.get_nr_lab()) + ", " + str(problema.get_nr_prob()) + ", "
                string += str(problema.get_descr()) + "), cu nota: " + str(content[i].get_nota()) + ".\n"

        return string

    def validare_cautare_problema_asignata(self, student, intrare):
        try:
            param = intrare.split(" ")
            if len(param) != 2:
                raise ParamError

            content = self.__content
            length = len(content)

            nr_lab = int(param[0])
            nr_prob = int(param[1])

            ok = 0
            for i in range(0, length):
                if content[i].get_student() == student:
                    problema = content[i].get_problema()
                    if problema.get_nr_lab() == nr_lab and problema.get_nr_prob() == nr_prob:
                        ok = 1

            if not ok:
                raise NotareError

        except ParamError:
            raise ParamError

        except NotareError:
            raise NotareError

        except ValueError:
            raise ValueError

    def get_studenti_dupa_problema(self, nr_lab, nr_prob):
        content = self.__content
        length = len(content)

        lista = []
        for i in range(0, length):
            problema = content[i].get_problema()
            if problema.get_nr_lab() == nr_lab and problema.get_nr_prob() == nr_prob:
                lista.append(content[i])

        return lista

    def ordonare_alfabetica(self, nr_lab, nr_prob, rev):
        lista = self.get_studenti_dupa_problema(nr_lab, nr_prob)

        lista_sortata = qSort_generic(lista, cmp_generic_nume, rev)

        return lista_sortata

    def ordonare_nota(self, nr_lab, nr_prob, rev):
        lista = self.get_studenti_dupa_problema(nr_lab, nr_prob)

        lista_sortata = qSort_generic(lista, cmp_generic_nota, rev)

        return lista_sortata

    def set_content(self, content):
        self.__content = content

    def content_to_text(self):
        content = self.__content
        length = len(content)

        text = ""
        for i in range(0, length):
            student = content[i].get_student()
            problema = content[i].get_problema()
            deadline = problema.get_deadline()
            nota = content[i].get_nota()

            text += str(student.get_stud_id()) + ", " + student.get_nume() + ", " + str(student.get_grupa()) + "; "
            text += str(problema.get_nr_lab()) + ", " + str(problema.get_nr_prob()) + ", " + problema.get_descr()
            text += ", " + str(deadline.get_zi()) + "." + str(deadline.get_luna()) + "." + str(deadline.get_an()) + "; "
            text += str(nota) + "\n"

        return text

    def adaugare_asignare(self, asignare):
        self.__content.append(asignare)

    def stergere_asignare(self, obiect, dupa_student):
        content = self.__content
        length = len(content)
        new_content = []

        for i in range(0, length):
            if dupa_student == 0:
                if content[i].get_problema() != obiect:
                    new_content.append(content[i])
            else:
                if content[i].get_student() != obiect:
                    new_content.append(content[i])

        self.__content = new_content

    def modificare_asignare(self, old, new, dupa_student):
        content = self.__content
        length = len(content)

        for i in range(0, length):
            if dupa_student == 0:
                if content[i].get_problema() == old:
                    content[i].set_problema(new)
            else:
                if content[i].get_student() == old:
                    content[i].set_student(new)

        self.__content = content

    def notare_problema(self, student, problema, nota):
        content = self.__content
        length = len(content)

        for i in range(0, length):
            if student == content[i].get_student():
                if problema == content[i].get_problema():
                    content[i].set_nota(nota)

    def cautare_problema(self, nr_lab, nr_prob):
        content = self.__content
        length = len(content)

        for i in range(0, length):
            if content[i].get_problema().get_nr_lab() == nr_lab and content[i].get_problema().get_nr_prob() == nr_prob:
                return content[i].get_problema()

        return -1

    def validare_asignare_problema(self, student, problema):
        content = self.__content
        length = len(content)

        for i in range(0, length):
            if content[i].get_student() == student:
                if content[i].get_problema() == problema:
                    raise UnicitateAsignareError

    def get_printable_content(self):
        content = self.__content
        length = len(content)

        string = ""
        for i in range(0, length):
            student = content[i].get_student()
            problema = content[i].get_problema()

            string += str(i) + ") Studentul: (ID: " + str(student.get_stud_id()) + ", Nume: " + str(student.get_nume())
            string += ", Grupa: " + str(student.get_grupa()) + ") are asignata problema: (Nr. lab.: "
            string += str(problema.get_nr_lab()) + ", Nr. prob.: " + str(problema.get_nr_prob()) + ", Descriere: "
            string += problema.get_descr() + ")\n"

        return string

    def __get_medie_from_student(self, student: Student):
        content = self.__content
        length = len(content)

        suma = 0
        nr_note = 0
        for i in range(0, length):
            if student == content[i].get_student():
                suma += content[i].get_nota()
                nr_note += 1

        return suma / nr_note

    def get_asignari_medie(self):
        content = self.__content
        length = len(content)

        studenti_inclusi = []
        lista_medii = []
        for i in range(0, length):
            if content[i].get_student() not in studenti_inclusi:
                medie = self.__get_medie_from_student(content[i].get_student())
                lista_medii.append([content[i].get_student(), medie])

                studenti_inclusi.append(content[i].get_student())

        return lista_medii

    def get_asignari_grupa(self):
        content = self.__content
        length = len(content)

        lista = {}
        for i in range(0, length):
            grupa = content[i].get_student().get_grupa()
            try:
                x = lista[grupa]

                if content[i].get_nota() < 7 and content[i].get_nota() != 0:
                    lista[grupa] += 1

            except KeyError:    # Daca inca nu avem date pt. grupa asta:
                lista[grupa] = 0
                if content[i].get_nota() < 7 and content[i].get_nota() != 0:
                    lista[grupa] += 1

        lista_tuple = []
        for key in lista.keys():
            if lista[key] != 0:
                lista_tuple.append((key, lista[key]))

        return lista_tuple

    def get_tuple_content(self):
        content = self.__content
        length = len(content)

        new_content = []
        for i in range(0, length):
            student = content[i].get_student().get_all()
            problema = content[i].get_problema().get_all_dl()
            new_content.append((student, problema))

        return new_content


class ListaAsignariFile(ListaAsignari):
    def __init__(self, content, path):
        super().__init__(content)

        self.__path = path
        self.set_content(self.readFromFile())

    def get_path(self):
        return self.__path

    def set_path(self, path):
        self.__path = path
        self.set_content(self.readFromFile())

    def readFromFile(self):
        content = []
        file = open(self.__path, "r")

        line = file.readline()
        while line:
            line = line.strip()
            param = line.split("; ")

            if len(param) == 3:
                student = param[0].split(", ")
                problema = param[1].split(", ")
                nota = param[2]

                asignare = Asignare(Student(int(student[0]), student[1], int(student[2])),
                                    Problema(int(problema[0]), int(problema[1]), problema[2], Data(problema[3])))

                asignare.set_nota(int(nota))

                content.append(asignare)

            line = file.readline()

        file.close()
        return content

    def __writeToFile(self, text):
        file = open(self.__path, "w")
        file.write(text)
        file.close()

    def adaugare_asignare_file(self, asignare: Asignare):
        super().adaugare_asignare(asignare)

        text = self.content_to_text()
        self.__writeToFile(text)

    def notare_problema_file(self, student, problema, nota):
        super().notare_problema(student, problema, nota)

        text = self.content_to_text()
        self.__writeToFile(text)

    def stergere_asignare_file(self, obiect, dupa_student):
        super().stergere_asignare(obiect, dupa_student)

        text = self.content_to_text()
        self.__writeToFile(text)

    def modificare_asignare_file(self, old, new, dupa_student):
        super().modificare_asignare(old, new, dupa_student)

        text = self.content_to_text()
        self.__writeToFile(text)


lista_asignari = ListaAsignariFile([], "Date/test_asignari.txt")
