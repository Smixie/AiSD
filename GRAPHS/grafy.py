import sys

import numpy as np
from collections import deque
from collections import defaultdict

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

class Graph():
	def __init__(self,vertices):
		self.graph = defaultdict(list)
		self.V = vertices

def edgeAdder(graph,u,v):
	graph.graph[u].append(v)

def cycle(graph, v, visited, recStack):
	visited[v] = True
	recStack[v] = True
	for neighbour in graph.graph[v]:
		if visited[neighbour] == False:
			if cycle(graph,neighbour, visited, recStack) == True:
				return True
		elif recStack[neighbour] == True:
			return True
	recStack[v] = False
	return False

def isCyclic(graph):
	visited = [False] * (graph.V + 1)
	recStack = [False] * (graph.V + 1)
	for node in range(graph.V):
		if visited[node] == False:
			if cycle(graph,node,visited,recStack) == True:
				return True
	return False

def find_min(tab,e):
    mini=99999999
    for i in range(e):
        if tab[i][0]<mini: mini=tab[i][0]
        if tab[i][1]<mini: mini=tab[i][1]
    return mini

tab_DFS = []
def DFSms(graph,v,visited):
	visited.add(v)
	tab_DFS.append(v)
	#print(v, end=' ')
	for i in graph.graph[v]:
		if i not in visited:
			DFSms(graph,i,visited)

def DFS_msasiedztwa(graph,v):
	visited = set()
	DFSms(graph,v,visited)

tab_DEL=[]
def DEL_msasiedztwa(graph):
	in_d = [0] * (graph.V)
	for i in graph.graph:
		for j in graph.graph[i]:
			in_d[j] += 1
	q = []
	for i in range(graph.V):
		if in_d[i] == 0:
			q.append(i)
	cnt = 0
	top = []
	while q:
		u = q.pop(0)
		top.append(u)
		for i in graph.graph[u]:
			in_d[i] -= 1
			if in_d[i] == 0:
				q.append(i)
	tab_DEL.append(top)

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
		try:
                    with open("cases.txt", 'r') as f:
                        nol = 1
                        for line in f:
                            if nol == 1:
                                v, e = map(int, line.split(" "))
                            else:
                                x = list(map(int, line.split()))
                                vertexes.append(x)
                            nol += 1
		except:
                    print("Błędne dane lub taki plik nie istnieje!")
                    continue
	    if len(vertexes)==0:
                print("Graf nie istnieje!")
                continue
            print("Wybierz na jakiej macierzy chcesz operowac: Macierz sasiedztwa(1) / Macierz grafu(2)")
            odp = input()
            if odp == "1":
                g=Graph(v)
		q = find_min(vertexes, e)
                #print(vertexes)
                if q!=0:
                    for i in range(e):
                        vertexes[i][0]=vertexes[i][0]-q
                        vertexes[i][1]=vertexes[i][1]-q
                #print(vertexes)
                for i in range(e):
                    edgeAdder(g,vertexes[i][0],vertexes[i][1])
                while True:
                    print("\nWybierz : DFS_msasiedztwa(1) / Algorytm Kahna(2) / Zakończ(3)")
                    while True:
                        try:
                            dfs = int(input())
                            break
                        except ValueError:
                            print("Podaj poprawne dane!")
                    if dfs == 1:
                        if isCyclic(g)==1:
                            print("Graf zawiera cykl.Sortowanie niemożliwe.")
                        else:
                            DFS_msasiedztwa(g,vertexes[0][0])
                            for i in range(len(tab_DFS)):
                                tab_DFS[i] += q
                            print(tab_DFS)
                            tab_DFS=[]
                    if dfs == 2:
                        if isCyclic(g):
                            print("Graf zawiera cykl.Sortowanie niemożliwe.")
                        else:
                            DEL_msasiedztwa(g)
                            #print(tab_DEL)
                            for i in range(len(tab_DEL[0])):
                                #print(tab_DEL[i])
                                tab_DEL[0][i] += q
                            print(tab_DEL[0])
                            tab_DEL=[]
                    if dfs == 3:
                        sys.exit()
            elif odp == "2":
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
        if chosen == 2:
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
