import formulas

def run():
    print("="*60)
    print("          C A L C U L A D O R A  D E  V O L U M E N E S")
    print("="*60)
    print('''
        Ingresa el tipo de figura doméstica a evaluar:
        [0] = Cilindro      [1] = Cono      [2] = Esfera
        [3] = Cubo          [4] = Ortoedro  [5] = Paralelepidpedo
        [6] = Pirámide      [7] = Tetraedro
    ''')
    tipo = str(int(formulas.get_param('el tipo de figura a tratar')))
    calc = formulas.get_fct(tipo)
    out = calc()
    print(f'El volumen de la figura es {out:.4f}')

if __name__ == '__main__':
    run()