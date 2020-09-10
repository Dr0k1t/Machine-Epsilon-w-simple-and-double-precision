import numpy as np
#Ejercicio 1
sim_e = 1
while np.float32(sim_e + 1) > 1: #numpy to convert
    sim_e /= 2
sim_e *= 2 #para cumplir con la fórmula B^(L-1)

print("El epsilon de la máquina con presición simple es:" , sim_e)
print("Simple con np.finfo", np.finfo(np.float32).eps)

doub_e = 1
while np.float(doub_e + 1) > 1:
    doub_e/= 2
doub_e *= 2 #para cumplir con la fórmula B^(L-1)

print("El epsilon de la máquina con doble precisión es:", doub_e)
print("Doble con np.finfo", np.finfo(np.float).eps)
