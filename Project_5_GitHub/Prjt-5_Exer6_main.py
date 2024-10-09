import statistics


def calculate_average(list_number: list):
    """
    Retourne la moyenne d'une liste de nombres

    :param list_number: La liste de nombres
    :return: Moyenne
    """

    count = 0
    for nbr in list_number:
        count += float(nbr)

    count_nbr = len(list_number)

    return float(count / count_nbr)

    # return statistics.mean(list_number)


if __name__ == '__main__':

    numbers = [10, 20, 30, 40, 50]
    average = calculate_average(numbers)

    print(f" Moyenne => {average:.2f}")
