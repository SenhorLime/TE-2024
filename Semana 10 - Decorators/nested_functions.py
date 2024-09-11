def party():
    print("Estou de fora!")

    def start_party() -> str:
        return "Estamos dentro! Uhulll"

    def finish_party() -> str:
        return "A festa acabou! =("

    print(start_party())
    print(finish_party())


party()
