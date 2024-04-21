
def moveRegister(newBit, _register):
    for i in range(len(_register)-2,-1,-1):
        _register[i +1] = _register[i]
    _register[0] = newBit
    return _register

def xorBits(bit1, bit2):
    if bit1 == bit2:
        return '0'
    return '1'

bitsToScramble = "110000101"
multiplicativeBits = [2,4] #Na tych dwóch pozycjach w rejestze xorujemy bity (licz od 0)
register = ['0','0','0','0','0'] #wyzerowany rejestr przed startem

scrambledBits = ''

#Zobaczyć rysunek żeby ogarnąć o co chodzi
for bit in bitsToScramble:
    xorA = xorBits(register[multiplicativeBits[0]],register[multiplicativeBits[1]]) #xorujemy bity w rejestrze na pozycjach zapisanych w multiplicativeBits
    xorB = xorBits(xorA, bit)   #xorujemy wynik pierwszego xorowania i kolejnego bitu do zakodowania

    print("Reg: ",register,"   ","bit: ",bit,"  ", "xorA: ", xorA, "    ", "xorB=output: ", xorB)
    scrambledBits += xorB #xorB to tez output
    register = moveRegister(bit,register) #przesuwamy rejestr i dodajemy na początek rejestru bit, który wprowadziliśmy
    # print(register)

print(scrambledBits)




