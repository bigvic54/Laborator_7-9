from Repository.repo_student import lista_stud
from Repository.repo_problema import lista_prob
from Repository.repo_asignare import lista_asignari

from Services.srv_student import ServiceStudent
from Services.srv_problema import ServiceProblema
from Services.srv_asignari import ServiceAsignare
from Services.srv_statistici import ServiceStatistici

from Exceptions.exceptions import *

from simple_colors import *
######################################################################################################################


# noinspection PyBroadException
class Console:
    def __init__(self):
        self.__initCommands()

        lista_stud.set_path("Date/lista_studenti.txt")
        lista_prob.set_path("Date/lista_probleme.txt")
        lista_asignari.set_path("Date/lista_asignari.txt")

        # Setez lista artificial, pentru a putea exemplifica corectitudinea functionalitatilor.
        """
        lista_stud.set_content([
            Student(1, "Pop Ion", 213), Student(2, "Antonovici Traian", 917), Student(15, "Adam Madalina", 917),
            Student(17, "Bob Mihai", 213), Student(23, "Farcas Stefan", 213),
            Student(44, "Andronic Constantin-Dinu", 213)
        ])

        lista_prob.set_content([
            Problema(1, 1, "Catalog studenti", Data("05.04.2021")), Problema(1, 2, "Mersul trenurilor",
            Data("12.21.2020")), Problema(2, 1, "Cont bancar", Data("21.11.2020")), Problema(2, 3, "Agentie de voiaj",
            Data("28.02.2021")), Problema(2, 7, "Programare dinamica", Data("31.01.2021"))
        ])

        a1 = Asignare(Student(1, "Pop Ion", 213), Problema(1, 1, "Catalog studenti", Data("05.04.2021")))
        a2 = Asignare(Student(2, "Antonovici Traian", 917), Problema(1, 1, "Catalog studenti", Data("05.04.2021")))
        a3 = Asignare(Student(15, "Adam Madalina", 917), Problema(1, 1, "Catalog studenti", Data("05.04.2021")))
        a4 = Asignare(Student(17, "Bob Mihai", 213), Problema(1, 1, "Catalog studenti", Data("05.04.2021")))
        a5 = Asignare(Student(17, "Bob Mihai", 213), Problema(2, 7, "Catalog studenti", Data("05.04.2021")))
        a6 = Asignare(Student(15, "Adam Madalina", 917), Problema(2, 1, "Cont bancar", Data("21.11.2020")))

        a1.set_nota(3)
        a2.set_nota(2)
        a3.set_nota(4)
        a4.set_nota(5)
        a5.set_nota(8)
        a6.set_nota(1)

        lista_asignari.set_content([a1, a2, a3, a4, a5, a6])
        """

    def __initCommands(self):
        self.__dict = {"student": {"adaugare": self.__s_adaugare, "stergere": self.__s_stergere,
                                   "modificare": self.__s_modificare, "afisare": self.__s_afisare,
                                   "cautare": self.__s_cautare, "asignare": self.__a_asignare,
                                   "notare": self.__a_notare, "generare": self.__s_generare},

                       "problema": {"adaugare": self.__p_adaugare, "stergere": self.__p_stergere,
                                    "modificare": self.__p_modificare, "afisare": self.__p_afisare,
                                    "cautare": self.__p_cautare, "generare": self.__p_generare},
                       "statistici": {"alfabetic": self.__st_alfabetic, "nota": self.__st_nota,
                                      "medie": self.__st_medie, "grupa": self.__st_grupa}
                       }

    def __s_adaugare(self):
        """
        Functia citeste datele de intrare si tipareste rezultatul / mesajul de eroare pentru adaugarea studentului.
        """

        print(yellow("Introduceti datele studentului pe care doriti sa il adaugati.\n"
                     "Fiecare pereche de date de intrare ar trebui sa contina ID-ul studentului, numele si prenumele, "
                     "dar si numarul grupei, separate prin cate o virgula si cate un spatiu.", 'bold'))

        ok = 0
        while not ok:
            try:
                intrare = input().strip()

                srv_student = ServiceStudent()
                srv_student.srv_adaugare_student(intrare)

                ok = 1

                print(cyan("Adaugarea a fost efectuata cu succes!", 'bold'))
                print(cyan("Lista de studenti a devenit:", 'bold'))
                print(cyan(lista_stud.get_printable_content(), 'bold'))

            except Exception as ex:
                print(red(ex, 'bold'))

    def __s_stergere(self):
        """
        Functia citeste datele de intrare si tipareste rezultatul / mesajul de eroare pentru stergerea studentului.
        """

        if lista_stud.get_length() == 0:
            print("Nu exista niciun student in baza de date, deci nu se poate efectua stergerea!")

        else:
            print(cyan("Lista de studenti este:", 'bold'))
            print(cyan(lista_stud.get_printable_content(), 'bold'))

            print(yellow("Introduceti ID-ul studentului pe care doriti sa il eliminati din baza de date: ", 'bold'))

            ok = 0
            while not ok:
                try:
                    stud_id = input().strip()

                    srv_student = ServiceStudent()
                    srv_student.srv_stergere_student(stud_id)

                    ok = 1

                    print(cyan("Stergerea a fost efectuata cu succes!", 'bold'))
                    print(cyan("Lista de studenti a devenit:", 'bold'), end=" ")
                    if lista_stud.get_length() == 0:
                        print(cyan("vida.", 'bold'))

                    else:
                        print('\n', end="")
                        print(cyan(lista_stud.get_printable_content(), 'bold'))

                except Exception as ex:
                    print(red(ex, 'bold'))

    def __s_modificare(self):
        """
        Functia citeste datele de intrare si tipareste rezultatul / mesajul de eroare pentru modificarea studentului.
        """

        if lista_stud.get_length() == 0:
            print("Nu exista niciun student in baza de date, deci nu se poate efectua modificarea!")

        else:
            print(cyan("Lista de studenti este:"))
            print(cyan(lista_stud.get_printable_content()))

            print(yellow("Introduceti ID-ul studentului pe care doriti sa il modificati: ", 'bold'))

            ok = 0
            while not ok:
                try:
                    stud_id = input().strip()

                    srv_student = ServiceStudent()
                    srv_student.srv_pre_modificare_student(stud_id)

                    print(yellow("Introduceti noul set de date pentru studentul ales.\n"
                                 "Fiecare pereche de date de intrare ar trebui sa contina ID-ul studentului, numele si "
                                 "prenumele, dar si numarul grupei, separate prin cate o virgula si cate un spatiu.",
                                 'bold'))

                    ok2 = 0
                    while not ok2:
                        try:
                            intrare = input()

                            srv_student = ServiceStudent()
                            srv_student.srv_modificare_student(stud_id, intrare)

                            ok = 1
                            ok2 = 1

                            print(cyan("Modificarea a fost efectuata cu succes!", 'bold'))
                            print(cyan(lista_stud.get_printable_content(), 'bold'))

                        except Exception as ex:
                            print(red(ex, 'bold'))

                except Exception as ex:
                    print(red(ex, 'bold'))

    def __s_cautare(self):
        """
        Functia citeste datele de intrare si tipareste rezultatul / mesajul de eroare pentru modificarea studentului.
        """

        if lista_stud.get_length() == 0:
            print("Nu exista niciun student in baza de date, deci nu se poate efectua cautarea!")

        else:
            print(yellow("Introduceti ID-ul studentului pe care doriti sa il cautati:", 'bold'))

            ok = 0
            while not ok:
                try:
                    intrare = input().strip()

                    srv_student = ServiceStudent()

                    student_gasit = srv_student.srv_cautare_student(intrare)

                    print(cyan("Studentul cu ID-ul dat are urmatoarele date:", 'bold'))
                    print(cyan(student_gasit, 'bold'))

                    ok = 1

                except Exception as ex:
                    print(red(ex, 'bold'))

    def __s_afisare(self):
        """
        Functia afiseaza lista de studenti.
        """

        if lista_stud.get_length() != 0:
            print(cyan(lista_stud.get_printable_content(), 'bold'))

        else:
            print("Lista de studenti este vida!\n")

    def __s_generare(self):
        """
         Functia citeste datele de intrare si tipareste lista cu studentii generati aleator.
        """

        print(yellow("Introduceti numarul de studenti pe care doriti sa ii generati:", 'bold'))

        ok = 0
        while not ok:
            try:
                intrare = input().strip()

                srv_student = ServiceStudent()
                srv_student.srv_solve_generare_student(intrare)

                print(cyan("Lista de studenti generata aleator este:", 'bold'))
                print(cyan(lista_stud.get_printable_content(), 'bold'))

                ok = 1

            except Exception as ex:
                print(red(ex, 'bold'))

    def __p_adaugare(self):
        """
        Functia citeste datele de intrare si tipareste rezultatul / mesajul de eroare pentru adaugarea problemei.
        """

        print(yellow("Introduceti datele problemei pe care doriti sa o adaugati.\n"
                     "Fiecare pereche de date de intrare ar trebui sa contine numarul laboratorului, numarul "
                     "problemei, descrierea si deadline-ul, fiecare separate prin cate un spatiu si o virgula.\n"
                     "Deadline-ul trebuie sa fie sub forma: zz.ll.aaaa.", 'bold'))

        ok = 0
        while not ok:
            try:
                intrare = input().strip()

                srv_problema = ServiceProblema()
                srv_problema.srv_adaugare_problema(intrare)

                ok = 1

                print(cyan("Adaugarea a fost efectuata cu succes!", 'bold'))
                print(cyan("Lista de probleme a devenit:", 'bold'))
                print(cyan(lista_prob.get_printable_content(), 'bold'))

            except Exception as ex:
                print(red(ex, 'bold'))

    def __p_stergere(self):
        """
        Functia citeste datele de intrare si tipareste rezultatul / mesajul de eroare pentru stergerea problemei.
        """

        if lista_prob.get_length() == 0:
            print("Nu exista nicio problema in baza de date, deci nu se poate efectua stergerea!")

        else:
            print("Lista de probleme este:")
            print(lista_prob.get_printable_content())

            print(yellow("Introduceti numarul laboratorului si numarul problemei (separate prin spatiu) ale problemei "
                         "pe care doriti sa o eliminati din baza de date: ", 'bold'))

            ok = 0
            while not ok:
                try:
                    intrare = input().strip()

                    srv_problema = ServiceProblema()
                    srv_problema.srv_stergere_problema(intrare)

                    ok = 1

                    print(cyan("Stergerea a fost efectuata cu succes!", 'bold'))
                    print(cyan("Lista de probleme a devenit:", 'bold'), end=" ")
                    if lista_stud.get_length() == 0:
                        print(cyan("vida.", 'bold'))

                    else:
                        print("\n", end="")
                        print(cyan(lista_prob.get_printable_content(), 'bold'))

                except Exception as ex:
                    print(red(ex, 'bold'))

    def __p_modificare(self):
        """
        Functia citeste datele de intrare si tipareste rezultatul / mesajul de eroare pentru modificarea problemei.
        """
        if lista_prob.get_length() == 0:
            print("Nu exista nicio problema in baza de date, deci nu se poate efectua modificarea!")

        else:
            print("Lista de probleme este:")
            print(lista_prob.get_printable_content())

            print(yellow("Introduceti numarul laboratorului si numarul problemei (separate prin spatiu) ale problemei "
                         "pe care doriti sa o modificati: ", 'bold'))

            ok = 0
            while not ok:
                try:
                    index = input().strip()

                    srv_problema = ServiceProblema()
                    nr_lab, nr_prob = srv_problema.srv_pre_modificare_problema(index)

                    print(yellow("Introduceti noul set de date pentru problema aleasa.\nFiecare pereche de date de "
                                 "intrare ar trebui sa contine numarul laboratorului, numarul problemei, descrierea si "
                                 "deadline-ul, fiecare separate prin cate un spatiu si o virgula.\n"
                                 "Deadline-ul trebuie sa fie sub forma: zz.ll.aaaa.", 'bold'))

                    ok2 = 0
                    while not ok2:
                        try:
                            intrare = input()

                            srv_problema = ServiceProblema()
                            srv_problema.srv_modificare_problema(nr_lab, nr_prob, intrare)

                            ok = 1
                            ok2 = 1

                            print(cyan("Modificarea a fost efectuata cu succes!", 'bold'))
                            print(cyan("Lista de probleme a devenit:", 'bold'))
                            print(cyan(lista_prob.get_printable_content(), 'bold'))

                        except Exception as ex:
                            print(red(ex, 'bold'))

                except Exception as ex:
                    print(red(ex, 'bold'))

    def __p_cautare(self):
        """
        Functia citeste datele de intrare si tipareste rezultatul / mesajul de eroare pentru cautarea problemei.
        """
        if lista_prob.get_length() == 0:
            print("Nu exista nicio problema in baza de date, deci nu se poate efectua cautare!")

        else:
            print(yellow("Introduceti numarul laboratorului si numarul problemei (separate prin spatiu)"
                  " pe care doriti sa o cautati:", 'bold'))

            ok = 0
            while not ok:
                try:
                    intrare = input().strip()

                    srv_problema = ServiceProblema()

                    problema_gasita = srv_problema.srv_cautare_problema(intrare)
                    problema_gasita = srv_problema.to_printable_form(problema_gasita)

                    print(cyan("Problema cautata are urmatoarele date:", 'bold'))
                    print(cyan(problema_gasita, 'bold'))

                    ok = 1

                except Exception as ex:
                    print(red(ex, 'bold'))

    def __p_afisare(self):
        """
        Functia afiseaza lista de probleme.
        """

        if lista_prob.get_length() != 0:
            print(cyan(lista_prob.get_printable_content(), 'bold'))

        else:
            print("Lista de probleme este vida!\n")

    def __p_generare(self):
        """
        Functia citeste datele de intrare si afiseaza lista de probleme generate.
        """

        print(yellow("Introduceti numarul de probleme pe care doriti sa le generati:", 'bold'))

        ok = 0
        while not ok:
            try:
                intrare = input().strip()

                srv_problema = ServiceProblema()

                srv_problema.srv_solve_generare_problema(intrare)

                print(cyan("Lista de probleme generata aleator este:", 'bold'))
                print(cyan(lista_prob.get_printable_content(), 'bold'))

                ok = 1

            except Exception as ex:
                print(red(ex, 'bold'))

    def __a_asignare(self):
        """
        Functia citeste datele de intrare si tipareste rezultatul / mesajul de eroare pentru asignarea unei probleme.
        """

        if lista_stud.get_length() == 0:
            print("Nu exista niciun student in baza de date, deci nu se poate efectua asignarea!")

        else:
            if lista_prob.get_length() == 0:
                print("Nu exista nicio problema in baza de date, deci nu se poate efectua asignarea!")

            else:
                print(cyan("Lista de studenti este:", 'bold'))
                print(cyan(lista_stud.get_printable_content(), 'bold'))

                print(cyan("Lista de probleme este:", 'bold'))
                print(cyan(lista_prob.get_printable_content(), 'bold'))

                print(yellow("Introduceti ID-ul studentului caruia doriti sa ii asignati o problema: ", 'bold'))

                ok = 0
                while not ok:
                    try:
                        intrare = input().strip()

                        srv_asignare = ServiceAsignare()

                        student = srv_asignare.srv_pre_asignare_problema(intrare)

                        print(yellow("Introduceti numarul laboratorului si numarul problemei pe care doriti sa o "
                                     "asignati studentului:", 'bold'))

                        ok2 = 0
                        while not ok2:
                            try:
                                intrare2 = input().strip()

                                srv_asignare.srv_asignare_problema(student, intrare2)

                                ok = 1
                                ok2 = 1

                                print(cyan("Studentul are acum asignate problemele:", 'bold'))
                                print(cyan(lista_asignari.get_probleme_from_student(student), 'bold'))

                            except Exception as ex:
                                print(red(ex, 'bold'))

                    except Exception as ex:
                        print(red(ex, 'bold'))

    def __a_notare(self):
        """
        Functia citeste datele de intrare si tipareste rezultatul / mesajul de eroare pentru notarea unei probleme
        asignate.
        """

        if lista_stud.get_length() == 0:
            print(red("Nu exista niciun student in baza de date, deci nu se poate efectua asignarea!", 'bold'))

        else:
            if lista_prob.get_length() == 0:
                print(red("Nu exista nicio probleme in baza de date, deci nu se poate efectua asignarea!", 'bold'))

            else:
                print(cyan("Lista de studenti este:", 'bold'))
                print(cyan(lista_stud.get_printable_content(), 'bold'))

                print(yellow("Introduceti ID-ul studentului caruia doriti sa ii notati o problema: ", 'bold'))

                ok = 0
                while not ok:
                    try:
                        intrare = input().strip()

                        srv_asignare = ServiceAsignare()

                        student = srv_asignare.srv_pre_asignare_problema(intrare)

                        if lista_asignari.get_nr_probleme(student) == 0:
                            raise NotareError("Studentul cu ID-ul dat nu are nicio problema asignata! Introduceti alt "
                                              "ID:")

                        print(cyan("Studentul are acum asignate problemele: ", 'bold'))
                        print(cyan(lista_asignari.get_probleme_from_student(student), 'bold'))

                        print(yellow("Introduceti numarul laboratorului si numarul problemei asignate studentului"
                                     " pe care doriti sa o notati studentului:", 'bold'))

                        ok2 = 0
                        while not ok2:
                            try:
                                intrare2 = input().strip()

                                srv_asignare.srv_pre_notare_problema(student, intrare2)

                                print(yellow("Introduceti nota (numar intreg cuprins intre 1 si 10) pe care doriti sa "
                                             "o asignati studentului la problema introdusa:", 'bold'))

                                ok3 = 0
                                while not ok3:
                                    try:
                                        intrare3 = input().strip()

                                        srv_asignare.srv_notare_problema(student, intrare2, intrare3)

                                        print(cyan("Studentul are acum asignate problemele: ", 'bold'))
                                        print(cyan(lista_asignari.get_probleme_from_student(student), 'bold'))

                                        ok = 1
                                        ok2 = 1
                                        ok3 = 1

                                    except Exception as ex:
                                        print(red(ex, 'bold'))

                            except Exception as ex:
                                print(red(ex, 'bold'))

                    except Exception as ex:
                        print(red(ex, 'bold'))

    def __st_alfabetic(self):
        """
        Functia citeste datele de intrare si tipareste rezultatul / mesajul de eroare pentru crearea statisticilor
        ordonate alfabetic.
        """

        if lista_asignari.get_length() == 0:
            print(red("Inca nu s-a facut nicio asignare, deci nu se pot fac statistici!", 'bold'))

        else:
            print(cyan("Lista de asignari este:", 'bold'))
            print(cyan(lista_asignari.get_printable_content(), 'bold'))

            print(yellow("Introduceti numarul laboratorului si numarul problemei in functie de care doriti sa generati"
                         " statisticile:", 'bold'))

            ok = 0
            while not ok:
                srv_statistici = ServiceStatistici()
                try:
                    intrare1 = input().strip()
                    intrare2 = input(yellow("Introduceti 'cresc' pentru a sorta crescator si 'desc' "
                                     "pentru a sorta descrescator: ", 'bold'))

                    print(cyan(srv_statistici.srv_studenti_ordonati(intrare1, intrare2, 'a', 0), 'bold'))

                    ok = 1

                except Exception as ex:
                    print(red(ex, 'bold'))

    def __st_nota(self):
        """
        Functia citeste datele de intrare si tipareste rezultatul / mesajul de eroare pentru crearea statisticilor
        ordonate descrescator dupa nota
        """

        if lista_asignari.get_length() == 0:
            print(red("Inca nu s-a facut nicio asignare, deci nu se pot fac statistici!", 'bold'))

        else:
            print(cyan("Lista de asignari este: ", 'bold'))
            print(cyan(lista_asignari.get_printable_content(), 'bold'))

            ok = 0
            while not ok:
                srv_statistici = ServiceStatistici()
                try:
                    intrare1 = input(yellow("Introduceti numarul laboratorului si numarul problemei in functie de care "
                                            "doriti sa generati statisticile:\n", 'bold')).strip()

                    intrare2 = input(yellow("Introduceti 'cresc' pentru a sorta crescator si 'desc' "
                                     "pentru a sorta descrescator: ", 'bold')).strip()

                    print(cyan(srv_statistici.srv_studenti_ordonati(intrare1, intrare2, 'n', 0), 'bold'))

                    ok = 1

                except Exception as ex:
                    print(red(ex, 'bold'))

    def __st_medie(self):
        """
        Functia citeste datele de intrare si tipareste rezultatul / mesajul de eroare pentru crearea statisticilor
        ordonate descrescator dupa nota.
        """

        if lista_asignari.get_length() == 0:
            print(red("Inca nu s-a facut nicio asignare, deci nu se pot fac statistici!", 'bold'))

        else:
            print(cyan("Lista de asignari este: ", 'bold'))
            print(cyan(lista_asignari.get_printable_content(), 'bold'))

            srv_statistici = ServiceStatistici()

            try:

                print(cyan("Lista de studenti cu nota mai mica notelor mai mica decat 5 este:", 'bold'))
                print(cyan(srv_statistici.srv_medie_mica(), 'bold'))

            except Exception as ex:
                print(red(ex, 'bold'))

    def __st_grupa(self):
        """
        Functia citeste datele de intrare si tipareste rezultatul / mesajul de eroare pentru crearea statisticilor.
        ordonand descrescator lista de grupe dupa numarul de note sub 7 asignate elevilor de la fiecare grupa.
        """

        srv_statistici = ServiceStatistici()
        print(yellow("Introduceti 'cresc' pentru a sorta crescator, sau 'desc' pentru a sorta descrescator.", 'bold'))

        ok = 0
        while not ok:
            try:
                intrare = input()
                statistici = srv_statistici.srv_grupe_ordonate_printable(intrare)

                print(cyan("Lista de grupe sortata dupa numarul de probleme cu nota sub 7 este:", 'bold'))
                print(cyan(statistici, 'bold'))

                ok = 1

            except Exception as ex:
                print(red(ex, 'bold'))

    def __read_submeniu(self):
        """
        Functia citeste submeniul.
        """

        print(magenta("-------------------------------------------------------------------------------------", 'bold'))
        print(magenta("Meniu:\n1) student (Acceseaza comenzile pentru lucru pe lista de studenti.)\n"
              "2) problema (Acceseaza comenzile pentru lucru pe lista de laboratoare / probleme.)\n"
              "3) statistici (Acceseaza comenzile pentru generarea statisticilor.)\n"
              "4) inchidere (Inchide aplicatia.)", 'bold'))
        print(magenta("-------------------------------------------------------------------------------------", 'bold'))

        intrare = input(
            "Introduceti comanda pentru submeniul dorit:\n").strip()  # Strip pt a scapa de spatiile nenecesare.
        intrare = intrare.lower()

        return intrare

    def __read_comanda(self, submeniu):
        """
        Functia citeste comanda.
        """

        print(magenta("-------------------------------------------------------------------------------------", 'bold'))
        if submeniu == "student":
            print(magenta("Comenzile din submeniul", 'bold'), magenta(submeniu, 'bold'), end="")
            print(magenta(":\n\ta) adaugare (Adauga un nou student in lista.)\n"
                  "\tb) stergere (Sterge un student din lista.)\n"
                  "\tc) modificare (Modifica datele unui student din lista.)\n"
                  "\td) afisare (Afiseaza lista de studenti.)\n"
                  "\te) cautare (Cauta un student din lista.)\n"
                  "\tf) asignare (Asigneaza unui student o problema din lista de probleme.)\n"
                  "\tg) notare (Adauga studentului o nota la o problema asignata.)\n"
                  "\th) generare (Genereaza un numar dat de studenti.)", 'bold'))

        elif submeniu == "problema":
            print(magenta("Comenzile din submeniul", 'bold'), magenta(submeniu, 'bold'), end="")
            print(magenta(":\n\ta) adaugare (Adauga o noua problema in lista.)\n"
                  "\tb) stergere (Sterge o problema din lista.)\n"
                  "\tc) modificare (Modifica datele unei probleme din lista.)\n"
                  "\td) afisare (Afiseaza lista de probleme.)\n"
                  "\te) cautare (Cauta o problema din lista.)\n"
                  "\tf) generare (Genereaza un numar dat de probleme.)", 'bold'))

        elif submeniu == "statistici":
            print(magenta("Comenzile din submeniul", 'bold'), magenta(submeniu, 'bold'), end="")
            print(magenta(":\n\ta) alfabetic "
                          "(Ordoneaza studentii cu o problema de laborator data alfabetic dupa nume.)\n"
                  "\tb) nota (Ordoneaza studentii cu o problema de laborator data in functie de nota.)\n"
                  "\tc) medie (Afiseaza studentii cu media notelor de la probleme mai mica decat 5.)\n"
                  "\td) grupa (Afiseaza lista de grupa sortata dupa numarul de probleme cu nota sub 7.)", 'bold'))

        print(magenta("-------------------------------------------------------------------------------------", 'bold'))

        intrare = input("Introduceti comanda dorita:\n").strip()
        intrare = intrare.lower()

        return intrare

    def run(self):
        """
        Functia ce are rolul de meniu.
        """

        while True:
            submeniu_raw = self.__read_submeniu()

            if submeniu_raw == "inchidere":
                print(magenta("Aplicatia se va inchide...", 'bold'))
                break

            try:
                submeniu = self.__dict[submeniu_raw]

                ok = 0
                while not ok:

                    comanda_raw = self.__read_comanda(submeniu_raw)

                    try:
                        comanda = submeniu[comanda_raw]
                        ok = 1
                        comanda()

                    except KeyError:
                        print("Aceasta comanda nu exista! Introduceti alta!\n")

                    except ValueError:
                        print("Aceasta comanda este invalida! Introduceti alta!\n")

                    except Exception as ex:
                        print(red(ex, 'bold'))

            except KeyError:
                print("Aceasta comanda pentru submeniu nu exista! Introduceti alta!\n")

            except ValueError:
                print("Aceasta comanda pentru submeniu este invalida! Introduceti alta!\n")

            except Exception as ex:
                print(red(ex, 'bold'))
