def square(value):
    """
    Calculer le carré d'un nombre

    :param value: Le nombre à calculer
    :return: Le carré du nombre recu
    """

    float_verify = number_float(value)
    int_verify = value.isdigit()

    if not int_verify and not float_verify:
        return print("Le paramètre doit être un nombre !")

    else:
        carre = float(value) ** 2
        return print(f"Le carré de {value} : {carre}")


def number_float(number):
    """
    Contrôle si un nombre est flottant

    :param number: Le nombre à vérifier
    :return: Vrai ou Faux
    """
    try:
        float(number)
        return True

    except ValueError:
        return False


if __name__ == '__main__':
    result = input('Mettre un nombre : ')
    square(result)
