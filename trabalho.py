"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
entrada = input('Digite um numero inteiro: ')


try:
    entrada = int(entrada)
    if entrada % 2 == 0:
        print(f'{entrada} é par')
    else:
        print('{} é ímpar'.format(entrada))
except:
    print('O número digitado não é um inteiro')  

# if entrada.isdigit() :
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O número {entrada_int} é {par_impar_texto}')
# else:
#     print('Você não digitou um número inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
relogio = input('What time is it? ')

try:
    relogio = int(relogio)
    if relogio >= 00 and relogio < 12:
        print('Bom dia')
    elif relogio >= 12 and relogio < 18:
        print('Boa tarde')
    elif relogio >= 18 and relogio < 24:
        print('Boa noite')
    else:
        print('O dia só tem 24horas')
except:
    print('O número digitado não é um inteiro')  
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
usuario = input('Agora digite seu primeiro nome: ')

try:
    usuario = int(usuario)    
    print('Você digitou um número, mas qual é o seu nome ? ')

except:
    contagem  = len(usuario)
    print(contagem)
    if contagem >=1 and contagem <= 4:
        print('Seu nome é curto')
    elif contagem <4 and contagem > 7:
        print('Seu nome é tamanho normal')
    elif contagem > 6:
            print('Seu nome é muito grande')
    else: 
        print('Você não digitou nada!')