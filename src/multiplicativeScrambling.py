import wave

file_path = '../samples/input/wow.wav'


def hex_to_binary(hex_string):
    # Konwertujemy łańcuch szesnastkowy na bajty
    bytes_data = bytes.fromhex(hex_string)
    # Konwertujemy bajty na liczbę całkowitą
    integer_value = int.from_bytes(bytes_data, byteorder='big')
    # Konwertujemy liczbę całkowitą na ciąg znaków binarnych
    binary_string = bin(integer_value)[2:]  # Pomijamy prefix '0b'
    return binary_string

# load wav file
def load_wav_file():
    with wave.open(file_path, 'rb') as wav_file:
        # parameters
        print("Liczba kanałów:", wav_file.getnchannels())
        print("Szerokość próbki (w bajtach):", wav_file.getsampwidth())
        print("Częstotliwość próbkowania:", wav_file.getframerate())
        print("Liczba ramek:", wav_file.getnframes())
        print("Typ kompresji:", wav_file.getcomptype())
        print("Kompresja:", wav_file.getcompname())
        return hex_to_binary(wav_file.readframes(wav_file.getnframes()).hex())


# save to the new WAV file
def create_wav_file(data, channels=1, sample_width=2, frame_rate=44100, file_path='sratatatata2222222222222222222222.wav'):
    with wave.open(file_path, 'wb') as wav_file:
        wav_file.setnchannels(channels)
        wav_file.setsampwidth(sample_width)
        wav_file.setframerate(frame_rate)
        wav_file.writeframes(data)  # actually save


def bytes_to_bits(byte_string):
    bits = []
    for byte in byte_string:
        bits.append(format(byte, '08b'))  # byte to bit, uzupelnia do 8 bitow w kazdej sekwencji
    return ''.join(bits)


CIAG_BITOW = load_wav_file()  # to jest szesnastkowo tutaj bo lepiej to widac


# np. xff oznacza po prostu zapis szesnastkowy FF, czyli 1111 1111

# example_data = b'\x00\x01\x02\x03\x04\x05'
# create_wav_file(example_data)

def moveRegister(newBit, _register):
    for i in range(len(_register) - 2, -1, -1):
        _register[i + 1] = _register[i]
    _register[0] = newBit
    return _register


def xorBits(bit1, bit2):
    if bit1 == bit2:
        return '0'
    return '1'


bitsToScramble = CIAG_BITOW
multiplicativeBits = [2, 4]  #Na tych dwóch pozycjach w rejestze xorujemy bity (licz od 0)
register = ['0', '0', '0', '0', '0']  #wyzerowany rejestr przed startem

scrambledBits = ''

#Zobaczyć rysunek żeby ogarnąć o co chodzi
licznik = 0
for bit in bitsToScramble:
    print('scramblowanie    ', licznik / len(bitsToScramble))
    licznik += 1
    xorA = xorBits(register[multiplicativeBits[0]], register[
        multiplicativeBits[1]])  #xorujemy bity w rejestrze na pozycjach zapisanych w multiplicativeBits
    xorB = xorBits(xorA, bit)  #xorujemy wynik pierwszego xorowania i kolejnego bitu do zakodowania

    # print("Reg: ",register,"   ","bit: ",bit,"  ", "xorA: ", xorA, "    ", "xorB=output: ", xorB)
    scrambledBits += xorB  #xorB to tez output
    register = moveRegister(bit,
                            register)  #przesuwamy rejestr i dodajemy na początek rejestru bit, który wprowadziliśmy
    # print(register)


# print(scrambledBits)


#Funkcja do przesuwania wszystkich bitów w prawo w rejestrze i dodawanie nowego bitu na początek
def moveRegister(newBit, _register):
    for i in range(len(_register) - 2, -1, -1):
        _register[i + 1] = _register[i]
    _register[0] = newBit
    return _register


def xorBits(bit1, bit2):
    if bit1 == bit2:
        return '0'
    return '1'


bitsToDescramble = scrambledBits
multiplicativeBits = [2, 4]  #To trzeba znać do descramblingu
register = ['0', '0', '0', '0', '0']  #wyzerowany rejestr przed startem

descrambledBits = ''
licznik = 0
for bit in bitsToDescramble:
    xorA = xorBits(register[multiplicativeBits[0]], register[
        multiplicativeBits[1]])  # xorujemy bity w rejestrze na pozycjach zapisanych w multiplicativeBits
    xorB = xorBits(xorA, bit)  # xorujemy wynik pierwszego xorowania i kolejnego bitu do zakodowania
    print('descramblowanie    ', licznik / len(bitsToScramble))
    licznik += 1
    # print("Reg: ", register, "   ", "bit: ", bit, "  ", "xorA: ", xorA, "    ", "xorB=output: ", xorB)
    descrambledBits += xorB  # xorB to tez output
    register = moveRegister(bit,
                            register)  # przesuwamy rejestr i dodajemy na początek rejestru bit, który wprowadziliśmy


# print(descrambledBits)

def binary_to_hex(binary_string):
    # Konwertujemy ciąg znaków binarnych na liczbę całkowitą
    integer_value = int(binary_string, 2)
    # Konwertujemy liczbę całkowitą na ciąg szesnastkowy (hexadecimal)
    hex_string = hex(integer_value)[2:]  # Pomijamy prefix '0x'
    return hex_string


finalBits = binary_to_hex(descrambledBits)
finalByesObject = bytes.fromhex(finalBits)

create_wav_file(finalByesObject)

# Assume 'audio_bytes' is a bytes object with your raw audio data
