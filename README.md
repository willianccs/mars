# Explorando Marte

Projeto de programação que simula a exploração de uma àrea de Marte com sondas espaciais.

## Funcionamento

Cada sonda é inserida na àrea apontando para uma direção (norte, leste, oeste ou sul). Dada essa posição inicial e uma sequência de movimentos (virar 90 graus para a esquerda, para a direita, ou mover-se um ponto a frente), o programa deve retornar a posição final da sonda.

## Entrada

A primeira linha da entrada de dados é a coordenada do ponto superior-direito da malha do planalto. Lembrando que a inferior esquerda sempre será (0,0).

O resto da entrada será informação das sondas que foram implantadas. Cada sonda é representada por duas linhas. A primeira indica sua posição inicial e a segunda uma série de instruções indicando para a sonda como ela deverá explorar o planalto.

A posição é representada por dois inteiros e uma letra separados por espaços, correpondendo à coordenada X-Y e à direção da sonda.
Cada sonda será controlada sequencialmente, o que quer dizer que a segunda sonda só irá se movimentar após que a primeira tenha terminado suas instruções.

## Saída

A saída deverá contar uma linha para cada sonda, na mesma ordem de entrada, indicando sua coordenada final e direção.

### Exemplos de Entrada e Saída

```code
####Entrada de Teste:
5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM
```

#### Saída esperada:

```code
1 3 N
5 1 E
```

## USO:

### Host

1.Clone o repositório

```code
git clone git@github.com:willianccs/mars.git
```

2.Dentro do diretório clonado, execute a aplicação

```code
python3 mars.py
```

3.Siga as intruções da aplicação e insira os dados solicitados.

### Docker

1.Clone o repositório

```code
git clone git@github.com:willianccs/mars.git
```

2.Dentro do diretório clonado, build a imagem localmente e execute a aplicação

```code
docker build -t explorando-marte .
docker run -it explorando-marte
```

3.Siga as intruções da aplicação e insira os dados solicitados.
