# TIE-02100 Johdatus ohjelmointiin
# Valtteri Vuorio, valtteri.vuorio@student.tut.fi, opiskelijanumero: 268084
# Tehtävän 3.3. ratkaisu:
# Ohjelma, joka kertoo, onko viinin käymisprosessi onnistunut.

def main():
    # Kysytään käyttäjältä mittausten lukumäärä.
    rivi = input("Enter the number of measurements: ")
    mittausten_lkm = int(rivi)

    # Tarkistetaan, että mittausten lukumäärä on positiivinen.
    if mittausten_lkm < 0 or mittausten_lkm == 0:
        print("The number of measurements must be a positive number.")

    # Määritetään muutuja, joka kertoo kuinka mones mittauskierros on menossa.
    i = 1

    # Luodaan muuttujat, jotka seuraavat viinin tilaa:
    # viinin_tila -muuttuja seuraa, kuinka monta kertaa viinin lämpötila
    # on ollut rajojen ulkopuolella
    viinin_tila = 0

    # edellinen_mittaus -muuttuja kertoo onko edellinen mittaus ollut rajoissa.
    edellinen_mittaus = 0

    # Kysytään käyttäjältä viinin lämpotila.
    for i in range(1,mittausten_lkm+1):
        rivi2 = input("Enter the temperature {}: ".format(i))
        viinin_lampotila = int(rivi2)


        # Tarkistetaan onko lämpötila välillä [20,25].
        if viinin_lampotila < 20 or viinin_lampotila > 25:
            edellinen_mittaus += 1

            # Jos kaksi perättäistä mittausta on "vääriä" siirrytään loppuun.
            if edellinen_mittaus == 2:
                break

            viinin_tila += 1

            # Jos "virheellisten" lämpötilojen määrä ylittää 10 %,
            # siirrytään loppuun.
            if viinin_tila / mittausten_lkm > 0.1:
                break

            i += 1

        # Jos lämpötila on välillä, asetetaan edellinenMittaus muuttuja nollaan
        # ja aloitetaan looppi uudelleen.
        if viinin_lampotila >= 20 and viinin_lampotila <= 25:
            i += 1
            edellinen_mittaus = 0

    # Lopuksi kerrotaan onko viinin käymisprosessi onnistunut.
    # Jouduin lisäämään if komennon mittaustenLKM positiivisuudelle.
    if mittausten_lkm > 0:
        if edellinen_mittaus == 2:
            print("Your wine is ruined.")

        if viinin_tila / mittausten_lkm > 0.1 and edellinen_mittaus != 2:
            print("Your wine is ruined.")

        if edellinen_mittaus != 2 and viinin_tila / mittausten_lkm <= 0.1:
            print("Your wine is ready.")


main()