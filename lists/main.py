# functii ajutatoare (helper/utility functions)
def read_int_list_from_line():
    linie = input()  # ia o intreaga linie de pe consola => un str
    lista = []
    for s in linie.split(' '):
        lista.append(int(s))
    return lista
def read_float_list_from_line():
    linie = input()  # ia o intreaga linie de pe consola => un str
    lista = []
    for s in linie.split(' '):
        lista.append(float(s))
    return lista

# 1
'''
5      <--- n, nr. de node
10
7
4
3
9
'''


def main():
    n = int(input())
    a = []

    for i in range(n):
        x = int(input())
        a.append(x)

    # a
    cnt = 0
    for x in a:
        if x < 5:
            cnt += 1
    print(cnt)

    suma = 0
    cnt = 0
    for x in a:
        if  x > 5:
            cnt += 1
            suma += x
    ma = suma // cnt
    print(ma)
    # c)
    print(a.count(7))
    # d)
    print(max(a))


# if __name__ == '__main__':
#     main()

# 2
'''
10 7 10 8 5 10
'''
def main():
    # TODO deoarece toate nr. sunt pe aceiasi linie, n este optional
    a = read_int_list_from_line()
    # dar il putem pastra intr-o variabila, daca il calculam
    n = len(a)
    print(max(a))
    print(a.count(max(a)))
# if __name__ == '__main__':
#     main()


# 3 (check negative indexes in Python https://www.geeksforgeeks.org/python-negative-index-of-element-in-list/ )
# 3-10
#3

