# Python Tik Tak Toe Game

# Array of responses
arr = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

# PlayBoard display
def printPlayBoard():
    print("\n")
    print(' '+arr[0][0]+' | '+arr[0][1]+' | '+arr[0][2])
    print("-----------")
    print(' '+arr[1][0]+' | '+arr[1][1]+' | '+arr[1][2])
    print("-----------")
    print(' '+arr[2][0]+' | '+arr[2][1]+' | '+arr[2][2])
    print("\n")

def getInput(sym):
    inp = input("Enter the matric position : ")
    assignInput(inp[0],inp[1],sym)
    printPlayBoard()

def assignInput(row,col,sym):
    arr[row][col]=sym


def driver():
    for e in range(0,9):
        if(e%2==0):
            getInput('x')
        else:
            getInput('0')

driver()


