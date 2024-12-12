# Construyamoms la disyunción

def disyuncion ():
     print('P', 'Q', 'P ∨ Q')
     for P in [1,0]:
          for Q in [1,0]:
               P_o_Q = max(P,Q) 
               print(f'{P} {Q}   {P_o_Q}')

disyuncion()