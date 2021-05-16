import math
import areas

def area_triangulo(a, b, c):
  lados = list(l for l in set((a,b,c)))
  if len(lados) == 1:
    tipo = "equilátero"
    area = areas.area_equilatero(lados[0])
  elif len(lados) == 2:
    if lados[1] == lados[0]*math.sqrt(2):
      tipo = "rectángulo"
      area = areas.area_rectangulo(lados[0],lados[1])
    else:
      tipo = "isósceles"
      area = areas.area_isosceles(lados[0],lados[1])
  else:
    if lados[2] == math.sqrt(math.pow(lados[0],2)+math.pow(lados[1],2)):
      tipo = "rectángulo"
      area = areas.area_rectangulo(lados[0],lados[1])
    else:
      tipo = "escaleno"
      area = areas.area_escaleno(a,b,c)
    
  return (f'Tienes un triángulo {tipo} con un área de {area:.4f} unidades cuadradas.')

if __name__ == '__main__':
    print("="*32)
    print("TIPO Y AREA DE UN TRIANGULO")
    print("="*32)
    print("Ingresa los lados del triángulo: ")
    lados = []
    for l in range(3): 
        valid = False
        while(valid == False):
            lado = input(f'Ingresa el lado {l+1}:')
            try:
                lados.append(float(lado))
                valid = True
            except ValueError:
                print('Valor inválido. Intenta de nuevo.')
    print(area_triangulo(lados[0],lados[1],lados[2]))