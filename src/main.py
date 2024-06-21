import wave
import numpy as np
import matplotlib.pyplot as plt

from countRepetitions import countRepetitions, countProbabilityNew

file_name = 'wow'
file_path = '../samples/input/' + file_name + '.wav'

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
def create_wav_file(data, channels=1, sample_width=2, frame_rate=44100, file_path='../samples/output/' + file_name + '_output.wav'):
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
print(len(CIAG_BITOW))

# np. xff oznacza po prostu zapis szesnastkowy FF, czyli 1111 1111

def moveRegister(newBit, _register):
    for i in range(len(_register) - 2, -1, -1):
        _register[i + 1] = _register[i]
    _register[0] = newBit
    return _register


def xorBits(bit1, bit2):
    if bit1 == bit2:
        return '0'
    return '1'

#1. Plik oryginalny
#2. Plik oryginalny z szumem
#3. Plik scramblowany z szumem/bez
#4. Plik descramblowany z szumem/bez

bitsToScramble = CIAG_BITOW
toScramble = countRepetitions(bitsToScramble)
disturbedSequenceNoScrambling = countProbabilityNew(bitsToScramble)  #Sekwencja z szumem bez użycia scramblera

plt.bar(list(toScramble.keys()), toScramble.values(), color='g')
#plt.yticks(np.arange(min(toScramble.values()),max(toScramble.values())+1,1))
plt.xticks(np.arange(0,max(toScramble.keys())+1,10))
plt.yscale("log")
plt.ylabel("Ilość wystąpień długości danej sekwencji")
plt.xlabel("Długość danej sekwencji zer")
plt.title("Histogram wystąpień sekwencji zer | Przed scramblowaniem")
plt.show()

multiplicativeBits = [9, 15]  #Na tych dwóch pozycjach w rejestze xorujemy bity (licz od 0)
#register = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']  #wyzerowany rejestr przed startem
register = ['1', '1', '0', '0', '1', '0', '1', '0', '0', '0', '1', '1', '0', '0', '0', '1']
scrambledBits = []

#Zobaczyć rysunek żeby ogarnąć o co chodzi
for bit in bitsToScramble:
    xorA = xorBits(register[multiplicativeBits[0]], register[
        multiplicativeBits[1]])  #xorujemy bity w rejestrze na pozycjach zapisanych w multiplicativeBits
    xorB = xorBits(xorA, bit)  #xorujemy wynik pierwszego xorowania i kolejnego bitu do zakodowania

    scrambledBits.append(xorB)  # xorB to tez output
    register = moveRegister(xorB,
                            register)  #przesuwamy rejestr i dodajemy na początek rejestru bit, który wprowadziliśmy

scrambled = countRepetitions("".join(scrambledBits))    #Słownik z długościami sekwencji zer po scramblowaniu
disturbedSequenceScrambling = countProbabilityNew("".join(scrambledBits))   #Sekwencja z szumem z użyciem scramblera TRZEBA TO DESCRAMBLOWAĆ
# disturbedSeqScr = countProbabilityNew("".join(scrambledBits))
#plt.bar(list(scrambled.values()), scrambled.keys(), color='g') #STARE
plt.bar(list(scrambled.keys()), scrambled.values(), color='g')
#plt.yticks(np.arange(min(scrambled.keys()),max(scrambled.keys())+1,1))
#plt.xticks(np.arange(0,max(scrambled.values())+1,1))
plt.xticks(np.arange(0,max(toScramble.keys())+10,10))
plt.yscale("log")
plt.ylabel("Ilość wystąpień długości danej sekwencji")
plt.xlabel("Długość danej sekwencji zer")

plt.title("Histogram wystąpień sekwencji zer | Po scramblowaniu")
plt.show()

bitsToDescramble = "".join(scrambledBits)



#bitsToDescramble = disturbedSequenceScrambling  #descramblowanie sekwencji z szumem



multiplicativeBits = [9, 15]  #To trzeba znać do descramblingu
#register = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']  #wyzerowany rejestr przed startem
register = ['1', '1', '0', '0', '1', '0', '1', '0', '0', '0', '1', '1', '0', '0', '0', '1']
descrambledBits = []
for bit in bitsToDescramble:
    xorA = xorBits(register[multiplicativeBits[0]], register[
        multiplicativeBits[1]])  # xorujemy bity w rejestrze na pozycjach zapisanych w multiplicativeBits
    xorB = xorBits(xorA, bit)  # xorujemy wynik pierwszego xorowania i kolejnego bitu do zakodowania
    # print("Reg: ", register, "   ", "bit: ", bit, "  ", "xorA: ", xorA, "    ", "xorB=output: ", xorB)
    descrambledBits.append(xorB)  # xorB to tez output
    register = moveRegister(bit,
                            register)  # przesuwamy rejestr i dodajemy na początek rejestru bit, który wprowadziliśmy


def binary_to_hex(binary_string):
    # Konwertujemy ciąg znaków binarnych na liczbę całkowitą
    integer_value = int(binary_string, 2)
    # Konwertujemy liczbę całkowitą na ciąg szesnastkowy (hexadecimal)
    hex_string = hex(integer_value)[2:]  # Pomijamy prefix '0x'
    return hex_string

finalBits = binary_to_hex("".join(descrambledBits))
finalByesObject = bytes.fromhex(finalBits)

create_wav_file(finalByesObject)