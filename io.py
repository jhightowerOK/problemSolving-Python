
def add(num1, num2):
    sum = num1 + num2
    return sum

def saveFile(message):
    fp=open("messagesb","ab")
    encoded = message.encode("UTF-8")
    fp.write(encoded);
    num=234
    fp.write(num)
    fp.close()


def main():
    col=0
    row=0
    width =int(input("Line Width: "))
    while row < width:
        col=0
        while col <= row:
            print("* ",end="")
            col = col + 1
        print()
        row = row + 1
    saveFile("Finished\n")
    saveFile("Done")


main()
