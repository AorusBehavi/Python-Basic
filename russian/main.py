import data
from data import X
from data import R
from data import Z
from time import sleep
from data import select

class Learn():
    print(data.info)
    void = int(input("Выберите пространство: "))

    def Math():
        a = int(input("Введите A: "))
        b = int(input("Введите B: "))
        print(f"{Z}1 - Простые \n2 - Уместные \n3 - Сравнение{X}")
        option = int(input(select))

        # Простые
        if option == 1:
            print(f'''
+   {a + b}
-   {a - b}
*   {a * b}
/   {a / b}
**  {a ** b}
//  {a // b}
%   {a % b}''')
        # Уместные
        if option == 2:
            a += b;  print(f"\n+= {a}")
            a -= b;  print(f"-=   {a}")
            a *= b;  print(f"*=   {a}")
            a /= b;  print(f"/=   {a}")
            a **= b; print(f"**=  {a}")
            a //= b; print(f"//=  {a}")
            a %= b;  print(f"%=   {a}")
        # Сравнение
        if option == 3:
            print(f'''
==  {a == b}
!=  {a != b}
>   {a > b}
<   {a < b}
>=  {a >= b}
<=  {a <= b}''')

    def While():
        print(f"{Z}1 - Нечетные числа \n2 - Четные числа \n3 - Секундомер\n4 - Таймер{X}")
        i = 0; option = int(input(select))

        # Нечетные числа
        if option == 1:
            while i <= 99:
                i += 1
                if (i % 2) != 1: continue;
                print(f"{Z}Нечетное:{X} {i}"); sleep(0.1)
        # Четные числа
        if option == 2:
            while i <= 98:
                i += 1
                if (i % 2) == 1: continue;
                print(f"{Z}Четное:{X} {i}"); sleep(0.1)
        # Секундомер
        if option == 3:
            while True:
                print(f"\r{Z}Секундомер:{X} {i}", end=""); i += 1; sleep(1)
        # Таймер
        if option == 4:
            i = int(input("Таймер на: "))
            while i >= 1:
                print(f"\r{Z}Таймер: {X} {i}", end=""); i -= 1; sleep(1)

    def List():
        print(f"{Z}1 - Операции\n2 - Словари\n3 - Индексы{X}")
        option = int(input(select))

        # Операции
        if option == 1:
            n = list(range(10))
            print(f"{n}\n"
                  f"{Z}Количество элементов: {len(n)}\n"
                  f"Переворот элементов...{X}"); n.reverse()
            print(f"{n}\n{Z}Максимальное значение: {max(n)}\n"
                  f"Минимальное значение: {min(n)}\n"
                  f"{Z}Вставка индекса 0 со значением 10{X}"); n.insert(1, 10); print(n)
            print(f"{Z}Удаление значения 10{X}"); n.remove(10); print(n)
            print(f"{Z}Добавление значения -1{X}"); n.append(-1); print(n)
        # Словари
        if option == 2:
            print(f"{Z}Словарь включает себя геров из видеоигр{X}")
            name = input("Укажите имя героя: ")
            print(f"{Z}Указанный герой из: {X}", data.book.get(name.title(),
                  f"\n{Z}Ошибка запроса: ключ не соответсвует словарю\n"
                  f"{R}KeyError: key does not match dictionary"))
        # Индексы
        if option == 3:
            print(data.slice)

    def Error():
        print(f"{Z}1 - Выброшены \n2 - Обнаружены{X}")
        option = int(input(select))

        # Выброшены
        if option == 1:
            print(data.throw)
        # Обнаружены
        if option == 2:
            try: print(text)
            except NameError: print(f"{Z}Поймано исключение {R}NameError{Z}")
            try: print("text" + 10)
            except TypeError: print(f"Поймано исключение {R}TypeError{Z}")
            try: a = int('value')
            except ValueError: print(f"Поймано исключение {R}ValueError{Z}")
            try: eval("print(text")
            except SyntaxError: print(f"Поймано исключение {R}SyntaxError{Z}")
            try: from time import sqrt
            except ImportError: print(f"Поймано исключение {R}ImportError{Z}")
            try: n = 10; assert n < 10
            except AssertionError: print(f"Поймано исключение {R}AssertionError{Z}")
            # try: eval("while True: print(10)")
            print(f"Поймано исключение {R}IndentionalError{Z}")
            try: print(10 / 0)
            except ZeroDivisionError: print(f"Поймано исключение {R}ZeroDivisionError{Z}")
            try: import unity
            except ModuleNotFoundError: print(f"Поймано исключение {R}ModuleNotFoundError{Z}")

    def File():
        name = input("Укажите название файла: ")
        print(f"{Z}1 - Кол-во символов\n2 - Резервная копия\n3 - Генератор массива{X}")
        option = int(input(select))
        # Кол-во символов
        if option == 1:
            file = open(name, "rb")
            print(len(file.read()))
            file.close()
        # Резервная копия
        if option == 2:
            name_backup = "backup_" + name
            file = open(name, "rb")
            file_backup = open(name_backup, "wb")
            file_backup.write(file.read())
            file.close()
            file_backup.close()
        # Генератор массива
        if option == 3:
            file = open(name, "r", encoding="utf-8")
            list = file.readlines()
            print(list)

    def Format():
        print(f"{Z}1 - Заполнитель\n2 - Регистр текста\n3 - Гласный или согласный{X}")
        option = int(input(select))

        # Заполнитель
        if option == 1:
            text = input("Желаемый текст: ")
            size = input("Размер строки: ")
            fill = input("Заполнитель: ")

            print(f"{Z}1 - Центр \n2 - Слева \n3 - Справа{X}")
            option = int(input(select))
            pos = None

            if option == 1: pos = "^"
            if option == 2: pos = "<"
            if option == 3: pos = ">"

            print(('{0:'+fill+pos+size+'}').format(text))
        # Регистр текста
        if option == 2:
            text = input("Введите любой текст: ")
            print("Нижний              ", text.lower())
            print("Вверхний            ", text.upper())
            print("Заглавный           ", text.title())
            print("Измененный          ", text.swapcase())
            print("Приведенный         ", text.capitalize())
        # Гласный или согласный
        if option == 3:
            word = input("Введите слово: ")
            we = word.lower().endswith
            ws = word.lower().startswith
            he = f"{Z}Введеное слово заканчивается на {X}"
            hs = f"{Z}Введеное слово начинается с {X}"

            if we("а") or we("о") or we("у") or we("э") or we("ы") or\
               we("я") or we("е") or we("ё") or we("ю") or we("и") or \
               we("a") or we("o") or we("e") or we("i") or we("u") or we("y"): print(he, "гласный")
            else: print(he, "согласный")

            if ws("а") or ws("о") or ws("у") or ws("э") or ws("ы") or\
               ws("я") or ws("е") or ws("ё") or ws("ю") or ws("и") or \
               ws("a") or ws("o") or ws("e") or ws("i") or ws("u") or we("y"): print(hs, "гласного")
            else: print(hs, "согласного")

    if void == 1: Math()
    if void == 2: While()
    if void == 3: List()
    if void == 4: Error()
    if void == 5: File()
    if void == 6: Format()
