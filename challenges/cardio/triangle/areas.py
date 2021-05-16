import math

def area_isosceles(a,b):
  return (b*math.sqrt(math.pow(a,2)+math.pow(b,2)/4))/2

def area_equilatero(l):
  return pow(l,2) * math.sqrt(3) / 4

def area_rectangulo(b,h):
  return b*h/2

def area_escaleno(a,b,c):
  s = (a + b + c) / 2
  return math.sqrt(s*(s-a)*(s-b)*(s-c))
