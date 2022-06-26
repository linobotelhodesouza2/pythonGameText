print('Boas Vindas ao Python The Game!')
print('Gostaria muito de saber o seu nome!')
nome_jogador = input('Digite o seu nome: ')
print('Olá, é um prazer ter voçê {} jogando o nosso jogo!'.format(nome_jogador))

idade_jogador = int(input('Eu gostaria de saber em que ano voçê nasceu? '))#convertendo o ano de nascimento em numero
idade_calculada = 2022 - idade_jogador
print('Que legal,, vi aqui que voçê {} tem {} anos!'.format(nome_jogador, idade_calculada))
