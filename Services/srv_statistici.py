import Repository.repo_asignare as repo

from Validators.validators import ValidatorProblema
from Exceptions.exceptions import *

from Misc.utils import cmp_generic_nr_probleme, gnome_sort_generic

######################################################################################################################


class ServiceStatistici:
    def srv_studenti_ordonati(self, intrare1, intrare2, tip_ordonare, debug):
        """
        Functia primeste string-ul cu datele problemei dupa care se va cauta, asigura validitatea acestor date, le
        prelucreaza si construieste un string ordonat user-friendly (daca debug = 0); in caz contrar, returneaza
        lista ordonata.

        :param intrare1: Un sir de caractere ce ar trebui sa reprezinte nr. laboratorului si al problemei in functie de
        care trebuie sa fie efectuata ordonarea.

        :param intrare2: Un sir de caractere ('cresc' sau 'desc') ce reprezinta daca sortarea va fi crescatoare sau
        descrescatoare.

        :param tip_ordonare: Tipul de ordonare a studentilor: 'a' = alfabetic, 'n' = nota.
        :param debug: 1 daca functia este folosita in cadrul testelor cu assert; 0 in caz contrar.
        """

        validator_problema = ValidatorProblema()
        try:

            if intrare2 == "cresc":
                rev = False

            elif intrare2 == "desc":
                rev = True

            else:
                raise RevError

            validator_problema.validare_intrare_problema(intrare1)

            param = intrare1.split(" ")
            nr_lab, nr_prob = int(param[0]), int(param[1])

            if tip_ordonare == "n":
                lista_ordonata = repo.lista_asignari.ordonare_nota(nr_lab, nr_prob, rev)

            else:
                lista_ordonata = repo.lista_asignari.ordonare_alfabetica(nr_lab, nr_prob, rev)

            if len(lista_ordonata) > 0:
                string = ""
                for i in range(0, len(lista_ordonata)):
                    student = lista_ordonata[i].get_student()
                    string += str(i + 1) + ") Studentul: (ID: "
                    string += str(student.get_stud_id()) + ", Nume: " + student.get_nume() + ", Grupa" + ": "
                    string += str(student.get_grupa()) + ") cu nota: " + str(lista_ordonata[i].get_nota()) + ".\n"

                if not debug:
                    return string

                else:
                    return lista_ordonata

            else:
                raise ExistentaError

        except ParamError:
            raise ParamError("Nu s-au introdus doua numere! Introduceti alte date de intrare:")

        except NrLabError:
            raise NrLabError("Numarul laboratorului introdus este invalid! Introduceti alte date de intrare:")

        except NrProbError:
            raise NrProbError("Numaorul problemei introduse este invalid! Introduceti alte date de intrare:")

        except ExistentaError:
            raise ExistentaError("Nu exista niciun student cu aceasta problema asignata!"
                                 "Introduceti alte date de intrare:")

        except RevError:
            raise RevError("Trebuie sa introduceti 'cresc' sau 'desc'. Introduceti din nou: ")

    def srv_medie_mica(self, debug=0):
        """
        Functia obtine din repo lista studentilor si mediile acestora, si creeaza un string user-friendly pentru
        afisare, format din datele studentilor cu media la probleme mai mica decat 5.

        :param debug: 1 daca functia este folosita in cadrul testelor cu assert; 0 in caz contrar.
        """

        try:
            lista = repo.lista_asignari.get_asignari_medie()

            if len(lista) == 0:
                raise ExistentaError

            else:
                string = ""
                lista_debug = []

                for i in range(0, len(lista)):
                    if lista[i][1] < 5:
                        string += str(i+1) + ") Studentul " + str(lista[i][0].get_nume()) + " cu media: "
                        string += str(lista[i][1]) + ".\n"
                        lista_debug.append(lista[i])

                if string == "":
                    string = "vida."

                if not debug:
                    return string

                elif string == "":
                    return None

                else:
                    return lista_debug

        except ExistentaError:
            raise ExistentaError("Inca nu s-au efectuat asignari, deci nu se poate efectua statistica!")

    def srv_grupe_ordonate(self, intrare):
        """
        Functia obtine din repo lista de asignari in functie de grupa, si o sorteaza descrescator dupa note.
        """

        try:
            if intrare == "cresc":
                rev = False

            elif intrare == "desc":
                rev = True

            else:
                raise RevError

            if repo.lista_asignari.get_length() == 0:
                raise ExistentaError

            lista = repo.lista_asignari.get_asignari_grupa()

            # Sortam lista dupa numarul de probleme (value-ul din lista) in ordinea data.
            lista_sortata = gnome_sort_generic(lista, cmp_generic_nr_probleme, rev)

            return lista_sortata

        except ExistentaError:
            raise ExistentaError("Inca nu s-au efectuat asignari, deci nu se poate efectua statistica!")

        except RevError:
            raise RevError("Trebuie sa introduceti 'cresc' sau 'desc'. Introduceti din nou: ")

    def srv_grupe_ordonate_printable(self, intrare):
        """
        Functia primeste grupele sortate dupa numarul de probleme cu nota sub 7 si pregateste un string user-friendly
        care va fi afisat in Console.
        """

        try:
            lista_sortata = self.srv_grupe_ordonate(intrare)

            string = ""
            for i in range(0, len(lista_sortata)):
                string += str(i + 1) + ") Grupa: " + str(lista_sortata[i][0]) + " are " + str(lista_sortata[i][1])
                string += " probleme cu nota mai mica decat 7.\n"

            return string

        except ExistentaError:
            raise ExistentaError("Inca nu s-au efectuat asignari, deci nu se poate efectua statistica!")
