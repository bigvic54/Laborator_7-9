class Student:
    def __init__(self, stud_id, nume, grupa):
        self.__stud_id = stud_id
        self.__nume = nume
        self.__grupa = grupa

    def __eq__(self, other):
        return self.__stud_id == other.get_stud_id()

    def get_stud_id(self):
        return self.__stud_id

    def get_nume(self):
        return self.__nume

    def get_grupa(self):
        return self.__grupa

    def get_all(self):
        return self.__stud_id, self.__nume, self.__grupa

    def set_stud_id(self, stud_id):
        self.__stud_id = int(stud_id)

    def set_nume(self, nume):
        self.__nume = nume

    def set_grupa(self, grupa):
        self.__grupa = int(grupa)

    def set_all(self, stud_id, nume, grupa):
        self.set_stud_id(stud_id)
        self.set_nume(nume)
        self.set_grupa(grupa)
