def safe_divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "nie mozna dzielic przez zero"

def parse_int(value):
    try:
        return int(value)
    except ValueError:
        return "wartosc nie jest liczba calkowita"
    
def parse_number(value):
    try:
        return int(value)
    except ValueError:
        return "wartosc nie jest liczba calkowita"
    except TypeError:
        return "nieprawidlowy typ danych"

# wlasne wyjątki
class MyCustomError(Exception):
    def __init__(self,message):
        self.message=message
        super().__init__(message)

try:
    raise MyCustomError("wystąpił błąd w aplikacji")
except MyCustomError as e:
    print(f"Błąd: {e}")
finally:
    print("hejo")

class AplicationError(Exception):
    #ogólny wyjątek aplikacji
    pass
class ValidationError(AplicationError):
    #wyjątek dotyczy walidacji danych
    pass
class DataBaseError(AplicationError):
    #wyjątek dotyczy bazy danych
    pass
try:
    raise ValidationError("nieprawidłowe dane")
except DataBaseError:
    print("błąd bazy danycy")
except AplicationError:
    print("ogólny błąd aplikacji")
except ValidationError:
    print("błąd obliczeń")
finally:
    print("ten blok wykonuje się zawsze")
