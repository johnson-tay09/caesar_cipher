# def encrypt(text, shift):
#     # make shift loop back around after 26 shifts.
#     if shift > 26:
#         shift = shift % 26
#     if shift < 1:
#         shift = 26 + shift
#     text = text.lower().replace(" ", "")
#     return "".join(chr(ord(char) + shift) for char in text)


# def decrypt(text, shift):
#     encrypt(text, shift * -1)


# print(encrypt("abc", -2))

letters = "abcdefghijklmnopqrstuvwxyz"


def get_cipherletter(new_shift, letter):

    if letter in letters:
        return letters[new_shift]
    else:
        return letter


def encrypt(shift, message):
    message = message.lower()
    result = ""

    for letter in message:
        new_shift = (letters.find(letter) + shift) % len(letters)
        result = result + get_cipherletter(new_shift, letter)

    return result


def decrypt(shift, message):
    message = message.lower()
    result = ""

    for letter in message:
        new_shift = (letters.find(letter) - shift) % len(letters)
        result = result + get_cipherletter(new_shift, letter)

    return result


print(encrypt(1, "abc"))
print(decrypt(1, "bcd"))