from pympler.asizeof import asizesof


def dobro(lista):
    lista_dobro = []
    for item in lista:
        lista_dobro.append(item * 2)

    return lista_dobro


x = dobro(range(50))
print(x, asizesof(x))


def dobro_generator(lista):
    for item in lista:
        yield item * 2

y = dobro_generator(range(50))

for _ in range(50):
    print(y, next(y), asizesof(y))


# for a in y:
#     print(a)