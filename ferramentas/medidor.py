# -*- coding: utf-8 -*-
"""Roda as tabelas que vao para o README.

    python -m ferramentas.medidor
    python -m ferramentas.medidor --completo
"""
import sys
import time

from narcisistas import busca, juiz, varredura

DIGITOS = 12
DIGITOS_JUIZ = 6
DIGITOS_COMPLETO = 18


def titulo(texto):
    print()
    print(texto)
    print('-' * len(texto))


def a_lista():
    titulo('Os narcisistas com ate %d digitos' % DIGITOS)
    print('%-10s %-10s %s' % ('digitos', 'quantos', 'quais'))
    total = 0
    for n, quantos, quais in varredura.por_quantidade_de_digitos(DIGITOS):
        total += quantos
        texto = ', '.join(str(x) for x in quais) if quais else '(nenhum)'
        if len(texto) > 64:
            texto = texto[:61] + '...'
        print('%-10d %-10d %s' % (n, quantos, texto))
    print()
    print('total ate %d digitos: %d' % (DIGITOS, total))
    vazios, quais = varredura.vazios(DIGITOS)
    print('quantidades de digitos sem nenhum narcisista: %d  %s' % (vazios, quais))


def a_prova():
    titulo('Por que a lista e finita')
    print('Um numero de n digitos vale pelo menos 10^(n-1).')
    print('A soma das potencias dos digitos dele vale no maximo n * 9^n.')
    print('Quando o teto fica abaixo do piso, acabou — para esse n e para todos os maiores.')
    print()
    print('%-8s %-24s %-24s %s' % ('digitos', 'teto: n * 9^n', 'piso: 10^(n-1)', 'folga'))
    for n, teto, piso, f in varredura.tabela_da_folga(DIGITOS_COMPLETO):
        print('%-8d %-24d %-24d %s' % (n, teto, piso, '%+d' % f))
    limite = busca.maior_quantidade_de_digitos_possivel()
    print()
    print('o maior n em que ainda e possivel: %d' % limite)
    print('com %d digitos a folga ja e %+d' % (limite + 1, busca.folga(limite + 1)))
    print()
    print('Entao a lista inteira cabe em %d digitos, e e finita. Sem busca nenhuma.' % limite)


def a_economia():
    titulo('Multiconjuntos contra numeros')
    print('%-8s %-18s %-24s %s' % ('digitos', 'multiconjuntos', 'numeros', 'economia'))
    for n, multi, nums, razao in varredura.economia(DIGITOS_COMPLETO):
        print('%-8d %-18d %-24d %.3e vezes' % (n, multi, nums, razao))
    print()
    n = busca.maior_quantidade_de_digitos_possivel()
    print('com %d digitos, que e o teto do problema:' % n)
    print('   multiconjuntos: %d' % busca.quantos_multiconjuntos(n))
    print('   numeros       : %d' % busca.quantos_numeros(n))
    print('   economia      : %.3e vezes'
          % (busca.quantos_numeros(n) / busca.quantos_multiconjuntos(n)))


def o_juiz():
    titulo('As duas conferencias')
    print('multiconjunto x numero a numero: %d tamanhos conferidos (ate %d digitos)'
          % (varredura.conferir_contra_juiz(DIGITOS_JUIZ), DIGITOS_JUIZ))
    testados = sum(juiz.quantos_testados(n) for n in range(1, DIGITOS_JUIZ + 1))
    print('   a forca bruta testou %d numeros' % testados)
    todos = busca.ate_n_digitos(DIGITOS)
    print('todo achado e mesmo narcisista : %d conferidos' % varredura.conferir_propriedade(todos))


def completo():
    titulo('Varredura ate %d digitos' % DIGITOS_COMPLETO)
    comeco = time.time()
    total = 0
    for n in range(1, DIGITOS_COMPLETO + 1):
        achados = busca.com_n_digitos(n)
        total += len(achados)
        if achados:
            print('%2d digitos: %s' % (n, ', '.join(str(x) for x in achados)))
    print()
    print('total ate %d digitos: %d' % (DIGITOS_COMPLETO, total))
    multiconjuntos = sum(busca.quantos_multiconjuntos(n)
                         for n in range(1, DIGITOS_COMPLETO + 1))
    numeros = sum(busca.quantos_numeros(n) for n in range(1, DIGITOS_COMPLETO + 1))
    print('multiconjuntos olhados: %d' % multiconjuntos)
    print('numeros que a forca bruta olharia: %d' % numeros)
    print('economia: %.3e vezes' % (numeros / multiconjuntos))
    print()
    print('tempo: %.1f s' % (time.time() - comeco))

    if busca.maior_quantidade_de_digitos_possivel() != 60:
        print('MEDIDA MUDOU: o teto de digitos deveria ser 60')
        sys.exit(1)
    print('o teto de %d digitos bateu' % 60)


def main():
    if '--completo' in sys.argv:
        completo()
        return
    a_lista()
    a_prova()
    a_economia()
    o_juiz()


if __name__ == '__main__':
    main()
