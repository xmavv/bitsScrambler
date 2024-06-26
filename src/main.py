from countRepetitions import countRepetitions, simulateTransfer
from convertingFiles import loadWavFile, createWavFile
from convertingSystem import binaryToHex
from multiplicativeScrambling import multiplicativeDescrambling, multiplicativeScrambling
from Histogram import showHistogram

fileName = 'wow'

CIAG_BITOW, settings = loadWavFile(fileName)

#PRZED SCRAMBLOWANIEM
bitsToScramble = CIAG_BITOW
toScramble = countRepetitions(bitsToScramble)
#disturbedSequenceNoScrambling = simulateTransfer(bitsToScramble)  #Sekwencja z szumem bez użycia scramblera
showHistogram(toScramble.keys(), toScramble.values(), 1, False)

#SCRAMBLOWANIE
multiplicativeBits = [9, 15]  #Na tych dwóch pozycjach w rejestze xorujemy bity (licz od 0)
register = ['1', '1', '0', '0', '1', '0', '1', '0', '0', '0', '1', '1', '0', '0', '0', '1']
scrambledBits = multiplicativeScrambling(bitsToScramble, multiplicativeBits, register)
scrambled = countRepetitions(scrambledBits)    #Słownik z długościami sekwencji zer po scramblowaniu
disturbedScrambledSequence = simulateTransfer(scrambledBits)   #Sekwencja z szumem z użyciem scramblera TRZEBA TO DESCRAMBLOWAĆ
showHistogram(scrambled.keys(), scrambled.values(), 10, True)

#DESCRAMBLOWANIE
bitsToDescramble = scrambledBits #descramblowanie sekwencji bez szumu
# bitsToDescramble = disturbedScrambledSequence  #descramblowanie sekwencji z szumem
multiplicativeBits = [9, 15]  #to trzeba znać do descramblingu
register = ['1', '1', '0', '0', '1', '0', '1', '0', '0', '0', '1', '1', '0', '0', '0', '1']
descrambledBits = multiplicativeDescrambling(bitsToDescramble, multiplicativeBits, register)

finalBits = binaryToHex(descrambledBits)
finalByesObject = bytes.fromhex(finalBits)

createWavFile(finalByesObject, settings.numberOfChannels, settings.sampWidth, settings.framerate, fileName)

#1. Plik oryginalny
#2. Plik oryginalny z szumem
#3. Plik scramblowany z szumem/bez
#4. Plik descramblowany z szumem/bez