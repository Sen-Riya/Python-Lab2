# (4) Create a Python program to efficiently manage and handle a library's collection of books.
# Each book in the library is represented with the following attributes: title, author, publisher,volume, year of publication, and ISBN (International Standard Book Number).
# Design and implement a module named LibraryManager.py that includes functions to manage books in the library. Collect data for 25 recently published books on topics such as OperatingSystems, Data Structures, and Machine Learning using Python, published between 2020 and 2024. Store this information in a dictionary where the key is the ISBN, and the value is another dictionary containing the book details.
# Within the LibraryManager.py module, create functions to:
# • Add a book to the library.
# • Remove a book from the library by its ISBN.
# • Retrieve and display the details of a book using its ISBN.
# • Search for books by title or author.
# • List all books currently in the library.
# • Update the details of an existing book.
# • Check if a book is available in the library by its ISBN.
# Demonstrate the functionality of your module by adding a few sample books, removing a book,retrieving the details of a book, searching for books, listing all books, updating book details,and checking the availability of a book.

class LibraryManager:
    def __init__(self):
        self.books = {}

    def add_book(self, isbn, title, author, publisher, volume, year):
        if isbn in self.books:
            print(f"Book with ISBN {isbn} already exists.")
            return
        self.books[isbn] = {
            'title': title,
            'author': author,
            'publisher': publisher,
            'volume': volume,
            'year': year
        }
        print(f"Book '{title}' added successfully.")

    def remove_book(self, isbn):
        if isbn not in self.books:
            print(f"No book found with ISBN {isbn}.")
            return
        removed_book = self.books.pop(isbn)
        print(f"Book '{removed_book['title']}' removed successfully.")

    def retrieve_book(self, isbn):
        return self.books.get(isbn, "No book found with this ISBN.")

    def search_books(self, keyword):
        results = []
        for isbn, details in self.books.items():
            if keyword.lower() in details['title'].lower() or keyword.lower() in details['author'].lower():
                results.append((isbn, details))
        return results

    def list_books(self):
        return self.books

    def update_book(self, isbn, title=None, author=None, publisher=None, volume=None, year=None):
        if isbn not in self.books:
            print(f"No book found with ISBN {isbn}.")
            return
        if title:
            self.books[isbn]['title'] = title
        if author:
            self.books[isbn]['author'] = author
        if publisher:
            self.books[isbn]['publisher'] = publisher
        if volume:
            self.books[isbn]['volume'] = volume
        if year:
            self.books[isbn]['year'] = year
        print(f"Book with ISBN {isbn} updated successfully.")

    def check_availability(self, isbn):
        return isbn in self.books


# Demonstration
if __name__ == "__main__":
    library = LibraryManager()


    library.add_book("9700010346789", "Operating Systems", "A", "X", 1, 2022)
    library.add_book("9456887678907", "Data Structure and Interpretation ", "B", "Y", 2, 2021)
    library.add_book("9781617295980", "Machine Learning", "C", "Z", 3, 2023)


    library.remove_book("9456887678907")


    book_details = library.retrieve_book("9781617295980")
    print("Retrieved Book Details:", book_details)


    search_results = library.search_books("Machine Learning")
    print("Search Results:", search_results)


    all_books = library.list_books()
    print("All Books:", all_books)

    library.update_book("9781617295980", title="Machine Learning with Python, Updated Edition")

    
    availability = library.check_availability("9781617295980")
    print("Availability:", availability)
