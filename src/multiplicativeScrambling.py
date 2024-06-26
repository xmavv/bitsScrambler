
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
def multiplicativeScrambling(bitsToScramble, key=None, register=None):
    if register is None:
        register = ['0', '0', '0', '0', '0']
    if key is None:
        key = [5, len(register)-1]

    scrambledBits = []

    for bit in bitsToScramble:
        xorA = xorBits(register[key[0]], register[key[1]])  # xorujemy bity w rejestrze na pozycjach zapisanych w multiplicativeBits
        xorB = xorBits(xorA, bit)  # xorujemy wynik pierwszego xorowania i kolejnego bitu do zakodowania

        scrambledBits.append(xorB)  # xorB to tez output
        register = moveRegister(xorB, register)  # przesuwamy rejestr i dodajemy na początek rejestru wynik z xorB

    return "".join(scrambledBits) #returning actual string with scrambled string bits

def multiplicativeDescrambling(bitsToDescramble, key=None, register=None):
    if register is None:
        register = ['0', '0', '0', '0', '0']
    if key is None:
        key = [5, len(register)-1]

    descrambledBits = []

    for bit in bitsToDescramble:
        xorA = xorBits(register[key[0]], register[key[1]])  # xorujemy bity w rejestrze na pozycjach zapisanych w multiplicativeBits
        xorB = xorBits(xorA, bit)  # xorujemy wynik pierwszego xorowania i kolejnego bitu do zakodowania

        descrambledBits.append(xorB)  # xorB to tez output
        register = moveRegister(bit, register)  # przesuwamy rejestr i dodajemy na początek rejestru bit, który wprowadziliśmy

    return "".join(descrambledBits) #returning actual string with descrambled bits data