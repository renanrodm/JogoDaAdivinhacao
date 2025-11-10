def geraCartelas():
    cartelas = [[], [], [], [], [], []]

    for i in range(1, 64):
        prox = i

        for cartela in cartelas:
            if prox % 2 == 1:
                cartela.append(i)

            prox = prox // 2

    return cartelas


def exibeCartela(cartela, n):
    print(f"\nCartela {n + 1}")

    for pos, n in enumerate(cartela):
        print(str(n).rjust(2), end=" ")

        if (pos + 1) % 8 == 0:
            print()


def exibeMensagemInicial():
    linha = "*" * 62
    largura_bordas = 60
    print(linha)
    print("*" + "Jogo da Adivinhação".center(largura_bordas) + "*")
    print(
        "*"
        + "Pense em um inteiro de 1 a 63 e não conte pra ninguém!".center(
            largura_bordas
        )
        + "*"
    )
    print(
        "*" + "Em seguida, tecle ENTER para continuar...".center(largura_bordas) + "*"
    )
    print(linha)
    input("\nPressione ENTER para começar...")


def exibeMensagemFinal():
    linha = "*" * 63
    largura_bordas = 61
    print()
    print(linha)
    print("*" + "Por: Renan Martins".center(largura_bordas) + "*")
    print("*" + "github.com/renanrodm".center(largura_bordas) + "*")
    print(linha)


def main():
    exibeMensagemInicial()

    cartelas = geraCartelas()

    valorEscolhido = 0
    for pos, cartela in enumerate(cartelas):
        exibeCartela(cartela, pos)

        while True:
            try:
                resp = input("\nO valor escolhido está nessa cartela (s/n)?: ")
                if resp not in ("s", "n"):
                    raise ValueError("Resposta inválida!")
                break
            except ValueError:
                print("Resposta inválida. Digite 's' ou 'n'")

        if resp == "s":
            valorEscolhido += cartela[0]

    print(f"\nAtenção! O valor escolhido foi....... {valorEscolhido}!!!!!")

    exibeMensagemFinal()


if __name__ == "__main__":
    main()
