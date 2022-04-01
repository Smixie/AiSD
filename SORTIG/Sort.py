import time
from random import randrange
import sys

sys.setrecursionlimit(5000)
# Algorytmy sortowania


def scalaj(t, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    l1 = []
    r1 = []
    compare = 0
    for x in range(n1):
        l1.append(t[l + x])

    for y in range(n2):
        r1.append(t[m + 1 + y])
    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        compare += 1
        if l1[i] > r1[j]:
            t[k] = l1[i]
            i += 1
        else:
            t[k] = r1[j]
            j += 1
        k += 1

    while i < n1:
        t[k] = l1[i]
        i += 1
        k += 1

    while j < n2:
        t[k] = r1[j]
        j += 1
        k += 1
    return compare


def mergesort(t, l, r):
    compare = 0
    if l < r:
        m = l + (r-l)//2
        compare += mergesort(t, l, m)
        compare += mergesort(t, m+1, r)
        compare += scalaj(t, l, m, r)
    return compare


def insertion_sort(t):
    comp = 0
    swap = 0
    for x in range(1, len(t)):
        key = t[x]
        j = x - 1
        comp += 1
        while j >= 0 and key > t[j]:
            t[j + 1] = t[j]
            j = j - 1
            swap += 1
            comp += 1
        t[j + 1] = key
    return swap, comp


def dzielenie(t, m, p):
    pivot = t[p]
    i = m - 1
    ile = 0
    for j in range(m, p):
        ile += 1
        if t[j] > pivot:
            i += 1
            ile += 1
            t[i], t[j] = t[j], t[i]
    t[i+1], t[p] = t[p], t[i+1]
    return i+1, ile


def quicksort(t, l, p):
    razem = 0
    if l < p:
        pod, ile = dzielenie(t, l, p)
        razem += ile
        razem += quicksort(t, l, pod - 1)
        razem += quicksort(t, pod + 1, p)
    return razem


def shellsort(t, n):
    interval = 1
    j = 1
    check = 0
    exchange = 0
    while (pow(3, j) - 1) / 2 < n:
        interval = (pow(3, j) - 1) // 2
        j += 1

    while interval > 0:
        for x in range(interval, n):
            temp = t[x]
            j = x
            check += 1
            while j >= interval and t[j - interval] < temp:
                t[j] = t[j - interval]
                j -= interval
                check += 1
                exchange += 1
            t[j] = temp
        interval = (interval - 1)//3
    return check,exchange


def heap(t, n, i):
    count = 0
    maxi = i
    childleft = 2 * i + 1
    childright = 2 * i + 2
    if childleft < n and t[childleft] < t[i]:
        maxi = childleft
    if childright < n and t[childright] < t[maxi]:
        maxi = childright
    if maxi != i:
        count += 1
        t[i], t[maxi] = t[maxi], t[i]
        count += heap(t, n, maxi)
    return count


def heapsort(t, n):
    count = 0
    for x in range(n//2, -1, -1):
        heap(t, n, x)
    for y in range(n-1, 0, -1):
        t[y], t[0] = t[0], t[y]
        count += heap(t, y, 0)
    return count

# Wykonanie wszystkich algorytmów


def execute_all_random(n):
    # print("----------Merge Sort----------")
    to_avg = 0
    print("n = {}".format(n))
    max_check = 0
    for x in range(1, 11):
        table = create_random(n)
        start_time = time.time()
        comp = mergesort(table, 0, n - 1)
        exe_time = time.time() - start_time
        to_avg += exe_time
        max_check= max(comp, max_check)
    print("Merge Sort\t{:.4f}\t-\t{}".format(to_avg / 10, comp))

    # print("----------Heap Sort----------")
    to_avg = 0
    max_swap = 0
    for x in range(1, 11):
        table = create_random(n)
        start_time = time.time()
        count = heapsort(table, n)
        exe_time = time.time() - start_time
        to_avg += exe_time
        max_swap = max(count, max_swap)
    print("Heapsort\t{:.4f}\t{}".format(to_avg / 10, max_swap))

    # print("----------Insertion Sort----------")
    to_avg = 0
    max_swap = 0
    max_check = 0
    for x in range(1, 11):
        table = create_random(n)
        start_time = time.time()
        swaps,comps = insertion_sort(table)
        exe_time = time.time() - start_time
        to_avg += exe_time
        max_swap = max(swaps,max_swap)
        max_check = max(comps, max_check)
    print("Insertion Sort\t{:.4f}\t{}\t{}".format(to_avg / 10, max_swap, max_check)) #time zamiana porownanie

    # print("----------Shell Sort----------")
    to_avg = 0
    max_swap = 0
    max_check = 0
    for x in range(1, 11):
        table = create_random(n)
        start_time = time.time()
        check, exchange = shellsort(table, n)
        exe_time = time.time() - start_time
        to_avg += exe_time
        max_swap = max(exchange, max_swap)
        max_check = max(check, max_check)
    print("Shell Sort\t{:.4f}\t{}\t{}".format(to_avg / 10, max_swap, max_check))
    print(" ")


def execute_all_ashape(n):
    # print("----------Merge Sort----------")
    to_avg = 0
    print("n = {}".format(n))
    max_check = 0
    for x in range(1, 11):
        table = a_shape(n,5)
        start_time = time.time()
        comps = mergesort(table, 0, n - 1)
        exe_time = time.time() - start_time
        to_avg += exe_time
        max_check = max(comps, max_check)
    print("Merge Sort\t{:.4f}\t-\t{}".format(to_avg / 10, comps))

    # print("----------Heap Sort----------")
    to_avg = 0
    max_swap = 0
    for x in range(1, 11):
        table = a_shape(n,5)
        start_time = time.time()
        count = heapsort(table, n)
        exe_time = time.time() - start_time
        to_avg += exe_time
        max_swap = max(count, max_swap)
    print("Heapsort\t{:.4f}\t{}".format(to_avg / 10, max_swap))

    # print("----------Insertion Sort----------")
    to_avg = 0
    max_swap = 0
    max_check = 0
    for x in range(1, 11):
        table = a_shape(n,5)
        start_time = time.time()
        swaps, comps = insertion_sort(table)
        exe_time = time.time() - start_time
        to_avg += exe_time
        max_swap = max(swaps, max_swap)
        max_check = max(comps, max_check)
    print("Insertion Sort\t{:.4f}\t{}\t{}".format(to_avg / 10, max_swap, max_check))

    # print("----------Shell Sort----------")
    to_avg = 0
    max_swap = 0
    max_check = 0
    for x in range(1, 11):
        table = a_shape(n,5)
        start_time = time.time()
        check, exchange = shellsort(table, n)
        exe_time = time.time() - start_time
        to_avg += exe_time
        max_swap = max(exchange, max_swap)
        max_check = max(check, max_check)
    print("Shell Sort\t{:.4f}\t{}\t{}".format(to_avg / 10, max_swap, max_check))
    print(" ")


def execute_all_asc(n):
    # print("----------Merge Sort----------")
    to_avg = 0
    print("n = {}".format(n))
    max_check = 0
    for x in range(1, 11):
        table = create_ascending(n)
        start_time = time.time()
        comps = mergesort(table, 0, n - 1)
        exe_time = time.time() - start_time
        to_avg += exe_time
        max_check = max(comps, max_check)
    print("Merge Sort\t{:.4f}\t-\t{}".format(to_avg / 10, max_check))

    # print("----------Heap Sort----------")
    to_avg = 0
    max_swap = 0
    for x in range(1, 11):
        table = create_ascending(n)
        start_time = time.time()
        count = heapsort(table, n)
        exe_time = time.time() - start_time
        to_avg += exe_time
        max_swap = max(count, max_swap)
    print("Heapsort\t{:.4f}\t{}".format(to_avg / 10, max_swap))

    # print("----------Insertion Sort----------")
    to_avg = 0
    max_swap = 0
    max_check = 0
    for x in range(1, 11):
        table = create_ascending(n)
        start_time = time.time()
        swaps, comps = insertion_sort(table)
        exe_time = time.time() - start_time
        to_avg += exe_time
        max_swap = max(swaps, max_swap)
        max_check = max(comps, max_check)
    print("Insertion Sort\t{:.4f}\t{}\t{}".format(to_avg / 10, max_swap, max_check))

    # print("----------Shell Sort----------")
    to_avg = 0
    max_swap = 0
    max_check = 0
    for x in range(1, 11):
        table = create_ascending(n)
        start_time = time.time()
        check, exchange = shellsort(table, n)
        exe_time = time.time() - start_time
        to_avg += exe_time
        max_swap = max(exchange, max_swap)
        max_check = max(check, max_check)
    print("Shell Sort\t{:.4f}\t{}\t{}".format(to_avg / 10, max_swap, max_check))
    print(" ")


def execute_all_desc(n):
    # print("----------Merge Sort----------")
    to_avg = 0
    print("n = {}".format(n))
    max_check = 0
    for x in range(1, 11):
        table = create_descending(n)
        start_time = time.time()
        comps = mergesort(table, 0, n - 1)
        exe_time = time.time() - start_time
        to_avg += exe_time
        max_check = max(comps, max_check)
    print("Merge Sort\t{:.4f}\t-\t{}".format(to_avg / 10, max_check))

    # print("----------Heap Sort----------")
    to_avg = 0
    max_swap = 0
    for x in range(1, 11):
        table = create_descending(n)
        start_time = time.time()
        count = heapsort(table, n)
        exe_time = time.time() - start_time
        to_avg += exe_time
        max_swap = max(count, max_swap)
    print("Heapsort\t{:.4f}\t{}".format(to_avg / 10, max_swap))

    # print("----------Insertion Sort----------")
    to_avg = 0
    max_swap = 0
    max_check = 0
    for x in range(1, 11):
        table = create_descending(n)
        start_time = time.time()
        swaps, comps = insertion_sort(table)
        exe_time = time.time() - start_time
        to_avg += exe_time
        max_swap = max(swaps, max_swap)
        max_check = max(comps, max_check)
    print("Insertion Sort\t{:.4f}\t{}\t{}".format(to_avg / 10, max_swap, max_check))

    # print("----------Shell Sort----------")
    to_avg = 0
    max_swap = 0
    max_check = 0
    for x in range(1, 11):
        table = create_descending(n)
        start_time = time.time()
        check, exchange = shellsort(table, n)
        exe_time = time.time() - start_time
        to_avg += exe_time
        max_swap = max(exchange, max_swap)
        max_check = max(check, max_check)
    print("Shell Sort\t{:.4f}\t{}\t{}".format(to_avg / 10, max_swap, max_check))
    print(" ")


def execute_all_vshape(n):
    # print("----------Merge Sort----------")
    to_avg = 0
    print("n = {}".format(n))
    max_check = 0
    for x in range(1, 11):
        table = v_shape(n,5)
        start_time = time.time()
        comps = mergesort(table, 0, n - 1)
        exe_time = time.time() - start_time
        to_avg += exe_time
        max_check = max(comps, max_check)
    print("Merge Sort\t{:.4f}".format(to_avg / 10, max_check))

    # print("----------Heap Sort----------")
    to_avg = 0
    max_swap = 0
    for x in range(1, 11):
        table = v_shape(n,5)
        start_time = time.time()
        count = heapsort(table, n)
        exe_time = time.time() - start_time
        to_avg += exe_time
        max_swap = max(count, max_swap)
    print("Heapsort\t{:.4f}\t-\t{}".format(to_avg / 10, max_swap))

    # print("----------Insertion Sort----------")
    to_avg = 0
    max_swap = 0
    max_check = 0
    for x in range(1, 11):
        table = v_shape(n,5)
        start_time = time.time()
        swaps, comps = insertion_sort(table)
        exe_time = time.time() - start_time
        to_avg += exe_time
        max_swap = max(swaps, max_swap)
        max_check = max(comps, max_check)
    print("Insertion Sort\t{:.4f}\t{}\t{}".format(to_avg / 10, max_swap, max_check))

    # print("----------Shell Sort----------")
    to_avg = 0
    max_swap = 0
    max_check = 0
    for x in range(1, 11):
        table = v_shape(n,5)
        start_time = time.time()
        check, exchange = shellsort(table, n)
        exe_time = time.time() - start_time
        to_avg += exe_time
        max_swap = max(exchange, max_swap)
        max_check = max(check, max_check)
    print("Shell Sort\t{:.4f}\t{}\t{}".format(to_avg / 10, max_swap, max_check))
    print(" ")


# Tworzenie danych do testów


def create_random(n):
    local_table = []
    for x in range(n):
        local_table.append(randrange(1, 10 * n))
    return local_table


def create_ascending(n):
    local_table = []
    for x in range(n):
        local_table.append(x+1)
    return local_table


def create_descending(n):
    local_table = []
    for x in range(n, 0, -1):
        local_table.append(x)
    return local_table


def v_shape(n, k):
    local_table = []
    for x in range(n):
        if x < n / 2 - 1:
            local_table.append(n * 10 - 4 * x - k)
        elif x == n / 2 - 1:
            local_table.append(x)
        elif x > n / 2 - 1:
            local_table.append(x * 2 + k)
    return local_table


def a_shape(n, k):
    local_table = []
    l = k
    for x in range(n):
        if x < n / 2 - 1:
            local_table.append(1 + l)
            l += 2
        if x == n / 2 - 1:
            local_table.append(n + 100)
            l = n + 100 - 2
        if x > n / 2 - 1:
            local_table.append(l)
            l -= 2
    return local_table


def shell_sort_input(t, n):
    interval = 1
    j = 1
    ch = 0
    exch = 0
    while (pow(3, j) - 1) / 2 < n:
        interval = (pow(3, j) - 1) // 2
        j += 1

    while interval > 0:
        print("Przyrost = ", interval)
        for x in range(interval, n):
            temp = t[x]
            j = x
            ch += 1
            while j >= interval and t[j - interval] < temp:
                t[j] = t[j - interval]
                j -= interval
                ch += 1
                exch += 1
            t[j] = temp
        interval = (interval - 1)//3
    return ch,exch


def dzielenie_input(t, l, p):
    pivot = t[p]
    print("Pivot = ", pivot)
    i = l - 1
    ile = 0
    zmiany = 0
    for j in range(l, p):
        ile += 1
        if t[j] > pivot:
            zmiany += 1
            i += 1
            t[i], t[j] = t[j], t[i]
    i += 1
    if i != p:
        t[i], t[p] = t[p], t[i]
    return i, ile, zmiany


def quicksort_input(t, l, p):
    razem = 0
    zmiany = 0
    if l < p:
        pod, ile, zmiany = dzielenie_input(t, l, p)
        razem += ile
        x, zm = quicksort_input(t, l, pod - 1)
        razem += x
        zmiany += zm
        y, zm1= quicksort_input(t, pod + 1, p)
        razem += y
        zmiany += zm1
    return razem , zmiany


def scalaj_input(t, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    l1 = []
    r1 = []
    swap = 0
    for x in range(n1):
        l1.append(t[l + x])

    for y in range(n2):
        r1.append(t[m + 1 + y])
    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if l1[i] >= r1[j]:
            t[k] = l1[i]
            i += 1
            swap += 1
        else:
            t[k] = r1[j]
            j += 1
        k += 1

    while i < n1:
        t[k] = l1[i]
        i += 1
        k += 1

    while j < n2:
        t[k] = r1[j]
        j += 1
        k += 1
    return swap


def mergesort_input(t, l, r):
    swap = 0
    if l < r:
        m = l + (r-l)//2
        swap += mergesort_input(t, l, m)
        swap += mergesort_input(t, m+1, r)
        swap += scalaj_input(t, l, m, r)
    return swap


quicktest = [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000]
testcases = [3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000, 27000, 30000]

test_table = [9, 5, 1, 4, 3, 25, 8, 7, 15, 10]
chosen = []
chosen1 = []
chosen2 = []
chosen3 = []
chosen4 = []

print("1 - WCZYTANIE Z KLAWIATURY")
print("2 - TESTY")
pick = int(input())

if pick == 1:
    print("Ile liczb chcesz podać?")
    y = int(input())
    for x in range(y):
        v = int(input())
        chosen.append(v)
        chosen1.append(v)
        chosen2.append(v)
        chosen3.append(v)
        chosen4.append(v)

    print("-----Quick sort-----")
    print(chosen)
    start = time.time()
    x ,d = quicksort_input(chosen, 0, y - 1)
    print("Czas działania = {} sekundy".format(time.time() - start))
    print("Zmiany ",d)
    print("Porównania ",x)
    print(chosen)

    print("\n-----Shell Sort-----")
    print(chosen1)
    start1 = time.time()
    ch , exch = shell_sort_input(chosen1, y)
    print("Czas działania = {} sekundy".format(time.time() - start1))
    print("Porównania = ",ch)
    print("Zamiany = ",exch)
    print(chosen1)

    print("\n-----Merge Sort-----")
    print(chosen2)
    start2 = time.time()
    sw = mergesort_input(chosen2, 0, y-1)
    print("Czas działania = {} sekundy".format(time.time() - start2))
    print("Liczba scaleń ",sw)
    print(chosen2)

    print("\n-----Insertion Sort-----")
    print(chosen3)
    start3 = time.time()
    swap, comp = insertion_sort(chosen3)
    print("Czas działania = {} sekundy".format(time.time() - start3))
    print("Zamiany = {} ".format(swap))
    print("Porównania = {} ".format(comp))
    print(chosen3)

    print("\n-----Heap Sort-----")
    print(chosen4)
    start4 = time.time()
    count = heapsort(chosen4, y)
    print("Czas działania = {} sekundy".format(time.time() - start4))
    print("Liczba zamian = ",count)
    print(chosen4)

if pick == 2:
    print("Name\ttime\tswap\tcheck")
    print("1. Losowo")
    for x in range(len(testcases)):
        test = testcases[x]
        execute_all_random(test)
    print("2. Rosnąco")
    for x in range(len(testcases)):
        test = testcases[x]
        execute_all_asc(test)
    print("3. Malejąco")
    for x in range(len(testcases)):
        test = testcases[x]
        execute_all_desc(test)
    print("4. A-Shape")
    for x in range(len(testcases)):
        test = testcases[x]
        execute_all_ashape(test)
    print("5. V-Shape")
    for x in range(len(testcases)):
        test = testcases[x]
        execute_all_vshape(test)

    print("Quick Sort")
    to_avg = 0
    print("Random")
    for x in range(len(quicktest)):
        test = quicktest[x]
        for y in range(10):
            t = create_random(test)
            start = time.time()
            z = quicksort(t, 0, test-1)
            to_avg += time.time() - start
        print("{}\t{:.4f}\t{}".format(test, to_avg/10, z))

    to_avg = 0
    print("Malejące")
    for x in range(len(quicktest)):
        test = quicktest[x]
        for y in range(10):
            t = create_descending(test)
            start = time.time()
            z = quicksort(t, 0, test-1)
            to_avg += time.time() - start
        print("{}\t{:.4f}\t{}".format(test, to_avg/10, z))

    to_avg = 0
    print("Rosnące")
    for x in range(len(quicktest)):
        test = quicktest[x]
        for y in range(10):
            t = create_ascending(test)
            start = time.time()
            z = quicksort(t, 0, test-1)
            to_avg += time.time() - start
        print("{}\t{:.4f}\t{}".format(test, to_avg/10,z))

    to_avg = 0
    print("A-shape")
    for x in range(len(quicktest)):
        test = quicktest[x]
        for y in range(10):
            t = a_shape(test,5)
            start = time.time()
            z = quicksort(t, 0, test-1)
            to_avg += time.time() - start
        print("{}\t{:.4f}\t{}".format(test, to_avg/10, z))

    to_avg = 0
    print("V-shape")
    for x in range(len(quicktest)):
        test = quicktest[x]
        for y in range(10):
            t = v_shape(test,5)
            start = time.time()
            z = quicksort(t, 0, test-1)
            to_avg += time.time() - start
        print("{}\t{:.4f}\t{}".format(test, to_avg/10, z))
