# your code goes here
from math import floor
entrada = input()

try :
    numero = int(entrada)
except ValueError :
    numero = floor(entrada)
    
resultado = "Par" if numero % 2 == 0 else "Impar"
print(resultado)
