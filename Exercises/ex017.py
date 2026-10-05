import emoji
from math import hypot
son = input(emoji.emojize('Vai um teorema de pitágoras ai? :nerd_face: ')).lower().strip()
if son in ('sim','claro','lógico','logico','bó','bo','s','si','yes','yeah','yep','y'):
    print('Ok, vamos lá!')
    a = float(input('Digite o comprimento do cateto oposto: ').replace(',','.'))
    b = float(input('agora o comprimento do cateto adjacente: ').replace(',','.'))
    h = hypot(a,b)
    print(emoji.emojize(f'O comprimento da hipotenusa mede {h:.2f} centimetros :call_me_hand:'))
elif son in ('não','nao','nah','no','n'):
    print('Tudo bem, talvez outra hora.')
