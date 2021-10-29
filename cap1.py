# Incepi sa refaci cele 30 exercitii din primul capitol
#  dar in Python

# spaced learning :) sa-ti insusesti asta (putem dupa ce avem toate informatiile sa le invatam, si dupa doar le repetam in mijlocul vacantei)
#   si le pastram si in memoria de lunga durata


# # TODO putem importa functii si variabile din alte fisiere
# from functions import pi, is_prime
# # la import, executa totul din fisier
#
# print(is_prime(101))

# # 8
# # TODO   type "main" and press Tab to autocomplete the beginning of our program
# if __name__ == '__main__':
#     # # citim de la tastatura trei intregi
#     # a = int(input('a='))  # input citeste un rand de la tastatura ca string, iar int extrage un intreg din acel string
#     # b = input('b=')
#     # b = int(b)
#
#     a = float(input('a = '))
#     b = float(input('b = '))
#     c = float(input('c = '))
#     # print(sum([1, 2, 3]))  # TODO as to not shadow sum(), we'll find some other name
#     suma = 0
#
#     if a > 0:
#         suma += a
#     if b > 0:
#         suma += b
#     if c > 0:
#         suma += c
#
#     print(suma)
#
#     #
#     # print(a, b, c)  # cout << a << ' ' << b <<" "<<c<< endl;


# 13
# ca input ai catetele si calculezi ipotenuza
# vezi sa folosesti main
# ca bonus sa rezolvi si 11

# 11
# if __name__ == '__main__':
#
#     a = 5
#     b = 6
#     c = 9
#
#     suma = a + b + c
#     print(round(suma/3))

# # 13
# from math import sqrt
#
# if __name__ == '__main__':
#     cat1 = 6
#     cat2 = 6
#
#     # cat1 ** 2 is cat1 to the power of 2
#
#    ip = sqrt( cat1 ** 2 + cat2 * cat2 )
#     print(ip)
#

# Tema 1-20
#1
# if __name__ == '__main__':
#
#     x = int(input("x = "))
#     y = int(input("y = "))
#
#     A = 2 + x + y
#     B = x * A - 2 + y
#     C = A - 2 * B + x
#     print(A, B, C)

#2
# from math import sqrt
# if __name__ == '__main__':
#     a = 3
#     b = 5
#     c = 4
#
#     perimeter = a + b + c
#     semiperimeter = perimeter / 2
#     area =sqrt(semiperimeter*(semiperimeter - a) * (semiperimeter - b) * (semiperimeter - c))
#     print(perimeter, semiperimeter, area)

#3

#4

#5
# n = 200
# crestereaI = n * 50/100
# result = n + crestereaI
#
# print(crestereaI, result)

#6
# x = int(input(" x = "))
# interest = x * 0.3
# after3months =  x  + 3 * interest
# print( after3months )

#7
# x = int(input(" x = "))
# firstmonth = x + ( x * 0.3 )
# secondmonth = firstmonth + ( firstmonth * 0.3 )
# thirdmonth = secondmonth + (secondmonth * 0.3 )
#
# print ( firstmonth, secondmonth , thirdmonth )

#8
# if __name__ == '__main__':
#
# x = float(input(" x = "))
# y = float(input(" y = "))
# z = float(input(" z = "))
#
# suma = 0
#
# if x > 0:
#     suma += x
# if z > 0:
#     suma += z
# if y > 0:
#     suma += y
#
# print( suma ) # what's wrong?

#9
# #10
# from math import sqrt
#
# a = int(input( " a = "))
# b = int(input( " b = "))
# c = int(input( " c = "))
#
# if a * a + b * b == c * c:
#     print ( "Sunt pitagorice. ")
# else :
#     print( " Nu sunt pitagorice")

#11

# a = int(input(" a = "))
# b = int(input(" b = "))
# c = int(input(" c = "))

# suma = a + b + c

# print( suma / 3)

#12
# a = int(input(" a = "))
# b = int(input(" b = "))
# c = int(input(" c = "))
# t = int(input(" t = "))
#
# med = (a + b + c) / 3
# medsem = (3 * med) / 4
#
# print( medsem)

#13
# cat1 = int(input(" cat1 = "))
# cat2 = int(input(" cat2 = "))
# ip = 0
#
# ip = cat1 * cat1 + cat2 * cat2
#
# print(ip)

# #14
# # l = int(input(" l = "))
# # perimeter = l * 4
# # area = l * l
# # print( perimeter , area )
#
# # 15
# salariul = int(input(" salariul = "))
# procentul = int(input(" procentul = "))
#
# result = (procentul / 100) * salariul
#
# print(result)

# #16
# baniiLuiIonel = int(input(" baniiLuiIonel = "))
# cadou1 = int(input(" cadou1 = "))
# cadou2 = int(input( " cadou2 = "))
# cadou3 = int(input(" cadour = "))
# result = 0
#
# result = baniiLuiIonel - ( cadou1 + cadou2 + cadou3)
# print(result)

# # 17
# p = int(input(" p = "))
# first = p
# second = first * 2
# third = second * 2
# fourth = third * 2
# fifth = fourth * 2
# suma = first + second + third + fourth + fifth
# print(suma, '(', first, '+', second, '+', third, '+',
#       fourth, '+', fifth, ')')
# print(f'{suma} ({first}+{second}+{third}+{fourth}+{fifth})')

# #18
# n = int(input(" n = "))
# first = 0
# second = 0
# sum = 0
# if n > 100:
#     first = n % 10
#     # TODO marea diferenta: / da cu virgula mereu,
#     #   iar // este folosit pentru catul impartirii
#     second = (n // 10) % 10
#     sum = first + second
#     print( first, second, sum)

# #21
# a = float(input(" a = "))
# b = float(input(" b = "))
# c = float(input(" c = "))
# sum = 0
# if a > 0:
#     sum += a
# if b > 0:
#     sum += a
# if c > 0:
#     sum += c
#
# print( sum )

# # 24
#
# n = int(input(" n = "))
#
# units = n % 10
# tens = ( n // 10 ) % 10
#
# if n % 2 == 1:
#     print( units + tens)
# if n % 2 == 0:
#     print ('Numar par')

# # 30
# a = float(input(" a ="))
# b = float(input(" b = "))
# c = float(input(" c = "))
# d = float(input(" d = "))
# e = float(input(" e = "))
# # contor
#
# majoritateaNegative = 0
# majoritateaPozive = 0
# if a > 0:
#     majoritateaPozive += 1
# if b > 0:
#     majoritateaPozive += 1
# if c > 0:
#     majoritateaPozive += 1
# if d > 0:
#     majoritateaPozive += 1
# if e > 0:
#     majoritateaPozive += 1
#
# if majoritateaPozive >= 3:
#     print('Majoritatea sunt pozitive')
# else:
#     print(" Majoritatea negative ")

# 19 20 22 23 25 26 27 28 29