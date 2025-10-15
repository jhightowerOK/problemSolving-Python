

def main():
    col=0
    row=0
    width =int(input("Width: "))
    while(row<width):
        col=0
        while col < width:
            print("* ",end="")
            col = col + 1
        print()
        row = row + 1
    print()
    

main()
