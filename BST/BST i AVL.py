import sys
from random import randint
import time

class BST:
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None


class AVLNode():
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None
        self.height = 1


class AVL():
    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        if key < root.key:
            root.left_child = self.insert(root.left_child, key)
        if key > root.key:
            root.right_child = self.insert(root.right_child, key)

        root.height=1+max(self.heightGet(root.left_child), self.heightGet(root.right_child))
        # balance factor
        balance=self.balance(root)
        if balance > 1 and key < root.left_child.key:  # ll
            return self.rightR(root)
        if balance < -1 and key > root.right_child.key:  # rr
            return self.leftR(root)
        if balance > 1 and key > root.left_child.key:  # lr
            root.left_child = self.leftR(root.left_child)
            return self.rightR(root)
        if balance < -1 and key < root.right_child.key:  # rl
            root.right_child = self.rightR(root.right_child)
            return self.leftR(root)
        return root

    def leftR(self, l): # left Rotate
        a = l.right_child
        b = a.left_child

        a.left_child = l
        l.right_child = b

        l.height = 1 + max(self.heightGet(l.left_child), self.heightGet(l.right_child))
        a.height = 1 + max(self.heightGet(a.left_child), self.heightGet(a.right_child))

        return a # new root

    def rightR(self, l): # right rotate
        a = l.left_child
        b = a.right_child
        a.right_child = l
        l.left_child = b

        l.height = 1 + max(self.heightGet(l.left_child), self.heightGet(l.right_child))
        a.height = 1 + max(self.heightGet(a.left_child), self.heightGet(a.right_child))

        return a  # new root

    def heightGet(self, root):
        if not root:
            return 0
        return root.height

    def balance(self,root):
        if not root:
            return 0
        return self.heightGet(root.left_child) - self.heightGet(root.right_child)

    def delete(self, root, key):
        if not root:
            return root
        elif key < root.key:
            root.left_child = self.delete(root.left_child, key)
        elif key > root.key:
            root.right_child = self.delete(root.right_child, key)
        else:
            if root.left_child is None:
                a = root.right_child
                root = None
                return a
            if root.right_child is None:
                a = root.left_child
                root = None
                return a
            a = self.min_val(root.right_child)
            root.key = a.key
            root.right_child=self.delete(root.right_child,a.key)
        if root is None:
            return root

        root.height = 1 + max(self.heightGet(root.left_child), self.heightGet(root.right_child))

        balance = self.balance(root)  # balancing tree
        if balance > 1 and self.balance(root.left_child) >= 0:  # ll
            return self.rightR(root)
        if balance < -1 and self.balance(root.right_child) <= 0:   # rr
            return self.leftR(root)
        if balance > 1 and self.balance(root.right_child) < 0:  # lr
            root.left_child = self.leftR(root.left_child)
            return self.rightR(root)
        if balance < -1 and self.balance(root.right_child) > 0:  # rl
            root.right_child = self.rightR(root.right_child)
            return self.leftR(root)
        return root

    def min_val(self, root):
        if root is None or root.left_child is None:
            return root
        return self.min_val(root.left_child)

    def insertion_binary(self, tab):
        if not tab:
            return
        median = len(tab) // 2
        root = AVLNode(tab[median])
        root.right_child = self.insertion_binary(tab[:median])  # chyba right_child
        root.left_child = self.insertion_binary(tab[median + 1:])  # chyba left_child
        return root


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


def random_number_generator(n):
    tab = []
    for x in range(n):
        tab.append(randint(10, 10*n))
    return tab


def heap(t, n, i):
    maxi = i
    childleft = 2 * i + 1
    childright = 2 * i + 2
    if childleft < n and t[childleft] < t[i]:
        maxi = childleft
    if childright < n and t[childright] < t[maxi]:
        maxi = childright
    if maxi != i:
        t[i], t[maxi] = t[maxi], t[i]
        heap(t, n, maxi)


def heapsort(t, n):
    for x in range(n//2, -1, -1):
        heap(t, n, x)
    for y in range(n-1, 0, -1):
        t[y], t[0] = t[0], t[y]
        heap(t, y, 0)


post_order_tab = []
tree = AVL()
while True:
    print("Menu:\n1 - BST\n2 - AVL\n3 - Testy\n4 - Zakończ działanie programu")
    x = input()
    if x == "1":
        root = None
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
                print(
                    "Menu procedur:\n1 - Wyszukiwanie min i max\n2 - Usunięcie elementu\n3 - Wypisanie in-order"
                    "\n4 - Wypisanie pre-order\n5 - Usunięcie całego drzewa(post-order)\n6 - Wypisanie pre-order podrzewa"
                    "\n7 - Równoważenie drzewa\n8 - Powrót do menu głównego")
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
                        post_order(root, post_order_tab)
                        for x in post_order_tab:
                            root = delete(root, x)
                        print("\n")
                    if chosen == 6:
                        print("Podaj klucz do podrzewa: ")
                        key = int(input())
                        if type(key) == int:
                            print("Find a key")
                            find_and_print(root, key)
                            print("\n")
                    if chosen == 7:
                        print("Maintenance in progress")  #
                    if chosen == 8:
                        break
        else:
            print("To nie jest liczba podaj poprawną wartość!")
    if x == "2":
        print("Ile chcesz podać liczb?")
        ile_liczb = input()
        if ile_liczb.isnumeric():
            ile_liczb = int(ile_liczb)
            ile = 0
            data = []
            while ile < ile_liczb:
                number = int(input())
                if type(number) == int:
                    data.append(number)
                    ile += 1
            start = time.time()
            heapsort(data,len(data))
            print("Czas sortowania ---- {} ----".format(time.time() - start))
            root = tree.insertion_binary(data)
            while True:
                print(
                    "Menu procedur:\n1 - Wyszukiwanie min i max\n2 - Usunięcie elementu\n3 - Wypisanie in-order"
                    "\n4 - Wypisanie pre-order\n5 - Usunięcie całego drzewa(post-order)\n6 - Wypisanie pre-order podrzewa"
                    "\n7 - Powrót do menu głównego")
                chosen = int(input())
                if type(chosen) == int:
                    if chosen == 1:
                        print("Największa wartość : ")
                        find_max(root)
                        print("\nNajmniejsza wartość : ")
                        find_min(root)
                        print("\n")
                    if chosen == 2:
                        print("Podaj ile wartości chcesz usunąć: ")
                        value = int(input())
                        if type(value) == int:
                            for v in range(value):
                                value_td = int(input())
                                if type(value_td) == int:
                                    root = tree.delete(root, value_td)
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
                        post_order(root, post_order_tab)
                        for x in post_order_tab:
                            root = tree.delete(root, x)
                        print("\n")
                    if chosen == 6:
                        print("Podaj klucz do podrzewa: ")
                        key = int(input())
                        if type(key) == int:
                            print("Ścieżka od klucza")
                            find_and_print(root, key)
                            print("\n")
                    if chosen == 7:
                        break
        else:
            print("To nie jest liczba podaj poprawną wartość!")
    if x == "3":
        print("Test")
    if x == "4":
        sys.exit()
    else:
        print("Podaj poprawną wartość")
