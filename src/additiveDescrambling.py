# ogólnie jest ponownie przepisana funckja xor_strings tutaj
# może powinniśmy to umieścić jeszcze w jakimś osobnym pliku żeby scrambling i descrambling z tego korzystał
def xor_strings(bit_string1, bit_string2):
    result = []
    for i in range(len(bit_string1)):
        xor_result = str(int(bit_string1[i]) ^ int(bit_string2[i]))
        result.append(xor_result)

    return ''.join(result)


def descramble_bits(scrambled_bit_string, random_sequence):
    descrambled_bits = xor_strings(scrambled_bit_string, random_sequence)
    return descrambled_bits
