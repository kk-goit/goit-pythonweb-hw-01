from abc import ABC, abstractmethod

class Book:
  def __init__(self, title, author, year):
    self.title = title
    self.author = author
    self.year = year

  def __str__(self):
    return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

  def __eq__(self, title: str):
    return self.title == title

class LibraryInterface(ABC):
  def __init__(self):
    self.books = []

  @abstractmethod
  def add_book(self, book: Book):
    pass

  @abstractmethod
  def remove_book(self, title: str):
    pass

  @abstractmethod
  def show_books(self):
    pass

class Library(LibraryInterface):
  def add_book(self, the_book: Book):
    self.books.append(the_book)

  def remove_book(self, title: str):
    for the_book in self.books:
      if the_book == title:
        self.books.remove(the_book)
        break

  def show_books(self):
    if len(self.books) == 0:
      print("Librariy is empty now")
      return

    for the_book in self.books:
      print(the_book)

class LibraryManager:
  def __init__(self, library: LibraryInterface):
    self.lib = library

  def add_book(self, title, author, year):
    self.lib.add_book(Book(title, author, year))

  def remove_book(self, title):
    self.lib.remove_book(title)

  def show_books(self):
    self.lib.show_books()


def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                print("Invalid command. Please try again.")

if __name__ == "__main__":
  main()
