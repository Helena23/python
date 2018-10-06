import  sys

arg = sys.argv

vao = float(arg[1])
degrauIdeal = 0.17
numDegraus = vao / degrauIdeal
espelho = vao / numDegraus
conversorParaCm = 100
piso1 = (2 * (conversorParaCm * espelho)) - 63
piso2 = (2 * (conversorParaCm * espelho)) - 64
if(arg[2] == "v"):
    print(" Vão:{}\n Número de degraus:{}\n Espelho:{}\n Piso1:{}\n Piso2:{}".format(vao, numDegraus, espelho, piso1,
                                                                                     piso2))
elif(arg[2] == "p"):
    print("Piso1:{}\nPiso2:{}".format(piso1,piso2))

