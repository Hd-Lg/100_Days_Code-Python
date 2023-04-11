alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):
    raw_text = ''
    if direction == 'decode':
        shift *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            raw_text += alphabet[new_position]
        else:
            raw_text += char

    print(f"The {direction}d text is {raw_text}")


run = True
while run == True:
    direction = input('Type "encode" to encrypt, type "decode" to decrypt:\n')
    text = input('Type your message:\n').lower()
    shift = int(input('Type the shift number:\n'))

    shift = shift % 26

    caesar(text, shift, direction)

    run_again = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if run_again == 'no':
        run = False
        print("Goodbye!")
