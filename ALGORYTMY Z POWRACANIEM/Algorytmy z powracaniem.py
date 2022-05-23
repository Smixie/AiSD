import networkx


class Error(Exception):
    """Base class for other exceptions"""
    pass


class BadValue(Error):
    """Bad input value"""
    pass


class DoubledValue(Error):
    """Doubled value"""
    pass


class AdjGraph():
    def __init__(self, size):
        self.adjMatrix = []
        for x in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.V = size
        self.edges = 0
        self.path = []

    def add_edges(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
        self.edges += 1

    def print(self):
        for x in self.adjMatrix:
            for val in x:
                print(val, end=" ")
            print()

    def printpath(self, path):
        for vrt in path:
            print(vrt, end=" ")
        print(path[0],"\n")

    # Hamilton
    def check(self, path, vertex, pos):
        if self.adjMatrix[path[pos-1]][vertex] == 0:
            return False

        for x in path:
            if vertex == x:
                return False
        return True

    def hamiltonrec(self, path, pos):
        if pos == self.V:
            if self.adjMatrix[path[pos - 1]][path[0]] == 1:
                return True
            else:
                return False

        for v in range(1,self.V):
            if self.check(path, v, pos):
                path[pos] = v
                if self.hamiltonrec(path, pos+1):
                    return True
            path[pos] = -1
        return False

    def hamiltonian(self):
        path = [-1] * self.V
        path[0] = 0
        if not self.hamiltonrec(path,1):
            print("Graf wejściowy nie zawiera cyklu.\n")
            return False

        self.printpath(path)
        return True

    # Euler
    def isEuler(self):
        for x in range(self.V):
            s = 0
            for y in range(self.V):
                s += self.adjMatrix[x][y]
            if s % 2 == 1:
                return False
        return True

    def dfs_euler(self, v):
        for i in range(self.V):
            while self.adjMatrix[v][i]:
                self.adjMatrix[v][i] = 0
                self.adjMatrix[i][v] = 0
                self.dfs_euler(i)
        self.path.append(v)

density = [10, 20, 30, 40, 50, 60, 70, 80, 90]
vertexes = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]


while True:
    print("1 - Dane wczytane z klawiatury\n2 - Dane wczytane z pliku\n3 - Zakończ")
    choice = input()
    vertexes = []
    if choice == "1":
        while True:
            try:
                print("Podaj ilosc wierzchołków krawędzi : ")
                v, e = map(int, input().split(" "))
                break
            except ValueError:
                print("Podaj poprawne dane!")
        print("Podaj krawędzie")
        y = 0
        while y < e:
            try:
                x = input().strip()
                i = x.split()
                p = [int(j) for j in i]
                if len(p) != 2:
                    raise BadValue
                else:
                    if p not in vertexes:
                        vertexes.append(p)
                        y += 1
                    else:
                        raise DoubledValue
            except ValueError:
                print("To nie jest poprawna wartość!")
            except BadValue:
                print("Podano złe wartości krawędzi")
            except DoubledValue:
                print("Taka wartość już istnieje nie można jej dodać ponownie!")

        g = AdjGraph(v)  # Macierz sąsiedztwa od 0
        for edges in vertexes:
            v1, v2 = edges
            g.add_edges(v1, v2)

        print("\nCykl Hamiltona w grafie nieskierowanym: ")
        g.hamiltonian()

        print("Cykl Eulera w grafie nieskierowanym:")
        if g.isEuler():
            g.dfs_euler(0)
            for x in g.path:
                print(x, end=" ")
            print("\n")
        else:
            print("Graf wejściowy nie zawiera cyklu.\n")
    if choice == "2":
        vertexes_file = []
        try:
            with open("cases.txt", 'r') as f:
                nol = 1
                for line in f:
                    if nol == 1:
                        vf, ef = map(int, line.split(" "))
                    else:
                        x = list(map(int, line.split()))
                        if x not in vertexes_file:
                            vertexes_file.append(x)
                        else:
                            raise DoubledValue
                    nol += 1
        except FileNotFoundError:
            print("Błędne dane lub taki plik nie istnieje!")
        except ValueError:
            print("Plik zawiera niepoprawne dane! Należy go sprawdzić!")
        except DoubledValue:
            print("Jedna z wartości wystepuje wielokrotnie i nie zostanie dodana! Sprawdź plik.")

        g1 = AdjGraph(vf)  # Macierz sąsiedztwa od 0
        for edges in vertexes_file:
            v1, v2 = edges
            g1.add_edges(v1, v2)

        print("\nCykl Hamiltona w grafie nieskierowanym: ")
        g1.hamiltonian()

        print("Cykl Eulera w grafie nieskierowanym:")
        if g1.isEuler():
            g1.dfs_euler(0)
            for x in g1.path:
                print(x, end=" ")
            print("\n")
        else:
            print("Graf wejściowy nie zawiera cyklu.\n")

    if choice == "3":
        break
    if choice not in ["1", "2", "3"]:
        print("Podaj poprawną wartość!")

