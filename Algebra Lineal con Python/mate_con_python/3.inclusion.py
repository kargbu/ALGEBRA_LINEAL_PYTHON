''' El operador inclusión se puede codear de la siguiente manera:

for P in [True, False]:
     for Q in [True, False]:
          print(P, Q, P and Q)
'''
'''
def el_y ():
     print('P', 'Q', 'P ∧ Q')
     for P in [1, 0]:
          for Q in [1, 0]:
                print(f'{P} {Q}   {P and Q}')

# Llamando a la función
el_y ()


Podemos definir con una función a la inclusión.
'''

def inclusion ():
     print('P', 'Q', 'P ∧ Q')
     for P in [1,0]:
          for Q in [1,0]:
               P_y_Q = P * Q
               print(f'{P} {Q}   {P_y_Q}')

inclusion()