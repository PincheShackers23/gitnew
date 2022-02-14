import random
import numpy as np

contador = np.zeros(50)
cromo = np.zeros((50,20))
cromoOld = np.zeros((50,20))
acumulada = np.zeros(50)
nuevaPoblacion = np.zeros((50,20))
repes = 0
hijos = np.zeros((2, 20))
encuentro = 0
calTotal = 0
numeroCool = 0
generacion = 0

# Creacion de cadenas de binarios (cromosomas)

for i in range(0,50): #Numero de cromosomas
    for j in range(0,20): #Numero de genes
        cromo[i][j] = random.randint(0,1) #Asignacion de genes



while encuentro == 0:
    for i in range(0,50):
        for j in range(0,20):
            if cromo[i][j] == 1:
                contador[i] += 1
            acumulada[i] = acumulada[i - 1] + contador[i]
    calTotal = contador.sum()
    generacion += 1
    print 'Generacion: ',generacion
    print cromo


    # Seleccion de padres
    for i in range(0, 50):
        if contador[i] == 20:
            encuentro = 1
            numeroCool = i


    while repes < 50:

        r1 = round(random.random(), 2)
        r2 = round(random.random(), 2)

        c1 = r1 * calTotal
        c2 = r2 * calTotal
        aux1 = 1
        aux2 = 1
        pa1 = 0
        pa2 = 0

        # Seleccion de padres

        for i in range(50):
            if acumulada[i] > c1 and aux1 != 0:
                pa1 = i
                aux1 = 0
            if acumulada[i] > c2 and aux2 != 0:
                pa2 = i
                aux2 = 0

        #print cromo
        #print contador
        #print calTotal
        #print acumulada
        #print r1, r2, c1, c2
        #print "El padre 1 es: ", pa1
        #print cromo[pa1]
        #print "El padre 2 es: ", pa2
        #print cromo[pa2]

        # Cruzamiento en punto---------------------------------
        pc = 0.80
        d = round(random.random(), 2)
        #print d
        xRand = 0

        xRand = random.randint(1, 19)
        #print xRand
        if d < pc:
            #print "Cruzamiento"
            for i in range(0, xRand):
                hijos[0][i] = cromo[pa1][i]
                hijos[1][i] = cromo[pa2][i]
            for i in range(xRand, 20):
                hijos[0][i] = cromo[pa2][i]
                hijos[1][i] = cromo[pa1][i]
        else:
            #print "Los padres son los nuevos individuos"
            hijos[0] = cromo[pa1]
            hijos[1] = cromo[pa2]
        #print hijos

        # Mutacion
        #print "Mutacion"
        pm = 0.5
        for i in range(0, 2):
            for j in range(0, 20):
                q = round(random.random(), 3)
                if q < pm:
                    if hijos[i][j] == 0:
                        hijos[i][j] = 1
                    elif hijos[i][j] == 1:
                        hijos[i][j] = 0
        #print hijos

        for i in range(0, 20):
            nuevaPoblacion[repes][i] = hijos[0][i]
            nuevaPoblacion[repes + 1][i] = hijos[1][i]




        #print 'repes: ',repes
        #print cromo
        repes +=2

        #Fin de while ya son 50
    #reset contador y acumulada
    repes = 0

    #print contador
    for i in range(0,50):
        contador[i] = 0
        acumulada[i] = 0
        for j in range(0,20):
            cromoOld[i][j] = cromo[i][j]
            cromo[i][j] = nuevaPoblacion[i][j]

print 'El cromosoma con todos los unos esta en la linea: ',numeroCool + 1
print cromoOld[numeroCool]


