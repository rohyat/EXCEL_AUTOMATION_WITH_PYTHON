def column_edit(s, row, column, wb):
    coln = int(input("ENTER THE COLUMN NUMBER\n"))
    if(coln > column):
        print("U HAVE ENTERED WRONG COLUMN NUMBER\n")
    else:
        f = int(input('''PRESS THE RIGHT OPTION THIS WILL DONE TO ALL CELLS OF COLUMN EXCEPT FIRST\n'1'--FOR ADD(+)\n'2'--FOR SUBTRACT(-)\n'3'--FOR MULTIPLY(*)\n'''))
        if(f == 1):
            n = int(
                input("ENTER THE NUMBER YOU WANT TO ADD TO CELLS OF COLUMN NUMBER\n"))
            for i in range(2, row+1):
                s.cell(i, coln).value = s.cell(i, coln).value+n
            wb.save("data.xlsx")
        elif(f == 2):
            n = int(
                input("ENTER THE NUMBER YOU WANT TO SUBTRACT TO CELLS OF COLUMN NUMBER\n"))
            for i in range(2, row+1):
                s.cell(i, coln).value = s.cell(i, coln).value-n
            wb.save("data.xlsx")
        elif(f == 3):
            n = int(
                input("ENTER THE NUMBER YOU WANT TO MULTIPLY TO CELLS OF COLUMN NUMBER\n"))
            for i in range(2, row+1):
                s.cell(i, coln).value = s.cell(i, coln).value*n
            wb.save("data.xlsx")
        else:
            print("U HAVE CHOSEN A INVALID CHOICE\n")


def cell_edit(s, row, column, wb):
    rown = int(input("ENTER THE ROW NUMBER OF CELL\n"))
    coln = int(input("ENTER THE COLUMN NUMBER OF CELL\n"))
    if(rown > row or coln > column):
        print("U HAVE ENTERED VALUE OUT OF RANGE\n")
    else:
        value = int(input("PRESS\n1--STRING\n2--INTEGER\n"))
        if(value == 1):
            newvalue = input("ENTER THE NEW STRING\n")
            s.cell(rown, coln).value = newvalue
        elif(value == 2):
            newvalue = input("ENTER THE NEW NUMBER\n")
            s.cell(rown, coln).value = newvalue
        else:
            print("U HAVE ENTERED WRONG CHOICE\n")


def add_row(s, row, column, wb):
    print("UR ROW WILL BE EDITED AFTER THE LAST PRESENT ROW\n")
    for j in range(1, column+1):
        value = int(input("PRESS\n1--STRING\n2--INTEGER\n"))
        if(value == 1):
            newvalue = input("ENTER THE NEW STRING\n")
            s.cell(row+1, j).value = newvalue
        elif(value == 2):
            newvalue = input("ENTER THE NEW NUMBER\n")
            s.cell(row+1, j).value = newvalue
    row = row+1
    wb.save("data.xlsx")
