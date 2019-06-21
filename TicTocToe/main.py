"""
TicTacToe
20.06.19 L034E

"""
from __future__ import print_function

def draw_field():
    inner_cells = input()
    cells = []
    if len(inner_cells) < 9:
        print("wrong inputs datas")
    else:        
        for i in range(0, len(inner_cells)):
            cells.append(inner_cells[i])
        print("---------")
        print("| " + cells[0] + " " + cells[1]+ " " + cells[2] + " |")
        print("| " + cells[3] + " "+ cells[4] + " " + cells[5] + " |")
        print("| " + cells[6] + " "+ cells[7] + " " + cells[8] + " |")
        print("---------")

# draw_field()
game_field = [["-", "-", "-", "-", "-", "-"],
         ["|", " ", " ", " ", " ", "|"],
         ["|", " ", " ", " ", " ", "|"],
         ["|", " ", " ", " ", " ", "|"],
         ["-", "-", "-", "-", "-", "-"]]
def draw_field1(g_f):

    for row in g_f:
        for elem in row:
            print(elem, end=' ')
        print()

draw_field1(game_field)


"""

рисуется пустое поле и координаты каждого свободного места
первый игрок вводит символ и координаты места
рисуется поле с символом
второй игрок вводит символ и координаты
рисуется поле
Если по диагонали field[0][0], field[1][1],field[2][2] т.е. field[i][j], где i == j
                  field[2][1], field[1][1],field[0][2]
Если по горизонтали т.е. в одной строке                  
Если по вертикали т.е. в одном столбце                    

"""


