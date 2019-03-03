import re
import operator

englishLetterFreqSorted = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z']

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
        y = (a * x + b) % 26
        ciphertext = ciphertext + get_letter_from_value(y)

    print("Resulting ciphertext:")
    print(ciphertext)
    return ciphertext


def letter_frequency_analysis(ciphertext):
    """
    This function take a ciphertext and tries to covert each letter in the ciphertext according to letter frequency.

    It then prints this conversion

    Example: if letter 'z' is most common in the cipher-text. Then 'z' is converted to letter 'e' because e is the most
    common letter in an English sentence.
    :param ciphertext:
    """
    sorted_cipher_list_letter_value = get_letter_count_dict(ciphertext)
    sorted_cipher_list_letter = [x[0] for x in sorted_cipher_list_letter_value]

    analysis_dictionary = dict(zip(sorted_cipher_list_letter, englishLetterFreqSorted))

    print(analysis_dictionary)

    result = ""

    for character in ciphertext:
        result = result + analysis_dictionary.__getitem__(character)
    print(result)


def get_letter_count_dict(message):
    """
    This function takes the original message and counts the letter frequency in the message.
        :return sorted_letter_cnt_dict as a dictionary
    """

    letter_count = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    for letter in message:
        letter_count[letter] += 1

    sorted_letter_cnt_dict = sorted(letter_count.items(), key=operator.itemgetter(1))
    sorted_letter_cnt_dict.reverse()

    return sorted_letter_cnt_dict


test_msg = r"""
A message is a discrete unit of communication intended by the source for consumption by some recipient or group of recipients. A message may be delivered by various means, including courier, telegraphy, carrier pigeon and electronic bus. A message can be the content of a broadcast.
"""
affine_tester(test_msg)




