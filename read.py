def whole_sheet(sname, row, column,wb):
    for i in range(1, row+1):
        for j in range(1, column+1):
            print(sname.cell(i, j).value)
            print(" ")
        print("\n")


def column_of_sheet(sname, row, column,wb):
    coln = int(input("ENTER A VALID COLUMN NUMBER\n"))
    if(coln > column):
        print("U HAVE ENTERED WRONG COLUMN NUMBER\n")
    else:
        for i in range(1, row+1):
            print(sname.cell(i, coln).value)


def row_of_sheet(sname, row, column,wb):
    rown = int(input("ENTER A VALID ROW NUMBER\n"))
    if(rown > row):
        print("U HAVE ENTERED A INVALID CHOICE\n")
    else:
        for j in range(1, column+1):
            print(sname.cell(rown, j).value)


def cell_of_sheet(sname, row, column,wb):
    rown = int(input("ENTER A VALID ROW NUMBER\n"))
    coln = int(input("ENTER A VALID COLUMN NUMBER\n"))

    if(rown > row or coln > column):
        print("U HAVE ENTERED A INVALID CHOICE\n")
    else:
        print(sname.cell(rown, coln).value)


    