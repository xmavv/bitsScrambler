import wave
# Assume 'audio_bytes' is a bytes object with your raw audio data
audio_bytes = b'010101010101010101'
with wave.open('output.wav', 'wb') as wav_file:
    wav_file.setnchannels(1) # Mono
    wav_file.setsampwidth(2) # Sample width in bytes
    wav_file.setframerate(44100) # Sample rate
    wav_file.writeframes(audio_bytes)