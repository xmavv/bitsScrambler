def hexToBinary(hex_string):
    #na obiekt bytes z hexadecymalnego
    bytes_data = bytes.fromhex(hex_string)
    #z bytes na inta
    integer_value = int.from_bytes(bytes_data, byteorder='big')
    #z inta na liczbe dwojkowa
    binary_string = bin(integer_value)[2:]  # pomijamy prefix '0b'
    return binary_string

def binaryToHex(binary_string):
    # Konwertujemy ciąg znaków binarnych na liczbę całkowitą
    integer_value = int(binary_string, 2)
    # Konwertujemy liczbę całkowitą na ciąg szesnastkowy (hexadecimal)
    hex_string = hex(integer_value)[2:]  # Pomijamy prefix '0x'
    return hex_string