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

Our task was to implement bits scrambler, working with both additive and multiplicative approach.

To generate pseudo-random keys, working with our methods, we decided to work on two scenarios:
  - generating random keys based on our application, each time new key is generated
  - generating keys based on shift register and polynomials, each time key is the same, well fitted to the length of original bit string

To make it even more real-word project, we decided to get bits from an .mp3 or .wav file, and then scramble them.

#### Converting file to bits

To convert raw .mp3 or .wav files we used ffmpeg package

#### Additive method

Additive method works...

(mamy juz wczesniej podany rejestr, robimy operacje xor, nastepnie aby odscramblowac znowu ta operacja jest wykonywana, jest to metoda synchroniczna - klucz sie nie zmienia nigdy)

#### Multiplicative method

Multiplicative method works...

(mamy juz wczesniej podany rejestr, natomiast ten rejestr oddzialuje z naszym ciagiem bitow ktory podajemy, wiec za kazdym razem jest inny, dla roznych ciogow bitow. tutaj jakis algorytm ktory tworzy nam ten klucz, np bierzemy bity co drugi i jakos laczymy z tym kluczem ktory byl w rejestrze. wowczas mamy ten klucz i teraz znowu wykonujemy operacje xor na tym kluczu i naszym ciagu bitow, aby dalo sie go odscramblowac, jest to metoda synchroniczna, klucz z rejestru wchodzi przez podany algorytm w nasz orginalny ciag bitow)

## Built with
to run this app, You will need to download ffmpeg

this may help You https://phoenixnap.com/kb/ffmpeg-windows
