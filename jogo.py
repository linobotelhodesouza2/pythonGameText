print('Boas Vindas ao Python The Game!')
print('Gostaria muito de saber o seu nome!')
nome_jogador = input('Digite o seu nome: ')
print('Olá, é um prazer ter voçê {} jogando o nosso jogo!'.format(nome_jogador))

idade_jogador = int(input('Eu gostaria de saber em que ano voçê nasceu? '))#convertendo o ano de nascimento em numero
idade_calculada = 2022 - idade_jogador
print('Que legal,, vi aqui que voçê {} tem {} anos!\n '.format(nome_jogador, idade_calculada))

print('Agora que já te conheço posso te levar em muitas aventuras, oque deseja fazer?')
escolha = input('SIM - quero iniciar uma aventura \nNÃO - quero ficar por aqui\n').upper()# deixa a letra em caixa alta

#ESTRUTURA DE CONDIÇÃO IF ELSE
if 'SIM' == escolha:
    print('Que bom que voçê é um aventureiro, vamos começar então!')

# ESTRUTURA DE REPETIÇÃO WHILE
    resposta = ''# variavel recebe um valor vazio
    tentativa = 0
    while resposta != 'DEUS':# loop enquanto a resposta nao for colocada sempre ira repetir
        resposta = input('Qual a resposta para vida e tudo mais?: ')
        tentativa = tentativa + 1
    print('\nPara chegar a esse resultado voçê utilizou {} tentativas'.format(tentativa))
    print('Parabéns, voçê acertou!')

else:
    if 'NÃO' == escolha:
        print('Pena que voçê não quer se aventurar,\n GAME OVER!')
    else:
        print('Voçê digitou um comando inválido, Jogo Encerrado')#digitando um comando fora dos dois comandos sim ou nao

