MILE_TO_KM = 1.609344

def conv_mile_to_km(miles):
    return miles * MILE_TO_KM

def conv_km_to_mile(kms):
    return kms / MILE_TO_KM

def get_type_conv():
    valid = False
    while(valid == False):
        type_to_conv = input('[0]: Millas a Km    [1]: Km a Millas : ')
        if (type_to_conv == '0') or (type_to_conv == '1'):
            valid = True
        else:
            print('Valor inválido. Intenta de nuevo.')
    return type_to_conv

def get_float_value(prompt):
    valid = False
    out = 0.0
    while(valid == False):
        inp = input(prompt)
        try:
            out = float(inp)
            valid = True
        except ValueError:
            print('Inválido. Intente de nuevo.')
    return out

def run():
    print('='*40)
    print(f'{"="*5} CONVERSOR DE UNIDADES {"="*5}')
    print('Seleccione la unidad a convertir:')
    type_to_conv = get_type_conv()
    if type_to_conv == '0':
        input_ = get_float_value('Introduce las millas a convertir: ')
        out_ = conv_mile_to_km(input_)
        unit = 'km'
    elif type_to_conv == '1':
        input_ = get_float_value('Introduce los kms a convertir: ')
        out_ = conv_km_to_mile(input_)
        unit = 'mi'
    print(f'El resultado es {out_:.4f} {unit}')

if __name__ == '__main__':
    run()