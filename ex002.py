n = input('Digite algo e te passarei as informações sobre esse "algo" :) :')
print('O tipo primitivo de "{}" é {}'.format(n,type(n)))
print('"{}" é capitalizado? {}'.format(n,n.istitle()))
print('"{}" está em caixa alta? {}'.format(n,n.isupper()))
print('"{}" é um número? {} '.format(n,n.isnumeric()))
print('"{}" é uma palavra? {}'.format(n,n.isalpha()))
print('"{}" está minúsculo? {}'.format(n,n.islower()))
print('"{}" só tem espaços? {}'.format(n,n.isspace()))
print('"{}" é alfanumérico? {}'.format(n,n.isalnum()))



