def soma_multiplos(n):
    soma = 0

    for num in range(n):
        if num % 3 == 0 or num % 5 == 0:
            soma += num

    return soma

# Leitura da entrada de exemplo e teste da função
n = int(input())
print(soma_multiplos(n))
