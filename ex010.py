pe = (input('Qual será o produto que gostaria de levar? ').lower())
pv = float('129.99')
pl = float('149.99')
#8% de aumento
percentcartao = 8
#5% de desconto
percentpix = 5
if  pe == 'ventilador':
    print('O preço do nosso ventilador depende da forma de pagamento escolhida')
elif pe == 'liquidificador':
    print('O preço do nosso liquidificador muda conforme a forma de pagamento')
fpagamento = input('Qual será a forma de pagamento? Pix ou Cartão? ').lower()
if fpagamento == 'cartão' and pe == 'liquidificador':
    print(f'''O preço inicial do nosso liquidificador é de R$ {pl:.2f}
mas como a compra será efetuada no cartão, um aumento de {percentcartao}% será adicionado
ficando num total de R$ {pl+(pl*percentcartao/100):.2f}''')
elif fpagamento == 'pix' and pe == 'liquidificador':
    print(f'''O preço inicial do nosso liquidificador é de R$ {pl:.2f}
mas como sua compra será efetuada pelo pix, daremos um desconto de {percentpix}% a você
assim ficando um total de R$ {pl-(pl*percentpix/100):.2f}''')
elif pe == 'ventilador' and fpagamento == 'pix':
    print(f'''O preço inicial do nosso Ventilador é de R$ {pv:.2f}
mas como sua ocmpra será efetuada pelo pix, teremos um desconto de {percentpix}% na sua compra
ficando no total de R$ {pv-(pv*percentpix/100):.2f}''')
elif pe == 'ventilador' and fpagamento == 'cartão':
    print(f'''O valor inicial do Ventilador é de R$ {pv:.2f}
mas como o seu pedido será pago no cartão há um aumento de {percentcartao}%
ficando assim um total de R${pv+(pv*percentcartao/100):.2f}''')
else:
    print('tente novamente')