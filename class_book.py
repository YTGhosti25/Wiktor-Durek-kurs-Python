class Book:
    def __init__(self):
        self.title="title"
        self.author="autor"
        self.isbn=0
        self.available=False
    def __str__(self):
        return f"Title: {self.title}, Autor: {self.author}, ISBN: {self.isbn}, Available: {self.available}"
    def new_book(self,title, author, isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.available=True
    def borrow(self):
        self.available=False
    def return_book(self):
        self.available=True
    def is_avaiable(self):
        print(self.available)

class Person:
    def __init__(self,name,surname,id_number):
        self.name=name
        self.surname=surname
        self.id_number=id_number

    def new_person (self,name,surname,id_number):
        self.name=name
        self.surname=surname
        self.id_number=id_number
    def get_info(self):
        print("Nazywam się ",self.name, self.surname,", mój numer id to: ",self.id_number)

class Reader(Person):
    def __init__(self,name,surname,id_number):
        super().__init__(name,surname,id_number)
        self.borrowed_books=[Book]
    def borrowed_books (self):
        print(self.borrowed_books)
    def borrow_book(self, book: Book):
        if Book.is_avaiable:
            Book.is_avaiable=False
            self.borrowed_books.append(Book)
        else:
            print("Książka niedostępna")
    def return_book(self,book: Book):
        if Book in self.borrowed_books:
            Book.return_book
            self.borrowed_books.remove(Book)
        else:
            print("Nie wyporzyczyłeś takiej książki")

class Librarian(Person):
    def check_availability(book: Book):
        if Book:
            print("Książka pod tytułem ", book.title, " jest dostępna")
        else:
            print("Książka pod tytułem ", book.title, " nie jest dostępna")



ksiazka = Book()

ksiazka.new_book("Hobbit","J.R.R Tolkien",1)
print(ksiazka)
human1=Reader("Wojtek","Kozioł",1)
liblarian=Librarian("Bartek","Kowalczyk",11)
human1.get_info()

liblarian.check_availability(ksiazka)
human1.borrow_book(ksiazka)
print(human1.borrowed_books)
liblarian.check_availability(ksiazka)

human1.return_book(ksiazka)
print(human1.borrowed_books)
