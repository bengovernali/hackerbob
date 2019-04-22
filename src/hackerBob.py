user_password = input('Please enter a password: ')
hash = 'apfhtr'
rotate_by = 13

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encode_password(password):
    i = 0
    encoded_password = ''
    while i < len(password):
        letter = password[i]
        i += 1
        index_in_alphabet = alphabet.index(letter)
        new_index = index_in_alphabet + rotate_by
        if new_index >= len(alphabet):
            new_index -= len(alphabet)
        encoded_password += alphabet[new_index]
    return encoded_password


def crack_password(enc_password, user_password):
    i = 0
    for char in hash:
        if char == enc_password[i]:
            print("%s is the correct character for index %d" % (user_password[i], i))
        else:
            print("%s is the incorrect character for index %d" % (user_password[i], i))
        i += 1


crack_password(encode_password(user_password), user_password)
