import os
import csv
from prettytable import PrettyTable
from prettytable import from_csv
from rich import print
from rich.panel import Panel
ghdf = "column title"
tofile = ""
row3 = []
ui = 0
gas = False
agh = False
while True:
    print(Panel.fit("Roma's SpreadSheets!"))
    print("+------------------------------------+")
    print("|N for New File, R for Read, ! - Exit|")
    print("+------------------------------------+")
    sel = input(">")
    if sel.upper() == "R":
        while True:
            name = input("Name(or /quit):")
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
            name = input("Name:")
            name = name + ".csv"
            print(f"New file [cyan]{name}")
            po = input("Number of columns:")
            try:
                ndf = int(po)
            except:
                print("Error")
            with open(name, mode='w') as file:
                while True:
                    cell2 = input(f"(/quit)Enter {ghdf}({ndf} left):")
                    if gas == True:
                        if ui == cell2:
                            print("Wrong cell text")
                            continue
                    if cell2 == "/quit":
                        agh = True
                        ghdf = "column title"
                        break
                    row3.append(cell2)
                    ndf = ndf - 1
                    ui = cell2
                    gas = True
                    if ndf == 0:
                        ghdf = "cell"
                        tofile = ",".join(row3)+"\n"
                        file.write(tofile)
                        tofile = ""
                        row3 = []
                        ndf = int(po)
                        os.system('cls')
                        continue
    if sel == "!":
        break


