print('')
print('')
print('')
print('')
print('')
print('='*80)
print('Bem vindo ao meu quiz')
print('='*60)
n1 = int(input('Qual minha idade?:'))
if (n1==15):
    print('+1 ponto')
    r1 = 1
else:
    print('0 pontos')
    r1 = 0


n2 = str(input('Qual o meu nome?:'))
if (n2=='Rony'):
    print('+1 ponto')
    r3 = r1 + 1
elif(n2=='rony'):
    print('Falta a letra maiúscula no começo\n0 pontos')
    r3 = r1 + 0
else:
    print('0 ponto')
    r3 = r1 + 0


n3 = str(input('Qual minha linguagem de programação?:'))
if (n3=='Python'):
    print('+1 ponto')
    r4 = r3 + 1
elif (n3=='python'):
    print('Meu deus letra maiúscula no começo preste atenção!\n0 pontos')
    r4 = r3 + 0
else:
    print('0 pontos')
    r4 = r3 + 0


n4 = str(input('Qual meu segundo nome hacker?:'))
if (n4=='Bruno'):
    print('+1 ponto')
    r5 = r4 + 1
elif (n4=='bruno'):
    print('Presta atenção letra maiúscula nos nomes e começos de frase!\n0 ponto')
    r5 = r4 + 0
else:
    print('Meu nome no mundo hacker é Bruno!')
    print('0 ponto')
    r5 = r4 + 0

n5 = int(input('Eu fiquei quantos dias sem programar por conta do pc quebrado?:'))
if (n5==4, 5, 6):
    print('+1 ponto')
    r6 = r5 + 1
elif (n5 >= 7):
    print('Na verdade foram 4 dias sem contar segunda\n0 ponto')
    r6 = r5 + 0
else:
    print('0 ponto')
    r6 = r5 + 0
print('-'*60)
n6 = (r6)
if (n6 >= 5):
    print('Você é meu melhor amigo!')
    print('TOTAL DE PONTOS:{}'.format(n6))
elif (n6 <= 4):
    print('Você não sabe muito sobre mim!\nTOTAL DE PONTOS:{}'.format(n6))
print('-'*60)
print('='*80)






