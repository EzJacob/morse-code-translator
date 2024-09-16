# This program translates morse code to string and vice versa


import json


def enter_file_prompt(type_of_input):
    while True:
        print("1. Enter input via console.")
        print("2. Enter input via file.")
        print("3. Go Back.")
        method = input()
        if method == "1":
            return input(f"Enter your {type_of_input}:\n")
        if method == "2":
            file_path = input(f"Enter your file path with {type_of_input}:\n")
            try:
                with open(file_path, 'r') as f:
                    return f.read()
            except FileNotFoundError:
                print(f"Error: The file '{file_path}' was not found.")
                return None
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                return None
        if method == "3":
            return None


def translate_text_character_to_morse(ch):
    for key, value in letter_dic.items():
        if value == ch.upper():
            return key
    return '*'


def translate_morse_character_to_text(ch):
    if ch in letter_dic:
        return letter_dic[ch]
    return '*'


# between each word there needs to be 7 spaces
def check_spaces_between_words(word):
    if word[0] == ' ' or word[-1] == ' ':
        return False
    return True


# between each letter there needs to be 3 spaces
def check_spaces_between_letters(letters):
    for letter in letters:
        if ' ' in letter:
            return False
    return True


def morse_code_to_text(user_input):
    translated_text = ""
    words = user_input.split("       ")
    word_count = 0
    for word in words:
        word_count += 1
        if not check_spaces_between_words(word):
            print(f"Wrong number of spaces between words. Word number {word_count}: {word}")
        if word == '':
            continue
        if word == '\n':
            translated_text += '\n'
            continue
        letters = word.split("   ")
        if not check_spaces_between_letters(letters):
            print(f"Wrong number of spaces between each letter. Word number {word_count}: {word}")
        for ch in letters:
            translated_text += translate_morse_character_to_text(ch)
        translated_text += ' '
    if translated_text[-1] == ' ':
        translated_text = translated_text[:-1]

    print(translated_text)


def text_to_morse_code(user_input):
    translated_morse_code = ""
    words = user_input.split(" ")
    for word in words:
        if word == '':
            continue
        if word == '\n':
            translated_morse_code += '\n'
            continue
        for ch in word:
            translated_morse_code += translate_text_character_to_morse(ch) + "   "
        translated_morse_code = translated_morse_code[:-3]
        translated_morse_code += "       "
    translated_morse_code = translated_morse_code[:-7]

    print(translated_morse_code)


if __name__ == '__main__':
    letter_dic = {}
    try:
        with open('letter_dictionary.json', 'r') as file:
            letter_dic = json.load(file)
    except FileNotFoundError:
        print("Error: The file 'letter_dictionary.json' was not found.")
        exit(1)
    except json.JSONDecodeError:
        print("Error: The file 'letter_dictionary.json' contains invalid JSON.")
        exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        exit(1)

    while True:
        print("\n0. Read the rules.")
        print("1. Translate morse code to text.")
        print("2. Translate text to morse code.")
        print("3. Show translatable characters.")
        print("4. Exit")
        option = input()
        if option == "0":
            print("When translating morse code to text make sure to have 3 spaces between each character and 7 spaces "
                  "between each word.\nWhen translating text to morse code, the translated text won't be able to "
                  "include multiple spaces consecutively")
        if option == "1":
            # check if you want to input a file
            user_input = enter_file_prompt("morse code")
            if user_input is None:
                continue
            morse_code_to_text(user_input)
        if option == "2":
            user_input = enter_file_prompt("text")
            if user_input is None:
                continue
            text_to_morse_code(user_input)
        if option == "3":
            print(letter_dic)
        if option == "4":
            exit()
