X = "\033[0m"
R = "\033[31m"
Z = "\033[37m"

# <editor-fold desc = "Dictionary">
AC = "Assasins Creed"
GTA = "Grand Theft Auto"
NFS = "Need For Speed"
COD = "Call Of Duty"
HL = "Half Life"
ME = "Mass Effect"
CP = "Cyberpunk 2077"

book = {
"Джонни Сильверхенд" : CP,
"Джуди Альварез" : CP,
"Альт Каннингем" : CP,
"Горо Такэмура" : CP,
"Панам Палмер" : CP,
"Франклин Клинтон" : GTA,
"Томми Версетти" : GTA,
"Тревор Филипс" : GTA,
"Карл Джонсон" : GTA,
"Майкл Таунли" : GTA,
"Лестер Крест" : GTA,
"Нико Беллик" : GTA,
"Тайлер Морган" : NFS,
"Райан Купер" : NFS,
"Джек Рурк" : NFS,
"Соуп Мактавиш" : COD,
"Саймон Райли" : COD,
"Джон Прайс" : COD,
"Эцио Аудиоторе" : AC,
"Эдвард Кенуэй" : AC,
"Гордон Фриман" : HL,
"Барни Калхаун" : HL,
"Аликс Вэнс" : HL,
"Миранда Лоусон" : ME,
"Джон Шепард" : ME,
"Сергей Нечаев" : "Atomic Heart",
"Игорь Химинюк" : "Chernobylite",
"Александр Дегтярев" : "Stalker",
"Кайл Крейн" : "Dying Light",
"Вито Скалетта" : "Mafia 2",
"Адам Дженсен" : "Deus Ex",
"Джек Райан" : "Bioshock",
"Морган Ю" : "Prey",
}
# </editor-fold>

info = f'''Основные знания Python в коде (от AorusBehavi)
{Z}1 - Операторы
2 - Циклы
3 - Массивы
4 - Исключения
5 - Файлы
6 - Форматирование{X}'''

select = "Выберите опцию: "

throw = f'''
{Z}print(text)
Ошибка Имени: имя 'text' не определено
{R}NameError: name 'text' is not defined

{Z}a = int('value')
Ошибка значения: недопустимый литерал 'value' для int()
{R}ValueError: invalid literal 'value' for int()


{Z}print('10' + 10)
Ошибка Типа: невозможно неявно преборазовать 'int' в 'str'
{R}TypeError: can't implicitly convert 'int' to 'str'

{Z}print(text +)
Ошибка Синтаксиса: неверный синтаксис
{R}SyntaxError: invalid syntax

{Z}from time import sqrt
Ошибка Импорта: невозможно импортировать 'sqrt' из 'time
{R}ImportError: cannot import name 'sqrt' from 'time\'

{Z}n = 10; assert n < 10
Ошибка Утверждения: 'n' должно быть меньше нуля
{R}AssertionError: 'n' must be lower than 0

{Z}while True: print(10)
Ошибка Отступа: ожидается блок отступа
{R}IndentationError: expected an indented block

{Z}print(10 / 0)
Ошибка Деления Нуля: деление на нуль
{R}ZeroDivisionError: division by zero

{Z}import unity
Ошибка Модуля: модуль 'unity' необнаружен
{R}ModuleNotFoundError: no module named 'unity\''''

slice = f'''
{Z}list [{X}start{Z} : {X}end{Z} : {X}step{Z}]
{X}start{Z} - начало среза (смещение {X}0{Z})
{X}end{Z} - конец среза (смещение {X}-1{Z})
{X}step{Z} - шаг среза (смещение {X}-1{Z})'''