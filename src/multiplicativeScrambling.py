from countRepetitions import countRepetitions, countProbabilityNew
import numpy as np
import matplotlib.pyplot as plt
from colorama import Fore, Style, init
init(autoreset=True) #inicjalizacja biblioteki colorama do kolorowego tekstu


def moveRegister(newBit, _register):
    for i in range(len(_register)-2,-1,-1):
        _register[i +1] = _register[i]
    _register[0] = newBit
    return _register

def xorBits(bit1, bit2):
    if bit1 == bit2:
        return '0'
    return '1'

bitsToScramble = "00111000011111000110101100000010101101110000000010101111100000000001111110101010101011111000000011111111000000010110101010101010101100000000111111111"
                 #00111000011111000110101100000010101101110000000010101111100000000001111110101010101011111000000011000110111001001111011111111010101100000000111111111
#Wyświetl symulację wystąpienia desynchronizacji
toScramble = countRepetitions(bitsToScramble)
print("\nSekwencja przed scramblingiem: \n",Fore.CYAN + bitsToScramble)
print("Bity zaklocajace stanowia ", Fore.RED + str(countProbabilityNew(bitsToScramble)), " % calej dlugosci sekwencji")

plt.bar(list(toScramble.keys()), toScramble.values(), color='g')
plt.show()

#DANE DLA SCRAMBLINGU muszą być identyczne przy descramblingu
multiplicativeBits = [2,4] #Na tych dwóch pozycjach w rejestze xorujemy bity (licz od 0)
register = ['0','0','0','0','0'] #wyzerowany rejestr przed startem

scrambledBits = []      #tablica do bitów po scramblowaniu

#Algorytm scrmablingu multiplikatywnego. Zobaczyć rysunek żeby ogarnąć o co chodzi
for bit in bitsToScramble:
    xorA = xorBits(register[multiplicativeBits[0]],register[multiplicativeBits[1]]) #xorujemy bity w rejestrze na pozycjach zapisanych w multiplicativeBits
    xorB = xorBits(xorA, bit)   #xorujemy wynik pierwszego xorowania i kolejnego bitu do zakodowania

    #print("Reg: ",register,"   ","bit: ",bit,"  ", "xorA: ", xorA, "    ", "xorB=output: ", xorB)
    scrambledBits.append(xorB) #xorB to tez output
    register = moveRegister(xorB,register) #przesuwamy rejestr i dodajemy na początek rejestru wynik z xorB

#Tworzenie stringa z tablicy bitów po scramblowaniu
strScrambledBits = "".join(scrambledBits)
#Wyświetl symulację desynchronizacji dla ciągu bitów po scramblowaniu
scrambled = countRepetitions(strScrambledBits)
print("\nSekwencja po scramblingu \n",Fore.CYAN + strScrambledBits)
print("Bity zaklocajace stanowia ", Fore.RED  + str(countProbabilityNew(strScrambledBits)), " % calej dlugosci sekwencji")

plt.bar(list(scrambled.keys()), scrambled.values(), color='g')
plt.show()


