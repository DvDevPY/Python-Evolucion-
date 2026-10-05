import emoji
tempC = float(input('Qual é a temperatura em C° nesse momento? ').replace(',','.'))
tempF = 9 * tempC / 5 + 32
print(f'A temperatura de {tempC:.2f}C° equivale a {tempF:.2f}F°')
if tempF >= 100:
    print(emoji.emojize("Wow, it's too hot bro :fire:"))
elif tempF <= 50:
    print(emoji.emojize("Bro i'm freezing, it's much cold :ice:"))