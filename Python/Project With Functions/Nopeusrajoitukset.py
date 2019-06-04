#TIE-02100 Johdatus ohjelmointiin
#Valtteri Vuorio, 268084
#vuorio.valtteri@student.tut.fi
#Ohjelma, joka ottaa nopeuksia ja laskee niihin liittyviä tilastoja
#Jaoin ohjelman mahdollisimman moneen funktioon.
#Mielestäni se teki koodista erittäin helppoa lukea ja debuggata.


def rajoitus():
    a = int(input("Enter the speed limit for the measurement location: "))
    if a <= 0:
        print("The speed limit must be expressed as a positive integer.")
        return 0
        #palauttaa nollan, koska en keksinyt parempaa tapaa
        #lopettaa ohjelman suorittamisen
    else:
        return a


def kysely():
    lista = []
    k = 0
    print("Enter the results of the speed measurements, "
          "finish with an empty line:")
    while k == 0:
        b = str(input())
        if b == "":
            k += 1
        if b != "":
            c = int(b)
            lista.append(c)
    return lista


def vaihteluvali(lista):
    suurin = max(lista)
    pienin = min(lista)
    vaihtelu = suurin - pienin
    return vaihtelu


def mediaani(lista):
    list = sorted(lista)
    LKM = len(list)
    if LKM % 2 == 0:
        tulos = (list[(LKM-1)//2]+list[(LKM-1)//2+1])/2
        return tulos
    if LKM % 2 == 1:
        tulos = list[LKM//2]
        return tulos


#Funktio, joka laskee sakkojen, rikesakkojen ja alle 20 kmh menneiden määrän.
def sakot(lista, raja):
    sakkoLKM = 0
    rikesakkoLKM = 0
    alitusLKM = 0
    for i in range(0, len(lista)):
        if lista[i] <= 20:
            alitusLKM += 1
        if raja + 8 <= lista[i] < raja + 20:
            rikesakkoLKM += 1
        if lista[i] >= raja + 20:
            sakkoLKM += 1
    return rikesakkoLKM, sakkoLKM, alitusLKM


#Funkito , joka poistaa alle 20 kmh menneet listasta seuraavia laskuja varten.
def listan_siivous(lista):
    lista2 = [] + lista
    k = 0
    for i in range(0, len(lista)):
        if lista[i] <= 20:
            del lista2[i-k]
            k += 1
    return lista2


def tulostus(raja, nopeudet, vaihtelu, median, rikesakot, sakko, alitus):
    if alitus != 0:
        print("Ignored", alitus,
              "measurement results whose values were under 20 km/h")
    print("Range:", vaihtelu)
    print("Median: {:.1f}".format(median))
    if rikesakot > 0:
        print("The on-the-spot-fine for speeding would have been issued to",
              rikesakot, "drivers")
    if sakko > 0:
        print("The fine for speeding would have been issued to", sakko,
              "drivers")
    if rikesakot != 0 or sakko != 0:
        print("Speeders in the order of measurements:")
        for i in range(0, len(nopeudet)):
            if nopeudet[i] >= raja + 8:
                print(nopeudet[i])


def main():
    raja = rajoitus()
    #Jos nopeusrajoitukseksi annettu negatiivinen luku,
    #ei tehdä laskuja eikä tulosteta mitään.
    if raja != 0:
        nopeudet = kysely()
        rikesakot, sakko, alitus = sakot(nopeudet, raja)
        lista_laskemiseen = listan_siivous(nopeudet)
        #jos lista on tyhjä, ei lasketa muuta.
        if lista_laskemiseen != []:
            vaihtelu = vaihteluvali(lista_laskemiseen)
            median = mediaani(lista_laskemiseen)
            tulostus(raja, lista_laskemiseen, vaihtelu,
                     median, rikesakot, sakko, alitus)
        else:
            print("Ignored", alitus,
                  "measurement results whose values were under 20 km/h")


main()