import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import AnnotationBbox, OffsetImage

# Inicializo el plano que contiene la figura
fig, axes = plt.subplots()
axes.get_xaxis().set_visible(False)
axes.get_yaxis().set_visible(False)

step = 1./3
tangulos = []
# Creo los cuadrados claros en el tablero
tangulos.append(patches.Rectangle(
                                (0, step),
                                step,
                                step,
                                facecolor='cornsilk')
                                )
tangulos.append(patches.Rectangle(*[(step, 0), step, step],
        facecolor='blue'))
tangulos.append(patches.Rectangle(*[(2 * step, step), step, step],
        facecolor='cornsilk'))
tangulos.append(patches.Rectangle(*[(step, 2 * step), step, step],
        facecolor='cornsilk'))
# Creo los cuadrados oscuros en el tablero
tangulos.append(patches.Rectangle(*[(2 * step, 2 * step), step, step],
        facecolor='lightslategrey'))
tangulos.append(patches.Rectangle(*[(0, 2 * step), step, step],
        facecolor='lightslategrey'))
tangulos.append(patches.Rectangle(*[(2 * step, 0), step, step],
        facecolor='lightslategrey'))
tangulos.append(patches.Rectangle(*[(step, step), step, step],
        facecolor='lightslategrey'))
tangulos.append(patches.Rectangle(*[(0, 0), step, step],
        facecolor='lightslategrey'))

fig.savefig("tablero_" + str('2') + ".png")