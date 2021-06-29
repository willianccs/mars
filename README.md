# Explorando Marte

Projeto de programação que simula a exploração de uma àrea de Marte com sondas espaciais.

## Funcionamento:

Cada sonda é inserida na àrea apontando para uma direção (norte, leste, oeste ou sul). Dada essa posição inicial e uma sequência de movimentos (virar 90 graus para a esquerda, para a direita, ou mover-se um ponto a frente), o programa deve retornar a posição final da sonda.

## ENTRADA

A primeira linha da entrada de dados é a coordenada do ponto superior-direito da malha do planalto. Lembrando que a inferior esquerda sempre será (0,0).

O resto da entrada será informação das sondas que foram implantadas. Cada sonda é representada por duas linhas. A primeira indica sua posição inicial e a segunda uma série de instruções indicando para a sonda como ela deverá explorar o planalto.

A posição é representada por dois inteiros e uma letra separados por espaços, correpondendo à coordenada X-Y e à direção da sonda.
Cada sonda será controlada sequencialmente, o que quer dizer que a segunda sonda só irá se movimentar após que a primeira tenha terminado suas instruções.

## SAÍDA

A saída deverá contar uma linha para cada sonda, na mesma ordem de entrada, indicando sua coordenada final e direção.

### Exemplos de Entrada e Saída:

####Entrada de Teste:
```
5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM
```

#### Saída esperada:
```
1 3 N
5 1 E
```
