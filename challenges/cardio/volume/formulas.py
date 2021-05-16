import math

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

def vol_cilindro():
    radio = get_param('el radio de la base')
    alto = get_param('la altura del cilindro')
    return math.pi * math.pow(radio,2) * alto

def vol_esfera():
    radio = get_param('el radio de la esfera')
    return math.pi * math.pow(radio, 3) * (4/3)

def vol_cubo():
    lado = get_param('el lado del cubo')
    return math.pow(lado,3)

def vol_piramide():
    tipo = int(get_param('el tipo de base de la pirámide\n([0] triangular;[1] Rectangular; [2] Poligonal)'))
    if tipo == 0:
        ancho = get_param('el ancho de la base')
        largo = get_param('el largo de la base')
        alto = get_param('el alto de la pirámide')
        return (ancho * largo * alto)/6
    elif tipo == 1:
        ancho = get_param('el ancho de la base')
        largo = get_param('el largo de la base')
        alto = get_param('el alto de la pirámide')
        return (ancho * largo * alto)/3
    elif tipo == 2:
        lados = get_param('el número de lados')
        apotema = get_param('el largo de la apotema')
        return math.pow(apotema,2) * lados * math.tan(math.pi/lados)
    else:
        return -1.0

def vol_cono():
    radio = get_param('el radio de la base')
    alto = get_param('la altura del cono')
    return (math.pi * math.pow(radio,2) * alto)/3

def vol_tetraedro():
    lado = get_param('el lado del tetraedro')
    return (math.pow(lado,3)*math.sqrt(2))/12

def vol_ortoedro():
    ancho_base = get_param('el ancho de la base')
    largo_base = get_param('el largo de la base')
    alto = get_param('la altura')
    return ancho_base * largo_base * alto

def vol_paralelepipedo():
    ancho_base = get_param('el ancho de la base')
    largo_base = get_param('el largo de la base')
    alto = get_param('la altura')
    return ancho_base * largo_base * alto

def get_fct(select):
    fct = {
        '0' : vol_cilindro,
        '1' : vol_cono,
        '2' : vol_esfera,
        '3' : vol_cubo,
        '4' : vol_ortoedro,
        '5' : vol_paralelepipedo,
        '6' : vol_piramide,
        '7' : vol_tetraedro
    }
    return fct.get(select)