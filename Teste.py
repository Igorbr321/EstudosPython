looping = True

while looping == True:

    decision = input("1 - Verificar se uma frase é palíndromo\n2- Sair\n")

    teste = int(decision)
    match teste:
        case 1:
            frase = str(input('\nDigite algo: ')).upper().strip()
            juntar = frase.replace(' ', '')
            fraseinv = juntar[::-1]
            if juntar == fraseinv:
                print('Está frase é um PALÍNDROMO.\n')
            else:
                print('Está frase NÃO É UM PALÍNDROMO.\n')
        case 2:
            print("Você saiu do programa")
            looping = False
        case _:
            print("Esta não é uma opção válida, digite novamente.")