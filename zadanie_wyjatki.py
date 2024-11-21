def divide(a,b):
    try:
        if a == 0 or b== 0:
            raise ZeroDivisionError
        elif not(isinstance(a,int)) or not(isinstance(b,int)):
            raise ValueError
        else:
            return a/b
    except ZeroDivisionError:
        return "nie mozna dzielic przez zero"
    except ValueError:
        return "nieprawidłowa liczba"
    except Exception:
        return "ogólny błąd"
    finally:
        print("Przetwarzanie zakończone")

print(divide(4,'a'))

def list_to_int(list):
    try:

        return int(list)
    except ValueError:
        return "nie da się przekonwertować listy"
    except ValueError:
        return "pusta lista"
    finally:
        "przetwarzanie zakończone"
