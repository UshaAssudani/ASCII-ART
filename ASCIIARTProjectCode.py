import os
import msvcrt as msv
import sys
from colorama import init, Fore, Back, Style

init()


def choose_color():
    os.system("cls")
    print("\n\n",""*10,"SELECT COLOR",""*10,"\n")
    print("1. Red")
    print("2. Green")
    print("3. Yellow")
    print("4. Blue")
    print("5. Magenta")
    print("6. Cyan")
    print("7. White")

    ch = msv.getch().decode()

    return {
        "1": Fore.RED,
        "2": Fore.GREEN,
        "3": Fore.YELLOW,
        "4": Fore.BLUE,
        "5": Fore.MAGENTA,
        "6": Fore.CYAN,
        "7": Fore.WHITE
    }.get(ch, Fore.CYAN)

current_color = Fore.CYAN



data = [
    " ***  ****   ***  ****  ***** *****  ***  *   * ***** ***** *   * *     *   * *   *  ***  ****   ***  ****   **** ***** *   * *   * *   * *   * *   * *****        ***                     ***  ***   ****  ****  *   * *****  ***  *****  ***  ***** ",
    "*   * *   * *   * *   * *     *     *     *   *   *      *  *  *  *     ** ** **  * *   * *   * *   * *   * *       *   *   * *   * *   *  * *   * *     *        * ***                   *   *   *       *     * *   * *     *         * *   * *   * ",
    "*   * ****  *     *   * ***   ****  *  ** *****   *      *  ***   *     * * * * * * *   * ****  *   * ****  *****   *   *   * *   * * * *   *     *     *         * * *       *****       *   *   *       *   **  ***** ****  ****      *  ***  ***** ",
    "***** *   * *   * *   * *     *     *   * *   *   *   *  *  *  *  *     *   * *  ** *   * *     *   * *  *      *   *   *   *  * *  ** **  * *    *    *          * * *              ***  *   *   *   ***       *     *     * *   *     * *   *     * ",
    "*   * ****   ***  ****  ***** *      ***  *   * *****  ***  *   * ***** *   * *   *  ***  *      ***  *   * ****    *   *****   *   *   * *   *   *   *****        ***  *****        ***   ***  ***** ***** ****      * ****   ***      *  ***      * "
]



def print_block(i, j):
    print(current_color + Back.BLACK + i[j] + Style.RESET_ALL, end="")



def oneCharacter():
    global current_color
    current_color = choose_color()

    os.system("cls")
    text = input("\nEnter a Character -- ").upper()

    if len(text) != 1:
        oneCharacter()
    else:
        n = (ord(text)-17)*6 if ord(text)>=48 and ord(text) <= 57 else 26*6 if text ==" " else 27 * 6 if text == "@" else 28 * 6 if text == "_" else 29 * 6 if text == "-" else 30 * 6 if text == "." else ((ord(text) - 64)-1)*6
        for i in data:
            for j in range(n , n + 6):
                print_block(i, j)
            print()

def alphaNumWords():
    global current_color
    current_color = choose_color()

    os.system("cls")
    text = input("\nEnter String (<= 15 Character) -- ").upper()

    if not (1 <= len(text) <= 15):
        alphaNumWords()
    else:
        for i in data:
            for x in text:
                n =(ord(x)-17)*6 if ord(x)>=48 and ord(x) <= 57 else 26*6 if x ==" " else 27 * 6 if x == "@" else 28 * 6 if x == "_" else 29 * 6 if x == "-" else 30 * 6 if x == "." else ((ord(x) - 64)-1)*6 
                for j in range(n , n + 6):
                    print_block(i, j)
            print()

def alphaRange():
    global current_color
    current_color = choose_color()

    os.system("cls")
    text = input("\nEnter Range Like (A-D) -- ").upper()

    if len(text) != 3:
        alphaRange()
    else:
        sr = (ord(text[0]) - 64)
        er = (ord(text[2]) - 64)
        for i in data:
            for x in range(sr, er+1):
                n = (x - 1) * 6
                for j in range(n , n + 6):
                    print_block(i, j)
            print()

def onlyAlpha():
    global current_color
    current_color = choose_color()

    os.system("cls")
    text = input("\nEnter String (<= 15 Character) -- ").upper()

    if not text.isalpha():
        onlyAlpha()
    else:
        for i in data:
            for x in text:
                n =((ord(x) - 64)-1)*6 
                for j in range(n , n + 6):
                    print_block(i, j)
            print()

def onlyNum():
    global current_color
    current_color = choose_color()

    os.system("cls")
    text = input("\nEnter Numbers (<= 15 Character) -- ").upper()

    if not text.isnumeric():
        onlyNum()
    else:
        for i in data:
            for x in text:
                n =(ord(x)-17)*6
                for j in range(n , n + 6):
                    print_block(i, j)
            print()



def mainUI():
    os.system("cls")
    print("\n\n",""*10,"ASCII ART PROJECT",""*10,"\n")
    print("1. One Character")
    print("2. Words")
    print("3. Range")
    print("4. Only Alphabets")
    print("5. Only Numbers")
    print("6. Exit")

    ch = msv.getch().decode()

    if ch == "1":
        oneCharacter()
    elif ch == "2":
        alphaNumWords()
    elif ch == "3":
        alphaRange()
    elif ch == "4":
        onlyAlpha()
    elif ch == "5":
        onlyNum()
    elif ch == "6":
        return

    print("\n\nTo Continue so then Press y..")
    ch = msv.getch()
    if ch.decode() in ("y", "Y"):
        mainUI()

mainUI()
