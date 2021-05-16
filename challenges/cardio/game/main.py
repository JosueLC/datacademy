from getpass import getpass

def check_score(inputs, scores):
    scene = "{}{}".format(inputs[0],inputs[1])
    rules = {
        '00' : [0,0],
        '01' : [0,1],
        '02' : [1,0],
        '10' : [1,0],
        '11' : [0,0],
        '12' : [0,1],
        '20' : [0,1],
        '21' : [1,0],
        '22' : [0,0]
    }
    scores = [sum(x) for x in zip(*[scores,rules.get(scene)])]
    return scores

def get_opc_player(name):
    valid = False
    while(valid == False):
        inp = getpass(prompt=f'{name} selecciona una opción ([0]=Piedra, [1]=Papel, [2]=Tijera) :')
        try:
            opc = int(inp)
            if opc < 3:
                valid = True
            else:
                raise ValueError
        except ValueError:
            print('Valor inválido. Intenta de nuevo.')
    return opc

if __name__ == '__main__':
    print('='*32)
    print("PIEDRA, PAPEL O TIJERA")
    print('='*32)
    pl1_name = input('Ingresa el nombre del primer jugador: ')
    pl2_name = input('Ingresa el nombre del segundo jugador: ')
    round_ = 1
    pl1_score = 0
    pl2_score = 0
    while (pl1_score < 3) and (pl2_score < 3):
        print('-'*40)
        print(f'{"="*10} ROUND {round_} {"="*10}')
        print(f'{pl1_name}: {pl1_score}  -  {pl2_name}: {pl2_score}')
        print('-'*40)
        #Jugador 1
        pl1_opc = get_opc_player(pl1_name)
        #Jugador 2
        pl2_opc = get_opc_player(pl2_name)
        pl1_score, pl2_score = check_score([pl1_opc, pl2_opc],[pl1_score, pl2_score])
        print(f'Nueva puntuación: {pl1_name}: {pl1_score}  -  {pl2_name}: {pl2_score}')
        round_ += 1
    print('='*40)
    print(f'GANADOR {pl1_name if pl1_score == 3 else pl2_name}.')