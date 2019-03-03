import re


def get_value_from_letter(letter):
    return {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7,
        'i': 8,
        'j': 9,
        'k': 10,
        'l': 11,
        'm': 12,
        'n': 13,
        'o': 14,
        'p': 15,
        'q': 16,
        'r': 17,
        's': 18,
        't': 19,
        'u': 20,
        'v': 21,
        'w': 22,
        'x': 23,
        'y': 24,
        'z': 25
    }[letter]


def get_letter_from_value(number):
    return {
        0: 'a',
        1: 'b',
        2: 'c',
        3: 'd',
        4: 'e',
        5: 'f',
        6: 'g',
        7: 'h',
        8: 'i',
        9: 'j',
        10: 'k',
        11: 'l',
        12: 'm',
        13: 'n',
        14: 'o',
        15: 'p',
        16: 'q',
        17: 'r',
        18: 's',
        19: 't',
        20: 'u',
        21: 'v',
        22: 'w',
        23: 'x',
        24: 'y',
        25: 'z'
    }[number]


def affine_tester(message):
    """
    This function takes in a string to be encrypted  and formats the message.
    a and b are keys for the cipher
    The keys and message are passed to affine_cipher

    :param message:
    """
    a = 9
    b = 5
    msg = message_formatter(message)
    letter_frequency_analysis(affine_cipher(a, b, msg))


def message_formatter(string):
    """
    This function returns a formatted string where it becomes all lowercase without any other characters in between.

    :param string:
    :return string_to_return:
    """
    string = re.sub('[^0-9a-zA-Z]+', '', string)
    string_to_return = string.lower()
    return string_to_return


def affine_cipher(a, b, message):
    ciphertext = ""
    print("Original Message: ")
    print(message)
    print("\nEncrypting message with key (" + str(a) + ", " + str(b) + ")...\n")

    for letter in message:
        x = get_value_from_letter(letter)
        y = (a * x + b ) % 26

        ciphertext = ciphertext + get_letter_from_value(y)
    print("Resulting ciphertext:")
    print(ciphertext)
    return ciphertext


def letter_frequency_analysis(ciphertext):
    get_letter_count(ciphertext)


def get_letter_count(message):
    letter_count = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    for letter in message:
        letter_count[letter] += 1
    print(letter_count)



a = r"""
Swift is a fantastic way to write software, whether its for phones, desktops, servers, or anything else that runs code. Its a safe, fast, and interactive programming language that combines the best in modern language thinking with wisdom from the wider Apple engineering culture and the diverse contributions from its open-source community. The compiler is optimized for performance and the language is optimized for development, without compromising on either.

Swift is friendly to new programmers. Its an industrial-quality programming language thats as expressive and enjoyable as a scripting language. Writing Swift code in a playground lets you experiment with code and see the results immediately, without the overhead of building and running an app.

Swift defines away large classes of common programming errors by adopting modern programming pattern.
"""

affine_tester(a)




