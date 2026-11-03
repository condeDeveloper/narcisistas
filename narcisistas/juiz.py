# -*- coding: utf-8 -*-
"""O juiz: testa numero por numero, do primeiro ao ultimo.

Nao conhece multiconjunto, nao sabe que a ordem dos digitos nao importa, e nao
pula nada. Para cada inteiro no intervalo, soma os digitos elevados a
quantidade de digitos e compara.

E inviavel acima de sete ou oito digitos — e e exatamente por isso que ele
serve de juiz: ele nao tem como estar errado, so lento.
"""


def eh_narcisista(n):
    """True se n e narcisista, decidido na marra."""
    if n < 0:
        raise ValueError('n nao pode ser negativo: %r' % (n,))
    texto = str(n)
    expoente = len(texto)
    soma = 0
    for caractere in texto:
        soma += int(caractere) ** expoente
        if soma > n:
            return False
    return soma == n


def varrer(baixo, alto):
    """Todos os narcisistas no intervalo, testando um por um."""
    if baixo < 0 or alto < baixo:
        raise ValueError('intervalo invalido: %r a %r' % (baixo, alto))
    return [n for n in range(baixo, alto + 1) if eh_narcisista(n)]


def com_n_digitos(n):
    """Todos os narcisistas de exatamente n digitos, pela varredura bruta."""
    if n < 1:
        raise ValueError('n tem que ser positivo: %r' % (n,))
    if n == 1:
        return varrer(0, 9)
    return varrer(10 ** (n - 1), 10 ** n - 1)


def quantos_testados(n):
    """Quantos inteiros a varredura bruta precisa olhar para n digitos."""
    return 10 if n == 1 else 9 * 10 ** (n - 1)
