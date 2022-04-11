#Desenvolva um algoritmo capaz de encontrar o menor dentre 3 números inteiros quaisquer dados pelo teclado.
n1 = int(input("Digite o primeiro número:"))
n2 = int(input("Digite o segundo número:"))
n3 = int(input("Digite o terceiro número:"))
listaDeNumeros = [n1, n2, n3]
listaDeNumeros.sort()
print("O menor número é", listaDeNumeros[0])
