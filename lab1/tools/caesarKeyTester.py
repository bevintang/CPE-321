import sys

def incUpper(char, key):
    newOrd = ord(char) + key
    if (newOrd > ord('Z')):
        newOrd -= 26
    return chr(newOrd)

def incLower(char, key):
    newOrd = ord(char) + key
    if (newOrd > ord('z')):
        newOrd -= 26
    return chr(newOrd)

def writeWithKey(key, line):
    for char in line:
        newChar = '/'
        if char.isupper():
            newChar = incUpper(char, key)
        elif char.islower():
            newChar = incLower(char, key)
        else:
            newChar = char
        sys.stdout.write(newChar)

def cycleKey(key):
    fileName = sys.argv[1]
    file = open(fileName)
    print("Key " + str(26 - key) + ": ")
    for line in file:
        writeWithKey(key, line)
    print("\n")
    file.close()

def main():
    key = 0
    while (key != 26):
        cycleKey(key)
        key += 1

if __name__ == '__main__':
    main()