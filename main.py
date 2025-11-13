from library_books import library_books
from datetime import datetime, timedelta
import tkinter as tk

#Tkinter tutorial used: https://www.geeksforgeeks.org/python/python-gui-tkinter

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author

def view_books(library_books):
    for book in library_books:
        print(book["id"]+"."+book["title"]+"."+book["author"])


# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books

def search_books(library_books, search_term, search_type):
    #Search terms and info are all changed to lower case to not be case-sensitive
    matches = []
    search_term = search_term.lower()

    #Loops through database, checks for matches
    for book in library_books:
        if search_type == "author":
            if book["author"].lower() == search_term:
                matches.append(book)
        elif search_type == "genre":
            if book["genre"].lower() == search_term:
                matches.append(book)

    return matches

# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out

def checkout_book(library_books, ID):
    #Loops through database to find book, uses datetime
    for book in library_books:
        if book["id"] == ID:
            if book["available"]:
                book["available"] = False
                book["due_date"] = datetime.now() + timedelta(weeks=2)
                book["checkouts"] += 1
            else:
                print("Sorry, " + book["title"] + " is not available.")

# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out

def return_book(library_books, ID):
    for book in library_books:
        if book["id"] == ID:
            book["available"] = True
            book["due_date"] = None

def return_overdue_books(library_books):
    overdue_books = []

    for book in library_books:
        if not(book["available"]):
            time = datetime.strptime(book["due_date"], "%Y-%m-%d")
            if time < datetime.now():
                overdue_books.append(book)

    return overdue_books

# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.
class Book:
    def __init__(self, id, title, author, genre, available, due_date, checkouts):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
        self.due_date = due_date
        self.checkouts = checkouts

    def checkout(self):
        if self.available:
            self.available = False
            self.due_date = datetime.now() + timedelta(weeks=2)
            self.checkouts += 1
        else:
            print("Sorry, " + self.title + " is not available.")

    def return_book(self):
        self.available = True
        self.due_date = None

    def view_details(self):
        print(self.id+"."+self.title+"."+self.author)

def create_book_objects(library_books):
    book_list = []

    for book in library_books:
        #Dictionary Unpacker argument
        book = Book(**book)
        book_list.append(book)

    return book_list

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    # You can use this space to test your functions
    window = tk.Tk()



    while running:
        print("")