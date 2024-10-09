class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"Nom: {self.name} \nAge: {self.age}")


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display_details(self):
        super().display_details()
        print(f"Salaire: {self.salary}")


if __name__ == '__main__':

    person = Person("Elohim", 18).display_details()
    employee = Employee("Angel's", 23, 2500).display_details()

    """
    person.display_details()
    employee.display_details()
    """
