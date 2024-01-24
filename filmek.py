import FilmekO

def beolvas():
    filmek = []
    beFile = open("film.txt", "r", encoding="UTF-8")
    beFile.readline()
    sorok = beFile.readlines()
    beFile.close()

    for index in range(len(sorok)):
        tisztitottSor = sorok[index].strip()
        daraboltSor = tisztitottSor.split(";")
        cim = daraboltSor[0]
        rendezo = daraboltSor[1]
        foszereplo = daraboltSor[2]
        ev = int(daraboltSor[3])
        perc = int(daraboltSor[4])

        film = FilmekO.Filmek(cim, rendezo, foszereplo, ev, perc)
        filmek.append(film)

    return filmek

def adatokSorai(lista):
    print(f"\nAz adatok sorainak száma: {len(lista)}", end="")

def legrovidebb(lista):
    minIndex = 0
    for index in range(0, len(lista), 1):
        if lista[index].perc < lista[minIndex].perc:
            minIndex += index
    print(f"\nA legrövidebb film címe: {lista[minIndex].cim}")

