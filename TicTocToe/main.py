"""
TicTacToe
20.06.19 L034E

"""

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

draw_field()





