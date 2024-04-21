import random
from fromFileToBit import wav_to_bytes, mp3_to_bytes, bytes_to_bits

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

# tu można dodać ścieżkę do pliku audio
file_path = '../samples/input/wow.wav'
# file_path = '../samples/wow.mp3'

# wybór odpowiedniej funkcji konwersji na podstawie rozszerzenia pliku
if file_path.endswith('.wav'):
    audio_bytes = wav_to_bytes(file_path)
elif file_path.endswith('.mp3'):
    audio_bytes = mp3_to_bytes(file_path)
else:
    raise ValueError("Niewspierany format pliku")



#konwersja bajtów na bity i scramblowanie
bit_string = bytes_to_bits(audio_bytes)
bits_key = generate_sequence(len(bit_string))
print("Klucz szyfrowania: ",bits_key[:100])
#take_first_100 = bit_string[:100]
# bit_string = '010101010'
scrambled_bit_string = scramble_bits(bit_string)


print("Oryginalny ciąg bitów:", bit_string[:100])  # pokaż pierwsze 100 bitów ciągu wejściowego
print("Scrambled ciąg bitów:", scrambled_bit_string[:100]) # pokaż pierwsze 100 bitów ciągu wyjściowego


def subtract_binary(bin1, bin2):
    # Uzyskaj długość obu liczb binarnych
    len1 = len(bin1)
    len2 = len(bin2)

    # Uzyskaj maksymalną długość dla wyniku
    max_len = max(len1, len2)

    # Uzupełnij liczby zerami z lewej strony, jeśli są krótsze niż maksymalna długość
    bin1 = bin1.zfill(max_len)
    bin2 = bin2.zfill(max_len)

    # Przekształć ciągi binarne w listy intów
    num1 = [int(x) for x in bin1]
    num2 = [int(x) for x in bin2]

    # Odejmowanie binarne
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

    # Jeśli jest zapożyczenie na najbardziej znaczącym bicie, oznacza to, że wynik jest ujemny
    if borrow == 1:
        return "Wynik ujemny, nie można odejmować."

    # Usuń wiodące zera z wyniku
    result = ''.join(map(str, result))

    # Jeśli wynik jest pusty (0), zwróć 0
    if not result:
        return "0"

    return result




#   TESTOWANIE KODOWANIA I DEKODOWANIA
#KODOWANIE
binary_num1 = '00000000000010100101101001' #CIĄG DO SCRAMBLINGU
binary_num2 = '11010010101110100001111000' # KLUCZ
result = binary_addition(binary_num1, binary_num2)
print("Wynik dodawania:", result)
print()
#DEKODOWANIE I PORÓWNANIE
print("Wynik odejmowania:", subtract_binary(result, binary_num2))
print("Ciąg do scramblingu:", binary_num1)
