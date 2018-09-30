def cycleKey():
    fileName = input('Enter filen name:')
    file = open(fileName)
    for line in file:
        print(line)
    file.close()

def main():
    cycleKey()

if __name__ == '__main__':
    main()