
#Funkcja do przesuwania wszystkich bitów w prawo w rejestrze i dodawanie nowego bitu na początek
def moveRegister(newBit, _register):
    for i in range(len(_register)-2,-1,-1):
        _register[i +1] = _register[i]
    _register[0] = newBit
    return _register

def xorBits(bit1, bit2):
    if bit1 == bit2:
        return '0'
    return '1'

bitsToDescramble = "00111110010001101000111010100011110100111110001111001000110111010101111010001111001100000000000011100100101100101010101010101010101100111110110100110"
bitsWithNoise =    "00111110010001101000111010100011110100111110001111001000110111010101111010001111001100000000000011011011010101001100100010101010101100111110110100110"
#DANE DO DESCRAMBLINGU, muszą być takie same jak do scramblingu
multiplicativeBits = [2,4]
register = ['0','0','0','0','0']

descrambledBits = []    #Tablica do bitów po descramblingu

#Algorytm descramblingu. Zobaczyć rysunek
for bit in bitsWithNoise:
    xorA = xorBits(register[multiplicativeBits[0]], register[multiplicativeBits[1]])  # xorujemy bity w rejestrze na pozycjach zapisanych w multiplicativeBits
    xorB = xorBits(xorA, bit)  # xorujemy wynik pierwszego xorowania i kolejnego bitu do zakodowania

    print("Reg: ", register, "   ", "bit: ", bit, "  ", "xorA: ", xorA, "    ", "xorB=output: ", xorB)
    descrambledBits.append(xorB)  # xorB to tez output
    register = moveRegister(bit,register)  # przesuwamy rejestr i dodajemy na początek rejestru bit, który wprowadziliśmy

#Tworzenie stringa z tablicy bitów po descramblowaniu
strDescrambledBits = "".join(descrambledBits)
print("Sekwencja po descramblowaniu ",strDescrambledBits)