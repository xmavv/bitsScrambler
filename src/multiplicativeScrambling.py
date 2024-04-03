import random
from fromFileToBit import wav_to_bytes, mp3_to_bytes, bytes_to_bits

def generate_sequence(length):
    sequence = ''.join(random.choice(['0', '1']) for _ in range(length))
    return sequence


def binary_multiplication(binary_num1, binary_num2):
    """
    Funkcja mnożąca dwie liczby binarne.

    Args:
    binary_num1 (str): Pierwsza liczba binarna.
    binary_num2 (str): Druga liczba binarna.

    Returns:
    str: Wynik mnożenia w postaci binarnej.
    """
    result = '0' * (len(binary_num1) + len(binary_num2))  # Inicjalizacja wyniku jako ciąg zer

    for i in range(len(binary_num2) - 1, -1, -1):
        if binary_num2[i] == '1':
            result = binary_addition(result, binary_num1 + '0' * (len(binary_num2) - 1 - i))

    return result

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
        print(i)
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

def scramble_bits(bit_string):
    scrambled_bits = binary_addition(bit_string, bits_key)
    return scrambled_bits

# tu można dodać ścieżkę do pliku audio
file_path = '../samples/wow.wav'
# file_path = '../samples/wow.mp3'

# wybór odpowiedniej funkcji konwersji na podstawie rozszerzenia pliku
if file_path.endswith('.wav'):
    audio_bytes = wav_to_bytes(file_path)
elif file_path.endswith('.mp3'):
    audio_bytes = mp3_to_bytes(file_path)
else:
    raise ValueError("Niewspierany format pliku")



# konwersja bajtów na bity i scramblowanie
bit_string = bytes_to_bits(audio_bytes)
bits_key = generate_sequence(len(bit_string))
print("Klucz szyfrowania: ",bits_key[:100])
#take_first_100 = bit_string[:100]
# bit_string = '010101010'
scrambled_bit_string = scramble_bits(bit_string)


print("Oryginalny ciąg bitów:", bit_string[:100])  # pokaż pierwsze 100 bitów ciągu wejściowego
print("Scrambled ciąg bitów:", scrambled_bit_string[:100]) # pokaż pierwsze 100 bitów ciągu wyjściowego


#
# #Do testowania mnożenia dwóch ciągów bitów
# #Przykładowe dane wejściowe
# binary_num1 = '10100101101001' #CIĄG DO SCRAMBLINGU
# binary_num2 = '110100001111000' # KLUCZ
#
# # Wywołanie funkcji mnożenia
# result = binary_multiplication(binary_num1, binary_num2)
# print("Wynik mnożenia:", result)