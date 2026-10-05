sal = float(input('Digite qual o valor do salário: '))
per = 15
print(f'''Um funcionário que recebia um total de R$ {sal:.2f} 
com um aumento de {per}% passará a receber R$ {(sal*per/100)+sal:.2f}''')
