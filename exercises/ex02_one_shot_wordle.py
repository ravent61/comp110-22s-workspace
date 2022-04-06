"""EX02 Wordle."""

__author__ = "730355583"


SECRET_WORD: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
LEN_SECRET_WORD: int = len(SECRET_WORD)


index: int = 0
result: str = ""

guess: str = input(f"What is your {LEN_SECRET_WORD}-letter guess? ")

while len(guess) != LEN_SECRET_WORD:
    guess = input("That was not py" + str(LEN_SECRET_WORD) + " letters! Try again: ")
    

while index < len(guess):
    char: str = guess[index]
    index_for_matches: int = 0

    exists: bool = False
    if char == SECRET_WORD[index]:
        result += GREEN_BOX
    else:
        while not exists and index_for_matches < LEN_SECRET_WORD:
            if char == SECRET_WORD[index_for_matches]:
                exists = True
            else:
                index_for_matches += 1
        
        if exists is True:
            result += YELLOW_BOX
        else:
            result += WHITE_BOX

    index += 1

print(result)

if guess == SECRET_WORD:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")