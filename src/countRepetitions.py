import numpy as np
import matplotlib.pyplot as plt

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

dictionary = countRepetitions("001110000111110001101011010101101110000000000001010111111111110101010101011111111111110000000101101010101010101011111111111")

plt.bar(list(dictionary.keys()), dictionary.values(), color='g')
plt.show()
