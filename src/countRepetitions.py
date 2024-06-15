from config import *
import random

def generate_sequence(length):
    sequence = ''.join(random.choice(['0', '1']) for _ in range(length))
    return sequence

def countRepetitions(sequence):
    count = 1
    countRep = {}
    sequence = sequence + 'x'
    for i in range(len(sequence)-1):
        if sequence[i] == sequence[i + 1]:
            count += 1
        else:
            if not (count in countRep):
                countRep[count] = 1
            else:
                countRep[count] = countRep[count] + 1
            count = 1
    return countRep


sequence = "001110000111110001101011010101101110000000000001010111111111110101010101011111111111110000000101101010101010101011111111111000000"

def simulateHitOrMiss(propability):
    rand = random.random() #Generowanie losowej flaot liczby z przedziału 0 - 1
    if (rand < propability):
        return True
    return False

def countProbabilityNew(bits):
    packets = [] #pakiety danych, między którymi następuje synchronizacja
    #Tworzenie pakietów
    for i in range(0,len(bits) - PACKET_LEN ,PACKET_LEN):
        packet = bits[i: i + PACKET_LEN]
        packets.append(packet)
    packet = bits[len(packets)*PACKET_LEN::]    #ostatni pakiet
    packets.append(packet)
    #Sprawdzanie czy może wystąpić desynchronizacja bitów w każdym pakiecie
    disturbedBits = 0
    print("Pakiety: ",packets)
    for packet in packets:
        zeroSequenceCounter = 1
        disturbBits = False
        anySequences = False
        print("Pakiet: ",packet)
        for i in range(len(packet)-1):
            if packet[i] == packet[i+1] and packet[i] == '0':
                zeroSequenceCounter += 1
            elif zeroSequenceCounter >= MIN_DISTURBED_BITS:
                anySequences = True
                print("Znaleziono sekwencje zer o dlugosci: ",zeroSequenceCounter)
                #Jeśli długość sekwencji jest większa niż zakładane długości w tablicy prawdopodobieństwa to ustalamy, że na pewno wystąpi desynchronizacja
                if zeroSequenceCounter > len(PROPABILITY_OF_DISRUPTION) + MIN_DISTURBED_BITS:
                    disturbBits = True
                    print("Sekwencja jest bardzo dluga i na pewno wystapi desynchronizacja")
                #Jeśli długość sekwencji jest w tablicy prawdopodobieństwa to losujemy trafienie lub pudło dotyczące wystąpienia desynchronizacji
                else:
                    propability = PROPABILITY_OF_DISRUPTION[zeroSequenceCounter - MIN_DISTURBED_BITS] #Pobranie prawd. dla danej dlugosci sekwencji
                    disturbBits = simulateHitOrMiss(propability)    #Losowanie wystapienia desynchronizacji danych
                    zeroSequenceCounter = 1
                    print("Prawdopodobienstwo desynchronizacji to: ",propability)
                    print("Czy wystapila desynchronizacja: ",disturbBits)
            else:
                zeroSequenceCounter = 1

            if (disturbBits):
                noise = len(packet) - i - 1
                print("Powstal szum o dlugosci ", noise, " bitow")
                disturbedBits += noise
                break
        if not anySequences:
            print("Brak sekwencji zer, ktore moga spowodowac desynchronizacje")

    return disturbedBits

#randomSequence = generate_sequence(200)

#total = countPropabilityNew(randomSequence)
#print(total)


