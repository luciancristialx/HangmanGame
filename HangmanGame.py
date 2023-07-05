import random

def readInputFile(fileName):
    file = open(fileName, "r")
    listOfWords = file.read().splitlines()
    file.close()
    return listOfWords
def hangmanAlgorithm(fileName):
    words = readInputFile(fileName)
    chosenWord = random.choice(words)
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessMade = ''

    while len(chosenWord) > 0:
        #Define variable to store temporary word
        tempWord = ""

        # Display number of characters to be guessed (e.g. ______)
        for letter in chosenWord:
            if letter in guessMade:
                tempWord = tempWord + letter
            else:
                tempWord = tempWord + "_" + ""
        print("Guess the word: ", tempWord)

        # Check if tempWord = chosenWord
        if tempWord == chosenWord:
            print(tempWord)
            print("You won!")
            break

        # Get letter from user & check whether it can be found in valid characters list
        guessLetter = input("Enter letter: ")
        if guessLetter in validLetters:
            guessMade = guessMade + guessLetter
        else:
            print("Enter a valid character: ")
            guessLetter = input()

        if guessLetter not in chosenWord:
            turns = turns - 1
            if turns == 9:
                print("9 turns left")
                print("  ---------  ")
            if turns == 8:
                print("8 turns left")
                print("  ---------  ")
                print("      O      ")
            if turns == 7:
                print("7 turns left")
                print("  ---------  ")
                print("      O      ")
                print("      |      ")
            if turns == 6:
                print("6 turns left")
                print("  ---------  ")
                print("      O      ")
                print("      |      ")
                print("     /       ")
            if turns == 5:
                print("5 turns left")
                print("  ---------  ")
                print("      O      ")
                print("      |      ")
                print("     / \     ")
            if turns == 4:
                print("4 turns left")
                print("  ---------  ")
                print("    \ O      ")
                print("      |      ")
                print("     / \     ")
            if turns == 3:
                print("3 turns left")
                print("  ---------  ")
                print("    \ O /    ")
                print("      |      ")
                print("     / \     ")
            if turns == 2:
                print("2 turns left")
                print("  ---------  ")
                print("    \ O /|   ")
                print("      |      ")
                print("     / \     ")
            if turns == 1:
                print("1 turn left")
                print("  ---------  ")
                print("    \ O /_|  ")
                print("      |      ")
                print("     / \     ")
            if turns == 0:
                print("You lost!")
                print("  ---------  ")
                print("      O_|    ")
                print("     /|\     ")
                print("     / \     ")
                break

name = input("Enter your name: ")
print("Welcome, ",name,"!\n\nInstructions")
print("--------------------")
print("Try to guess the word in less than 10 attempts!")
print("--------------------\n")
hangmanAlgorithm("RandomWords.txt")