import data
from data import X
from data import R
from data import Z
from time import sleep
from data import select

class Learn():
    print(data.info)
    void = int(input("Select void: "))

    def Math():
        a = int(input("Enter A: "))
        b = int(input("Enter B: "))
        print(f"{Z}1 - Base \n2 - Relevant \n3 - Compare{X}")
        option = int(input(select))

        # Base
        if option == 1:
            print(f'''
+   {a + b}
-   {a - b}
*   {a * b}
/   {a / b}
**  {a ** b}
//  {a // b}
%   {a % b}''')
        # Relevant
        if option == 2:
            a += b;  print(f"\n+= {a}")
            a -= b;  print(f"-=   {a}")
            a *= b;  print(f"*=   {a}")
            a /= b;  print(f"/=   {a}")
            a **= b; print(f"**=  {a}")
            a //= b; print(f"//=  {a}")
            a %= b;  print(f"%=   {a}")
        # Compare
        if option == 3:
            print(f'''
==  {a == b}
!=  {a != b}
>   {a > b}
<   {a < b}
>=  {a >= b}
<=  {a <= b}''')

    def While():
        print(f"{Z}1 - Odd numbers \n2 - Even numbers \n3 - Stopwatch\n4 - Timer{X}")
        i = 0; option = int(input(select))

        # Odd
        if option == 1:
            while i <= 99:
                i += 1
                if (i % 2) != 1: continue;
                print(f"{Z}Odd:{X} {i}"); sleep(0.1)
        # Even
        if option == 2:
            while i <= 98:
                i += 1
                if (i % 2) == 1: continue;
                print(f"{Z}Even:{X} {i}"); sleep(0.1)
        # Stopwatch
        if option == 3:
            while True:
                print(f"\r{Z}Stopwatch:{X} {i}", end=""); i += 1; sleep(1)
        # Timer
        if option == 4:
            i = int(input("Timer on: "))
            while i >= 1:
                print(f"\r{Z}Timer: {X} {i}", end=""); i -= 1; sleep(1)

    def List():
        print(f"{Z}1 - Operations\n2 - Dictionaries\n3 - Indexes{X}")
        option = int(input(select))

        # Operations
        if option == 1:
            n = list(range(10))
            print(f"{n}\n"
                  f"{Z}Elements length: {len(n)}\n"
                  f"Elements reverse...{X}"); n.reverse()
            print(f"{n}\n{Z}Мax value: {max(n)}\n"
                  f"Min value: {min(n)}\n"
                  f"{Z}Insert index 0 with value 10{X}"); n.insert(1, 10); print(n)
            print(f"{Z}Remove value 10{X}"); n.remove(10); print(n)
            print(f"{Z}Append value -1{X}"); n.append(-1); print(n)
        # Dictionaries
        if option == 2:
            print(f"{Z}Dicitionary consists names of characters from videogames{X}")
            name = input("Enter character name: ")
            print(f"{Z}Character from: {X}", data.book.get(name.title(),
                  f"{R}KeyError: key does not match dictionary"))
        # Indexes
        if option == 3:
            print(data.slice)

    def Error():
        print(f"{Z}1 - Throwed \n2 - Expected{X}")
        option = int(input(select))

        # Throwed
        if option == 1:
            print(data.throw)
        # Expected
        if option == 2:
            try: print(text)
            except NameError: print(f"{Z}Catched exception {R}NameError{Z}")
            try: print("text" + 10)
            except TypeError: print(f"Catched exception {R}TypeError{Z}")
            try: a = int('value')
            except ValueError: print(f"Catched exception {R}ValueError{Z}")
            try: eval("print(text")
            except SyntaxError: print(f"Catched exception {R}SyntaxError{Z}")
            try: from time import sqrt
            except ImportError: print(f"Catched exception {R}ImportError{Z}")
            try: n = 10; assert n < 10
            except AssertionError: print(f"Catched exception {R}AssertionError{Z}")
            # try: eval("while True: print(10)")
            print(f"Catched exception {R}IndentionalError{Z}")
            try: print(10 / 0)
            except ZeroDivisionError: print(f"Catched exception {R}ZeroDivisionError{Z}")
            try: import unity
            except ModuleNotFoundError: print(f"Catched exception {R}ModuleNotFoundError{Z}")

    def File():
        name = input("Enter file name: ")
        print(f"{Z}1 - Symbols length\n2 - Backup file\n3 - List generator{X}")
        option = int(input(select))
        # Symbols length
        if option == 1:
            file = open(name, "rb")
            print(len(file.read()))
            file.close()
        # Backup file
        if option == 2:
            name_backup = "backup_" + name
            file = open(name, "rb")
            file_backup = open(name_backup, "wb")
            file_backup.write(file.read())
            file.close()
            file_backup.close()
        # List generator
        if option == 3:
            file = open(name, "r", encoding="utf-8")
            list = file.readlines()
            print(list)

    def Format():
        print(f"{Z}1 - Text filler\n2 - Text case\n3 - Vowel or consonant{X}")
        option = int(input(select))

        # Заполнитель
        if option == 1:
            text = input("Enter text: ")
            size = input("String length: ")
            fill = input("Filler: ")

            print(f"{Z}1 - Centre \n2 - Left \n3 - Right{X}")
            option = int(input(select))
            pos = None

            if option == 1: pos = "^"
            if option == 2: pos = "<"
            if option == 3: pos = ">"

            print(('{0:'+fill+pos+size+'}').format(text))
        # Регистр текста
        if option == 2:
            text = input("Enter any text: ")
            print("Lowered            ", text.lower())
            print("Uppered            ", text.upper())
            print("Titled             ", text.title())
            print("Swapped            ", text.swapcase())
            print("Capitalized        ", text.capitalize())
        # Vowel or consonant
        if option == 3:
            word = input("Enter word: ")
            we = word.lower().endswith
            ws = word.lower().startswith
            he = f"{Z}Word ends on {X}"
            hs = f"{Z}Word starts on {X}"

            if we("a") or we("o") or we("e") or we("i") or we("u") or we("y"): print(he, "vowel")
            else: print(he, "consonant")

            if ws("a") or ws("o") or ws("e") or ws("i") or ws("u") or we("y"): print(hs, "vowel")
            else: print(hs, "consonant")

    if void == 1: Math()
    if void == 2: While()
    if void == 3: List()
    if void == 4: Error()
    if void == 5: File()
    if void == 6: Format()
