class Book:
  def __init__(self,title, author, isbn):
      self.title=title
      self.author=author
      self.isbn=int(isbn)
      self.available=True
  def __str__(self):
      return f"Tytuł: {self.title}, Autor: {self.author}, ISBN: {self.isbn}, Dostępność: {self.available}"
  def book_info(self):
      print(f"Tytuł: {self.title}, Autor: {self.author}, ISBN: {self.isbn}, Dostępność: {self.available}")
  def new_book(self,title, author, isbn):
      self.title=title
      self.author=author
      self.isbn=int(isbn)
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
      self.id_number=int(id_number)
  def new_person (self,name,surname,id_number):
      self.name=name
      self.surname=surname
      self.id_number=id_number
  def get_info(self):
      print("Nazywam się",self.name, self.surname,"mój numer id to:",self.id_number)

class Reader(Person):
  def __init__(self,name,surname,id_number):
      super().__init__(name,surname,id_number)
      self.borrowed_books={}
  def borrow_book(self, book: Book):
      if book.available:
          book .borrow()
          self.borrowed_books[book.isbn]=("Książka: "+book.title+", Autor: "+book.author)
      else:
          print("Książka niedostępna")
  def return_book(self,book: Book):
      if book.isbn in self.borrowed_books:
          book.return_book()
          del self.borrowed_books[book.isbn]
      else:
          print("Nie wyporzyczyłeś takiej książki")

class Librarian(Person):
  def check_availability(self, book: Book):
      if book.available:
          print("Książka pod tytułem", book.title, "jest dostępna")
      else:
          print("Książka pod tytułem", book.title, "nie jest dostępna")

def main():
    # wstępne dane by przyspieszyć testowanie 
    ksiazka={}
    ksiazka[1]=Book("Hobbit","J.R.R Tolkien",1)
    ksiazka[2]=Book("Meow","Tony the cat",2)
    humans={}
    humans[1]=Reader("Wojtek","Kozioł",1)
    humans[2]=Reader("Antek","Wilk",2)
    humans[11]=Librarian("Bartek","Kowalczyk",11)

    while True:
        choice=int(input("\nwybierz opcję, 1=nowy człowiek, 2=informacje o człowieku, \n3=nowa książka, 4=informacje o książce, \n5=spytaj bibliotekarza o książkę, \n6=wyporzycz książkę, 7=zwróć książkę, 8=koniec\n"))
        print("\n")
        
        if choice == 1:
            choice=int(input("wybierz funkcje, 1=czytelnik, 2=bibliotekarz: "))
            if choice == 1:
                name=input("Imię: ")
                surname=input("Nazwisko: ")
                id_number=int(input("Numer identyfikacyjny: "))
                if id_number not in humans:
                    humans[id_number]=Reader(name,surname,id_number)
                    print("Stworzono")
                else:
                    print("Już istneije człowiek z takim id!")
            else:
                name=input("Imię:")
                surname=input("Nazwisko:")
                id_number=int(input("Numer identyfikacyjny:"))
                if id_number not in humans:
                    humans[id_number]=Librarian(name,surname,id_number)
                    print("Stworzono")
                else:
                    print("Już istneije człowiek z takim id!")

        elif choice ==2:
            id_number=int(input("Podaj id osoby której informacje chcesz sprawdzić: "))
            if id_number in humans:
                humans[id_number].get_info()
                if isinstance(humans[id_number],Reader):
                    print(humans[id_number].borrowed_books)
            else:
                print("Nie ma takiego człowieka z takim id!")
        
        elif choice == 3:
            title=input("Tytuł: ")
            author=input("Autor: ")
            isbn=int(input("Isbn: "))
            if isbn not in ksiazka:
                ksiazka[isbn]=Book(title,author,isbn)
            else:
                print("Książka z podanym isbn już istnieje!")

        elif choice == 4:
            isbn=int(input("Podaj isbn książki którą chcesz sprawdzić: "))
            if isbn in ksiazka:
                ksiazka[isbn].book_info()
            else:
                print("nie ma takiej książki!")

        elif choice == 5:
            id_number=int(input("Podaj id bibliotekarza którego chcesz się spytać o książkę: "))
            if id_number in humans:
                if isinstance(humans[id_number],Librarian):
                    isbn=int(input("Podaj isbn książki do sprawdzenia: "))
                    if isbn in ksiazka:
                        humans[id_number].check_availability(ksiazka[isbn])
                    else:
                        print("Nie ma takiej książki!")
                else:
                    print("Podany człowiek nie jest bibliotekarzem!")
            else:
                print("Nie ma takeigo człowieka")

        elif choice == 6:
            id_number=int(input("Podaj id czytelnika który chce wyporzyczyć książkę: "))
            if id_number in humans:
                if isinstance(humans[id_number],Reader):
                    isbn=int(input("Podaj isbn książki którą chcesz wyporzyczyć: "))
                    if isbn in ksiazka:
                        humans[id_number].borrow_book(ksiazka[isbn])
                    else:
                        print("Nie ma takiej książki!")
                else:
                    print("Podany człowiek nie jest czytelnikiem")
            else:
                print("Nie ma takeigo człowieka")

        elif choice == 7:
            id_number=int(input("Podaj id czytelnika który chce zwrócić książkę: "))
            if id_number in humans:
                if isinstance(humans[id_number],Reader):
                    isbn=int(input("Podaj isbn książki którą chcesz zwrócić: "))
                    if isbn in ksiazka:
                        humans[id_number].return_book(ksiazka[isbn])
                    else:
                        print("Nie ma takiej książki!")
                else:
                    print("Podany człowiek nie jest czytelnikiem")
            else:
                print("Nie ma takeigo człowieka")

        elif choice == 8:
            break



main()
