import wave
from pydub import AudioSegment


#bigger file, less bits
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

#smaller file, compression makes more bits then
def mp3_to_bytes(file_path):
    audio = AudioSegment.from_mp3(file_path)
    audio_bytes = audio.raw_data
    return audio_bytes

#path
wav_file_path = '../samples/wow.wav'
mp3_file_path = '../samples/wow.mp3'

#conversion
# audio_bytes = wav_to_bytes(wav_file_path)
audio_bytes = mp3_to_bytes(mp3_file_path)

def bytes_to_bits(byte_string):
    bits = []
    for byte in byte_string:
        bits.append(format(byte, '08b'))  #byte to bit, uzupelnia do 8 bitow w kazdej sekwencji
    return bits

bit_string = bytes_to_bits(audio_bytes) #all bytes

#print
for index, byte_bits in enumerate(bit_string):
    print(f"Bajt {index}: {byte_bits}")

#pierwsze 100bajtow nie zkonwertowane (w postaci szesnatskowej)
print(audio_bytes[:100])
print("dlugosc ciągu bajtów:", len(bytes_to_bits(audio_bytes)))