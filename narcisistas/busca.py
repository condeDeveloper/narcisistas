# -*- coding: utf-8 -*-
"""Numeros narcisistas: iguais a soma dos proprios digitos elevados a
quantidade de digitos.

    153  = 1^3 + 5^3 + 3^3
    9474 = 9^4 + 4^4 + 7^4 + 4^4

Existem exatamente 88 deles em base dez, e o maior tem 39 digitos. Nao e
"ate onde procuraram": e teorema, e a prova cabe numa linha (veja
``maior_quantidade_de_digitos_possivel``).

O problema de enumerar e que varrer os numeros de 39 digitos e impossivel.
O truque e varrer MULTICONJUNTOS de digitos: a soma das potencias nao depende
da ORDEM dos digitos, so de quantos de cada um existem. Com n digitos, sao
C(n+9, 9) multiconjuntos em vez de 10^n numeros — para n = 15, a diferenca e
de 1,3 milhao contra um quatrilhao.
"""
from itertools import combinations_with_replacement


def soma_das_potencias(digitos, expoente):
    """A soma de cada digito elevado ao expoente."""
    return sum(d ** expoente for d in digitos)


def digitos_de(n):
    """Os digitos de n, em ordem."""
    if n < 0:
        raise ValueError('n nao pode ser negativo: %r' % (n,))
    return [int(c) for c in str(n)]


def eh_narcisista(n):
    """True se n e igual a soma dos digitos elevados a quantidade de digitos."""
    ds = digitos_de(n)
    return n == soma_das_potencias(ds, len(ds))


def com_n_digitos(n):
    """Todos os narcisistas com exatamente n digitos, por multiconjunto.

    Para cada combinacao de n digitos (com repeticao, sem ordem), calcula a
    soma das potencias e pergunta se o resultado tem exatamente esses digitos.
    A ordem nao importa para a soma, mas importa para a igualdade — e por isso
    a conferencia final compara os digitos ORDENADOS.
    """
    if n < 1:
        raise ValueError('n tem que ser positivo: %r' % (n,))
    menor = 10 ** (n - 1) if n > 1 else 0
    maior = 10 ** n - 1
    achados = []
    for combinacao in combinations_with_replacement(range(10), n):
        soma = soma_das_potencias(combinacao, n)
        if soma < menor or soma > maior:
            continue
        if sorted(digitos_de(soma)) == list(combinacao):
            achados.append(soma)
    return sorted(achados)


def ate_n_digitos(n):
    """Todos os narcisistas com ate n digitos."""
    saida = []
    for k in range(1, n + 1):
        saida.extend(com_n_digitos(k))
    return saida


def quantos_multiconjuntos(n):
    """C(n+9, 9): quantos multiconjuntos de n digitos existem."""
    numerador = 1
    for i in range(9):
        numerador = numerador * (n + 9 - i) // (i + 1)
    return numerador


def quantos_numeros(n):
    """Quantos numeros de exatamente n digitos existem."""
    return 9 * 10 ** (n - 1) if n > 1 else 10


def maior_quantidade_de_digitos_possivel():
    """A prova de que a lista e finita, em codigo.

    Um numero de n digitos vale pelo menos 10^(n-1). A soma das potencias dos
    digitos dele vale no maximo n * 9^n, que e o caso de n noves. Quando
    n * 9^n fica MENOR que 10^(n-1), nenhum numero de n digitos consegue
    alcancar a propria soma, e acabou — para esse n e para todos os maiores,
    porque 10^(n-1) cresce mais rapido.

    Devolve o maior n em que ainda e possivel.
    """
    n = 1
    while n * 9 ** n >= 10 ** (n - 1):
        n += 1
    return n - 1


def folga(n):
    """Quanto o teto da soma passa do menor numero de n digitos.

    Positivo quer dizer que ainda e possivel; negativo, que acabou.
    """
    return n * 9 ** n - 10 ** (n - 1)
