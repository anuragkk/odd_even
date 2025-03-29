alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
             'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
             'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

print("Welcome to ceaser_cypher")
word = input("please enter the word\n").upper()
encrypt_or_decrypt = input("please select if you like to encrypt or decrypt\n ").lower()
shift_amount = int(input("what is the shift amount \n"))


def ceaser_cypher(input_word, shift, mode):
    result_text = ""
    if mode == "decrypt":
        shift = -shift

    for letter in input_word:
        if letter in alphabets:
            index = alphabets.index(letter)
            new_index = (index + shift) % 26
            result_text += alphabets[new_index]
        else:
            result_text += letter
    return result_text


result = ceaser_cypher(input_word=word, shift=shift_amount, mode=encrypt_or_decrypt)

print(f"{encrypt_or_decrypt.capitalize()}ed word: {result}")
