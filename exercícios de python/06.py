'''
	Entrar com o ano e informar se o mesmo é bissexto ou não.
        Como funciona o ano bissexto ver opções a abaixo tabela abaixo:
        1- Todo ano divisível por 4 é bissexto;
        2- Todo ano divisível por 100 não é ano bissexto;
        3- Mas se o   ano for também divisível por 400 é ano bissexto;
'''
ano = int(input("Digite o ano: "))

if( (ano % 4 == 0) or (ano % 100 != 0) and (ano % 400 == 0) ):
    print("É bissexto !")
else:
    print("Não é bissexto !")

