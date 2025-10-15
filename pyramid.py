def printRow(row,width):
    col=0
    noSpaces = (width-row)//2
    while col < noSpaces:
        print("  ",end="")
        col = col + 1
    col=0
    while col < row:
        print("* ",end="")
        col = col + 1
    print()

def main():
    
    width =int(input("Width: "))
    while width%2==0 or width<1 or width>15:
        width =int(input("Width: "))

    #Top of Pryamid
    col=0
    row=1
    while(row<=width):
        printRow(row,width)
        row = row + 2
    
     #Bottom of Pryamid
    col=0
    row=width-2;
    while(row>0):
        printRow(row,width)
        row = row - 2
    print()

    

main()


