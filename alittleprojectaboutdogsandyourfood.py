from math import floor
quantrac= float(input('Quanto de ração você compra em R$? '))
pk = 13
kg = quantrac / pk
print(f'Com o Valor de R${quantrac} você pode comprar {kg:.2f}kg de ração')
conspd = 0.2
dr = kg / conspd
print(f'Em um mês comprando R${quantrac:.2f} de ração haverá um total de R${quantrac*4:.2f} gastos por {kg*4:.2f}kg por mês')
print(f'Levando em conta que todo dia são {conspd}kg de consumo e são {kg:.2f} a cada compra de ração')
print(f'Em até {floor(dr)} dias toda a ração será consumida')
print(f'Consumindo um total de {conspd*30}kg em ração no mês')
kgbd = 15
pbd = 79.99
print(f'Comprando R${pbd} num saco de {kgbd}kg de ração, seria consumido em {kgbd/conspd:.0f} dias')
