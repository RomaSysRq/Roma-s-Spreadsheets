import os
import csv
from prettytable import PrettyTable
from prettytable import from_csv
from rich import print
from rich.panel import Panel
ghdf = "заголовок колонки"
tofile = ""
row3 = []
ui = 0
gas = False
agh = False
while True:
    print(Panel.fit("Roma's SpreadSheets!"))
    print("+----------------------------------------------------+")
    print("|N для новой таблицы, R для чтения таблицы, ! - выход|")
    print("+----------------------------------------------------+")
    sel = input(">")
    if sel.upper() == "R":
        while True:
            name = input("Имя(или /quit):")
            name = name + ".csv"
            if name == "/quit.csv":
                os.system('cls')
                break
            else:
                with open(name, "r") as fp:
                    x = from_csv(fp)
                print(x)
    if sel.upper() == "N":
        while True:
            if agh == True:
                os.system('cls')
                break
            name = input("Имя:")
            name = name + ".csv"
            print(f"Новый файл - [cyan]{name}")
            po = input("Число колонок:")
            try:
                ndf = int(po)
            except:
                print("Ошибка")
            with open(name, mode='w') as file:
                while True:
                    cell2 = input(f"(/quit)Введите {ghdf}({ndf} осталось):")
                    if gas == True:
                        if ui == cell2:
                            print("Wrong cell text")
                            continue
                    if cell2 == "/quit":
                        agh = True
                        ghdf = "заголовок колонки"
                        break
                    row3.append(cell2)
                    ndf = ndf - 1
                    ui = cell2
                    gas = True
                    if ndf == 0:
                        ghdf = "клетку"
                        tofile = ",".join(row3)+"\n"
                        file.write(tofile)
                        tofile = ""
                        row3 = []
                        ndf = int(po)
                        os.system('cls')
                        continue
    if sel == "!":
        break


