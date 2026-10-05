d = float(input('Digite a distância em metros: '))
mm = d * 10**3
cm = d * 10**2
dm = d * 10
dam = d / 10
hm = d / 10**2
km = d / 10**3
print(f'''A distância de {d} metros convertida em quilômetros são: {km}km\nA distância em hectômetros é de: {hm}hm
A distância em decâmetros é: {dam}dam\nA distância em decímetros é: {dm}dm\nA distância em centímetros é: {cm}cm
E a distância em milímetros é: {mm}mm.''')