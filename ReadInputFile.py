#Testing function
def readInputFile(fileName):
    file = open(fileName,"r")
    words = file.read().splitlines()
    print(words)
    file.close()

readInputFile("RandomWords.txt")