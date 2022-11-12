class Varasto:
    def __init__(self, tilavuus, alku_saldo):
        if tilavuus > 0.0:
            self.tilavuus = tilavuus
        else:
            # virheellinen, nollataan
            self.tilavuus = 0.0

        if alku_saldo < 0.0:
            # virheellinen, nollataan
            self.saldo = 0.0
        elif alku_saldo <= self.tilavuus:
            # mahtuu
            self.saldo = alku_saldo
        else:
            # täyteen ja ylimäärä hukkaan!
            self.saldo = self.tilavuus

    # huom: ominaisuus voidaan myös laskea. Ei tarvita erillistä kenttää viela_tilaa tms.
    def paljonko_mahtuu(self):
        if self.tilavuus > 0: #tänne lisätty turhia lohkoja jotta nested blocks sääntö rikkoutuu
            if self.saldo > 0:
                if self.tilavuus > self.saldo:
                    return self.tilavuus - self.saldo
                else:
                    return 0.0
            else:
                return self.tilavuus
        else:
            return 0

    def lisaa_varastoon(self, maara):
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        eka = 4 #lisätty rikkomaan max statements
        toka = 3
        kolmas = 2
        summa = eka + toka
        summa += kolmas
        print(summa)

        lista =[]
        lista.append(eka)
        lista.append(toka)
        lista.append(kolmas)

        print(max(lista))
        return maara

    def __str__(self):
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
