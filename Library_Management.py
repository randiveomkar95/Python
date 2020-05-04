"""
    LIBRARY MANAGEMENT SYSTEM
"""
class Library:
    def __init__(self,listOfBooks):
        self.availableBooks = listOfBooks

    def displayAvailableBooks(self):
        print("Available Books Are the:")
        for book in self.availableBooks:
            print(book)

    def lendBook(self,requestedBook):
        if requestedBook in self.availableBooks:
            print("You have now borrowed the the book")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry the book is not available in our List")

    def addBook(self,returnedBook):
        self.availableBooks.append(returnedBook)
        print("You have returned the book Thank you")

class Customer:
    def requestBbook(self):
        print("Enter the name of book you would like to borrow")
        self.book = input()
        return self.book

    def returnBook(self):
        print("Enter the name of book which you are returning: ")
        self.book = input()
        return self.book

library = Library(['book1', 'book2', 'book3'])
customer = Customer()

while True:
    print("=========================================")
    print("Enter 1 to display the available books")
    print("Enter 2 to request for a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit")
    print("=========================================")

    userChoice = int(input())
    if userChoice == 1:
        library.displayAvailableBooks()
    elif userChoice == 2:
        requestedBook = customer.requestBbook()
        library.lendBook(requestedBook)
    elif userChoice == 3:
        returnedBook = customer.returnBook()
        library.addBook(returnedBook)
    elif userChoice == 4:
        quit()
