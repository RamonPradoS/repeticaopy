from random import randint
soma = 0
nro = 0
cont = 0
qtdimpar = 0
while nro != 32:
    nro = randint(0,50)
    if nro %2 != 0:
        qtdimpar = qtdimpar +1
    cont = cont +1
    print(nro)
    soma = soma + 1
    soma = soma + nro

print('Quantidade de numeros gerado: '+str(cont))
print('Quantidade de numeros impares: '+str(qtdimpar))
print("A soma de todos os números são: " + str(soma))