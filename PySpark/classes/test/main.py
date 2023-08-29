from bank_account import SavingAccount
from library import Book, Library

if __name__ == '__main__':
    
    saving = SavingAccount('12345', 1000, 0.05)
    print(saving.get_balance())
    saving.apply_interest()
    print(saving.get_balance())

    book1 = Book("The Catcher in the Rye", "J.D. Salinger")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")

    library = Library("Central")
    library.add_book(book1)
    library.add_book(book2)

    library.display_books()