import wave
from AudioSettings import AudioSettings
from convertingSystem import hexToBinary

file_path = '../samples/input/wow.wav'
def loadWavFile(fileName):
    filePath = '../samples/input/' + fileName + '.wav'

    with (wave.open(filePath, 'rb') as wav_file):
        return (
            hexToBinary(wav_file.readframes(wav_file.getnframes()).hex()),
            AudioSettings(
                wav_file.getnchannels(),
                wav_file.getsampwidth(),
                wav_file.getframerate(),
                wav_file.getnframes(),
                wav_file.getcomptype(),
                wav_file.getcompname()
            )
        )
def createWavFile(data, channels, sample_width, frame_rate, fileName):
    filePath = '../samples/output/' + fileName + '_output.wav'
    with wave.open(filePath, 'wb') as wav_file:
        wav_file.setnchannels(channels)
        wav_file.setsampwidth(sample_width)
        wav_file.setframerate(frame_rate)
        wav_file.writeframes(data)  #bytes object