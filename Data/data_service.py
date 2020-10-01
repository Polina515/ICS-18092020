
from dataclasses import dataclass

@dataclass
class MoveOfGoods:
    number: int
    code: int
    remainder: float
    profit: float
    output: float

class DirectoryOfGoods:
    code: int
    type: str

move_array = []
move_array.append(MoveOfGoods(1, 1, 23.54, 64.56, 72.52))
move_array.append(MoveOfGoods(2, 2, 11.72, 21.45, 21.10))
move_array.append(MoveOfGoods(1, 3, 57.54, 87.35, 95.59))
move_array.append(MoveOfGoods(2, 4, 31.26, 41.26, 61.10))
move_array.append(MoveOfGoods(1, 5, 42.48, 32.78, 52.56))
move_array.append(MoveOfGoods(2, 6, 25.56, 65.15, 95.96))
move_array.append(MoveOfGoods(2, 7, 31.10, 65.86, 87.85))
move_array.append(MoveOfGoods(1, 8, 24.25, 75.70, 79.84))
move_array.append(MoveOfGoods(1, 9, 9.45, 21.15, 23.62))
move_array.append(MoveOfGoods(3, 1, 15.77, 43.26, 48.59))
move_array.append(MoveOfGoods(3, 2, 7.85, 1437, 14.14))
move_array.append(MoveOfGoods(3, 3, 38.55, 58.52, 64.05))
move_array.append(MoveOfGoods(3, 4, 20.94, 27.64, 40.94))
move_array.append(MoveOfGoods(3, 5, 28.46, 21.96, 35.22))
move_array.append(MoveOfGoods(3, 6, 17.13, 43.65, 64.29))
move_array.append(MoveOfGoods(3, 7, 20.84, 44.13, 58.86))
move_array.append(MoveOfGoods(3, 8, 16.25, 50.72, 53.49))
move_array.append(MoveOfGoods(3, 9, 6.33, 14.17, 15.83))

directory_array = []
directory_array.append(DirectoryOfGoods(1, "Масло"))
directory_array.append(DirectoryOfGoods(2, "Сир твердий"))
directory_array.append(DirectoryOfGoods(3, "Молоко"))
directory_array.append(DirectoryOfGoods(4, "Сир"))
directory_array.append(DirectoryOfGoods(5, "Маргарин"))
directory_array.append(DirectoryOfGoods(6, "М'ясо"))
directory_array.append(DirectoryOfGoods(7, "Ковбаса"))
directory_array.append(DirectoryOfGoods(8, "Фарш м'ясний"))
directory_array.append(DirectoryOfGoods(9, "М'ясо кістки"))

def printMoveOfGoods(moveOfGoods):
    '''printMoveOfGoods function prints
    "Рух товарів"
    with names and values'''

    print("Номер складу: {number}, Код товару: {code}, Залишок на початок місяця,грн: {remainder}, Прибуток,грн: {profit}, Вибуток,грн: {output}"
          .format(number=moveOfGoods.number, code=moveOfGoods.code, remainder=moveOfGoods.remainder, profit=moveOfGoods.profit, output=moveOfGoods.output))

for data in move_array:
    printMoveOfGoods(data)

def printDirectoryOfGoods(directoryOfGoods):
    '''printDirectoryOfGoods function prints
    "Довідник товарів"
    with names and values'''

    print("Код товару: {code}, Назва товару: {type}"
          .format(code=directoryOfGoods.code, type=directoryOfGoods.type))

for data in directory_array:
    printDirectoryOfGoods(data)











