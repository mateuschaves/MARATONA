'''
    1.	Escreva um programa que apresente o menu de opções abaixo:
    OPÇÕES:
    1 - SAUDAÇÃO
    2 - BRONCA
    3 - FELICITAÇÃO
    0 - FIM
            O programa deve ler a opção do usuário e exibir, para cada opção, a respectiva mensagem:
    1 - Olá. Como vai ?
    2 - Vamos estudar mais.
    3 - Meus Parabéns !
    0 - Fim de serviço.
'''

parada = 1

while (parada != 0):
    print("1 - Saudação")
    print("2 - Bronca")
    print("3 - Felicitação")
    print("0 - Fim")
    s = int(input("Escolha a saudação: "))
    if  (s == 1):
        print("Olá, como vai ? ")
    elif (s == 2):
        print("Vamos estudar mais !")
    elif (s == 3):
        print("Meus Parabéns !")
    elif (s == 0):
        parada = 0


