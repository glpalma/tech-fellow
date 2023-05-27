def ler_candidatos(num_candidatos: int) -> list:
    candidatos = []

    for i in range(num_candidatos):
        nome, ponto_prof, ponto_tec, ponto_acad = input().split()
        ponto_prof = int(ponto_prof)
        ponto_tec = int(ponto_tec)
        ponto_acad = int(ponto_acad)

        candidatos.append((nome, ponto_prof + ponto_tec + ponto_acad))

    return candidatos


def ordenar_candidatos(candidatos: list) -> None:
    candidatos.sort(key=lambda x: x[0])  # ordena por nome
    candidatos.sort(key=lambda x: x[1], reverse=True)  # ordena por pontuaçãp
    # se a ordenação do python for estável, deve funcionar


def main():
    num_candidatos = int(input())
    candidatos = ler_candidatos(num_candidatos)
    ordenar_candidatos(candidatos)

    for cand in candidatos:
        print(cand[0])


main()
