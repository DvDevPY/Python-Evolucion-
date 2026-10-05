import math
n = float(input('Digite o angulo a ser calculado: '))
cos = math.cos(math.radians(n))
sin = math.sin(math.radians(n))
tan = math.tan(math.radians(n))
print(f'''o cosseno de {n} corresponde a {cos:.2f}
O seno de {n} corresponde a {sin:.2f}
e por fim a Tangente corresponde a {tan:.2f}''')
