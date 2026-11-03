# -*- coding: utf-8 -*-
import unittest

from narcisistas import busca, juiz


class TestBusca(unittest.TestCase):

    def test_os_classicos(self):
        for n in (153, 370, 371, 407, 1634, 8208, 9474):
            self.assertTrue(busca.eh_narcisista(n), n)
            self.assertTrue(juiz.eh_narcisista(n), n)

    def test_o_153(self):
        self.assertEqual(1 ** 3 + 5 ** 3 + 3 ** 3, 153)

    def test_todo_digito_sozinho_e_narcisista(self):
        for n in range(10):
            self.assertTrue(busca.eh_narcisista(n), n)
        self.assertEqual(busca.com_n_digitos(1), list(range(10)))

    def test_nao_existe_com_dois_digitos(self):
        self.assertEqual(busca.com_n_digitos(2), [])
        self.assertEqual(juiz.com_n_digitos(2), [])

    def test_os_de_tres_e_quatro_digitos(self):
        self.assertEqual(busca.com_n_digitos(3), [153, 370, 371, 407])
        self.assertEqual(busca.com_n_digitos(4), [1634, 8208, 9474])

    def test_o_multiconjunto_acha_o_mesmo_que_a_forca_bruta(self):
        for n in range(1, 7):
            self.assertEqual(busca.com_n_digitos(n), juiz.com_n_digitos(n), 'n = %d' % n)

    def test_a_contagem_de_multiconjuntos(self):
        # C(n+9, 9)
        self.assertEqual(busca.quantos_multiconjuntos(1), 10)
        self.assertEqual(busca.quantos_multiconjuntos(2), 55)
        self.assertEqual(busca.quantos_multiconjuntos(3), 220)
        self.assertEqual(busca.quantos_multiconjuntos(10), 92378)

    def test_a_prova_de_finitude(self):
        self.assertEqual(busca.maior_quantidade_de_digitos_possivel(), 60)
        self.assertGreater(busca.folga(60), 0)
        self.assertLess(busca.folga(61), 0)

    def test_a_folga_so_cresce_e_depois_vira(self):
        # ate certo ponto o teto ganha do piso com folga crescente
        for n in range(1, 20):
            self.assertGreater(busca.folga(n), 0, 'n = %d' % n)
        # e a partir de 61 nunca mais
        for n in range(61, 70):
            self.assertLess(busca.folga(n), 0, 'n = %d' % n)

    def test_digitos_de(self):
        self.assertEqual(busca.digitos_de(153), [1, 5, 3])
        self.assertEqual(busca.digitos_de(0), [0])
        self.assertEqual(busca.digitos_de(9474), [9, 4, 7, 4])

    def test_entrada_invalida_e_recusada(self):
        with self.assertRaises(ValueError):
            busca.com_n_digitos(0)
        with self.assertRaises(ValueError):
            busca.digitos_de(-1)
        with self.assertRaises(ValueError):
            juiz.eh_narcisista(-1)


if __name__ == '__main__':
    unittest.main()
