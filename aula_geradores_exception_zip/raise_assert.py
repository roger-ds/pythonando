def soma(n1, n2):
    if n1 < n2 or n2 < 0:
        raise ValueError("n1 e n2 não podem ser negativos")
    assert n1 > 2, "Deu merda!"
    return 1 + 1

print(soma(2, 2))
