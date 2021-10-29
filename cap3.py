from math import floor


def read_int_list():
    # vom face o metoda de a citi o lista de intregi fara sa stim cate numere citim,
    #  dar le citim pe toate de pe acelasi rand
    rand = input()
    # print(rand)
    stringuri = rand.split()  # ne da o lista cu scrierea (str a) numerelor
    # print(stringuri)
    for i in range(len(stringuri)):
        stringuri[i] = int(stringuri[i])
    return stringuri


def read_float_list():
    # vom face o metoda de a citi o lista de intregi fara sa stim cate numere citim,
    #  dar le citim pe toate de pe acelasi rand
    rand = input()
    # print(rand)
    stringuri = rand.split()  # ne da o lista cu scrierea (str a) numerelor
    # print(stringuri)
    for i in range(len(stringuri)):
        stringuri[i] = float(stringuri[i])
    return stringuri


# def main():
#     print(read_int_list())

# 1
def main():
    note = read_int_list()
    n = len(note)

    cntFail = 0  # grades < 5

    # parcurgi lista:
    for i in range(n):
        if note[i] < 5:  # a)
            cntFail += 1


# if __name__ == '__main__':
#    main()

# 4
def main():
    v = read_float_list()
    n = len(v)

    for i in range(n):
        v[i] = round(v[i])

    for i in range(n - 1, -1, -1):
        print(v[i], end=" ")

    # for i in reversed(range(n))


# if __name__ == '__main__':
#     main()

# TODO tema:
#  1 b,c,d  2, 3, 5+ doar sa-ti gasesti timp
# 1/b
def main():
    note = read_int_list()
    n = len(note)
    mA = 0

    for i in range(n):
        if note[i] > 5:
            mA += note[i]
    print(mA)


# if __name__ == '__main__':
#     main()
# c

def main():
    note = read_int_list()
    n = len(note)
    cnt = 0

    for i in range(n):
        if note[i] == 7:
            cnt += 1
    print(cnt)


# if __name__ == '__main__':
#     main()

# d
def main():
    note = read_int_list()
    n = len(note)
    max = 0

    for i in range(n):
        if max < note[i]:
            max = note[i]
    print(max)


# if __name__ == '__main__':
#     main()

# 2
def main():
    numbers = read_int_list()
    n = len(numbers)
    max = 0
    cnt_max = 0

    for i in range(n):
        if max < numbers[i]:
            max = numbers[i]
        if max == numbers[i]:
            cnt_max += 1
    print(max, cnt_max)


# if __name__ == '__main__':
#     main()

# 3
def main():
    num = read_int_list()
    n = len(num)
    cnt = 0

    for i in range(n - 1):
        if num[i] % num[-1] == 0:
            cnt += 1
    print(cnt)


# if __name__ == '__main__':
#     main()

# 5
def main():
    numbers = read_int_list()
    n = len(numbers)
    suma = 0

    for i in range(n):
        if (i + 1) % 2 != 1 and numbers[i] % 2 == 0:  # i->0!!
            suma += i
    print(suma)


# if __name__ == '__main__':
#     main()

# 6
def main():
    numbers = read_int_list()
    n = len(numbers)
    num1 = 0
    num2 = 0
    suma = 0

    for i in range(n):
        num1 = num1 * 10 + numbers[i]
    print(num1)

    for i in reversed(range(n)):
        num2 = num2 * 10 + numbers[i]
    print(num2)
    print(num1 + num2)


# if __name__ == '__main__':
#     main()

# 7
def main():
    numbers = read_int_list()
    n = len(numbers)

    for i in range(n):
        if numbers[i] == 0:
            numbers[i] += 3
    for i in range(n):
        print(numbers[i])


# if __name__ == '__main__':
#     main()

# 8
def main():
    nums = read_int_list()
    n = len(nums)

    for num in nums:  # iterate the "items"
        print(num, 0, end=" ")


# if __name__ == '__main__':
#     main()

# 9
def main():
    nums = read_float_list()
    n = len(nums)

    for i in range(n // 2 + 1):
        if floor(nums[i]) == floor(nums[-i - 1]):
            print(nums[i], nums[-i - 1])


# if __name__ == '__main__':
#     main()

# 11
def main():
    nums = read_int_list()
    n = len(nums)

    first = nums[0]
    # for i, num in enumerate(nums):  # orice for din Python decide de la inceput toti indicii pe care ii va parcurge
    #     if first == num:
    #         del nums[i]
    #     i-=1  # nu are vreun efect la pasul urmator
    # for i in reversed(range(n)):
    #     if first == nums[i]:
    #         del nums[i]
    #     i-=1
    i = 0
    while i < len(nums):
        if first == nums[i]:
            del nums[i]
            i -= 1  # ca sa nu sara peste elemente egale
        i += 1
    print(nums)


# if __name__ == '__main__':
#     main()

# 13 inserare

def main():
    # lista = []
    # lista.append(3)
    # lista += [4,5,6]

    lista = [5,3,4,5,10]
    # print(lista.count(5))
    # lista.remove(5)  # removes the first occurence of the value 5

    lista.insert(2, -100)  # adauga pe pozitia 2 elementul -100, iar toate elementele (icnepand cu pozitia 2) se muta mai la dreapta
    print(lista)


# if __name__ == '__main__':
#     main()

def main():
    nums = read_float_list()
    n = len(nums) # for(i = 0; i <
    i = 0
    while i < n:
        if nums[i] < 0:
            nums.insert(i,0)
            i += 1
            n += 1
        i += 1
    print(nums)
# if __name__ == '__main__':
#     main()

#19
def main():
    nums = read_int_list()
    n = len(nums)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if nums[i] > nums[j] and i < j :
                cnt += 1
                print(nums[i],nums[j])
    print(cnt)
# if __name__ == '__main__':
#      main()

#21
def main():
    nums = read_int_list()
    n = len(nums)

    # a,b = 2,3
    # a,b = b,a
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] % 2 == 0 and nums[j] % 2 == 0:
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
    print(nums)
# if __name__ == '__main__':
#     main()

# 24
def main():
    '''
2.3 12.09 218.98021 31.05 -212.098 12.75

    '''
    nums = read_float_list()
    n = len(nums)

    i = 0
    j = n-1
    while i < len(nums) // 2:

        print(round(floor(nums[i]) + nums[j]-floor(nums[j]), 3))

        i+=1
        j-=1

# if __name__ == '__main__':
#     main()

# TODO 10, 12, 14, 15, 16, 22 (poti citi sir de caractere direct cu input), 18
# E.g. 22
def main():
    '''
ACBEzlE
    '''
    s = input()
    for i in range(len(s)):
        print(s[i], f'Ascii={ord(s[i])}')  # ord('c') este codul ascii al lui 'c'
# if __name__ == '__main__':
#     main()

def main():
    '''
14 -13 21 1 120 1000 21
    :return:
    '''
    nums = read_int_list()
    n = len(nums)
    min = 0
    max = 0
    i_min = -1 # initializezi cu o pozitie care nu exista
    i_max = -1

    for i in range(n):
        if nums[i] < min:
            min = nums[i]
            i_min = i
        if nums[i] > max:
            max = nums[i]
            i_max = i

    # slices
    # sortam elementele de la i_min pana la i_max
    #  face o lista cu ele sortate si le atribuie pas cu pas in pozitiile din lista
    nums[i_min:i_max+1] = sorted(nums[i_min:i_max+1])


    print(nums, nums[2:4])

# if __name__ == '__main__':
#     main()

# TODO about list slices:
def main():
    # a = 2
    # b = 3
    # print(a,b)
    # a,b = 3, 10
    # print(a,b)

    l = [1,2,3]

    l[0] = 4
    print(l)
    l[:] = 2,3,4
    print(l)

    l[:2] = 'a', 'b'
    print(l)
    l[2:] = 'C'
    print(l)

    l = [1,2,3,'a', 'b', 'c']
    print(l[1:5])


# if __name__ == '__main__':
#     main()

