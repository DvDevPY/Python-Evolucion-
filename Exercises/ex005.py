n = str(input('Olá aluno, digite seu nome: '))
nota1 = float(input('{} digite qual foi sua nota no primeiro bimestre: '.format(n)))
nota2 = float(input('Certo agora preciso da nota do segundo bimestre: '))
media = (nota1+nota2)/2
print("Sua nota final foi {:.2f}".format(media))
