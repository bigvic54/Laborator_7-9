class Asignare:
    def __init__(self, student, problema):
        self.__student = student
        self.__problema = problema
        self.__nota = 0

    def __eq__(self, other):
        return other.get_student() == self.get_student() and other.get_problema() == self.get_problema()

    def get_student(self):
        return self.__student

    def get_problema(self):
        return self.__problema

    def set_problema(self, problema):
        self.__problema = problema

    def set_student(self, student):
        self.__student = student

    def set_nota(self, nota):
        self.__nota = nota

    def get_nota(self):
        return self.__nota

    def get_asignare_tuple(self):
        return self.__student, self.__problema
