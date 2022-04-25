import sys

import numpy as np
from collections import deque

successors = {}
predecessors = {}
incydencji = {}
brak_incydencji = {}
end_matrix = []
numbers = []


class Error(Exception):
    """Base class for other exceptions"""
    pass


class BadValue(Error):
    """Bad input value"""
    pass


def create_tabs():
    successor = []
    predecessor = []
    incydencja = []
    for x in range(len(vertexes)):  # Następnicy
        if vertexes[x][0] in successors:
            successor = successors[vertexes[x][0]]
            successor.append(vertexes[x][1])
            successor.sort()
            successors[vertexes[x][0]] = successor
        else:
            successors[vertexes[x][0]] = [vertexes[x][1]]
        if vertexes[x][0] not in numbers:
            numbers.append(vertexes[x][0])
        if vertexes[x][1] not in numbers:
            numbers.append(vertexes[x][1])

    for x in range(len(vertexes)):  # Poprzednicy
        if vertexes[x][1] in predecessors:
            predecessor = predecessors[vertexes[x][1]]
            predecessor.append(vertexes[x][0])
            predecessor.sort()
            predecessors[vertexes[x][1]] = predecessor
        else:
            predecessors[vertexes[x][1]] = [vertexes[x][0]]

    for x in range(len(vertexes)):  # Incydencja
        if vertexes[x][1] in incydencji:
            incydencja = incydencji[vertexes[x][1]]
            incydencja.append(vertexes[x][0])
            incydencja.sort()
            incydencji[vertexes[x][1]]= incydencja
        else:
            incydencji[vertexes[x][1]] = [vertexes[x][0]]

        if vertexes[x][0] in incydencji:
            incydencji[vertexes[x][0]].append(vertexes[x][1])
        else:
            incydencji[vertexes[x][0]] = [vertexes[x][1]]

    numbers.sort()

    for check in numbers:  # Sprawdzenie czy wszystko występuje
        if check not in predecessors:
            predecessors[check] = ["a"]
        if check not in successors:
            successors[check] = ["a"]
        if check not in incydencji:
            incydencji[check] = ["a"]

    for i in sorted(incydencji):  # Brak incydencji
        tab = incydencji[i]
        brak_incydencji[i] = []
        for x in numbers:
            if x not in tab:
                brak_incydencji[i].append(x)


def create_endpoint(v):
    for x in range(v):  # Macierz tylko z zerami
        row = []
        for y in range(v + 4):
            row.append(0)
        end_matrix.append(row)

    y = 0
    for x in range(v):  # Kolumna v + 1 -> następniki
        last = successors[numbers[x]][-1]
        if successors[numbers[x]][0] == "a":
            end_matrix[y][v] = 0
        else:
            end_matrix[y][v] = successors[numbers[x]][0]
        for el in successors[numbers[x]]:
            if last == "a":
                end_matrix[y][numbers.index(numbers[x])] = 0
            else:
                idx = numbers.index(el)
                end_matrix[y][idx] = last
        y += 1

    z = 0
    for x in range(v):  # Kolumna v + 2 -> poprzednicy
        last = predecessors[numbers[x]][-1]
        if last != "a":
            end_matrix[z][v + 1] = predecessors[numbers[x]][0]
            value = last + v
        else:
            end_matrix[z][v + 1] = 0
        for el in predecessors[numbers[x]]:
            if el != "a":
                idx = numbers.index(el)
                end_matrix[z][idx] = value
            else:
                end_matrix[z][numbers.index(numbers[x])] = 0
        z += 1

    z = 0
    for x in range(v):  # Kolumna v + 3 -> brak połącznia
        if brak_incydencji[numbers[x]][0] == "a":
            end_matrix[z][v + 2] = 0
        else:
            end_matrix[z][v + 2] = brak_incydencji[numbers[x]][0]
        last = brak_incydencji[numbers[x]][-1]
        for el in brak_incydencji[numbers[x]]:
            if last == "a":
                end_matrix[z][numbers.index(numbers[x])] = 0
            else:
                idx = numbers.index(el)
                end_matrix[z][idx] = -last
        z += 1


def DFS_mgrafu(vrt):
    L = []
    color = ["white"] * vrt
    cykl = [False]
    for u in numbers:
        idx = numbers.index(u)
        if color[idx] == "white":
            dfs_visited(vrt, u, color, L, cykl)
        if cykl[0]:
            break
    if cykl[0]:
        L = []

    L.reverse()
    return L


def dfs_visited(vert, u, color, L, cykl):
    if cykl[0]:
        return
    idx = numbers.index(u)
    color[idx] = "grey"
    for v in range(len(end_matrix[idx])-4):
        if min(numbers) <= end_matrix[idx][v] <= max(numbers):
            if color[numbers.index(numbers[v])] == "grey":
                cykl[0] = True
                return
            if color[numbers.index(numbers[v])] == "white":
                dfs_visited(vert, numbers[v], color, L, cykl)

    color[idx] = "black"
    L.append(u)


def DEL_mgrafu(vrt):
    in_degree = [0] * vrt
    for u in range(vrt):
        for v in range(vrt):
            if min(numbers) + vrt <= end_matrix[u][v]:
                in_degree[u] += 1

    Q = deque()
    for u in range(len(in_degree)):
        if in_degree[u] == 0:
            Q.appendleft(u)
    L = []

    while Q:
        u = Q.pop()
        L.append(numbers[u])
        for v in successors[numbers[u]]:
            if v == "a":
                break
            ind = numbers.index(v)
            in_degree[ind] -= 1
            if in_degree[ind] == 0:
                Q.appendleft(ind)
    if len(L) == vrt:
        return L
    else:
        return []


while True:
    print("1. Macierz grafu\n2. Zakończ działanie")
    try:
        chosen = int(input())
    except ValueError:
        print("Zła wartość!")
        continue
    else:
        global v, e
        if chosen == 1:
            vertexes = []
            print("1. Dane z klawiatury\n2. Wczytane z pliku")
            try:
                read = int(input())
            except ValueError:
                print("Zła wartość!")
                continue
            if read == 1:
                while True:
                    try:
                        print("Podaj ilosc wierzchołków/krawędzi : ")
                        v, e = map(int, input().split(" "))
                        break
                    except ValueError:
                        print("Podaj poprawne dane!")

                print("Podaj krawędzie")
                y = 0
                while y < e:
                    try:
                        x = list(map(int, input().split()))
                        if len(x) != 2:
                            raise BadValue
                        vertexes.append(x)
                        y += 1
                    except ValueError:
                        print("To nie jest poprawna wartość!")
                    except BadValue:
                        print("Podano złe wartości krawędzi")
            if read == 2:
                with open("cases.txt", 'r') as f:
                    nol = 1
                    for line in f:
                        if nol == 1:
                            v, e = map(int, line.split(" "))
                        else:
                            x = list(map(int, line.split()))
                            vertexes.append(x)
                        nol += 1
            # Tworznie macierzy grafu / wyświetlenie
            create_tabs()
            create_endpoint(v)
            print("Matrix")
            print(np.matrix(end_matrix))
            print("Wierzchołki")
            for x in numbers:
                print(x, end=" ")

            while True:
                print("\nWybierz : DFS_mgraf(1) / Algorytm Kahna(2) / Zakończ(3)")
                while True:
                    try:
                        dfs = int(input())
                        break
                    except ValueError:
                        print("Podaj poprawne dane!")
                if dfs == 1:
                    out = DFS_mgrafu(v)
                    if not out:
                        print("Graf zawiera cykl.Sortowanie niemożliwe.")
                    else:
                        print(out)
                if dfs == 2:
                    order = DEL_mgrafu(v)
                    if not order:
                        print("Graf zawiera cykl.Sortowanie niemożliwe.")
                    else:
                        print(order)
                if dfs == 3:
                    sys.exit()
        if chosen == 3:
            break

# for i in sorted(output):
#     print(i, output[i], end="\n")
# print("Następnicy")
# for i in sorted(successors):
#     print(i, successors[i], end="\n")
#
# print("Poprzednicy")
# for i in sorted(predecessors):
#     print(i, predecessors[i], end="\n")
#
# print("Brak incydencji")
# for i in sorted(brak_incydencji):
#     print(i, brak_incydencji[i], end="\n")
