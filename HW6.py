from colorama import *
init()
height = int(input('> Enter height of rectangular: '))
width = int(input('> Enter width of rectangular: '))
symbol = input(Fore.BLUE +'Enter symbol to build rectangular with: ')
for a in range (height):
 print(Fore.BLUE + symbol * width)


