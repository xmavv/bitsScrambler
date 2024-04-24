
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

bitsToDescramble = "10110001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011"
multiplicativeBits = [2,4] #To trzeba znać do descramblingu
register = ['0','0','0','0','0'] #wyzerowany rejestr przed startem

descrambledBits = ''

for bit in bitsToDescramble:
    xorA = xorBits(register[multiplicativeBits[0]], register[multiplicativeBits[1]])  # xorujemy bity w rejestrze na pozycjach zapisanych w multiplicativeBits
    xorB = xorBits(xorA, bit)  # xorujemy wynik pierwszego xorowania i kolejnego bitu do zakodowania

    print("Reg: ", register, "   ", "bit: ", bit, "  ", "xorA: ", xorA, "    ", "xorB=output: ", xorB)
    descrambledBits += xorB  # xorB to tez output
    register = moveRegister(bit,register)  # przesuwamy rejestr i dodajemy na początek rejestru bit, który wprowadziliśmy

print(descrambledBits)