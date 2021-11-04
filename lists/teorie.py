'''
teorie despre liste, adica cum sunt folosite metodele, etc
'''

l = []

l.append(3)
print(l)
l.extend([2,3,4])
print(l)

# inserare pe o anumita pozitie:
l = ['a', 'b', 3, 100]
l.insert(1, 3.14)
print(l)

# preimplementate

# daca vrem sa stim de cate ori apare un element:
print(l.count(2), l.count(5))
# daca vrem sa eliminam elemente:
l.remove(3)  # TODO elimina doar prima aparitie
print(l)


# deconstructia listei in parametrii:
l = [1, 2, 3]
print(l)
print(*l, sep=' ') # este ca si cum ai scrie print(l[0], l[1], l[2]..) pt toate elementele din lista


