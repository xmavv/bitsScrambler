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

#001110000111110001101011000000001010110111000000001010111110000000000111111010100000001010101111100000111111110000010110101010101010101100000000111111111
bitsToScramble = "001110000111110001101011000000001010110111000000001010111110000000000111111010100000001010101111100000111111110000010110101010101010101100000000111111111"
                 #00111000011111000110101100000010101101110000000011101100000011011001011001001111101011111000000011111111000000001101001110101010101100000000111111111
#Wyświetl symulację wystąpienia desynchronizacji bez użycia scramblera
toScramble = countRepetitions(bitsToScramble)
print("\nPierwotna sekwencja: \n",Fore.CYAN + bitsToScramble)
print(Fore.MAGENTA + "     Symulacja przesylania danych bez scramblingu    ")
disturbedSeq = countProbabilityNew(bitsToScramble)

plt.bar(list(toScramble.values()), toScramble.keys(), color='g')
plt.yticks(np.arange(min(toScramble.keys()),max(toScramble.keys())+1,1))
plt.xticks(np.arange(0,max(toScramble.values())+1,1))
plt.xlabel("Ilość wystąpień długości danej sekwencji")
plt.ylabel("Długość danej sekwencji zer")
plt.title("Histogram wystąpień sekwencji zer | Przed scramblowaniem")
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
#Wyświetl symulację desynchronizacji dla ciągu bitów z użyciem Scramblingu
print(Fore.MAGENTA + "     Symulacja przesylania danych przy uzyciu scramblingu    ")
print("Sekwencja poddana scramblingowi: ",Fore.CYAN + strScrambledBits)
scrambled = countRepetitions(strScrambledBits)
disturbedSeqScr = countProbabilityNew(strScrambledBits)
plt.bar(list(scrambled.values()), scrambled.keys(), color='g')
plt.yticks(np.arange(min(scrambled.keys()),max(scrambled.keys())+1,1))
plt.xticks(np.arange(0,max(scrambled.values())+1,1))
plt.xlabel("Ilość wystąpień długości danej sekwencji")
plt.ylabel("Długość danej sekwencji zer")
plt.title("Histogram wystąpień sekwencji zer | Po scramblowaniu")
plt.show()


