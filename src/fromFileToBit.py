import wave

file_path = '../samples/input/wow.wav'

# load wav file
def load_wav_file():
    with wave.open(file_path, 'rb') as wav_file:
        # parameters
        print("Liczba kanałów:", wav_file.getnchannels())
        print("Szerokość próbki (w bajtach):", wav_file.getsampwidth())
        print("Częstotliwość próbkowania:", wav_file.getframerate())
        print("Liczba ramek:", wav_file.getnframes())
        print("Typ kompresji:", wav_file.getcomptype())
        print("Kompresja:", wav_file.getcompname())
        return wav_file.readframes(wav_file.getnframes())

# save to the new WAV file
def create_wav_file(data, channels=1, sample_width=2, frame_rate=44100, file_path='default_output.wav'):
    with wave.open(file_path, 'wb') as wav_file:
        wav_file.setnchannels(channels)
        wav_file.setsampwidth(sample_width)
        wav_file.setframerate(frame_rate)
        wav_file.writeframes(data)  # actually save

def bytes_to_bits(byte_string):
    bits = []
    for byte in byte_string:
        bits.append(format(byte, '08b'))  # byte to bit, uzupelnia do 8 bitow w kazdej sekwencji
    return ''.join(bits)

print(load_wav_file()) # to jest szesnastkowo tutaj bo lepiej to widac
# np. xff oznacza po prostu zapis szesnastkowy FF, czyli 1111 1111

# example_data = b'\x00\x01\x02\x03\x04\x05'
# create_wav_file(example_data)