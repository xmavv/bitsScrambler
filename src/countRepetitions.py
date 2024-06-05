
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

MIN_DISTURBED_BITS = 5

def countPropability(totalBits,countRep):
    maxRep = max(countRep.keys())
    disturbedBits = 0;
    for i in range(MIN_DISTURBED_BITS,maxRep):
        if i in countRep.keys():
            disturbedBits += (i - MIN_DISTURBED_BITS - 1)*countRep[i]

    return round((disturbedBits/totalBits * 100),2) #result in %

# sequence = "001110000111110001101011010101101110000000000001010111111111110101010101011111111111110000000101101010101010101011111111111"
# countRep = countRepetitions(sequence)
#
# print(countPropability(len(sequence),countRep))