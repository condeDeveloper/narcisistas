# narcisistas

```
153 = 1³ + 5³ + 3³
9474 = 9⁴ + 4⁴ + 7⁴ + 4⁴
```

Um número narcisista é igual à soma dos próprios dígitos elevados à quantidade de
dígitos. Eles são **88 ao todo** em base dez, e o maior tem 39 dígitos.

Repare no "ao todo". Não é "88 encontrados até agora" — a lista é **provadamente finita**,
e a prova cabe em duas linhas que este repositório executa antes de procurar qualquer
coisa.

```bash
python -m unittest discover -s testes -t . -v   # 20 testes
python -m ferramentas.medidor                   # todas as tabelas
python -m ferramentas.medidor --completo        # até 18 dígitos (job próprio)
```

Python 3.11+, sem dependência nenhuma fora da biblioteca padrão.

## A prova, em código

Um número de `n` dígitos vale **pelo menos** `10^(n-1)`. A soma das potências dos dígitos
dele vale **no máximo** `n · 9^n`, que é o caso de `n` noves. Quando o teto fica abaixo do
piso, nenhum número daquele tamanho consegue alcançar a própria soma — e nunca mais
conseguirá, porque `10^(n-1)` cresce mais rápido.

```
dígitos   teto: n·9^n              piso: 10^(n-1)           folga
1         9                        1                        +8
5         295.245                  10.000                   +285.245
10        34.867.844.010           1.000.000.000            +33.867.844.010
18        2.701.703.435.345.984.178   100.000.000.000.000.000   +2.601.703.435.345.984.178
```

A folga só cresce... até virar. O código procura o ponto de virada:

```
o maior n em que ainda é possível: 60
com 61 dígitos a folga já é −13.441.345.346.977.265.483.164.273.599.226.833.187.419.880.481.719.742.585.851
```

**A lista inteira cabe em 60 dígitos.** Isso sai sem buscar um número sequer.

## Varrer multiconjuntos, não números

A soma das potências dos dígitos **não depende da ordem** deles. `153`, `135`, `315` e
`531` dão todos a mesma soma. Então não é preciso varrer números — basta varrer
**multiconjuntos de dígitos**, que são `C(n+9, 9)`.

```
dígitos   multiconjuntos   números                    economia
3         220              900                        4x
6         5.005            900.000                    180x
10        92.378           9.000.000.000              97.430x
15        1.307.504        900.000.000.000.000        6,9 × 10⁸
18        4.686.825        900.000.000.000.000.000    1,9 × 10¹¹
60        56.672.074.888   9 × 10⁵⁹                   1,6 × 10⁴⁹
```

No teto do problema — 60 dígitos — a economia é de **dez elevado a quarenta e nove**. É a
diferença entre uma varredura impossível e uma tabela.

O detalhe que faz isso funcionar: depois de calcular a soma do multiconjunto, não basta
ela estar na faixa certa. É preciso conferir que os **dígitos ordenados da soma** são
exatamente o multiconjunto que a gerou. Sem essa conferência, a busca aceitaria somas que
batem o valor mas não os dígitos.

## O que foi encontrado

```
dígitos   quantos   quais
1         10        0 a 9
2          0        (nenhum)
3          4        153, 370, 371, 407
4          3        1634, 8208, 9474
5          3        54748, 92727, 93084
6          1        548834
7          4        1741725, 4210818, 9800817, 9926315
8          3        24678050, 24678051, 88593477
9          4        146511208, 472335975, 534494836, 912985153
10         1        4679307774
11         8        32164049650, 32164049651, 40028394225, ...
12         0        (nenhum)
14         1        28116440335967
16         2        4338281769391370, 4338281769391371
17         3        21897142587612075, 35641594208964132, 35875699062250035
```

**47 narcisistas até 18 dígitos**, varridos em 38 segundos — contra `10¹⁸` números que a
força bruta precisaria olhar.

E um padrão que não estava no plano: **pares consecutivos**. `24678050` e `24678051`,
`32164049650` e `32164049651`, `4338281769391370` e `4338281769391371`. Três vezes, em
tamanhos diferentes, dois narcisistas vizinhos.

## As conferências

```
multiconjunto x número a número : 6 tamanhos conferidos
   a força bruta testou 1.000.000 de números
todo achado é mesmo narcisista  : 41 conferidos
```

O juiz varre inteiro por inteiro e não sabe que a ordem dos dígitos não importa. Ele só
alcança seis dígitos — e é por isso que serve: onde ele chega, a resposta tem que ser a
mesma.

## O que as medidas me corrigiram

**Esperei a quantidade crescer com os dígitos.** Com 11 dígitos são **oito** narcisistas,
o recorde da faixa medida. Com 12, são **zero**. Com 13, zero. Com 14, um. A sequência
não tem tendência nenhuma: ela oscila e some.

**Achei que o 2 fosse o único tamanho vazio.** São vários — 2, 12, 13, 15 e 18 não têm
nenhum narcisista, dentro do que foi varrido. O vazio do 2 é famoso; os outros são iguais
a ele e ninguém fala deles.

**Quase conferi só a soma.** A primeira ideia da busca por multiconjuntos era aceitar
qualquer soma que caísse na faixa de `n` dígitos. Isso aceita lixo: a soma precisa ter
**exatamente aqueles dígitos**, e não apenas o tamanho certo. A conferência que salva é
comparar `sorted(digitos_de(soma))` com o multiconjunto — uma linha, sem a qual a tabela
inteira sairia inflada.

**O teto de 60 dígitos não é o maior narcisista.** São coisas diferentes: 60 é onde a
*possibilidade* acaba; o maior narcisista de verdade tem **39**. Entre 40 e 60 dígitos a
aritmética ainda permite, e mesmo assim não existe nenhum. A tabela do README diz qual
das duas coisas ela está medindo.

## Quatro achados

1. **A lista é finita, e a prova não procura nada:** o teto `n·9^n` cai abaixo do piso
   `10^(n-1)` em **61 dígitos**, então tudo cabe em 60 — calculado em milissegundos, antes
   de qualquer busca.
2. **Varrer multiconjuntos em vez de números economiza 10⁴⁹ vezes** no teto do problema:
   56.672.074.888 combinações contra 9 × 10⁵⁹ inteiros.
3. **47 narcisistas até 18 dígitos**, e a contagem por tamanho não tem tendência: sobe a
   oito em 11 dígitos e cai a **zero** em 12 e 13.
4. Narcisistas aparecem **em pares consecutivos** três vezes nos tamanhos medidos —
   24678050/51, 32164049650/51 e 4338281769391370/71.
