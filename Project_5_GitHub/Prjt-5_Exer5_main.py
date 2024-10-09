
def somme(a, b):
    """
    Calcule la somme de deux éléments.

    :param a: Premier élément, doit supporter l'opération d'addition.
    :param b: Deuxième élément, peut être de n'importe quel type compatible avec a.
    :return: La somme de a et b.
    """
    return a + b


def subtraction(a, b):
    """
    Calcule la différence entre deux éléments.

    :param a: Premier élément, doit supporter l'opération de soustraction.
    :param b: Deuxième élément, peut être de n'importe quel type compatible avec a.
    :return: La différence entre a et b.
    """
    return a - b


if __name__ == '__main__':

    add = somme(10, 25)
    print(add)

    sub = subtraction(25, 10)
    print(sub)
