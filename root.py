import read
import write

def main_fun(s, row, column,wb):
    x = int(input("PRESS\n'1' FOR READ\n'2' FOR WRITE\n'3' FOR EXIT\n"))
    if(x == 1):
        lets_read(s, row, column,wb)
    elif(x == 2):
        lets_write(s, row, column, wb)
    elif(x == 3):
        return
    else:
        print("U HAVE ENTERED INVALID CHOICE PLEASE CHOICE 1 OR 2 WHEN ASKED\n")
        main_fun(s, row, column)

def lets_read(sname, row, column,wb):
    print("YOU HAVE CHOSEN READ ENTER THE RIGHT CHOICE\n")
    a = int(input(
        "PRESS OPTION TO READ\n'1'---ENTIRE SHEET\n'2'---COLUMN\n'3'---ROW\n'4'---CELL\n"))
    if(a == 1):
        read.whole_sheet(sname, row, column,wb)
        main_fun(sname, row, column,wb)
    elif(a == 2):
        read.column_of_sheet(sname, row, column,wb)
        main_fun(sname, row, column,wb)
    elif(a == 3):
        read.row_of_sheet(sname, row, column,wb)
        main_fun(sname, row, column,wb)
    elif(a == 4):
        read.cell_of_sheet(sname, row, column,wb)
        main_fun(sname, row, column,wb)
    else:
        print("U HAVE ENTERED INVALID CHOICE\n")
        main_fun(sname, row, column,wb)

def lets_write(sname, row, column, wb):
    print("YOU HAVE CHOSEN WRITE\n")
    b = int(input("PRESS OPTION TO WRITE\n'1'--EDIT THIS FILE \n'2'--ADD NEW ROW\n"))
    if(b == 1):
        e = int(
            input("PRESS OPTION TO WRITE\n'1'--EDIT THE COLUMN\n'2'--EDIT THE CELL\n"))
        if(e == 1):
            write.column_edit(sname, row, column, wb)
            main_fun(sname, row, column,wb)
        elif(e == 2):
            write.cell_edit(sname, row, column, wb)
            main_fun(sname, row, column,wb)
        else:
            print("U HAVE ENTERED THE WRONG CHOICE\n")                                
            main_fun(sname, row, column,wb) 
    elif(b == 2):
        write.add_row(sname, row, column, wb)
        main_fun(sname, row, column,wb)
    else:
        print("U HAVE ENTERED A WRONG CHOICE\n")
        main_fun(sname, row, column,wb)
