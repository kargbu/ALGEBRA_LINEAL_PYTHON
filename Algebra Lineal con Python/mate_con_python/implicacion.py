# Construyamoms la implicación

def implicacion ():
     print('P', 'Q', 'P ⟹ Q')
     for P in [1,0]:
          for Q in [1,0]:
               P_implica_Q = max(1 - P,Q) 
               print(f'{P} {Q}   {P_implica_Q}')

implicacion()