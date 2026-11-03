# -*- coding: utf-8 -*-
"""Os numeros do README, presos. Todos sairam do medidor."""
import unittest

from ferramentas import medidor
from narcisistas import busca, juiz, varredura


class TestMedidas(unittest.TestCase):

    def test_quarenta_e_um_ate_doze_digitos(self):
        total = sum(q for _, q, _ in varredura.por_quantidade_de_digitos(medidor.DIGITOS))
        self.assertEqual(total, 41)
        self.assertEqual(len(busca.ate_n_digitos(medidor.DIGITOS)), 41)

    def test_a_contagem_por_quantidade_de_digitos(self):
        esperado = {1: 10, 2: 0, 3: 4, 4: 3, 5: 3, 6: 1,
                    7: 4, 8: 3, 9: 4, 10: 1, 11: 8, 12: 0}
        for n, quantos, _ in varredura.por_quantidade_de_digitos(medidor.DIGITOS):
            self.assertEqual(quantos, esperado[n], 'com %d digitos' % n)

    def test_dois_tamanhos_sem_nenhum_narcisista(self):
        vazios, quais = varredura.vazios(medidor.DIGITOS)
        self.assertEqual(vazios, 2)
        self.assertEqual(quais, [2, 12])

    def test_o_teto_de_sessenta_digitos(self):
        self.assertEqual(busca.maior_quantidade_de_digitos_possivel(), 60)
        self.assertEqual(busca.quantos_multiconjuntos(60), 56_672_074_888)
        self.assertEqual(busca.quantos_numeros(60), 9 * 10 ** 59)

    def test_a_economia_no_teto_e_de_dez_a_quarenta_e_nove(self):
        razao = busca.quantos_numeros(60) / busca.quantos_multiconjuntos(60)
        self.assertAlmostEqual(razao / 1e49, 1.588, places=3)

    def test_a_economia_cresce_com_os_digitos(self):
        linhas = varredura.economia(18)
        self.assertAlmostEqual(linhas[0][3], 1.0, places=6)
        self.assertAlmostEqual(linhas[5][3], 179.8, places=1)
        for anterior, seguinte in zip(linhas, linhas[1:]):
            self.assertGreater(seguinte[3], anterior[3])

    def test_as_duas_conferencias(self):
        self.assertEqual(varredura.conferir_contra_juiz(medidor.DIGITOS_JUIZ), 6)
        testados = sum(juiz.quantos_testados(n)
                       for n in range(1, medidor.DIGITOS_JUIZ + 1))
        self.assertEqual(testados, 1_000_000)
        todos = busca.ate_n_digitos(medidor.DIGITOS)
        self.assertEqual(varredura.conferir_propriedade(todos), 41)

    def test_o_maior_de_onze_digitos(self):
        onze = busca.com_n_digitos(11)
        self.assertEqual(len(onze), 8)
        self.assertEqual(onze[0], 32_164_049_650)
        self.assertEqual(onze[1], 32_164_049_651)

    def test_os_vizinhos_que_sao_os_dois_narcisistas(self):
        # 24678050 e 24678051 sao consecutivos e os dois narcisistas
        self.assertIn(24_678_050, busca.com_n_digitos(8))
        self.assertIn(24_678_051, busca.com_n_digitos(8))
        self.assertIn(32_164_049_650, busca.com_n_digitos(11))
        self.assertIn(32_164_049_651, busca.com_n_digitos(11))


if __name__ == '__main__':
    unittest.main()
