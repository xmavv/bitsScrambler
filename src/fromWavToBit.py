import wave

def wav_to_bytes(file_path):
    with wave.open(file_path, 'rb') as wave_file:
        #pobierz parametry .wav
        nchannels = wave_file.getnchannels()
        sampwidth = wave_file.getsampwidth()
        framerate = wave_file.getframerate()
        nframes = wave_file.getnframes()

        #odczytaj zawartosc .wav
        frames = wave_file.readframes(nframes)

    return frames

#path
wav_file_path = '../samples/wow.wav'

#conversion
audio_bytes = wav_to_bytes(wav_file_path)

def bytes_to_bits(byte_string):
    bits = []
    for byte in byte_string:
        bits.append(format(byte, '08b'))  #byte to bit, uzupelnia do 8 bitow w kazdej sekwencji
    return bits

bit_string = bytes_to_bits(audio_bytes) #all bytes

#print
for index, byte_bits in enumerate(bit_string):
    print(f"Bajt {index}: {byte_bits}")

#100bajtow nie zkonwertowane
print(audio_bytes[:100])
print("dlugosc ciągu bitów:", len(bytes_to_bits(audio_bytes)))