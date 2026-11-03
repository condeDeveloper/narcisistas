# -*- coding: utf-8 -*-
"""Mede a busca e confere os dois caminhos."""
from . import busca, juiz


def conferir_contra_juiz(ate_digitos):
    """Compara a busca por multiconjuntos com a varredura numero a numero.

    Devolve quantos tamanhos de numero foram conferidos.
    """
    conferidos = 0
    for n in range(1, ate_digitos + 1):
        por_multiconjunto = busca.com_n_digitos(n)
        por_forca_bruta = juiz.com_n_digitos(n)
        if por_multiconjunto != por_forca_bruta:
            raise AssertionError(
                'com %d digitos os dois discordam: multiconjunto %r, bruta %r'
                % (n, por_multiconjunto, por_forca_bruta))
        conferidos += 1
    return conferidos


def conferir_propriedade(numeros):
    """Confere, um a um, que todo numero achado e mesmo narcisista."""
    for n in numeros:
        if not busca.eh_narcisista(n):
            raise AssertionError('%d nao e narcisista' % n)
        if not juiz.eh_narcisista(n):
            raise AssertionError('o juiz discorda de %d' % n)
    return len(numeros)


def por_quantidade_de_digitos(ate_digitos):
    """Quantos narcisistas existem com cada quantidade de digitos."""
    linhas = []
    for n in range(1, ate_digitos + 1):
        achados = busca.com_n_digitos(n)
        linhas.append((n, len(achados), achados))
    return linhas


def economia(ate_digitos):
    """Multiconjuntos contra numeros, por quantidade de digitos."""
    linhas = []
    for n in range(1, ate_digitos + 1):
        multi = busca.quantos_multiconjuntos(n)
        nums = busca.quantos_numeros(n)
        linhas.append((n, multi, nums, nums / multi))
    return linhas


def tabela_da_folga(ate_digitos):
    """A folga entre o teto da soma e o menor numero, por quantidade de digitos."""
    return [(n, n * 9 ** n, 10 ** (n - 1), busca.folga(n))
            for n in range(1, ate_digitos + 1)]


def vazios(ate_digitos):
    """Quantas quantidades de digitos nao tem narcisista nenhum."""
    quantos = 0
    quais = []
    for n, achados, _ in por_quantidade_de_digitos(ate_digitos):
        if achados == 0:
            quantos += 1
            quais.append(n)
    return quantos, quais
