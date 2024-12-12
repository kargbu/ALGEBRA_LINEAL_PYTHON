''' 
Una proposición es un enunciado que se puede evaluar de verdadero o falso.
En programación se habla de una sentencia booleana. La manera en la cual
se aproximan a dichos conceptos es desde las evaluaciones de las tablas de
verdad de proposiciones.
'''

# Por ejemplo la tabla de verdad de la negación será

for P in [True, False]:
    print(P, not P)

'''
En python ∧ es or, el ∨ es and, ➔ es <= y ⟺ es ==. Así es como podemos 
construir todos los operadores lógicos de dos maneras, como operadores
booleanos o como una función con un argumento
'''

for P in [True, False]:
     for Q in [True, False]:
          print(P, Q, P and Q)