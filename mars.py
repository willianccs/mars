# Class for Rover.
class Rover:
    def __init__(self, direction, pos_x, pos_y):
        self.direction = direction
        self.pos_x = pos_x
        self.pos_y = pos_y


# Class for Plateau.
class Plateau:
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y


# Main block.
def main():
    try:
        qtd_sonda = int(input("Insira a quantidade de sondas: "))
    except ValueError:
        print("Erro ao converter para número inteiro. Certifique-se de inserir apenas um número")
        return
    dims = input(
        "Insira as dimensões do planalto (area) separado por espaço (ex: 5 5): ")
    planalto = criar_planalto(dims)
    if type(planalto) is str:
        print(planalto)
        return

    sonda_arr = []
    i = 0
    while i < qtd_sonda:
        pos = input(
            "Insira as coordenadas X, Y, D - posicao e direcao - para a sonda (ex: 1 2 N): ")
        rov = criar_sonda(pos, planalto)
        if type(rov) is str:
            print(rov)
        else:
            direcoes = input(
                "Insira os comandos (sequencia de movimentos) para a sonda - L,M,R (ex: LMLMLMLMM): ")
            sonda_arr.append(executar_comandos(planalto, rov, direcoes))
            i = i + 1

    for x in sonda_arr:
        print(str(x.pos_x) + " " + str(x.pos_y) + " " + x.direction)


# Function that creates plateau. Returns Plateau object.
def criar_planalto(dims):
    separador = dims.find(" ")
    if separador == -1:
        return "Erro: espaço não identificado."
    size_x = int(dims[0:separador])
    size_y = int(dims[separador+1:])
    return Plateau(size_x, size_y)


# Function that creates Rover. Returns Rover object.
def criar_sonda(pos, planalto):
    separador = pos.find(" ")
    if separador == -1:
        return "Erro: espaço não identificado."
    pos_x = int(pos[0:separador])
    if pos_x > planalto.size_x:
        return "Erro: a coordenada X está fora dos limites."
    _pos = pos[separador+1:]
    _separador = _pos.find(" ")
    pos_y = int(_pos[0:_separador])
    if pos_y > planalto.size_y:
        return "Erro: a coordenada Y está fora dos limites."
    direc = _pos[_separador+1:].upper()
    if direc != "N" and direc != "E" and direc != "S" and direc != "W":
        return "Erro: direção inválida. Insira novamente a posição e direção da sonda: "
    return Rover(direc, pos_x, pos_y)


# Function that processes the command string.
def executar_comandos(planalto, rov, commands):
    for i in range(0, len(commands)):
        if commands[i].upper() == "L":
            rov.direction = mudar_direcao(rov.direction, "L")
        elif commands[i].upper() == "R":
            rov.direction = mudar_direcao(rov.direction, "R")
        elif commands[i].upper() == "M":
            rov = move(rov, planalto)
        else:
            print("Entrada inválida")
    return rov


# Function to change rover direction
def mudar_direcao(direction, turn):
    if direction == "N":
        if turn == "L":
            return "W"
        elif turn == "R":
            return "E"
    elif direction == "E":
        if turn == "L":
            return "N"
        elif turn == "R":
            return "S"
    elif direction == "S":
        if turn == "L":
            return "E"
        elif turn == "R":
            return "W"
    elif direction == "W":
        if turn == "L":
            return "S"
        elif turn == "R":
            return "N"


# Function to move rover.
def move(rover, planalto):
    if rover.direction == "N":
        if rover.pos_y < planalto.size_y:
            rover.pos_y = rover.pos_y + 1
    elif rover.direction == "E":
        if rover.pos_x < planalto.size_x:
            rover.pos_x = rover.pos_x + 1
    elif rover.direction == "S":
        if rover.pos_y > 0:
            rover.pos_y = rover.pos_y - 1
    elif rover.direction == "W":
        if rover.pos_x > 0:
            rover.pos_x = rover.pos_x - 1
    return rover


main()
