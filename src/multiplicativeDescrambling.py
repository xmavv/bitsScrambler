def subtract_binary(bin1, bin2):
    len1 = len(bin1)
    len2 = len(bin2)

    max_len = max(len1, len2)

    #uzupelnia zerami gdyby ciagi mialy rozna dlugosc
    bin1 = bin1.zfill(max_len)
    bin2 = bin2.zfill(max_len)

    num1 = [int(x) for x in bin1]
    num2 = [int(x) for x in bin2]

    result = []
    borrow = 0

    for i in range(max_len - 1, -1, -1):
        diff = num1[i] - num2[i] - borrow

        if diff < 0:
            diff += 2
            borrow = 1
        else:
            borrow = 0

        result.insert(0, diff)

    # jesli jest zapozyczenie na najbardziej znaczacym bicie, oznacza to, że wynik jest ujemny
    if borrow == 1:
        return "Wynik ujemny, nie można odejmować."

    result = ''.join(map(str, result))

    # jak wynik jest pusty (0), zwróć 0
    if not result:
        return "0"

    return result

def descramble_bits(scrambled_bits_string, bits_key):
    result = subtract_binary(scrambled_bits_string, bits_key)
    return result