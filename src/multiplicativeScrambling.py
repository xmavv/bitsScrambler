import random
from fromFileToBit import bytes_to_bits

def generate_sequence(length):
    sequence = ''.join(random.choice(['0', '1']) for _ in range(length))
    return sequence


def binary_addition(binary_num1, binary_num2):
    """
    Funkcja dodająca dwie liczby binarne.

    Args:
    binary_num1 (str): Pierwsza liczba binarna.
    binary_num2 (str): Druga liczba binarna.

    Returns:
    str: Wynik dodawania w postaci binarnej.
    """
    result = ''
    carry = 0

    for i in range(len(binary_num1) - 1, -1, -1):
        if i >= len(binary_num1) - len(binary_num2):
            j = i - (len(binary_num1) - len(binary_num2))
            temp_sum = int(binary_num1[i]) + int(binary_num2[j]) + carry
        else:
            temp_sum = int(binary_num1[i]) + carry

        result = str(temp_sum % 2) + result
        carry = temp_sum // 2

    if carry:
        result = '1' + result

    return result

def scramble_bits(bit_string, bits_key):
    scrambled_bits = binary_addition(bit_string, bits_key)
    return scrambled_bits

#konwersja bajtów na bity i scramblowanie
bit_string = "010101010111111000010101000000010101111100000011101010100"
bits_key = generate_sequence(len(bit_string))
#print("Klucz szyfrowania: ",bits_key[:100])
#take_first_100 = bit_string[:100]
# bit_string = '010101010'
#scrambled_bit_string = scramble_bits(bit_string, bits_key)


#print("Oryginalny ciąg bitów:", bit_string[:100])  # pokaż pierwsze 100 bitów ciągu wejściowego
#print("Scrambled ciąg bitów:", scrambled_bit_string[:100]) # pokaż pierwsze 100 bitów ciągu wyjściowego


def subtract_binary(bin1, bin2):
    len1 = len(bin1)
    len2 = len(bin2)

    max_len = max(len1, len2)

    bin1 = bin1.zfill(max_len)
    bin2 = bin2.zfill(max_len)

    num1 = [int(x) for x in bin1]
    num2 = [int(x) for x in bin2]

    result = []
    borrow = 0

    for i in range(max_len - 1, -1, -1):
        diff = num1[i] - num2[i] - borrow

        if diff < 0:
            diff += 2
            borrow = 1
        else:
            borrow = 0

        result.insert(0, diff)

    if borrow == 1:
        return "Wynik ujemny, nie można odejmować."

    result = ''.join(map(str, result))

    if not result:
        return "0"

    return result




#   TESTOWANIE KODOWANIA I DEKODOWANIA
#KODOWANIE
binary_num1 = '00000000000010100101101001' #CIĄG DO SCRAMBLINGU
binary_num2 = '11010010101110100001111000' # KLUCZ
result = binary_addition(binary_num1, binary_num2)
print("Wynik kodowania:", result)
print()
#DEKODOWANIE I PORÓWNANIE
print("Wynik dekodowania:", subtract_binary(result, binary_num2))
print("Ciąg do scramblingu:", binary_num1)
