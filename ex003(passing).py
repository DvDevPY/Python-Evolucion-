nome = (input('Digite seu nome: '))
print('O que foi digitado "{}" é do tipo primitivo'.format(nome),type(nome))
print('O que foi digitado "{}" é numérico? '.format(nome),nome.isnumeric())
print('O que foi digitado "{}" é alfabético? '.format(nome),nome.isalpha())
print('O que foi digitado "{}" está capitalizado? '.format(nome),nome.istitle())
print('O que foi digitado "{}" está maiúsculo? '.format(nome),nome.isupper())
print('O que foi digitado "{}" está minúsculo? '.format(nome),nome.islower())
print('Resumindo tudo isso acima, "{}" é bom? '.format(nome),bool(nome))
if\
    bool(nome):
        print('bom é pouco "{}" é que nem mel'.format(nome))
