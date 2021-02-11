class Problema:
    def __init__(self, nr_lab, nr_prob, descr, deadline):
        self.__nr_lab = nr_lab
        self.__nr_prob = nr_prob
        self.__descr = descr
        self.__deadline = deadline

    def __eq__(self, other):
        return self.__nr_lab == other.get_nr_lab() and self.__nr_prob == other.get_nr_prob()

    def get_nr_lab(self):
        return self.__nr_lab

    def get_nr_prob(self):
        return self.__nr_prob

    def get_descr(self):
        return self.__descr

    def get_deadline(self):
        return self.__deadline

    def get_all(self):
        return self.__nr_lab, self.__nr_prob, self.__descr, self.__deadline

    def get_all_dl(self):
        return self.__nr_lab, self.__nr_prob, self.__descr

    def set_nr_lab(self, nr_lab):
        self.__nr_lab = int(nr_lab)

    def set_nr_prob(self, nr_prob):
        self.__nr_prob = int(nr_prob)

    def set_descr(self, descr):
        self.__descr = descr

    def set_deadline(self, deadline):
        self.__deadline = deadline

    def set_all(self, nr_lab, nr_prob, descr, deadline):
        self.set_nr_lab(nr_lab)
        self.set_nr_prob(nr_prob)
        self.set_descr(descr)
        self.set_deadline(deadline)
