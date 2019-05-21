def is_valid_input(letter_guessed, old_letters_guessed):
    if len(letter_guessed) > 1:
        return False
    elif not letter_guessed.isalpha():
        return False
    elif letter_guessed in old_letters_guessed:
        return False
    else:
        return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if is_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        sorted(old_letters_guessed, key=str.lower)
        print('X\n', ' -> '.join(old_letters_guessed))
        return False

def check_win(secret_word, old_letters_guessed):
    for i in range(len(secret_word)-1):
        if secret_word[i] not in old_letters_guessed:
            return False
    return True

def show_hidden_word(secret_word, old_letters_guessed):
    hidden_word = ""
    secret_word = secret_word[:-1]
    for i in secret_word:
        if i in old_letters_guessed:
            hidden_word += i+" "
        else:
            hidden_word += "_ "
    return hidden_word

def choose_word(file_path, index):
    input_file = open(file_path, "r")
    lines = input_file.readlines()
    num_lines = file_lengthy(file_path)
    # index %= (num_lines-1)
    input_file.close()
    return num_lines, lines[index]

def file_lengthy(fname):
        with open(fname) as f:
            for i, l in enumerate(f):
                pass
        return i + 1

MAX_TRIES = 6
letters_guessed = []
HANGMAN_PHOTOS = {1: "x-------x",
                  2: """
                  x-------x
                  |
                  |
                  |
                  |
                  |
                  """,
                  3: """
                  x-------x
                  |       |
                  |       0
                  |
                  |
                  |
                  """,
                  4: """
                  x-------x
                  |       |
                  |       0
                  |       |
                  |
                  |
                  """,
                  5: """
                  x-------x
                  |       |
                  |       0
                  |      /|\\
                  |
                  |
                  """,
                  6: """
                  x-------x
                  |       |
                  |       0
                  |      /|\\
                  |      /
                  |
                  """,
                  7: """
                  x-------x
                  |       |
                  |       0
                  |      /|\\
                  |      / \\
                  |
                  """
                  }

HANGMAN_ASCII_ART = """
     _    _ 
    | |  | |
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                         __/ |                      
                        |___/"""
def main():
    print(HANGMAN_ASCII_ART)
    print(MAX_TRIES)
    path = "animals.txt"
    number = 1
    num_lines, word = choose_word(path, number)
    # word = input("Please enter a word: ") last assignment
    print("_ "*(len(word)-1)+"\n")
    win = False
    num_of_tries = 1

    while (not win) and (num_of_tries < 7):
        letter = input("Guess a letter:")
        if is_valid_input(letter, letters_guessed):
            if letter not in word or letter in letters_guessed:
                num_of_tries += 1
        try_update_letter_guessed(letter, letters_guessed)
        win = check_win(word, letters_guessed)
        print(show_hidden_word(word, letters_guessed))
        print(HANGMAN_PHOTOS[num_of_tries])

    if num_of_tries < 7:
        print("You won! :)")
    else:
        print("You died! :O")


main()