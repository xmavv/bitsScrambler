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
