n1 = int(input("Write a number and i'll show you the antecessor, predecessor,\ndouble, triple and square root: "))
a = n1 - 1
p = n1 + 1
d = n1 * 2
t = n1 * 3
s = n1**(1/2)
print('analysing your number "{}" , your predecessor is "{}" and your antecessor is "{}"'.format(n1,p,a))
print('about others operations, for example "{}" is the double, "{}" is the triple and "{:.3f}" is the square root'.format(d,t,s))
