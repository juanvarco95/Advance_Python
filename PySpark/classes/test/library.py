class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
class Library:
    def __init__(self, name: str) -> None:
        self.name = name
        self.books = []

    def add_book(self, book: str) -> None:
        self.books.append(book)
    
    def display_books(self) -> None:
        print(f'Books in {self.name} Library:')
        for book in self.books:
            print(book)


