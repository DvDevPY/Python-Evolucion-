import emoji
qd = int(input('Quantos dias o carro ficou alugado? '))
qk = float(input('E quantos km (quilometrôs) foram? ').replace(',','.'))
pd = 60
pk = 0.15
print(emoji.emojize(f'''O valor total a se pagar considerando que o :automobile: foi alugado por {qd} e rodou um total de {qk}
 foi de R${qd*pd+qk*pk:.2f}'''))