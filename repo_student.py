from Exceptions.exceptions import IDUnicError
from Domain.student import Student


class ListaStud:
    def __init__(self, content):
        self.__content = content
        self.__length = len(content)

    def get_content(self):
        return self.__content

    def get_tuple(self, index):
        return self.__content[index].get_stud_id(), self.__content[index].get_nume(), self.__content[index].get_grupa()

    def get_element(self, element):
        return self.__content[element]

    def get_length(self):
        return len(self.__content)

    def get_list(self):
        content = self.__content
        length = len(content)

        lista = []
        for i in range(0, length):
            lista.append((content[i].get_stud_id(), content[i].get_nume(), content[i].get_grupa()))

        return lista

    """def print_content(self):
        length = len(self.__content)

        for i in range(0, length):
            print(i, ":", end=" ")
            print(lista_stud.get_element(i))"""

    def get_printable_content(self):
        content = self.__content
        length = len(content)

        printable_lista_stud = ""

        for i in range(0, length):
            printable_lista_stud += str(i) + ": (ID: " + str(content[i].get_stud_id()) + ", Nume: "
            printable_lista_stud += str(content[i].get_nume()) + ", Grupa: " + str(content[i].get_grupa()) + ")\n"

        return printable_lista_stud

    """def get_printable_content(self, lista, index):
        if index == 0:
            print(lista[0])

        else:
            printare(lista, index - 1)
            print(lista[index])"""

    def set_content(self, content):
        self.__content = content

    """def content_to_text(self):
        content = self.__content
        length = len(content)

        text = ""
        for i in range(0, length):
            student = content[i]
            text += str(student.get_stud_id()) + ", " + student.get_nume() + ", " + str(student.get_grupa()) + "\n"

        return text"""

    def content_to_text(self, index=0):
        content = self.__content
        length = len(content)

        text = ""
        for i in range(0, length):
            student = content[i]
            text += str(student.get_stud_id()) + ", " + student.get_nume() + ", " + str(student.get_grupa()) + "\n"

        return text

    def adaugare_student(self, student: Student):
        """
        Functia adauga studentul dat in lista.

        :param student: Studentul ce trebuie sa fie adaugat.
        """

        self.__content.append(student)

    def stergere_student(self, index):
        """
        Functia sterge studentul din lista, dupa un index dat.

        :param index: Indexul studentului care va fi sters.
        """

        new_content = self.__content
        new_content.pop(index)

        self.__content = new_content

    def modificare_student(self, index, student_nou: Student):
        """
        Functia modifica studentul din lista dupa un anumit index, cu un student nou.

        :param index: Indexul studentului ce trebuie modificat.
        :param student_nou: Datele studentului nou (un obiect de tip Student).
        """

        new_content = self.__content
        new_content[index] = student_nou

        self.__content = new_content

    '''def cautare_student(self, stud_id):
        """
        Functia cauta studentul in lista, dupa ID.

        :param stud_id: ID-ul dupa care se va efectua cautarea.
        """

        content = self.__content
        length = len(content)

        index = -1
        for i in range(0, length):
            if content[i].get_stud_id() == stud_id:
                index = i
                break

        return index'''

    def cautare_student(self, index, stud_id):
        """
        Functia cauta studentul in mod recursiv in lista, dupa ID.

        :param index: Indexul curent al studentului din lista.
        :param stud_id: ID-ul dupa care se va efectua cautarea.

        Complexitatea acestei functii este:

            - caz defavorail: Theta(n) (Elementul cautat este pe prima pozitie in lista)
            - caz favorabil: Theta(1) (Elementul cautat este pe ultima pozitie in lista)
            - caz mediu: Theta(n)
            - overall time complexity: O(n)

        """

        content = self.__content
        if index == 0:
            if stud_id == content[index].get_stud_id():
                return index
            else:
                return -1

        else:
            if stud_id == content[index].get_stud_id():
                return index
            else:
                return self.cautare_student(index - 1, stud_id)

    def asignare_problema(self, index, problema):
        """
        Functia asigneaza problema data studentului cu indexul dat.

        :param index: Indexul studentului caruia trebuie sa ii fie asignata problema.
        :param problema: Problema ce trebuie sa fie asignata studentului.
        """

        student = self.__content[index]
        student.assign(problema)

        self.__content[index] = student

    def notare_problema(self, index, problema, nota):
        """
        Functia noteaza problema data studentului cu indexul dat cu nota data.

        :param index: Indexul studentului caruia trebuie sa ii fie notata problema.
        :param problema: Problema ce este asignata studentului.
        :param nota: Nota cu care trebuie sa fie notata problema studentului.
        """

        student = self.__content[index]
        student.notare(problema, nota)

        self.__content[index] = student


class ListaStudFile(ListaStud):
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
            param = line.split(", ")

            if len(param) == 3:
                content.append(Student(int(param[0]), param[1], int(param[2])))

            line = file.readline()

        file.close()
        return content

    def __writeToFile(self, text):
        file = open(self.__path, "w")
        file.write(text)
        file.close()

    def adaugare_student_file(self, student: Student):
        super().adaugare_student(student)

        text = self.content_to_text()
        self.__writeToFile(text)

    def stergere_student_file(self, index):
        super().stergere_student(index)

        text = self.content_to_text()
        self.__writeToFile(text)

    def modificare_student_file(self, index, student_nou: Student):
        super().modificare_student(index, student_nou)

        text = self.content_to_text()
        self.__writeToFile(text)

    """def validare_unicitate_stud_id(self, index, stud_id):
        content = self.get_content()
        length = len(content)
        stud_id = int(stud_id)

        try:
            for i in range(0, length):
                if content[i].get_stud_id() == stud_id and i != index:
                    raise IDUnicError

        except:
            raise IDUnicError"""

    def validare_unicitate_stud_id(self, index, stud_id, curent=0):
        if curent == len(self.get_content()):
            return

        else:
            stud_id = int(stud_id)

            try:
                if self.get_content()[curent].get_stud_id() == stud_id and curent != index:
                    raise IDUnicError

                self.validare_unicitate_stud_id(index, stud_id, curent + 1)
            except:
                raise IDUnicError


lista_stud = ListaStudFile([], "Date/test_studenti.txt")
