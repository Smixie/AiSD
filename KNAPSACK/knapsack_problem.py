class Error(Exception):
    """Base class for other exceptions"""
    pass


def kanpsackAZ(t,b,n):
    t.sort(key=lambda x: x[3], reverse=True)
    size = 0
    value = 0
    i = 0
    chosen = [0] * n
    el = []
    while size <= b:
        if i == n:
            break
        if size + t[i][1] <= b:
            size += t[i][1]
            value += t[i][2]
            chosen[t[i][0]] = 1
            el.append(t[i][0]+1)
        i += 1
    return el, chosen, size, value


def knapsackBf(b,n,t):
    fmax = 0
    size = 0
    bn = []
    for x in range(1,pow(2,n)):
        binary = list([int(y) for y in bin(x)[2:].zfill(n)])
        local = 0
        lsize = 0
        lchosen = []
        f = 0
        for y in range(n-1,-1,-1):
            if binary[y]:
                if lsize + t[f][1] <= b:
                    local += t[f][2]
                    lsize += t[f][1]
                    lchosen.append(t[f][0]+1)
            f += 1
        if local > fmax and lsize <= b:
            fmax = local
            size = lsize
            chosen = lchosen
            bn = binary
    return fmax,size, chosen, bn

b, n = [int(x) for x in input("Podaj pojemność plecaka\ilość przedmiotów\n").split()]

t = []
t1 = []
print("Podaj rozmiar i wartość przedmiotu")
x = 0
while x < n:
    try:
        r, w = [int(y) for y in input().split()]
        t.append([x, r, w, w/r])
        t1.append([x, r, w])
        x += 1
    except ValueError:
        continue


elm ,elementy, rozmiar, wartosc = kanpsackAZ(t,b,n)
print(f"Algorytm zachłanny\nRozmiar : {rozmiar}\nWartość : {wartosc}\nWybrane elementy : {elementy} {elm}\n")

fmax, size, elements, bn= knapsackBf(b,n,t1)
print(f"Algorytm wyczerpujący\nRozmiar : {size}\nWartość : {fmax}\nWybrane elementy : {bn} {elements}")
