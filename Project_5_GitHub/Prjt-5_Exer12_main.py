class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_title):
        self.books = [book for book in self.books if book.title != book_title]
        return f"'{book_title}' a été supprimé de la bibliothèque"

    def borrow_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                self.borrowed_books.append(book)
                return f"Vous avez emprunté '{book_title}'"

        return f"Le livre '{book_title}' n'est pas disponible"

    def return_book(self, book_title):
        for book in self.borrowed_books:
            if book.title == book_title:
                self.borrowed_books.remove(book)
                self.books.append(book)
                return f"Vous avez rendu '{book_title}'"
        return f"Le livre '{book_title}' n'a pas été emprunté"

    def available_books(self):
        return [book.title for book in self.books]

    def borrowed_books_list(self):
        return [book.title for book in self.borrowed_books]


if __name__ == '__main__':

    library = Library()

    # Ajouter un livre
    library.add_book(Book("Independance Day", "Will smith", 1998))
    library.add_book(Book("Les Aventures de Jack Burton dans les griffes du Mandarin",
                          "John Carpenter", 1986))
    library.add_book(Book("Columbo", "Peter Falk", 1982))
    library.add_book(Book("Avenger", "Joss Whedon", 2012))

    # Emprunter un livre
    print(library.borrow_book("Les Aventures de Jack Burton dans les griffes du Mandarin"))

    # Afficher les livres disponibles
    print("Livres disponibles:", library.available_books())

    # Afficher les livres empruntés
    print("Livres empruntés:", library.borrowed_books_list())

    # Rendre un livre
    print(library.return_book("Les Aventures de Jack Burton dans les griffes du Mandarin"))

    # Supprimer un livre
    print(library.remove_book("Avenger"))

    # Afficher les livres disponibles après retour
    print("Livres disponibles après retour:", library.available_books())
