import random
from additiveDescrambling import descramble_bits


# funkcja generująca losowy ciąg bitów o długości ciągu wejściowego
def generate_sequence(length):
    sequence = ''.join(random.choice(['0', '1']) for _ in range(length))
    print("Ciąg losowy:                 ", sequence)
    return sequence


# funckja wykonująca operację xor na dwóch ciągach bitów
def xor_strings(bit_string1, bit_string2):
    result = []
    for i in range(len(bit_string1)):
        xor_result = str(int(bit_string1[i]) ^ int(bit_string2[i]))
        result.append(xor_result)

    return ''.join(result)


def scramble_bits(bit_string):
    random_sequence = generate_sequence(len(bit_string))
    scrambled_bits = xor_strings(bit_string, random_sequence)
    return scrambled_bits, random_sequence

# konwersja bajtów na bity i scramblowanie
bit_string = "0100001101111000101011100101010001101010001010111111000101010"
scrambled_bit_string, random_sequence = scramble_bits(bit_string)

# descramblowanie
descrambled_bit_string = descramble_bits(scrambled_bit_string, random_sequence)

# wyniki
print("Oryginalny ciąg bitów:       ", bit_string)  # pokaż pierwsze 100 bitów ciągu wejściowego
print("Ciąg bitów po scramblingu:   ", scrambled_bit_string) # pokaż pierwsze 100 bitów ciągu wyjściowego
print("Ciąg bitów po descramblingu: ", descrambled_bit_string) # pierwsze 100 bitów po descramblingu
