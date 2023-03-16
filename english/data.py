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
"Johnny Silverhand" : CP,
"Judy Alvarez" : CP,
"Alt Cunningham" : CP,
"Goro Takemura" : CP,
"Panam Palmer" : CP,
"Franklin Clinton" : GTA,
"Tommy Vercetti" : GTA,
"Trevor Philips" : GTA,
"Carl Johnson" : GTA,
"Michael Townley" : GTA,
"Lester Crest" : GTA,
"Niko Bellic" : GTA,
"Tyler Morgan" : NFS,
"Ryan Cooper" : NFS,
"Jack Rourke" : NFS,
"Soap Mctavish" : COD,
"Simon Riley" : COD,
"John Price" : COD,
"Ezio Audiotore" : AC,
"Edward Kenway" : AC,
"Gordon Freeman" : HL,
"Barney Calhoun" : HL,
"Alyx Vance" : HL,
"Miranda Lawson" : ME,
"John Shepard" : ME,
"Sergey Nechaev" : "Atomic Heart",
"Igor Khiminyuk" : "Chernobylite",
"Alexander Degtyarev" : "Stalker",
"Kyle Crane" : "Dying Light",
"Vito Scaletta" : "Mafia 2",
"Adam Jensen" : "Deus Ex",
"Jack Ryan" : "Bioshock",
"Morgan Yu" : "Prey"
}
# </editor-fold>

info = f'''Base knowledges of Python in code (by AorusBehavi)
{Z}1 - Operators
2 - Cycles
3 - Arrays
4 - Exceptions
5 - Files
6 - Format text{X}'''

select = "Select option: "

throw = f'''
{Z}print(text)
{R}NameError: name 'text' is not defined

{Z}a = int('value')
{R}ValueError: invalid literal 'value' for int()


{Z}print('10' + 10)
{R}TypeError: can't implicitly convert 'int' to 'str'

{Z}print(text +)
{R}SyntaxError: invalid syntax

{Z}from time import sqrt
{R}ImportError: cannot import name 'sqrt' from 'time\'

{Z}n = 10; assert n < 10
{R}AssertionError: 'n' must be lower than 0

{Z}while True: print(10)
{R}IndentationError: expected an indented block

{Z}print(10 / 0)
{R}ZeroDivisionError: division by zero

{Z}import unity
{R}ModuleNotFoundError: no module named 'unity\''''

slice = f'''
{Z}list [{X}start{Z} : {X}end{Z} : {X}step{Z}]
{X}start{Z} - slice start (offset {X}0{Z})
{X}end{Z} - slice end (offset {X}-1{Z})
{X}step{Z} - slice step (offset {X}-1{Z})'''