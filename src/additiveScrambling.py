import random
from fromFileToBit import wav_to_bytes, mp3_to_bytes, bytes_to_bits

# funkcja generująca losowy ciąg bitów o długości ciągu wejściowego
def generate_sequence(length):
    sequence = ''.join(random.choice(['0', '1']) for _ in range(length))
    print("Pierwsze 100 bitów ciągu pseudolosowego:", sequence[:100])
    return sequence

# funckja wykonująca operację xor na dwóch ciągach bitów
def xor_bit_strings(bit_string1, bit_string2):
    return ''.join('1' if b1 != b2 else '0' for b1, b2 in zip(bit_string1, bit_string2))

# funkcja wykonująca addytwną metodę scramblingu
def scramble_bits(bit_string):
    pseudorandom_sequence = generate_sequence(len(bit_string))
    scrambled_bits = xor_bit_strings(bit_string, pseudorandom_sequence)
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
scrambled_bit_string = scramble_bits(bit_string)

# wyniki
print("Oryginalny ciąg bitów:", bit_string[:100], "...")  # pokaż pierwsze 100 bitów ciągu wejściowego
print("Scrambled ciąg bitów:", scrambled_bit_string[:100], "...") # pokaż pierwsze 100 bitów ciągu wyjściowego
