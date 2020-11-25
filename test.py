N = [5, 4, 3, 2, 1]
C = [4, 3, 2, 1]
T = [3, 2, 1]

class Tree(object):
    def __init__(self, label, left, right):
        self.left = left
        self.right = right
        self.label = label
def String2Tree(A):
    letrasProposicionales = [chr(x) for x in range(256, 600)]
    Conectivos = ['O', 'Y', '>', '=']
    Pila = []
    for c in A:
        if c in letrasProposicionales:
            Pila.append(Tree(c, None, None))
        elif c == '-':
            FormulaAux = Tree(c, None, Pila[-1])
            del Pila[-1]
            Pila.append(FormulaAux)
        elif c in Conectivos:
            FormulaAux = Tree(c, Pila[-1], Pila[-2])
            del Pila[-1]
            del Pila[-1]
            Pila.append(FormulaAux)
        else:
            print(u"Hay un problema: el símbolo " + str(c) + " no se reconoce")
    return Pila[-1]

def Inorderp(f):
    if f.right == None:
        return str(decod(f.label))
    elif f.label == "-":
        return f.label + Inorderp(f.right)
    else:
        return "(" + Inorderp(f.left) + f.label + Inorderp(f.right) + ")"



def codifica(x, y, z):
    assert(x in N), "Primer argumento inválido."
    assert(y in C), "Segundo argumento inválido."
    assert(z in T), "Tercer argumento inválido."
    letra = ((2 * z) + (6 * y) + (24 * x)) // 2
    return letra

def encontrarCode(n):
    for i in N:
        a = n - (i * 24)

        if(a > 0):
            for j in C:
                b = a - (j * 6)

                if(b > 0):
                    for k in T:
                        c = b - (k * 2)

                        if(c == 0):
                            x = i
                            y = j
                            z = k
                            return x, y, z

def decodifica(letra):
    # Funcion que codifica un caracter en su respectiva fila f y columna c de la tabla
    n = letra * 2
    x, y, z = encontrarCode(n)
    return x, y, z
num = []
for i in N:
    for j in C:
        for k in T:
            v1 = codifica(i, j, k)
            print(v1, end=" ")
            num.append(v1)
    print("")
print(num)
for v1 in num:
    x, y, z = decodifica(v1)
    print('Casilla: '+str(x)+', Elemento: '+str(y)+', Tipo: '+str(z))
letras = []
for i in N:
    for j in C:
        for k in T:
            v1 = codifica(i, j, k)
            cod = chr(v1 + 256)
            print(cod, end = " ")
            letras.append(cod)
print("")
for cod in letras:
    print('Letra = ' + cod, end =', ')
    x, y, z = decodifica(ord(cod) - 256)
    print('Casilla = ' + str(x), end =', ')
    print('Elemento = ' + str(y), end = ", ")
    print('Tipo = ' + str(z))
def cod(n):
    return chr(n + 256)
def decod(x):
    return decodifica(ord(x) - 256)

def regla_2():
    defensivo = 3
    formula = ""
    inicial3 = True

    while defensivo > 0:
        for i in range(defensivo):
            inicial = True
            for pos in range(len(N)):
                inicial2 = True
                for elem in range(len(C)):
                    if inicial2:
                        formula = formula + str(cod(codifica(pos + 1, elem + 1, 3)))
                        inicial2 = False
                    else:
                        formula = formula + str(cod(codifica(pos + 1, elem + 1, 3))) + 'O'
                if inicial:
                    inicial = False
                else:
                    formula = formula + 'O'
            if inicial3:
                inicial3 = False
            else:
                formula = formula + 'Y'
        inicial = True
        for i in range(5 - defensivo):

            for type in range(len(T)):
                if type + 1 != 3:
                    inicialDos = True
                    for elem in range(len(C)):
                        for pos in range(len(N)):
                            if inicialDos:
                                    formula = formula + str(cod(codifica(pos + 1, elem + 1, type + 1)))
                                    inicialDos = False
                            else:
                                    formula = formula + str(cod(codifica(pos + 1, elem + 1, type + 1))) + "O"

                else:
                    continue
            if inicial:
                inicial = False
            else:
                formula = formula + 'O'

            formula = formula + 'Y'




        defensivo -= 1


    print(formula)
    print(Inorderp(String2Tree(formula)))







def Regla3():
    formula = ""
    inicial = True
    for pos in range(len(N)):
        inicialDos = True
        for elem in range(len(C)):
            for type in range(len(T)):
                if inicialDos:
                    formula = formula + str(cod(codifica(pos + 1, elem + 1, type + 1)))
                    inicialDos = False
                else:
                    formula = formula + str(cod(codifica(pos + 1, elem + 1, type + 1))) + "O"
        if inicial:
            inicial = False
        else:
            formula = formula + 'Y'
    print(formula)
    print(Inorderp(String2Tree(formula)))


regla_2()
A = 'ĒĕOĘOěOĞġOĤOħOOĪĭOİOĳOOĶĹOļOĿOOłŅOňOŋOOĒĕOĘOěOĞġOĤOħOOĪĭOİOĳOOĶĹOļOĿOOłŅOňOŋOOYĒĕOĘOěOĞġOĤOħOO'
print(Inorderp(String2Tree(A)))