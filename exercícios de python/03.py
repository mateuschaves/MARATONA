
##    2.	Escreva um programa para ler o ano de nascimento de uma pessoa
##    e escrever uma mensagem que diga se ela poderá ou não votar
##    este ano (não é necessário considerar o mês em que ela nasceu).

ano_atual = 2018
ano_nascimento = int(input("Digite seu ano de nascimento: "))
idade = ano_atual - ano_nascimento

if( idade >= 16 and idade < 18):
    print("Você pode votar !")
elif (idade >= 18):
    print("Você precisa votar !")
else:
    print("Você não pode votar !")