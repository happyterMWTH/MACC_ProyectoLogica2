N = [5, 4, 3, 2, 1]
C = [4, 3, 2, 1]
T = [3, 2, 1]


class Tree(object):
    def __init__(self, label, left, right):
        self.left = left
        self.right = right
        self.label = label


def String2Tree(A):
    letrasProposicionales = [chr(x) for x in range(256, 2000)]
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


def InorderpE(f):
    if f.right == None:
        return f.label
    elif f.label == "-":
        return f.label + InorderpE(f.right)
    else:
        return "(" + InorderpE(f.left) + f.label + InorderpE(f.right) + ")"


def codifica(x, y, z):
    assert (x in N), "Primer argumento inválido."
    assert (y in C), "Segundo argumento inválido."
    assert (z in T), "Tercer argumento inválido."
    letra = ((2 * z) + (6 * y) + (24 * x)) // 2
    return letra


def encontrarCode(n):
    for i in N:
        a = n - (i * 24)
        if a > 0:
            for j in C:
                b = a - (j * 6)

                if b > 0:
                    for k in T:
                        c = b - (k * 2)

                        if c == 0:
                            x = i
                            y = j
                            z = k
                            return x, y, z


def decodifica(letra):
    # Funcion que codifica un caracter en su respectiva fila f y columna c de la tabla
    n = letra * 2
    x, y, z = encontrarCode(n)
    return x, y, z


def cod(n):
    return chr(n + 386) #16


def decod(x):
    return decodifica(ord(x) - 386) #16


def letras():
    num = []
    for i in N:
        for j in C:
            for k in T:
                v1 = codifica(i, j, k)
                num.append(cod(v1))
    print(num)
    return num




def regla_1_in(base):
    newN = N[0:base]

    formula = ""
    if base != 0:
        endF = True
        for pos in newN:
            inicial = True
            for elem in C:
                if inicial:
                    formula = formula + cod(codifica(pos, elem, 3))
                    inicial = False
                else:
                    formula = formula + cod(codifica(pos, elem, 3)) + 'O'
            if endF:
                endF = False
            else:
                formula = formula + 'Y'
    return formula
def regla_1_out(base):
    newN = N[base:6]

    formula = ""
    endF = True
    for pos in newN:
        inicial = True
        for elem in C:
            for type in T:
                if type == 3:
                    continue
                else:
                    if inicial:
                        formula = formula + cod(codifica(pos, elem, type))
                        inicial = False
                    else:
                        formula = formula + cod(codifica(pos, elem, type)) + 'O'
        if endF:
            endF = False
        else:
            formula = formula + 'Y'
    return formula
def regla_1_tot(base):
    if base != 0:
        formula = regla_1_in(base) + regla_1_out(base) + 'Y'
    else:
        formula = regla_1_out(base)
    return formula
def regla_1():
    formula = regla_1_tot(3) + regla_1_tot(2) + 'O'\
            + regla_1_tot(1) + 'O' + regla_1_tot(0) + 'O'

    return formula

def regla_2_m(base):
    formula = ""
    newN = N[5 - base:5]
    endF = True
    for pos in newN:
        inicial = True
        for elem in C:
            if inicial:
                formula = formula + cod(codifica(pos, elem, 1))
                inicial = False
            else:
                formula = formula + cod(codifica(pos, elem, 1)) + 'O'
        if endF:
            endF = False
        else:
            formula = formula + 'Y'
    return formula
def regla_2_p(magic, base):
    newN = N[5 - magic - base:5 - magic]
    formula = ""

    endF = True
    for pos in newN:
        inicial = True
        for elem in C:
            if inicial:
                formula = formula + cod(codifica(pos, elem, 2))
                inicial = False
            else:
                formula = formula + cod(codifica(pos, elem, 2)) + 'O'
        if endF:
            endF = False
        else:
            formula = formula + 'Y'
    return formula
def regla_2_d(base):
    newN = N[0:5 - base]
    formula = ""

    endF = True
    for pos in newN:
        inicial = True
        for elem in C:
            if inicial:
                formula = formula + cod(codifica(pos, elem, 3))
                inicial = False
            else:
                formula = formula + cod(codifica(pos, elem, 3)) + 'O'
        if endF:
            endF = False
        else:
            formula = formula + 'Y'
    return formula
def regla_2():
    formula = regla_2_m(2) + regla_2_p(2,2) + 'Y' + regla_2_d(4) + 'Y'\
            + regla_2_m(2) + regla_2_p(2,1) + 'Y' + regla_2_d(3) + 'YO' \
            + regla_2_m(1) + regla_2_p(1, 2) + 'Y' + regla_2_d(3) + 'YO' \
            + regla_2_m(1) + regla_2_p(1, 1) + 'Y' + regla_2_d(2) + 'YO' \
            + regla_2_m(1) + regla_2_d(1) + 'YO' \
            + regla_2_p(0, 1) + regla_2_d(1) + 'YO' \
            + regla_2_m(1) + regla_2_d(1) + 'YO'\
            + regla_2_d(0) + 'O'

    return formula
print(Inorderp(String2Tree(regla_2())))


def regla_3():
    formula = ""
    inicial = True
    for pos in range(len(N)):
        inicial2 = True
        for elem in range(len(C)):
            for type in range(len(T)):
                if inicial2:
                    formula = formula + cod(codifica(pos + 1, elem + 1, type + 1))
                    inicial2 = False
                else:
                    formula = formula + cod(codifica(pos + 1, elem + 1, type + 1)) + 'O'
        if inicial:
            inicial = False
        else:
            formula = formula + 'Y'
    return formula

def regla_4_def(pos, element, clase):
    formula = ""
    endF = ""
    inicial = True
    end = True
    for elem in range(len(C)):
        for type in range(len(T)):
            if end:
                end = False
                endF = '-' + cod(codifica(pos + 1, element + 1, clase + 1)) + '='
            if type == clase and element == elem:
                continue
            else:
                if inicial:
                    inicial = False
                    formula = formula + cod(codifica(pos + 1, elem + 1, type + 1))
                else:
                    formula = formula + cod(codifica(pos + 1, elem + 1, type + 1)) + 'O'
    formula = formula + endF
    return formula
def regla_4():
    formula = ""
    inicial = True
    for pos in range(len(N)):
        for elem in range(len(C)):
            for type in range(len(T)):
                if inicial:
                    inicial = False
                    formula = formula + regla_4_def(pos, elem, type)
                else:
                    formula = formula + regla_4_def(pos, elem, type) + 'Y'
    return formula

def regla_5_def(position, elem, type):
    formula = ""
    endF = ""
    inicial = True
    end = True
    for pos in range(len(N)):
        if end:
            end = False
            endF = '-' + cod(codifica(position + 1, elem + 1, type + 1)) + '='

        if pos == position:
            continue
        else:
            if inicial:
                inicial = False
                formula = cod(codifica(pos + 1, elem + 1, type + 1))
            else:
                formula = formula + cod(codifica(pos + 1, elem + 1, type + 1)) + 'O'

    formula = formula + endF

    return formula
def regla_5():
    formula = ""
    inicial = True
    for pos in range(len(N)):
        for elem in range(len(C)):
            for type in range(len(T)):
                if inicial:
                    inicial = False
                    formula = formula + regla_5_def(pos, elem, type)
                else:
                    formula = formula + regla_5_def(pos, elem, type) + 'Y'
    return formula
