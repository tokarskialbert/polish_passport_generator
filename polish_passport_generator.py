from random import *

def polish_passport():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    letters_as_numbers = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32,
                          33, 34, 35]
    before_check_nr_weights = [7, 3, 1, 7, 3, 1, 7, 3]
    check_number_weight = 9

    polish_passport_arr = []
    elements_value = []
    checksum = 0

    i = 0
    while i < 2:
        random_int = randrange(0, 25)
        letter = letters[random_int]
        letter_as_number = letters_as_numbers[random_int]
        polish_passport_arr.append(letter)
        elements_value.append(letter_as_number)
        i += 1

    i = 0
    while i < 6:
        random_int = randrange(9)
        polish_passport_arr.append(random_int)
        elements_value.append(random_int)
        i += 1

    i = 0
    while i < 8:
        checksum += (elements_value[i] * before_check_nr_weights[i])
        print(checksum)
        i += 1

    check_number = checksum % 10
    polish_passport_arr.insert(2, check_number)
    checksum += (check_number * check_number_weight)

    print("***")
    print("nr:")
    print(polish_passport_arr)
    print("elements value")
    print(elements_value)
    print("before check nr weights")
    print(before_check_nr_weights)
    print("check nr ", check_number)
    print("checksum ", checksum)


