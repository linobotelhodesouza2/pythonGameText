print('Boas Vindas ao Python The Game!')
print('Gostaria muito de saber o seu nome!')
nome_jogador = input('Digite o seu nome: ')
print('Olá, é um prazer ter voçê {} jogando o nosso jogo!'.format(nome_jogador))

idade_jogador = int(input('Eu gostaria de saber em que ano voçê nasceu? ')) #convertendo o ano de nascimento em numero
idade_calculada = 2022 - idade_jogador
print('Que legal,, vi aqui que voçê {} tem {} anos!\n '.format(nome_jogador, idade_calculada))

print('Agora que já te conheço posso te levar em muitas aventuras, oque deseja fazer?')
escolha = input('SIM - quero iniciar uma aventura \nNÃO - quero ficar por aqui\n').upper()  # deixa a letra em caixa alta

#ESTRUTURA DE CONDIÇÃO IF ELSE
if 'SIM' == escolha:
    print('Que bom que voçê é um aventureiro, vamos começar então!')

# ESTRUTURA DE REPETIÇÃO WHILE
    resposta = ''   # variavel recebe um valor vazio
    tentativa = 0
    while resposta != 'DEUS':   # loop enquanto a resposta nao for colocada sempre ira repetir
        resposta = input('Qual a resposta para vida e tudo mais?: ')
        tentativa = tentativa + 1   #variavel contadora para adicionar tentativas

        #break    serve para para o loop se eu errar na primeira tentativa ele já vai encerrar o loop

    print('\nPara chegar a esse resultado voçê utilizou {} tentativas'.format(tentativa))
    print('Parabéns, voçê acertou!')

# ESTRUTURA FOR
    print('Para cada tentativa voçê merece um parabéns!')
    for i in range(tentativa):  # contador for , criada a variavel i que vai controlar as voltas do loop  o in mostra que o contador vai estar em qual intervalo? funcao range que cria o intervalo que eu escrever no caso tentativa( tentativa)
        print('Parabens!')

# ESTRUTURAS DE DADOS - TUPLAS
    anos_lancamento = (1977, 1980, 1983, 1999, 2002, 2005, 2015, 2017, 2019)    #tupla
    star_wars = int(input('Ja vi que voçê é meio geek! Voçê sabe em que ano foi lançado algum filme do STAR WARS?: '))
    if star_wars in anos_lancamento:    # se na variavel star_wars voce acertar algum valor da tupla de os parabens
        print('Parabéns, voçê acertou!')
    else:
        print('Parece que voçê não é tão geek assim né! Sorte na próxima!')

# ESTRUTURAS DE DADOS - LISTAS
    print('Estou tão surpreso que voçê é um geek que gostaria de te dar a oportunidade de escrever e armazenar alguns comandos em python')
    print('Quando tiver digitado TODOS os comandos que conhece, digite SAIR')
    comando = ''
    lista_de_comando = []
    while comando != 'SAIR':
        comando = input('Digite um comando que voçê conhece e Python: ')
        lista_de_comando.append(comando)
    
    print(lista_de_comando)


else:
    if 'NÃO' == escolha:
        print('Pena que voçê não quer se aventurar,\n GAME OVER!')
    else:
        print('Voçê digitou um comando inválido, Jogo Encerrado')#digitando um comando fora dos dois comandos sim ou nao

''' 
    Exemplo de como remover dados de uma lista
    lista = ['Yoda', 'Luke', 'Darth Vader'] criando uma lista
    print(lista)
    lista.pop(1) removendo o dado da lista utilizando o .pop() e colocando o valor correspondente a 1 que será o valor de 'Luke' na lista 
    print(lista)
'''