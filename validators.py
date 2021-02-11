from Exceptions.exceptions import *
from Repository.repo_student import lista_stud
from Repository.repo_problema import lista_prob, Data


######################################################################################################################


class ValidatorStudent:
    def validare_stud_id(self, stud_id):
        try:
            if type(stud_id) == float:
                raise IDError

            stud_id = int(stud_id)
            if stud_id < 1:
                raise IDError

        except:
            raise IDError

    def validare_nume(self, nume):
        if nume == "":
            raise NumeError

        if type(nume) != str:
            raise NumeError

        for i in nume:
            if not i.isalpha() and i != " " and i != "-" and i != ".":
                raise NumeError

    def validare_grupa(self, grupa):
        try:
            if type(grupa) == float:
                raise GrupaError

            grupa = int(grupa)
            if grupa < 1:
                raise GrupaError

        except:
            raise GrupaError

    def validare_index_student(self, index):
        try:
            index = int(index)

            if index < 0:
                raise ValueError
            if index > lista_stud.get_length() - 1:
                raise IndexError

        except ValueError:
            raise ValueError
        except IndexError:
            raise IndexError

    def validare_asignare_problema(self, index, problema):
        content = lista_stud.get_content()

        probleme_student = content[index].get_probleme()
        length = len(probleme_student)

        for i in range(0, length):
            if probleme_student[i].get_problema() == problema:
                raise UnicitateAsignareError

    def validare_nota(self, intrare):
        try:
            nota = int(intrare)

            if nota < 1 or nota > 10:
                raise NotaError

        except ValueError:
            raise NotaError

        except NotaError:
            raise NotaError

    def validare_student(self, intrare):
        try:
            param = intrare.split(", ")
            if len(param) != 3:
                raise ParamError

            self.validare_stud_id(param[0])
            self.validare_nume(param[1])
            self.validare_grupa(param[2])

        except IDError:
            raise IDError

        except NumeError:
            raise NumeError

        except GrupaError:
            raise GrupaError

        except ParamError:
            raise ParamError

    def validare_student_object(self, student):
        try:
            self.validare_stud_id(student.get_stud_id())
            self.validare_nume(student.get_nume())
            self.validare_grupa(student.get_grupa())

        except IDError:
            raise IDError

        except NumeError:
            raise NumeError

        except GrupaError:
            raise GrupaError


######################################################################################################################


class ValidatorProblema:
    def validare_nr_lab(self, nr_lab):
        try:
            if type(nr_lab) == float:
                raise NrLabError

            nr_lab = int(nr_lab)
            if nr_lab < 1:
                raise NrLabError

        except:
            raise NrLabError

    def validare_nr_prob(self, nr_prob):
        try:
            if type(nr_prob) == float:
                raise NrProbError

            nr_prob = int(nr_prob)
            if nr_prob < 1:
                raise NrProbError

        except:
            raise NrProbError

    def validare_descr(self, descr):
        try:
            if descr == "":
                raise DescrError

            if type(descr) != str:
                raise DescrError

        except:
            raise DescrError

    def validare_deadline(self, deadline):
        try:
            zi = deadline.get_zi()
            if type(zi) == float:
                raise ZiError

            zi = int(zi)

            luna = deadline.get_luna()
            if type(luna) == float:
                raise LunaError

            luna = int(luna)

            an = deadline.get_an()
            if type(an) == float:
                raise AnError

            an = int(an)

            if an < 2020 or an > 2023:
                raise AnError

            if luna < 1 or luna > 12:
                raise LunaError

            if zi < 1 or zi > 31:
                raise ZiError

            if not (luna == 1 or luna == 3 or luna == 5 or luna == 7 or luna == 8 or luna == 10 or luna == 12):
                if zi > 30:
                    raise ZiError

            if luna == 2:
                if zi > 29:
                    raise ZiError

        except AnError:
            raise AnError

        except LunaError:
            raise LunaError

        except ZiError:
            raise ZiError

        except:
            raise DeadlineError

    def validare_index_problema(self, index):
        try:
            index = int(index)

            if index < 0:
                raise ValueError
            if index > lista_prob.get_length() - 1:
                raise IndexError

        except ValueError:
            raise ValueError
        except IndexError:
            raise IndexError

    def validare_cautare_problema(self, intrare):
        try:
            param = intrare.split(" ")
            if len(param) != 2:
                raise ParamError

            self.validare_nr_lab(param[0])
            self.validare_nr_prob(param[1])

        except ParamError:
            raise ParamError

        except NrLabError:
            raise NrLabError

        except NrProbError:
            raise NrProbError

    def validare_problema_object(self, problema):
        try:
            self.validare_nr_lab(problema.get_nr_lab())
            self.validare_nr_prob(problema.get_nr_prob())
            self.validare_descr(problema.get_descr())
            self.validare_deadline(problema.get_deadline())

        except NrLabError:
            raise NrLabError

        except NrProbError:
            raise NrProbError

        except DescrError:
            raise DescrError

        except DeadlineError:
            raise DeadlineError

        except ParamError:
            raise ParamError

    def validare_problema(self, intrare):
        try:

            param = intrare.split(", ")
            if len(param) != 4:
                raise ParamError

            self.validare_nr_lab(param[0])
            self.validare_nr_prob(param[1])
            self.validare_descr(param[2])
            self.validare_deadline(Data(param[3]))

        except NrLabError:
            raise NrLabError

        except NrProbError:
            raise NrProbError

        except DescrError:
            raise DescrError

        except DeadlineError:
            raise DeadlineError

        except ParamError:
            raise ParamError

    def validare_intrare_problema(self, intrare):
        try:
            param = intrare.split(" ")
            if len(param) != 2:
                raise ParamError

            self.validare_nr_lab(param[0])
            self.validare_nr_prob(param[1])

        except ParamError:
            raise ParamError

        except NrLabError:
            raise NrLabError

        except NrProbError:
            raise NrProbError


######################################################################################################################


class ValidatorAsignare:
    def validare_nota(self, intrare):
        try:
            nota = int(intrare)

            if nota < 1 or nota > 10:
                raise NotaError

        except ValueError:
            raise NotaError

        except NotaError:
            raise NotaError

