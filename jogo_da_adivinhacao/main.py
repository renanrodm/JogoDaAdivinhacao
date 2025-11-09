def geraCartelas():
    
    cartelas = [[],[],[],[],[],[]]
    
    for i in range(1, 64):
        prox = i

        for cartela in cartelas:
            if prox % 2 == 1:
                cartela.append(i)

            prox = prox // 2

    return cartelas

def exibeCartela(cartela, n):

    print(f"\nCartela {n+1}")

    for pos, n in enumerate(cartela):
        print(str(n).rjust(2), end=' ')

        if (pos+1) % 8 == 0:
            print()
         
def exibeMensagemInicial():
    print("*" * 63)
    print("*", "Jogo da Adivinhação".center(60), end="*")
    print("\n*","Pense em um inteiro de 1 a 63 e não conte pra ninguém!".center(60), end="*")
    print("\n*","Em seguida, tecle ENTER para continuar... e boa sorte!".center(60), end="*")
    print("\n*", "*".rjust(61))
    print("*" * 63)

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


if __name__ == "__main__":
    main()