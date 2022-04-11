#Em uma loja e CD´s existem apenas quatro tipos de preços que estão associados a cores. 
#Assim os CD´s que ficam na loja não são marcados por preços e sim por cores. 
#Desenvolva um algoritmo que a partir da entrada da cor o software mostra o preço.
#A loja está atualmente com a seguinte tabela de preços.
cor = str(input("Cor do produto selecionado: "))
if cor == "Verde":
    print("O valor do produto é 10.00 R$")
elif cor == "Azul":
    print("O valor do produto é 20.00 R$")
elif cor == "Amarelo":
    print("O valor do produto é 30.00 R$")
elif cor == "Vermelho":
    print("O valor do produto é 40.00 R$")
