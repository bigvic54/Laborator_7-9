from Exceptions.exceptions import NrProbUnicError

from Domain.problema import Problema

######################################################################################################################


class ListaProb:
    def __init__(self, content):
        self.__content = content
        self.__length = len(content)

    def get_content(self):
        return self.__content

    def get_element(self, element):
        return self.__content[element]

    def get_length(self):
        return len(self.__content)

    def get_list(self):
        content = self.__content
        length = len(content)

        lista = []
        for i in range(0, length):
            lista.append((content[i].get_nr_lab(), content[i].get_nr_prob(), content[i].get_descr(),
                          content[i].get_deadline()))

        return lista

    def print_content(self):
        length = lista_prob.get_length()

        for i in range(0, length):
            print(i, ":", end=" ")

            problema = self.__content[i]
            deadline = problema[3]
            zi, luna, an = deadline.get_content()

            print(problema[0], end="")
            print(",", problema[1], end="")
            print(",", problema[2], end="")
            print(",", zi, end=".")
            print(luna, end=".")
            print(an)

    def get_printable_content(self):
        content = self.__content
        length = len(content)

        printable_lista_prob = ""
        for i in range(0, length):
            printable_lista_prob += str(i) + ": (Nr. laborator: " + str(content[i].get_nr_lab()) + ", Nr. problema: "
            printable_lista_prob += str(content[i].get_nr_prob()) + ", Descriere: " + str(content[i].get_descr())
            printable_lista_prob += ", Deadline: " + str(content[i].get_deadline().get_zi()) + "."
            printable_lista_prob += str(content[i].get_deadline().get_luna()) + "."
            printable_lista_prob += str(content[i].get_deadline().get_an()) + ")\n"

        return printable_lista_prob

    def get_printable_element(self, index):
        element = self.__content[index]

        printable_element = "(Nr. laborator: " + str(element.get_nr_lab()) + ", Nr. problema: "
        printable_element += str(element.get_nr_prob()) + ", Descriere: " + str(element.get_descr()) + ", Deadline: "
        printable_element += str(element.get_deadline().get_zi()) + "." + str(element.get_deadline().get_luna()) + "."
        printable_element += str(element.get_deadline().get_an()) + ")"

    def set_content(self, content):
        self.__content = content

    def content_to_text(self):
        content = self.__content
        length = len(content)

        text = ""
        for i in range(0, length):
            problema = content[i]
            deadline = problema.get_deadline()
            text += str(problema.get_nr_lab()) + ", " + str(problema.get_nr_prob()) + ", " + problema.get_descr()
            text += ", " + str(deadline.get_zi()) + "." + str(deadline.get_luna()) + "." + str(deadline.get_an()) + "\n"

        return text

    def adaugare_problema(self, problema):
        """
        Functia adauga problema data in lista.

        :param problema: Problema ce trebuie sa fie adaugata in lista.
        """

        self.__content.append(problema)

    def stergere_problema(self, index):
        """
        Functia sterge problema din lista, dupa un index dat.

        :param index: Indexul problemei care va fi stearsa.
        """

        new_content = self.__content
        new_content.pop(index)

        self.__content = new_content

    def modificare_problema(self, index, problema):
        """
        Functia modifica problema din lista dupa un anumit index, cu o problema noua.

        :param index: Indexul problemei ce trebuie modificata.
        :param problema: Datele problemei noi (un obiect de tip Problema).
        """

        new_content = self.__content
        new_content[index] = problema

        self.__content = new_content

    '''def cautare_problema(self, nr_lab, nr_prob):
        """
        Functia cauta problema in lista, dupa numarul laboratorului si al problemei.

        :param nr_lab: Numarul laboratorului din care apartine problema dupa care se va efectua cautarea.
        :param nr_prob: Numarul problemei dupa care se va efectua cautarea.
        """

        content = self.__content
        length = len(content)

        index = -1
        for i in range(0, length):
            if content[i].get_nr_lab() == nr_lab:
                if content[i].get_nr_prob() == nr_prob:
                    index = i
                    break

        return index'''

    def cautare_problema(self, index, nr_lab, nr_prob):
        """
        Functia cauta in mod recursiv problema in lista, dupa numarul laboratorului si al problemei.

        :param index: Indexul curent al problemei din lista.
        :param nr_lab: Numarul laboratorului din care apartine problema dupa care se va efectua cautarea.
        :param nr_prob: Numarul problemei dupa care se va efectua cautarea.
        """

        content = self.__content

        if index == 0:
            if nr_lab == content[index].get_nr_lab() and nr_prob == content[index].get_nr_prob():
                return index

            else:
                return -1

        else:
            if nr_lab == content[index].get_nr_lab() and nr_prob == content[index].get_nr_prob():
                return index
            else:
                return self.cautare_problema(index - 1, nr_lab, nr_prob)


class Data:
    def __init__(self, raw):
        raw = raw.strip()
        self.__string = raw

        raw = raw.split(".")

        self.__zi = raw[0]
        self.__luna = raw[1]
        self.__an = raw[2]

    def get_zi(self):
        return self.__zi

    def get_luna(self):
        return self.__luna

    def get_an(self):
        return self.__an

    def get_string(self):
        return self.__string

    def set_zi(self, zi):
        self.__zi = zi

    def set_luna(self, luna):
        self.__luna = luna

    def set_an(self, an):
        self.__an = an

    def get_content(self):
        return self.__zi, self.__luna, self.__an

    def __eq__(self, other):
        return self.__zi == other.get_zi() and self.__luna == other.get_luna() and self.__an == other.get_an()


class ListaProbFile(ListaProb):
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

            if len(param) == 4:
                content.append(Problema(int(param[0]), int(param[1]), str(param[2]), Data(str(param[3]))))

            line = file.readline()

        file.close()
        return content

    def __writeToFile(self, text):
        file = open(self.__path, "w")
        file.write(text)
        file.close()

    def adaugare_problema_file(self, problema: Problema):
        super().adaugare_problema(problema)

        text = self.content_to_text()
        self.__writeToFile(text)

    def stergere_problema_file(self, index):
        super().stergere_problema(index)

        text = self.content_to_text()
        self.__writeToFile(text)

    def modificare_problema_file(self, index, problema_noua: Problema):
        super().modificare_problema(index, problema_noua)

        text = self.content_to_text()
        self.__writeToFile(text)

    def validare_unicitate_nr_prob(self, index, nr_lab, nr_prob):
        content = self.get_content()
        length = len(content)
        nr_lab = int(nr_lab)
        nr_prob = int(nr_prob)

        for i in range(0, length):
            if nr_lab == content[i].get_nr_lab() and i != index:
                if nr_prob == content[i].get_nr_prob():
                    raise NrProbUnicError


lista_prob = ListaProbFile([], "Date/test_probleme.txt")
