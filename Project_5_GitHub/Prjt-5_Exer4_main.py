import subprocess
import webbrowser
import os


class MyClass:

    def __init__(self, full_name):
        self.full_name = full_name

    def display_name(self):
        print("Le nom complet est : ", self.full_name)


class OtherClass:

    def __init__(self, first_name, name):
        self.first_name = first_name
        self.name = name

    def display_name(self):
        print(f"Nom complet : {self.first_name} {self.name}")


def debug():

    try:
        subprocess.run(["flake8", "--format=html", "--htmldir=flake8_rapport"])

        try:
            chemin = os.getcwd()
            fichier_html = f"{chemin}/flake8_rapport/index.html"
            webbrowser.open(fichier_html)

        except ValueError as er:
            print("Erreur lors de l'ouverture du fichier :", er)

    except subprocess.CalledProcessError as e:
        print(f"Erreur : {e}")


if __name__ == '__main__':
    debug()
