def get_param(name):
    val = 0.0
    invalid = True
    while(invalid):
        input_ = input(f'Ingresa el valor para {name}: ')
        try:
            val = float(input_)
            invalid = False
        except ValueError:
            print('Entrada inválida.')
    return val

def run():
    play = True
    lim_inf = get_param('el límite inferior')
    lim_sup = get_param('el límite superior')
    while(play):
        valor = get_param('comparar')
        if (valor > lim_inf) and (valor < lim_sup):
            print(f'el número {valor} está en el rango. Fin.')
            play = False
        elif (valor < lim_inf):
            lim_inf = valor
            print(f'Valor muy bajo. El nuevo límite inferior es {lim_inf}')
        elif (valor > lim_sup):
            lim_sup = valor
            print(f'Valor muy alto. El nuevo límite superior es {lim_sup}')

if __name__ == '__main__':
    run()