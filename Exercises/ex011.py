print('Ola sou o Robot, sou o responsável por passar o valor do seu salário atualizado')
nome = str(input('Qual o seu nome? '))
salariobruto = float(input('e qual o seu salário atual? '))
if salariobruto <= 1000:
    percentual = 15
elif salariobruto <= 1500:
    percentual = 10
else:
    percentual = 0
aumento = salariobruto * percentual / 100
salariofinal = salariobruto + aumento
if percentual == 0:
    print('Lamento muito {}, mas seu salário não recebeu nenhuma bonificação, continuando assim em R$ {:.2f}'
          .format(nome,salariobruto))
else:
    print('Parabens {}, seu salário recebeu uma bonificação de {}%, saindo de R$ {:.2f} para R$ {:.2f)'
          .format(nome, percentual, salariobruto, salariofinal))
