import sys
from random import randint


class BST:
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None


def insert(bst, key):
    if bst is None:
        return BST(key)

    if key < bst.key:
        bst.left_child = insert(bst.left_child, key)
    else:
        bst.right_child = insert(bst.right_child, key)

    return bst


def in_order(root):
    if root is not None:
        in_order(root.left_child)
        print(root.key, end=" ")
        in_order(root.right_child)


def pre_order(root):
    if root is not None:
        print(root.key, end=" ")
        pre_order(root.left_child)
        pre_order(root.right_child)


def post_order(root, tab):
    if root is None:
        return
    post_order(root.left_child, tab)
    post_order(root.right_child, tab)
    tab.append(root.key)


def find_min(root):
    temp = root
    while temp.left_child is not None:
        print(temp.key, end="->")
        temp = temp.left_child
    print(temp.key)
    return temp.key


def find_max(root):
    temp = root
    while temp.right_child is not None:
        print(temp.key, end="->")
        temp = temp.right_child
    print(temp.key)
    return temp.key


def find_and_print(root, key):
    if key == root.key:
        return pre_order(root)

    if key < root.key:
        return find_and_print(root.left_child, key)

    return find_and_print(root.right_child, key)


def delete(root, value):
    if root is None:
        return
    if value < root.key:
        root.left_child = delete(root.left_child, value)
    elif value > root.key:
        root.right_child = delete(root.right_child, value)
    else:
        if root.right_child is None:
            temp = root.left_child
            root = None
            return temp
        elif root.left_child is None:
            temp = root.right_child
            root = None
            return temp
        temp = find_min(root.right_child)
        root.key = temp.key
        root.right_child = delete(root, value)
    return root


def post_order_delete(root):
    post_order(root, post_order_tab)
    print("Deleted values")
    for x in range(len(post_order_tab)):
        val = post_order_tab[x]
        print(val, end="->")
        root = delete(root, val)


def random_number_generator(n):
    tab = []
    for x in range(n):
        tab.append(randint(10, 10*n))
    return tab


def shell_sort(t, n):
    interval = 1
    j = 1
    while (pow(3, j) - 1) / 2 < n:
        interval = (pow(3, j) - 1) // 2
        j += 1

    while interval > 0:
        for y in range(interval, n):
            temp = t[y]
            j = y
            while j >= interval and t[j - interval] < temp:
                t[j] = t[j - interval]
                j -= interval
            t[j] = temp
        interval = (interval - 1)//3


post_order_tab = []
while True:
    root = None
    print("Menu:\n1 - Dane wejściowe\n2 - Testy\n3 - Zakończ działanie programu")
    x = input()
    if x == "1":
        print("Ile chcesz podać liczb?")
        ile_liczb = input()
        if ile_liczb.isnumeric():
            ile_liczb = int(ile_liczb)
            ile = 0
            while ile < ile_liczb:
                try:
                    number = int(input())
                    if type(number) == int:
                        root = insert(root, number)
                        ile += 1
                except:
                    print("To nie jest liczba spróbuje jeszcze raz!")
            while True:
                print("Menu procedur:\n1 - Wyszukiwanie min i max\n2 - Usunięcie elementu\n3 - Wypisanie in-order"
                      "\n4 - Wypisanie pre-order\n5 - Usunięcie całego drzewa(post-order)\n6 - Wypisanie pre-order podrzewa"
                      "\n7 - Równoważenie drzewa\n8 - Powrót do menu głównego")
             #   try:
                chosen = int(input())
                if type(chosen) == int:
                    if chosen == 1:
                        print("Największa wartość : ")
                        find_max(root)
                        print("Najmniejsza wartość : ")
                        find_min(root)
                        print("\n")
                    if chosen == 2:
                        print("Podaj ile wartości chcesz usunąć: ")
                        value = int(input())
                        if type(value) == int:
                            for v in range(value):
                                value_td = int(input())
                                root = delete(root, value_td)
                        print("\n")
                    if chosen == 3:
                        print("In-order")
                        in_order(root)
                        print("\n")
                    if chosen == 4:
                        print("Pre-order")
                        pre_order(root)
                        print("\n")
                    if chosen == 5:
                        print("Delete post-order")
                        post_order_delete(root)
                        print("\n")
                    if chosen == 6:
                        print("Podaj klucz do podrzewa: ")
                        key = int(input())
                        if type(key) == int:
                            print("Find a key")
                            find_and_print(root, key)
                            print("\n")
                    if chosen == 7:
                        print("Nie wiem o co cmon") #
                    if chosen == 8:
                        break
              #  except:
                #    print("To chyba nie jest poprawna wartość! Spróbuj ponownie.")
        else:
            print("To nie jest liczba podaj poprawną wartość!")

    elif x == "2":
        print(x)
    elif x == "3":
        sys.exit()
    else:
        print("Podaj poprawną wartość")
