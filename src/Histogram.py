import numpy as np
import matplotlib.pyplot as plt

def showHistogram(x, y, gap, isScrambled):
    plt.bar(list(x), y, color='g')
    plt.xticks(np.arange(0, max(x) + gap, 10))
    plt.yscale("log")
    plt.ylabel("Ilość wystąpień długości danej sekwencji")
    plt.xlabel("Długość danej sekwencji zer")

    if isScrambled:
        plt.title("Histogram wystąpień sekwencji zer | Po scramblowaniu")
    else:
        plt.title("Histogram wystąpień sekwencji zer | Przed scramblowaniem")

    plt.show()