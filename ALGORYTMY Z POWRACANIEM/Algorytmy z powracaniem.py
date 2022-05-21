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


class AdjGraph(object):
    def __init__(self, size):
        self.adjMatrix = []
        for x in range(size):
            self.adjMatrix.append([0 for i in range(size)])

    def add_edges(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def print(self):
        for x in self.adjMatrix:
            for val in x:
                print(val, end=" ")
            print()


test_edges = [[0, 1], [0, 2], [1, 2], [2, 0], [2, 3]]
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
                x = list(map(int ,input().strip().split()))
                if len(x) != 2:
                    raise BadValue
                else:
                    if x not in vertexes:
                        vertexes.append(x)
                        y += 1
                    else:
                        raise DoubledValue
            except ValueError:
                print("To nie jest poprawna wartość!")
            except BadValue:
                print("Podano złe wartości krawędzi")
            except DoubledValue:
                print("Taka wartość już istnieje nie można jej dodać ponownie!")

        g = AdjGraph(v)
        for edges in vertexes:
            v1, v2 = edges
            g.add_edges(v1, v2)
        print(g.print())
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
            continue
        except ValueError:
            print("Plik zawiera niepoprawne dane! Należy go sprawdzić!")
            continue
        except DoubledValue:
            print("Jedna z wartości wystepuje wielokrotnie i nie zostanie dodana! Sprawdź plik.")
            continue
    if choice == "3":
        break
    if choice not in ["1", "2", "3"]:
        print("Podaj poprawną wartość!")

