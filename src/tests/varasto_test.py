import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10, 0)
        self.toinenVarasto = Varasto(-3, 0)
        self.kolmasVarasto = Varasto(5, -3)
        self.neljasVarasto = Varasto(3, 10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_varastoon_liikaa_lisaaminen_tayttaa_varaston(self):
        self.varasto.lisaa_varastoon(12)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_varastosta_saatavilla_tilavuuden_verran_kun_lisatty_tayteen(self):
        self.varasto.lisaa_varastoon(12)
        
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_varastosta_palautetaan_senverran_kuin_on_jaljella_jos_yritetaan_ottaa_enemman(self):
        self.varasto.lisaa_varastoon(5)

        saatu_maara = self.varasto.ota_varastosta(8)

        self.assertAlmostEqual(saatu_maara, 5)

    def test_varasto_tyhjenee_kun_yritetaan_ottaa_enemman_kuin_on(self):
        self.varasto.lisaa_varastoon(5)

        self.varasto.ota_varastosta(8)

        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_varaston_tilavuus_ei_voi_olla_negatiivinen(self):
        self.assertAlmostEqual(self.toinenVarasto.paljonko_mahtuu(), 0)
        self.assertAlmostEqual(self.toinenVarasto.saldo, 0)

    def test_varaston_alkusaldo_vähintään_nolla(self):
        self.assertAlmostEqual(self.kolmasVarasto.saldo, 0)

    def test_varastolla_oikea_alkusaldo_kun_saldo_isompi_kuin_tilavuus(self):
        self.assertAlmostEqual(self.neljasVarasto.saldo, 3)

    def test_lisattava_negatiivinen_maara_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(-3)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_jos_yritetaan_ottaa_negatiivinen_maara_palautetaan_nolla(self):
        self.varasto.lisaa_varastoon(5)

        otettu = self.varasto.ota_varastosta(-5)

        self.assertAlmostEqual(otettu, 0)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_str_palauttaa_oikean_merkkijonon(self):
        self.varasto.lisaa_varastoon(4)

        self.assertEqual(self.varasto.__str__(), "saldo = 4, vielä tilaa 6")

    