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

    def add_edges(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def print(self):
        for x in self.adjMatrix:
            for val in x:
                print(val, end=" ")
            print()

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
            print("Graf wejściowy nie zawiera cyklu.")
            return False

        self.printpath(path)
        return True

    def printpath(self, path):
        for vrt in path:
            print(vrt, end=" ")
        print(path[0],"\n")

    def isEuler(self):
        for x in g.adjMatrix:
            degrees = 0
            for y in x:
                degrees += y
            if degrees % 2 == 1:
                return False
        return True

    def Euler(self):
        if not self.isEuler():
            print("Graf wejściowy nie zawiera cyklu.")


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

        print("\nCykl Eulera w grafie nieskierowanym:")
        g.Euler()
        print("\n")

    if choice == "2":
        try:
            with open("cases.txt", 'r') as f:
                nol = 1
                for line in f:
                    if nol == 1:
                        v, e = map(int, line.split(" "))
                    else:
                        x = list(map(int, line.split()))
                        if x not in vertexes:
                            vertexes.append(x)
                        else:
                            raise DoubledValue
                    nol += 1
        except FileNotFoundError:
            print("Błędne dane lub taki plik nie istnieje!")
        except ValueError:
            print("Plik zawiera niepoprawne dane! Należy go sprawdzić!")
        except DoubledValue:
            print("Jedna z wartości wystepuje wielokrotnie i nie zostanie dodana! Sprawdź plik.")
    if choice == "3":
        break
    if choice not in ["1", "2", "3"]:
        print("Podaj poprawną wartość!")

