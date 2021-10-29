""" Multiline comment :))
.. doar ca nu sunt.. este doar un truc ca
    astea sunt siruri de caractere pe mai multe linii
Desi variabilele nu au tip la declaratie/ folosire,
    Si nu le putem spune sa fie numai de un anume tip,
    Putem sa le dam hint-uri (typehints)
"""



def is_prime(n: int) -> bool:  # o functie a caruit parametru are typehintul int, si returneaza un bool
    # return 2  # ne spune ca 2 nu este de tipul asteptat
    if n < 2:
        return False

    for div in range(2, n):
        if n % div == 0:
            return False
    return True

pi = 3.14

# Pentru codul din fisier care este specific doar lui (adica la importare nu vrem sa fie rulat)
#  adaugam un if:
if __name__ == '__main__':

    s: str
    # cand pui typehint-ul, editorul iti va recomanda mereu functiile
    s = 'abc'
    print(s)
    s = """
    Ana are mere
    Tu nu ai
    """
    print(s)

    s = 2  # TODO editorul ne atentioneaza ca i-am recomandat=hintuit
    #           alt tip pt aceasta variabila
    print(s)