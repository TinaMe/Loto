# -*- coding: utf-8 -*-

def main():
    import random

    seznam_stevil = []

    print "Pozdravljeni v programu Generator loto števil!"

    loto_stevila = int(raw_input("Prosimo vpišite, koliko naključnih loto števil želite: "))

    for i in range(0, loto_stevila):
        stevila = random.randint(1, 39)
        while stevila in seznam_stevil:
            stevila = random.randint(1, 39)

        seznam_stevil.append(stevila)

    seznam_stevil.sort()

    print "Generirane loto številke so: "
    print seznam_stevil

    print "Hvala za zaupanje in nasvidenje!"



if __name__ == '__main__':
    main()

