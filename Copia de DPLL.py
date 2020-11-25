# Algoritmo DPLL taller

# 1) S = {pq, rs, -r-s}
    # Dado a que no hay una cláusula unitaria, se elige l = p, se eliminan las cláusulas p y se remueve -p de las restantes
    # S' = {rs, -r-s}. I' = {p:1}
    # Dado a que no hay una cláusula unitaria, se elige l = r, se eliminan las cláusulas r y se remueve -r de las restantes
    # S'' = {-s}. I'' = {p:1, r:1}
    # Se realiza UnitPropagate sobre -s en S'' y se retorna s:0
    # S''' = {}. I''' = {p:1, r:1, s:0}, Satisfacible tanto que S''' es vacío

# 2) S = {pq, p-q, -pq, -p-q}
    # Dado a que no hay una cláusula unitaria, se elige l = p, se eliminan las cláusulas p y se remueve -p de las restantes
    # S' = {q, -q}. I' = {p:1}
    # Se realiza UnitPropagate sobre q en S' y se retorna q:1
    # S'' = {[]}
    # Dado a que S'' contiene una cláusula vacía, entonces S'' es Insatisfacible

# 3) S = {pq, -pq, -q-r, r-q}
    # Dado a que no hay una cláusula unitaria, se elige l = p, se eliminan las cláusulas p y se remueve -p de las restantes
    # S' = {q, -q-r, r-q}. I' = {p:1}
    # Se realiza UnitPropagate sobre q en S' y se retorna q:1
    # S'' = {-r, r}. I'' = {p:1, q:1}
    # Se vuelve a realizar UnitPropagate sobre -r en S'', retornando r:0
    # S''' = {[]}
    # Ahora que en S''' existe una cláusula vacía, es Insatisfacible.



def unitario(a):
    if len(a) == 1:
        return a
    elif len(a) == 2:
        if a[0] == '-':
            return '-' + a[1]
        else:
            return None
    else:
        return None
def complemento(a):
    if a[0] == '-':
        return a[1]
    else:
        return '-' + a[0]
def removeFrom(a, b):
    total = []
    for x in a:
        c = []
        for i in x:
            if i == b:
                continue
            else:
                c.append(i)
        total.append(c)
    return total
def removeClaus(S, a):
    total = []
    for i in S:
        if a in i:
            continue
        else:
            total.append(i)
    return total
def unitPropagate(S, I):
    global vacio
    if len(S) == 0:
        return S, I
    for i in S:
        if len(i) == 0:
            vacio = True
            return S, I
        else:
            vacio = False
            continue
    if not vacio:
        for i in S:
            if len(i) == 1:
                S = removeClaus(S, i[0])
                S = removeFrom(S, complemento(i[0]))
                x = i[0]
                if x[0] == '-':
                    I[x[1]] = 0
                else:
                    I[x[0]] = 1
                return unitPropagate(S, I)
            else: continue
        return S, I
def DPLL(S, I):
    global i
    S, I = unitPropagate(S, I)
    for i in S:
        if len(i) == 0:
            I = {}
            return "Insatisfacible", I
    if len(S) == 0:
        return "Satisfacible", I
    else:
        for i in S:
            if len(i) == 1:
                return DPLL(S, I)
        x = i[0]
        S = removeClaus(S, x)
        S = removeFrom(S, complemento(x))
        if x[0] == '-':
            I[complemento(x)] = 0
        else:
            I[x] = 1
        return DPLL(S, I)


A_1 = [['p', 'q', 'r'],
       ['-p', '-q', '-r'],
       ['-p', 'q', 'r'],
       ['-q', 'r'],
       ['q', '-r']]

A_2 = [['p', 'q', 'r', '-s'],
       ['p', 't', 's'],
       ['-p', '-q'],
       ['p', 'r', '-q', '-s']]

A_3 = [['p', 'q', '-r'],
       ['r', 's', 't'],
       ['t'],
       ['p', 's'],
       ['q', '-p']]

A_4 = [['p', '-q'],
       ['-p', '-q'],
       ['q', 'r'],
       ['-q', '-r'],
       ['-p', '-r'],
       ['p', '-r']]

A_5 = [['r', 'p', 's'],
       ['-r', '-p', 's'],
       ['-r', 'p', 's'],
       ['p', '-s']]




I = {}
a = DPLL(A_5, I)
print(a)
