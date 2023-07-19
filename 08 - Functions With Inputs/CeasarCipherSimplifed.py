from art import logo

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

retry = True
print(logo)


def caesar(txt, shf, dir):
    output_txt = ""

    for char in txt:
        if char not in alphabet:
            output_txt += char
        else:
            position = alphabet.index(char)
            new_position = None

            if dir == "encode":
                new_position = position + shf
            elif dir == "decode":
                new_position = position - shf
            else:
                break

            output_txt += alphabet[new_position]

    print(f'The {dir}d text is "{output_txt}"')


while retry:
    direction = input('\nType "encode" to encrypt, type "decode" to decrypt: ').lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    shift = shift % 26  # keeps the shift from exceeding the number of letters in the list.

    caesar(text, shift, direction)

    result = input("Would you like to restart the program? Y or N? ").lower()
    if result == "n" or result == "no":
        retry = False
        print("Goodbye!")
