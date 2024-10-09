import statistics

students = {'Alice': {'Mathématiques': 90, 'Francais': 80, 'Histoire': 95},
            'Bob': {'Mathématiques': 75, 'Francais': 85, 'Histoire': 70},
            'Charlie': {'Mathématiques': 88, 'Francais': 92, 'Histoire': 78}
            }


class Search:

    def __init__(self, data: str | None = None, name: str | None = None) -> None:

        self.name = ""
        self.data = data

        if name:
            name = name.strip()
            self.name = name.lower()

        for key, value in data.items():

            key = key.lower()

            if self.name in key:

                moyen = [float(value['Mathématiques']), float(value['Francais']), float(value['Histoire'])]

                print(f" Notes de {name} :  \n\n"
                      f" Mathématiques => {value['Mathématiques']}\n"
                      f" Francais => {value['Francais']}\n"
                      f" Histoire => {value['Histoire']}\n\n"
                      f" Moyenne => {statistics.mean(moyen):.2f}\n")
                break
        else:
            print(f"L'étudiant {name} n'existe pas dans la liste.")


if __name__ == '__main__':

    username = input("Entrez le nom de l’étudiant : ")
    Search(students, username)
