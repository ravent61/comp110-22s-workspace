"""EX03 Wordle."""

__author__ = "730355583"


SECRET_WORD: str = "codes"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
LEN_SECRET_WORD: int = len(SECRET_WORD)


def contains_char(search: str, char: str) -> bool:
    """Given a string to search through and a single character, return true if that character is present in the string."""
    assert len(char) == 1
    i: int = 0
    while i < len(search):
        if search[i] == char:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Given a guess string and a secret string, return a string of emoji like ex02."""
    assert len(guess) == len(secret)

    i: int = 0
    result: str = ""

    while i < len(secret):
        if guess[i] == secret[i]:
            result += GREEN_BOX
        elif contains_char(secret, guess[i]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        i += 1

    return result


def input_guess(exp_len: int) -> str:
    """Make the user guess until correct number of letters."""
    guess: str = input(f"Enter a {exp_len} character word: ")

    while len(guess) != exp_len:
        guess = input("That was not " + str(exp_len) + " chars! Try again: ")
        
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    while turns <= 6:
        print(f"=== Turn {turns}/6 ===")
        guess: str = input_guess(len(SECRET_WORD))
        result = emojified(guess, SECRET_WORD)
        print(result)
        
        correct: str = ""
        i: int = 0
        while i < len(SECRET_WORD):
            correct += GREEN_BOX
            i += 1
        
        if result == correct:
            print(f"You won in {turns}/6 turns!")
            break

        turns += 1
    
    if turns == 7:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
