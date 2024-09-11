import time


def calcula_duracao(funcao):
    def wrapper():
        tempo_inicial = time.time()
        funcao()
        tempo_final = time.time()

        print(
            "[{funcao}] Tempo total de execução: {tempo_total}".format(
                funcao=funcao.__name__, tempo_total=str(tempo_final - tempo_inicial)
            )
        )

    return wrapper


@calcula_duracao
def main():
    for n in range(0, 10000000):
        pass


main()
