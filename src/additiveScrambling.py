import random
from additiveDescrambling import descramble_bits


# I metoda generowania - funkcja generująca losowy ciąg bitów o długości ciągu wejściowego
def generate_sequence(length):
    sequence = ''.join(random.choice(['0', '1']) for _ in range(length))
    return sequence

# II metoda generowania - generowanie ciągu z rejestru
def generate_lfsr_sequence(initial_state):
    register = list(initial_state)  # generujemy rejestr z początkowym stanem initial_state
    generated_sequence = []  # tablica wynikowa

    # generowanie ciągu za pomocą rejestru przesuwającego o długości bit_string
    for i in range(len(bit_string)):

        new_bit = register[0]^register[2]  # xor na określonych indeksach rejestru
        generated_sequence.append(str(new_bit))  # dodanie bitu do nowego ciągu
        register = [new_bit] + register[:-1]  # przesunięcie rejestru w prawo oraz dodanie nowego bitu z przodu

    return ''.join(generated_sequence)

# funckja wykonująca operację xor na dwóch ciągach bitów
def xor_strings(bit_string1, bit_string2):
    result = []
    for i in range(len(bit_string1)):
        xor_result = str(int(bit_string1[i]) ^ int(bit_string2[i]))
        result.append(xor_result)

    return ''.join(result)


def scramble_bits(bit_string, random_sequence):
    scrambled_bits = xor_strings(bit_string, random_sequence)
    return scrambled_bits

# przykładowy ciąg do testów
bit_string = "0100001101111000101011100101010001101010001010111111000101010"

print("\nI METODA - random")
print("\nOryginalny ciąg bitów:                   ", bit_string)
# generowanie ciągu losowego
random_sequence = generate_sequence(len(bit_string))
print("Ciąg losowy (random):                    ", random_sequence)
# scramblowanie
scrambled_bit_string = scramble_bits(bit_string, random_sequence)
# descramblowanie
descrambled_bit_string = descramble_bits(scrambled_bit_string, random_sequence)
# wyniki
print("Ciąg bitów po scramblingu (random):      ", scrambled_bit_string) # pokaż pierwsze 100 bitów ciągu wyjściowego
print("Ciąg bitów po descramblingu (random):    ", descrambled_bit_string) # pierwsze 100 bitów po descramblingu


print("\nII METODA - LFSR")
print("\nOryginalny ciąg bitów:                   ", bit_string)
# stan początkowy dla LFSR
initial_register = [1, 0, 0]
# generowanie ciągu z rejestru
lfsr_sequence = generate_lfsr_sequence(initial_register)
print("Ciąg z rejestru (LFSR):                  ", lfsr_sequence)
# scramblowanie
lfsr_scrambled_bit_string = scramble_bits(bit_string, lfsr_sequence)  # Scramblowanie z LFSR
# descramblowanie
descrambled_bit_string_lfsr = descramble_bits(lfsr_scrambled_bit_string, lfsr_sequence)
# wyniki
print("Ciąg bitów po scramblingu (LFSR):        ", lfsr_scrambled_bit_string)
print("Ciąg bitów po descramblingu (LFSR):      ", descrambled_bit_string_lfsr)
