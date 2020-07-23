#Imports
import random

#Maior número que o programa gerará
numeromaximo = 25 

#Quantidade de números a serem gerados
quantidade = 15 

#Definindo o array a ser armazenado os números
numeros = []

#Função que gera um único número
def gerarNumero(numeromaximo):
    for i in range(1):
        
        #gerar o numero aleatório entre 1 e o número máximo definido
        numero = random.randint(1,numeromaximo)
        
        #Se o array ainda não contiver o número adiciona no array
        if numero not in numeros:
            numeros.append(numero)
        elif numero in numeros:
            gerarNumero(20)

#Função para gerar os números
def gerarNumeros(quantidade,numeromaximo):
    for i in range(quantidade):
        #Gerar numero aleatório entre 1 e o número máximo definido
        numero = random.randint(1,numeromaximo)
        
        #Se o array ainda não contiver o número adiciona no array
        if numero not in numeros:
            numeros.append(numero)
        
        #Se o array já contiver o número utiliza a função gerarNumero para gerar somente um número
        elif numero in numeros:
            gerarNumero(20)
            
#Chamada da função gerarNumeros    
gerarNumeros(quantidade,numeromaximo)

#Ordenando o array com sorted
numeros_ordenados = sorted(numeros)

#Imprimindo os números na tela
print(numeros_ordenados) 
