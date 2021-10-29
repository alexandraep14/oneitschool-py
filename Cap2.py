# # 8
# n = 5
#
# # # primele argumente din print() sunt valorile afisate
# # #  dar pt a-l putea configura (ii spunem ca valorile
# # #  sa aiba un anume separator, iar la final de tot sa afiseze niste caractere anume)
# # #  avem nevoie de alt mod de a le trimite, printr-o "cheie"
# # # Deci sep='-'  inseamna ca lui print ii trimitem si o variabile sep,
# # #   cu valoarea '-', iar programul va pune '-' intre orice doua valori
# # #     \/ valori    \/ argumentele speciale
# # print("x", '+', 23, sep='-', end='\n')
#
# # paralela cu C++
# #  range(n) -> for(int i = 0; i < n; i++)
# for i in range(n):  # range(n) => [0,1,2,...,n-1]
#     for j in range(n):
#         print("* ", end='')
#     print()
#
# # b
# for i in range(n):
#     # ce valori ia i este decis la inceput,
#     #   deci sa facem n-=1 nu-l va opri pe i din a parcurge toate valorile
#     for j in range(i+1):
#         print("* ", end='')
#     print()

# # 1
#
# n = int(input(" n = "))
# prod = 1
# for i in range(2, 2*n+1, 2):
#     # primul 2 este prima valoarea a lui i
#     # ultimul 2 este cu cat se modifica de la pas la pas
#     # 2*n+1 este stop, deci pozitia la care se opreste (!!!
#     #   !!! fara sa o foloseasca)
#     # print(i, end=' ')
#     prod *= i
# print(prod)

# 9
"""
3
63
153
62
"""
# n = int(input("n = "))
# minim = 10**9
# maxim = -10**9
#
# for i in range(n):
#     # de n ori citim x-ul, elementul curent din sir
#     x = int(input())
#     if x > maxim:
#         maxim = x
#     if x < minim:
#         minim = x
# # print(f'{maxim}{minim}')
# p10 = 1
# while p10 < minim:
#     p10 *= 10
# num = maxim * p10 + minim
# print(num)


# def is_even(n: int) -> bool:
#     """
#
#     """
#     return n % 2 == 0

# print(is_even(2.3))
# print(is_even(2))

# 6, 7, 9
# 8 b,d
# n = int(input(" n = "))
# minim = 100000
# maxim = -100000
# for  i in range(n):
#     x = int(input(" x = "))
#     if x > maxim:
#         maxim = x
#     if x < minim:
#             minim = x
# p10 = 1
# while p10 < minim:
#     p10 *= 10
#     num = maxim * p10 + minim
# print(num)
import math


# # 6
# def main():
#     n = 2
#     x = 5
#     y = 40
#
#     # informatic putem testa si toate posibilitatile
#     # Adica putem incepe de la 1 si inmultim in continuu cu 2
#     #  pana cand il depasim pe y ca marime a puterii
#     putere = 1
#
#     while putere <= y:
#         if x <= putere:
#             print(putere)
#         putere *= 2
#
# if __name__ == '__main__':
#     main()
#


# 8 b)
# n = 5
#
# for i in range(n):
#     for j in range(i-1 , n-1):  #<- aleluia
#
#         print("* ", end=' ')
#     print( )

# d)
# n = 5
#
# for i in range(n):
#     for j in range(i+1):
#         # if j != 0:  # aleluia again
#         print (j+1, end=' ')
#     print()

# 7

# def main():
#     n  = int(input(" n = "))
#
#     num = 1
#     E1 = 0
#     for i in range(1, n+1):
#         # print(i, i+1)
#         num = i *10 + i + 1
#         E1 += num
#         # print(num, suma )
#     print(f'E1={E1}')
#
# if __name__ == '__main__':
#     main()


# def main():
#     n = int(input(" n = "))
#
#     num = 1
#     E2 = 1
#
#     for i in range(2,n+1):  # num=12 si i=3 => num=123
#         num = num * 10 + i
#         E2 += num
#     print(f'E2 = {E2}')
#
# if __name__ == '__main__':
#     main()

# 5
# oglindit:
# 12 23 nu
# 123 321 da
# palindrom:
# 12 nu
# 9 11 292 DA!

# este palindrom daca numarul este acelasi citit atat de la st la dr
#  cat si de la dr. la st.
# PE SCURT, numarul este egal cu oglinditul lui

# functie care calculeaza oglinditul unui nr. natural
def oglindit(num):
    res = 0
    # num    res
    # 123    0
    # 12     3
    # 1      32
    # 0      321
    while num > 0:
        lastDigit = num % 10  # ultima cifra
        res = res * 10 + lastDigit
        # taiem ultima cifre din num
        num //= 10
    return res


# functie care verifica daca un nr. natural este palindrom
def estePalindrom(num):
    # Este egal num cu oglinditul lui?
    if oglindit(num) == num:
        return True
    else:
        return False


# def main():
#     a = 8
#     b = 13
#     suma = 0
#     mA = 0
#     cnt = 0
#     # print(oglindit(123))  # va afisa 321
#     for i in range(a,b+1):
#         if estePalindrom(i) == True:
#             # print(i, end=' ')
#             cnt += 1
#             suma += i
#     mA = suma / cnt
#     print(mA)
#
# if __name__ == '__main__':
#     main()


# 14

# def main():
#     n = int(input(" n = "))
#
#     for i in range(n):
#         for j in range(i+1,n+1):
#             for k in range(j+ 1, n + 1):
#                 if i**2 + j**2 == k**2:
#                     print(i , j, k)
# if __name__ == '__main__':
#     main()

# 15
"""
5
18_000
230
190_000
2_400
2_000_000
"""


# def main():
#     n = int(input(" n = "))
#     max1 = 0
#     max2 = 0
#     min = 0
#     for i in range(n):
#         x = int(input())
#         if max1 < x:
#             max2 = max1
#             max1 = x
#         elif  max2 < x:
#             max2 = x
#     print(max1, max2)

# if __name__ == '__main__':
#     main()

# 18
# def main():
#     n = int(input(" n = "))
#     mH = 0
#     suma = 0
#     for i in range(n):
#         x = int(input())
#         suma += 1/x
#     mH = n / suma
#     print(mH)

# if __name__ == '__main__':
#     main()

# 3 10 (cu tot cu functie) 11 12 13
# 16 17 19 generosity at its best

# 3
# 10
def suma_cifre(x: int) -> int:
    """
    Calculeaza suma cifrelor unui numar
    :param x: numar intreg
    :return: suma
    """
    sum = 0
    while x > 0:
        last_digit = x % 10
        sum += last_digit
        x //= 10
    return sum


'''
5
2
10
11
39
32
80
84
'''


def main():
    n = int(input(" n = "))
    a = int(input(" a = "))
    b = int(input(" b = "))

    summ = 0
    cnt = 0
    for i in range(n):
        x = int(input())
        if a <= suma_cifre(x) <= b:
            summ += x
            cnt += 1

    ma = summ / cnt

    print(ma, summ)


# if __name__ == '__main__':
#     main()
#
# #11
def main():
    s = int(input("s = "))

    for i in range(1, s):
        for j in range(i + 1, s):
            for k in range(j + 1, s):
                if i + j + k == s:
                    print(i, j, k)


# if __name__ == '__main__':
#     main()

# #12 7331 7 * 10
'''
4
17
3
234
17
3
23
11
11
'''


def is_prime(num):  # este numarul prim?
    """
    Verifica daca numarul este prim
    :param num: numar intreg
    :return:true or false
    """
    if num <= 1:
        return False

    for div in range(2, num):
        if num % div == 0:
            return False

    return True


def main():
    n = int(input())
    num = 0
    for i in range(n):
        x = int(input())  # nu inteleg de ce nu ia toate numerele
        lastdigit = x % 10
        num = num * 10 + lastdigit

    print(num)
    if is_prime(num):
        print("Este prim.")
    else:
        print("Nu este prim")

    # verifici daca num este prim :)
    # functia is_prime


# if __name__ == '__main__':
#     main()


# 16
def main():
    n = int(input(" n = "))
    max = 0
    cntmax = 0
    min = 0
    for i in range(n):
        x = int(input())

        if max < x:
            max = x
            cntmax = 1
        elif max == x:
            cntmax += 1  # nu mai inteleg nimic

    print("Nota ", max, " obtinuta de", cntmax, "elevi")


# if __name__ == '__main__':
#     main()

# 17

# 21

def main():
    n = int(input())

    while n > 0:
        last_digit = n % 10
        n //= 10
        if last_digit % 2 == 0:
            print(last_digit)


# if __name__ == '__main__':
#     main()

# 22
def invers_nr(n):
    """
    Calculeaza inversul numarului
    :param n: numar intreg
    :return: returneaza inversul numarului
    """
    num = 0
    while n > 0:
        last_digit = n % 10
        n //= 10
        num = num * 10 + last_digit
    return num


def main():
    n = int(input())
    num1 = 0
    num2 = 0
    n = invers_nr(n)
    while n > 0:
        last_digit = n % 10
        n //= 10
        if last_digit % 2 == 0:
            num1 = num1 * 10 + last_digit
        if last_digit % 2 == 1:
            num2 = num2 * 10 + last_digit
    print(num1, num2)


#
# if __name__ == '__main__':
#   main()

# 23

# aflam cate cifre va avea fiecare jumatate
def numara_cifre(n):
    """
    Numara cifrele
    :param n: numar intreg
    :return:calculeaza cate numere sunt
    """
    cnt = 0
    while n > 0:
        last_digit = n % 10
        n //= 10
        cnt += 1
    return cnt


def main():
    # citiri
    n = int(input())
    # numaram cate cifre are n, ca sa aflam dupa cate are fiecare jumatate
    cnt_n = numara_cifre(n)
    if cnt_n % 2 == 0:
        cnt1 = cnt_n // 2  # cate cifre are prima jumatate
        cnt2 = cnt_n // 2  # cate cifre are a doua jumatate
    else:
        cnt1 = cnt_n // 2  # cate cifre are prima jumatate
        cnt2 = cnt_n // 2 + 1  # cate cifre are a doua jumatate

    # primele cnt2 cifre le extragi in num2
    num1 = 0
    for i in range(cnt2):
        last_digit = n % 10  # cifrele le iei din numar :)
        n //= 10
        num1 = num1 * 10 + last_digit

    # urmatoarele cnt1 cifre le extragi in num1
    num2 = 0
    for j in range(cnt1):
        last_digit = n % 10
        n //= 10
        num2 = num2 * 10 + last_digit
    print(invers_nr(num2), invers_nr(num1))


# if __name__ == '__main__':
#     main()

# 24
def main():
    n = int(input())
    cnt = 0

    while n > 0:
        lastdigit = n % 10
        cnt += 1
        n //= 10
        if cnt % 2 == 1:
            print(lastdigit, end='')


# if __name__ == '__main__':
#     main()

# 25
def main():
    n = int(input())

    while n // 100 != 0:
        n //= 10
    firstdigit = n // 10
    secondigit = n % 10
    sum = firstdigit + secondigit
    print(sum)


# if __name__ == '__main__':
#     main()

# 26
def main():
    n = int(input())
    num = 0
    lastdigit = n % 10
    firstdigit = invers_nr(n) % 10
    num = firstdigit * 10 + lastdigit

    # daca num este par, atunci deja ai gasit raspunsul
    # iar daca nu este par, doar il inmultim cu 2
    if num % 2 == 1:
        num *= 2
    print(num)


# if __name__ == '__main__':
#     main()

# 27 28 29 30 31 32 33
# 27
# 724582
def main():
    n = int(input())
    num = 0
    poz = 1

    cnt = 0
    rev = invers_nr(n)
    while rev > 0:
        lastDigit = rev % 10
        if poz % 2 == 1:
            if lastDigit % 2 == 0:
                num = num * 10 + lastDigit
        poz += 1
        rev //= 10

    print(num)


# if __name__ == '__main__':
#     main()


def main():
    n = int(input())
    units = 0
    cnt = 0
    units = n % 10
    while n > 0:
        lastDigit = n % 10
        n //= 10
        if lastDigit == units:
            cnt += 1
    print(cnt, units)


# if __name__ == '__main__':
#     main()

# 29
def cifra_maxima(n):
    """
    calculeaza cifra maxima
    :param n:
    :return: maximul
    """
    max = 0
    while n > 0:
        last_digit = n % 10
        n //= 10
        if last_digit > max:
            max = last_digit
    return max


def main():
    n = int(input())
    lastDigit = 0
    cnt = 0
    max = 0
    # while n >0:
    #     lastDigit = n % 10
    #     n //= 10
    #     if lastDigit > max:
    #         max = lastDigit
    #         cnt = 1
    #     elif lastDigit == max:
    #         cnt += 1
    # print(max , cnt)

    max = cifra_maxima(n)
    # while n >0:
    #     lastDigit = n % 10
    #     n //= 10
    #     if lastDigit > max:
    #         max = lastDigit

    cnt = 0
    while n > 0:
        lastDigit = n % 10
        n //= 10
        if lastDigit == max:
            cnt += 1
    print(max, cnt)


# if __name__ == '__main__':
#     main()

# 30

def main():
    n = int(input())
    sum = 0
    nr = 2
    while sum + nr <= n:  # daca vezi ca mai poti sa aduagi inca un nr, atunci continuam
        sum += nr
        print(nr)  # afisam numarul care a fost adaugat la suma
        nr += 2


# if __name__ == '__main__':
#     main()


# 2, 5, 7, 9, 12, 17, 21, 30

# 2
def is_prime(num):
    """
    Calculeaza daca numarul este prim
    :param num: numar intreg
    :return: true or false
    """
    if num <= 1:
        return False
    for div in range(2, num):
        if num % div == 0:
            return False
    return True


def main():
    num = int(input())
    sum = 0
    cnt = 0
    m_a = 0
    for i in range(num):
        x = int(input())
        if is_prime(x) == True:
            sum += x
            cnt += 1
    m_a = sum / cnt
    print(m_a)


# if __name__ == '__main__':
#     main()

# 5
def oglindit(num):
    """
    Calculeaza oglinditului unui numa
    :param num: numar intreg
    :return: oglinditul
    """
    invers = 0
    while num > 0:
        last_digit = num % 10
        invers = invers * 10 + last_digit
        num //= 10
        return invers


def este_palindrom(num):
    """
    Calculeaza daca un numar este palindrom
    :param num:
    :return: true or false
    """
    if oglindit(num) == num:
        return True
    else:
        return False


def main():
    a = 8
    b = 13
    suma = 0
    m_p = 0
    cnt = 0
    for a in range(a, b):
        if este_palindrom(a) == True:
            suma += a
            cnt += 1

    m_p = suma / cnt
    print(m_p, suma)


# if __name__ == '__main__':
#     main()


# 7
def main():
    n = int(input())
    num = 0
    num2 = 0
    E1 = 0
    E2 = 0
    for i in range(1, n):
        num = i * 10 + i + 1
        E1 += num

    # print(E1, num)

    for i in range(1, n):
        num2 = num2 * 10 + i
        E2 += num2
    print(num2, E2)


# if __name__ == '__main__':
#     main()

# 9
def main():
    n = int(input())
    maxim = 0
    min = 9999999
    lastdigit = 0
    for i in range(n):
        x = int(input())
        if x > maxim:
            maxim = x
        if x < min:
            min = x
    num = maxim
    min = invers_nr(min)
    while min > 0:
        lastdigit = min % 10
        min //= 10
        num = num * 10 + lastdigit
    print(num)


# if __name__ == '__main__':
#     main()

12


def main():
    '''
5
237
23
453
11
    '''
    n = int(input())
    lastdigit = 0
    num = 0

    for i in range(n):
        x = int(input())
        lastdigit = x % 10
        num = num * 10 + lastdigit

    if is_prime(num):
        print('Numarul ', num, ' este prim.')
    else:
        print('Nu este prim.')


# if __name__ == '__main__':
#     main()

# 17
def main():
    n = int(input())
    m_elev = 0
    m_clasa = 0
    cnt = 0
    cnt2 = 0
    sum_melev = 0
    med_max = 0
    for i in range(n):
        x = int(input())
        y = int(input())
        m_elev = (x + y) / 2
        if m_elev > med_max:
            med_max = m_elev

    if m_elev > 5:
        cnt += 1
        sum_melev += m_elev
        m_clasa = sum_melev / cnt
        print('Media clasei este ', m_clasa, 'Niciun elev coringent.')
    else:
        cnt2 += 1
        print(cnt2, ' elevi corigenti.')

    print('Media maxima este ', med_max)


# if __name__ == '__main__':
#     main()

# 21
def main():
    n = int(input())
    last_digit = 0
    first_print = True
    while n > 0:
        last_digit = n % 10
        n //= 10
        if last_digit % 2 == 0:
            if first_print:
                print(last_digit, end='')  # am incercat cu sep = ' , '/ nu merge
                first_print = False
            else:
                print(',', last_digit, end='')


# if __name__ == '__main__':
#     main()
# ce a ramas de recapitulat din lista, plus:
# 31-35

# 31
def main():
    n = int(input('n = '))
    x = 10
    for i in range(x):
        sum = i + i + 1
        if sum % n == 0:
            print(i, i + 1)


# if __name__ == '__main__':
#      main()
def invers_nr(n):
    """
     Calculeaza inversul  unui  numar
    :param n: nr intreg
    :return: inversul numarului
    """
    num = 0
    last_digit = 0
    while n > 0:
        last_digit = n % 10
        n //= 10
        num = num * 10 + last_digit
    return num


def palindrom(n):
    """
    Calculeaza daca un numar este palindrom
    :param n: numar intreg
    :return: true / false
    """
    if invers_nr(n) == n:
        return True
    else:
        return False


# 32
def main():
    n = int(input('n = '))
    zecisiunitati = 0
    prima_cifra = 0
    invers = 0
    if palindrom(n) == True:
        zecisiunitati = n % 100
        print(zecisiunitati)
    else:
        invers = invers_nr(n)
        prima_cifra = invers % 10
        print(prima_cifra)


# if __name__ == '__main__':
#     main()

# 33
def main():
    n = float(input())
    i = n

    while i > 0:  # am incercat cu for i in range(i = n , 0 , i-= 2)/nu merge
        print(i)
        i -= 2


# if __name__ == '__main__':
#     main()

# 36
def main():
    n = int(input())
    b = int(input())

    num = 0
    p10 = 1  # units
    while n != 0:
        r = n % b

        num += p10 * r
        p10 *= 10

        # print(num, end= ' ')
        n //= b
    print(num)


# if __name__ == '__main__':
#     main()

def set_bits(n: int):
    """
    -> int: calculeaza cati biti de 1 are n in scrierea binara
    :param n: 
    :return: cnt
    """
    cnt = 0
    while n != 0:
        r = n % 2
        if r == 1:
            cnt += 1
        n //= 2
    return cnt


def main():
    # print(set_bits(32))  # 1
    # print(set_bits(312))  # 4
    # print(set_bits(17))  # 2

    a = int(input())
    b = int(input())
    if set_bits(a) > set_bits(b):
        print(a)
    else:
        print(b)


# if __name__ == '__main__':
#     main()

# TODO tema:
# 34
# 35.
'''
n=3
=> 3 9 27 81 243 729 2187 6561 19683
'''


# 38-40
# 34

def main():
    m = 50
    n = 9

    # if n % 2 == 0:
    #     x = n + 1
    # else:
    #     x = n + 2
    # for i in range(x, x + m+1, 2):
    #     print(i, end = ' ')

    if n % 2 == 0:
        x = n + 1
    else:
        x = n + 2
    first = x
    while x - first <= m:
        print(x, end=" ")
        x += 2


# if __name__ == '__main__':
#     main()


# 35

def main():
    n = int(input())
    x = 30000

    # for i in range(0, 100):  # matematic pt o orice n > 1 n ** 100 va fi mai mare decat 30000
    #     power = n ** i
    #     if power <= x:
    #         print(power, end=' ')
    #     else:
    #         break
    # print()

    power = 1
    while power < 30000:
        print(power, end=' ')
        power *= n


# if __name__ == '__main__':
#     main()

# 38
def main():
    a = int(input())
    b = int(input())
    c = int(input())
    suma = a + b + c

    while a + b != c:
        a = b
        b = c
        c = int(input())
        suma += c
    print(suma)


# if __name__ == '__main__':
#     main()

# 39
def main():
    n = int(input())
    # cum nu avem o regula clara pt a gasi al i-ulea nr prim,
    #  nu este util sa folosim for.
    # 7
    # 11
    # 13
    # 17
    # 19
    # este_prim()
    # TODO daca oricum n-ai o regula clara, le poti testa pe toate

    # # asa putem afisa oricate nr. prime, dar le vom limita la primele n
    # num = 1
    # while True:
    #     if is_prime(num):
    #         print(num, end=' ')
    #     num += 1

    cnt_found = 0  # we count the primes we found
    num = 2  # we iterate over the possible primes (so over all whole numbers)

    while cnt_found < n:
        # cat timp am gasit mai putin de n numere prime :)
        if is_prime(num):
            cnt_found += 1
            print(num)
        num += 1


# if __name__ == '__main__':
#     main()

def estePerfect(n):
    """
    Verifica daca numarul este perfect
    :param n:
    :return: Suma divizorilor este egala cum numarul
    """
    suma = 0
    for div in range(1, n):
        if n % div == 0:
            suma += div
    return suma == n


def numara_cifre_pare(n):
    """
    Numara cate cifre pare are un numar.
    :param n: a whole number
    :return: how many even digits does n have
    """
    cnt = 0
    while n > 0:
        last_Digit = n % 10
        if last_Digit % 2 == 0:
            cnt += 1
        n //= 10
    return cnt


def main():
    n = int(input())  # 123 => 321

    x = invers_nr(n)
    last_two = x % 100
    last_two = invers_nr(last_two)

    print(last_two)
    if estePerfect(last_two):
        print(numara_cifre(n))
    else:
        print(numara_cifre_pare(n))
    # while num > 100:  # conditia este opusul a ceea ce ne dorim


# if __name__ == '__main__':
#     main()

# TODO tema
# 1. Dupa modelul numara_cifre_pare vei adauga doc strings in functiile din cap2.py
# 2. 41-45

# 41
def cnt_divizori(x):
    cnt = 0
    for div in range(1, x):
        if x % div == 0:
            cnt += 1

    return cnt


def main():
    n = int(input())
    max = 0

    for i in range(n):
        x = int(input())
        if cnt_divizori(x) < max:
            max = cnt_divizori(x)
    print(max)


# if __name__ == '__main__':
#     main()

# 42


def main():
    n = int(input())
    maxim = 0
    cnt = 0

    for i in range(n):
        x = int(input())
        if is_prime(x) and maxim < x:
            maxim = x
            cnt = 1  # resetezi contorul cand se schimba maximul
        elif x == maxim:
            cnt += 1
    print(cnt)


# if __name__ == '__main__':
#     main()

43


def main():
    n = int(input())
    maxim = 0
    maxim2 = 0
    cnt = 0
    suma = 0
    for i in range(n):
        x = int(input())
        if x > maxim:
            maxim2 = maxim
            maxim = x
        elif x > maxim2:
            maxim2 = x

    suma = maxim + maxim2
    print(suma)


# if __name__ == '__main__':
#     main()

# 44
def main():
    n = int(input())
    cnt = 0
    for i in range(n):
        x = int(input())
        if is_prime(x):
            cnt += numara_cifre(x)

    print(cnt)


# if __name__ == '__main__':
#     main()

# 20, 26, 39
# 20
def main():
    n = int(input())
    i = n
    cnt = 0
    for i in range(n - 1, 0, -1):
        if is_prime(i):
            print(i)
            cnt += 1
            if cnt > 1:
                break


# if __name__ == '__main__':
#     main()

# 26

def main():
    n = int(input())
    last_Digit = 0
    first_Digit = 0
    x = 0
    num = 0

    last_Digit = n % 10
    x = invers_nr(n)
    first_Digit = x % 10
    num = first_Digit * 10 + last_Digit
    if num % 2 == 1:
        multiplu = num * 2
    multiplu = num
    print(multiplu)


# if __name__ == '__main__':
#     main()

# 39

def main():
    n = int(input())
    cnt = 0

    i = 1
    while cnt < n:
        if is_prime(i):
            print(i)
            cnt += 1
        i += 1


# if __name__ == '__main__':
#     main()


# 45

# o functie care verifica daca doua numere intregi au
#  unicul divizor comun 1
def divizor_unic(a, b):
    # divizorii lui a se afla in intervalul [1,a]
    # 1 il va divide oricum si pe a si pe b.
    # deci ramane de verificat doar daca
    #       a si b au divizori comuni in [2,a] (diferiti de 1)
    for i in range(2, a + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True


def main():
    n = int(input())

    for a in range(1, n + 1):
        for b in range(a, n + 1):
            if divizor_unic(a, b) == True:
                print(a, b)
            # if math.gcd(a, b) == 1:  # gcd=greatest common divider
            #     print(a, b)


# if __name__ == '__main__':
#     main()

# 46


def main():
    n = int(input())
    # num = n
    # while num > 9:
    #     c1 = num //10 % 10
    #     c2 = num % 10
    #     if c1 < c2:
    #         nu_sunt_descrescatoare = True
    #     if c1 > c2:
    #         nu_sunt_crescatoare = True
    # if nu_sunt_descrescatoare and nu_sunt_crescatoare:
    #     print('Nu este bine ordonat numarul')
    # else:
    #     print('Bine ordonat')

    num = n
    # sunt crescatoare?
    while num > 9:
        c1 = num // 10 % 10
        c2 = num % 10
        if c1 > c2:
            break
        num //= 10
    if num <= 9:  # adica nu au fost parcurse toate cifrele
        print("Sunt crescatoare, deci bine ordonate")
        return
    # sunt descrescatoare?gv
    num = n
    c1 = num // 10 % 10
    c2 = num % 10
    while num > 9 and c1 >= c2:
        c1 = num // 10 % 10
        c2 = num % 10
        num //= 10
    if num <= 9:  # adica nu au fost parcurse toate cifrele
        print("Sunt descrescatoare, deci bine ordonate")
        return

    print('Nu sunt bine ordonate')


# 48

# 47, 49, 50, 51, 52, 53
#
def main():
    n = int(input())

    for i in range(2, n + 1):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            print(i, cnt)


# if __name__ == '__main__':
#     main()
# 49
def main():
    n = int(input())
    a = 1

    b = 10
    for i in range(2, n + 1):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            if i > a and i < b:
                print(i, cnt)


# if __name__ == '__main__':
#     main()
# 50
'''
4
2
6
4
8
3
22
5
10

'''


def main():
    n = int(input())
    x = 0
    max = 0

    for i in range(n):
        a = int(input())
        b = int(input())

        x = b - a
        if x > max:
            a1 = a
            b1 = b
            max = x
    print(a1, b1)


# if __name__ == '__main__':
#     main()
# 52
def main():
    n = int(input())

    # afisam primele n perechi de numere impare consecutive:
    cnt = 0  # nr. de perechi afisate
    a = 3  # a si a+2 vor forma o pereche
    while n > cnt:
        if is_prime(a) and is_prime(a + 2):
            print(a, a + 2)
            cnt += 1

        a += 2


# if __name__ == '__main__':
#     main()
# 55
def main():
    n = int(input())

    # for i in range(n):
    #     # afisam prima linie
    #     for j in range(i*n + 1, (i+1)*n + 1):
    #         print(j, end=' ')
    #     # final de linie:
    #     print()

    num = 1
    for i in range(n):
        # afisam prima linie
        for j in range(n):
            print(num, end=' ')
            num += 1
            # cresc cu 1 la fiecare pas, si deoarece la inceput num era 1,
            #  crestesi creste cu 1, parcurge valorile de la 1,2,3,4,5..,16
            # si devine 17 in final, dar valoarea 17 nu mai este afisata

            # deci va afisa doar valorile necesare.

        # final de linie:
        print()


# if __name__ == '__main__':
#     main()

# 60

# refolosim partea cu while n > cnt (de la problema cu perechi)
# dar adaugam o functie cifra_control(num) pe care o folosim in conditie
def suma_cifrelor(num):
    """
    Calculeaza suma cifrelor lui num
    :param num:
    :return:
    """
    # pass
    suma = 0
    while num > 0:
        last_digit = num % 10
        suma += last_digit
        num //= 10
    return suma


def cifra_control(num):
    # cat timp suma cifrelor ale lui num este mai mare decat 9 (adica nu e cifra)
    # calculam din nou suma cifrelor, dar nu a lui num, ci a sumei cifrelor lui num
    x = num
    while x > 9:
        x = suma_cifrelor(x)
    return x


def main():
    n = int(input())
    x = int(input())

    # afisam primele n perechi de numere impare consecutive:
    cnt = 0  # nr. de perechi afisate
    a = 0  # a si a+2 vor forma o pereche
    while n > cnt:
        if cifra_control(a) == x:
            print(a)
            cnt += 1

        a += 1


# if __name__ == '__main__':
#     main()

# 56

def gaseste_cifre(digit, num):
    lastDigit = 0
    while num != 0:
        lastDigit = num % 10
        num //= 10
        if digit == lastDigit:
            return True
    return False


def main():
    a = int(input())
    b = int(input())

    # cum poti sa eviti repetarea cifrelor?
    # Poti fie sa iei ceva in ordine fie sa elimini dupa duplicatele (a doua merge doar cu liste)
    for digit in range(10):  # for each possible digit
        if gaseste_cifre(digit, a) and gaseste_cifre(digit, b):
            print(digit, end=' ')

    # lastDigit = 0
    # shared_digits = []
    # while a != 0 :
    #     lastDigit = a % 10
    #     a //= 10
    #     if gaseste_cifre(lastDigit, b):
    #         shared_digits.append(lastDigit)
    # shared_digits.sort()
    # print(shared_digits[0])
    # for i in range(len(shared_digits)-1):
    #     if shared_digits[i] != shared_digits[i+1]:
    #         print(shared_digits[i+1])

    '''
12323234
657284

    '''


# if __name__ == '__main__':
#     main()

# 57
def contains_digits(digits, n):
    # parcurge cifrele lui n si cautam grupul de 2 cifre:
    while n != 0:
        lastDigits = n % 100
        n //= 10
        if lastDigits == digits:
            return True
    return False


'''
2
4
2342
430
8248
15264
24245
0

'''


def main():
    a = int(input())
    b = int(input())

    needle = a * 10 + b
    cnt = 0

    x = int(input())
    while x != 0:

        if contains_digits(needle, x):
            cnt += 1

        x = int(input())

    print(cnt)


# if __name__ == '__main__':
#     main()

# 58
def main():
    x = int(input())

    max = 0

    p10 = 10  # partile numarului vor fi x % p10 si x // p10

    while p10 < x:
        print(x % p10, x // p10)
        part1 = x % p10
        part2 = x // p10
        if part1 * part2 > max:
            max = part1 * part2
            maxpart1 = part1
            maxpart2 = part2

        p10 *= 10
    print(f'{maxpart1}*{maxpart2}={max}')

# if __name__ == '__main__':
#     main()
# Natural Language Processing (AI)
#  application for education

# 56, 57, 58 sunt toate cu cifrele unui numar.
