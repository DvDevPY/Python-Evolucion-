l = float(input('Digite quanto mede a largula da sua parede: '))
h = float(input('Agora digite a medição da altura da sua parede: '))
a = l * h
pp = a / 2
print('''Para uma parede como a sua de {} metros de largura {} metros de altura
teremos uma área de {:.2f} m², você precisará de {:.2f} litros de tinta para pintar a parede inteira'''.format(l,h,a,pp))