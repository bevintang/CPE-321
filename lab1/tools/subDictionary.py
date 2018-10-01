import sys

alphas = {
        'a' : 'T',
        'b' : 'F',
        'c' : 'O',
        'd' : 'R',
        'e' : 'D',
        'f' : 'M',
        'g' : 'L',
        'h' : 'H',
        'i' : 'B',
        'j' : 'N',
        'k' : 'k',
        'l' : 'P',
        'm' : 'C',
        'n' : 'V',
        'o' : 'W',
        'p' : 'G',
        'q' : 'q',
        'r' : 'U',
        's' : 'I',
        't' : 'J',
        'u' : 'Y',
        'v' : 'A',
        'w' : 'K',
        'x' : 'E',
        'y' : 'S',
        'z' : 'X'
    }

counts = {
        'a' : 0,
        'b' : 0,
        'c' : 0,
        'd' : 0,
        'e' : 0,
        'f' : 0,
        'g' : 0,
        'h' : 0,
        'i' : 0,
        'j' : 0,
        'k' : 0,
        'l' : 0,
        'm' : 0,
        'n' : 0,
        'o' : 0,
        'p' : 0,
        'q' : 0,
        'r' : 0,
        's' : 0,
        't' : 0,
        'u' : 0,
        'v' : 0,
        'w' : 0,
        'x' : 0,
        'y' : 0,
        'z' : 0
    }

def printFromDict(char):
    if not char.isalpha():
        return char
    
    lowerChar = alphas[char.lower()]
    counts[char.lower()] = counts[char.lower()] + 1
    return lowerChar

def main():
    fileName = sys.argv[1]
    file = open(fileName)
    for line in file:
        for char in line:
            sys.stdout.write(printFromDict(char))
    file.close()
    
    # for entry in counts:
    #     print(entry + " : " + str(counts[entry]))

if __name__ == '__main__':
    main()