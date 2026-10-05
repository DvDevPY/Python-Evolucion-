from playsound3 import playsound
import random
rd = input('What do u wanna listen? \n'
           '"The Marías - No One Noticed" \n"Tyler The Creator - She" or "Timbaland - The Way I Are" ? '
           ).lower()
nmusic1 = 'The Marías - No One Noticed'
urlmusic1 = (
    r'C:\Users\Pichau\Music'
    r'\Possibilidades para futuros projetos'
    r'\The Marías - No One Noticed.mp3'
    )
music1 = (nmusic1,urlmusic1)
if rd in (
    'no one noticed','the marías',
    'noonenoticed','the marias',
    'no onenoticed','noone noticed'
    ):
    print("So let's start for -"
          f" {nmusic1}")
    playsound(urlmusic1)
nmusic2 = 'Tyler The Creator - She'
urlmusic2 = (
    r'C:\Users\Pichau\Music'
    r'\Possibilidades para futuros projetos'
    r'\Tyler The Creator - She (feat. Frank Ocean).mp3'
    )
music2 = (nmusic2,urlmusic2)
if rd in (
    'tyler the creator','tyler',
    'she','tylerthe creator',
    'tyler thecreator'
    ):
    print("So let's start for -"
          f" {nmusic2}")
    playsound(urlmusic2)
nmusic3 = 'The Way I Are'
urlmusic3 = (
    r'C:\Users\Pichau\Music'
    r'\Possibilidades para futuros projetos'
    r'\Timbaland - The Way I Are.mp3'
    )
music3 = (nmusic3,urlmusic3)
if rd in (
    'the way i are','theway i are',
    'timbaland','the wayi are'
    ):
    print("So let's start for -"
        f" {nmusic3}")
    playsound(urlmusic3)

if rd in (
        "random","aleatório","aleatorio","idk"
):
    musics = music1,music2,music3
    print("i'll choose for you!")
    chosen = random.choice(musics)
    print(f'The music chosen was\n{chosen[0]}')
    playsound(chosen[1])
