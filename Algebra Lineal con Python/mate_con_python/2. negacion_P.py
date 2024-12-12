'''
En este sentido no hay conectores lógicos sino se construyen desde un ciclo
y todos los conectores lógicos se pueden formar con un ciclo for. Piensa que
False < True, o bien, 0 < 1
'''

for P in [0, 1]:
     no_P = 1 - P
     print(P, no_P)

# Como una función
def negacion_P ():
     print("P", "¬P") # Imprimir encabezados
     for P in [1, 0]: # Modifiqué el orden del dominio
         no_P = 1 - P
         print(P, no_P)

# Llamando a la función
negacion_P()