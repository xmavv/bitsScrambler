## Table of contents

- [Overview](#overview)
  - [The task](#the-task)
    - [Converting file to bits](#converting-file-to-bits)
    - [Additive method](#additive-method)
    - [Multiplicative method](#multiplicative-method)
  - [Preview](#preview)
- [Built with](#built-with)

## Overwiev

### The task

this is our college project for the subject <i>Niezawodność i Diagnostyka Układów Cyfrowych</i>

our task was to implement bits scrambler, working with both additive and multiplicative approach.

to generate pseudo-random keys, working with our methods, we decided to work on two scenarios:
  - generating random keys based on our application, each time new key is generated
  - generating keys based on shift register and polynomials, each time key is the same, well fitted to the length of original bit string

to make it even more real-word project, we decided to get bits from an .mp3 or .wav file, and then scramble them.

#### Converting file to bits

to convert raw .mp3 or .wav files we used ffmpeg package

#### Additive method

Additive method works...

(mamy juz wczesniej podany rejestr, robimy operacje xor, nastepnie aby odscramblowac znowu ta operacja jest wykonywana, jest to metoda synchroniczna - klucz sie nie zmienia nigdy)

#### Multiplicative method

Multiplicative method works...

(mamy juz wczesniej podany rejestr, natomiast ten rejestr oddzialuje z naszym ciagiem bitow ktory podajemy, wiec za kazdym razem jest inny, dla roznych ciągow bitow. tutaj jakis algorytm ktory tworzy nam ten klucz, np bierzemy bity co drugi i jakos laczymy z tym kluczem ktory byl w rejestrze. wowczas mamy ten klucz i teraz znowu wykonujemy operacje xor na tym kluczu i naszym ciagu bitow, aby dalo sie go odscramblowac, jest to metoda synchroniczna, klucz z rejestru wchodzi przez podany algorytm w nasz orginalny ciag bitow)

### Preview

working with our <i>wow.wav</i> file, which sounds like this and contains 1320848 single bits

WOW.WAV FILE

![zero sequences histogram before scrambling](img/before_scrambling.png)

the longest zero sequence here is 95bits

after we scrambled it, so that zero sequences should be smaller, to prevent desynchronization, it looks like this

![zero sequences histogram before scrambling](img/multiplicative_scrambling.png)

now the longest sequence is only 20bits long

after scrambling our file should be encrypted, and so it sounds like that

(WARNING, LOUD NOISES)

FILEAFTERSCRAMBLIG.WAV FILE

next we descramble our string to get the actual data

DESCRAMBLED FILE WITH NOISES

as u can hear our file is mostly audible, but with small noise

thats because we simulated desynchronization probability, when our zero sequence is longer than selected value, in our case the probability with scrambler was 4%

to compare it here the file WITHOUT SCRAMBLER, where the whole desynchronization probability was 11%

BEZSCRAMBLERA FILE

of course if we didnt simulated any noise, our output file will be the same as the output

CALUTKI FAJNY PLIK

## Built with
to run this app, You will need to download ffmpeg

this may help You https://phoenixnap.com/kb/ffmpeg-windows
