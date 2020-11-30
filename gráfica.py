#-*-coding: utf-8-*-
# Edgar Andrade, Septiembre 2018

# Visualizacion de tableros de ajedrez 3x3 a partir de
# una lista de literales. Cada literal representa una casilla;
# el literal es positivo sii hay un caballo en la casilla.

# Formato de la entrada: - las letras proposionales seran: 1, ..., 9;
#                        - solo se aceptan literales (ej. 1, ~2, 3, ~4, etc.)
# Requiere también un número natural, para servir de índice del tablero,
# toda vez que pueden solicitarse varios tableros.

# Salida: archivo tablero_%i.png, donde %i es un número natural
####### CREACIÓN DE OBJETOS
magic = ['MagFire.png', 'MagWater.png', 'MagEarth.png', 'MagAir.png'] #aquí se añaden los nombres de los archivos de las imágenes
physic = ['PhyFire.png', 'PhyWater.png', 'PhyEarth.png', 'PhyAir.png']
defensive = ['DefFire.png', 'DefWater.png', 'DefEarth.png', 'DefAir.png']
objects = [magic, physic, defensive]
#################
# importando paquetes para dibujar
print("Importando paquetes...")
import FNC as f
import DPLL as dp
import matplotlib
import test as r
import time
matplotlib.use('Agg')
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
print("Listo!")

BG_color = (0.6132, 0.6523, 0.8359)



def dibujar_tablero(f, n):
    # Visualiza un tablero dada una formula f
    # Input:
    #   - f, una lista de literales
    #   - n, un numero de identificacion del archivo
    # Output:
    #   - archivo de imagen tablero_n.png

    # Inicializo el plano que contiene la figura
    fig, axes = plt.subplots()
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)

    # Dibujo el tablero
    step = 1/4
    tangulos = []
    # Creo los cuadrados claros en el tablero
    tangulos.append(patches.Rectangle(
                                    (0, (2 * step)),
                                    step,
                                    step,
                                    facecolor = BG_color)
                                    )
    tangulos.append(patches.Rectangle(
                                    (step, (2 * step)),
                                    step,
                                    step,
                                    facecolor = BG_color))
    tangulos.append(patches.Rectangle(((2 * step), (2 * step)),
                                    step,
                                    step,
                                    facecolor = BG_color))
    tangulos.append(patches.Rectangle((0, step),
                                      step,
                                      step,
                                      facecolor = BG_color))
    tangulos.append(patches.Rectangle((step, step),
                                      step,
                                      step,
                                      facecolor = BG_color))
    tangulos.append(patches.Rectangle(((2 * step), step),
                                      step,
                                      step,
                                      facecolor='blue'))


    # Creo las líneas del tablero
    for j in range(3):
        tangulos.append(patches.Rectangle(
            ((j * step), (2 * step)),
            step, 0.005,
            facecolor='blue')
        )
        tangulos.append(patches.Rectangle(
            ((j * step), (3 * step)),
            step, 0.005,
            facecolor='blue')
        )
        tangulos.append(patches.Rectangle(
            ((j * step), step),
            step, 0.005,
            facecolor='blue')
        )

    for j in range(4):
        tangulos.append(patches.Rectangle(
            (((j) * step), step),
            0.005,
            2 * step,
            facecolor='blue')
        )

    for t in tangulos:
        axes.add_patch(t)

    # Cargando imagen de caballo


    # Creando las direcciones en la imagen de acuerdo a literal
    direcciones = {}
    direcciones[1] = [0.125, 0.63]
    direcciones[2] = [0.375, 0.63]
    direcciones[3] = [0.625, 0.63]
    direcciones[4] = [0.125, 0.38]
    direcciones[5] = [0.375, 0.38]

    #plt.show()


    for l in f:
        print(l)
        pos = l[0]
        element = l[1]
        type = l[2]

        image_e = objects[type - 1]
        image = image_e[element - 1]
        arr_img = plt.imread(image, format='png')
        imagebox = OffsetImage(arr_img, zoom=0.10)
        imagebox.image.axes = axes
        ab = AnnotationBbox(imagebox, direcciones[pos], frameon=False)
        axes.add_artist(ab)
    fig.savefig("tablero_" + str(n) + ".png")



def solucion():

    do = False
    newInt = None
    while not do:
        time_1 = time.time()
        reg = r.letras()
        F = []
        c = 0
        while c < 5:
            x = reg[random.randrange(0, len(reg))]
            if x not in F:
                F.append(x)
                c += 1
            else:
                pass
        print("Elegidos (épico): ", F)
        x = [r.cod(r.codifica(5, 1, 3)), r.cod(r.codifica(4, 2, 3)), r.cod(r.codifica(3, 3, 3)), r.cod(r.codifica(2, 2, 2)), r.cod(r.codifica(1, 2, 1))]
        #A = r.regla_4() + r.regla_5() + 'Y' + r.regla_3() + 'Y' + F[0] + 'Y' #+ F[1] + 'Y' + F[2] + 'Y' + F[3] + 'Y' + F[4] + 'Y'
        A = r.regla_5() + r.regla_4() + 'Y' + F[0] + 'Y' + F[1] + 'Y' + F[2] + 'Y' + F[3] + 'Y' + F[4] + 'Y'
        A = r.regla_2() + r.regla_1() + 'Y' + r.regla_5() + 'Y' + r.regla_3() + 'Y' + F[0] + 'Y' + F[1] + 'Y' + F[2] + 'Y' + F[3] + 'Y' + F[4] + 'Y'
        A = x[0] + x[1] + 'Y' + x[2] + 'Y' + x[3] + 'Y' + x[4] + 'Y' + r.regla_4() + 'Y'
        #A = r.regla_2() + F[0] + 'Y' + F[1] + 'Y' + F[2] + 'Y' + F[3] + 'Y' + F[4] + 'Y'
        A = r.String2Tree(A)
        print(A)
        A = r.InorderpE(A)
        print(A)
        A = f.Tseitin(A, r.letras())
        print("resultado Tseitin: ", A)
        fC = f.formaClausal(A)
        print("resultado Clausal: ", fC)
        I = {}
        dPLL = dp.DPLL(fC, I)
        print("resultado DPLL: ", dPLL[1])
        I = {}
        for key in dPLL[1].keys():
            if ord(key) < 500:
                I[key] = dPLL[1][key]
        print("Interps")
        newInt = []
        for key in I.keys():
            if I[key] == 1:
                newInt.append(r.decod(key))
        if len(I) != 0:
            do = True
        time_2 = time.time()
        time_tot = time_2 - time_1
        print("Tiempo: ", time_tot)


    print(newInt)
    dibujar_tablero(newInt, 0)

solucion()