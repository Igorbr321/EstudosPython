from time import sleep
pvalor = int(input('Primeiro valor: '))
svalor = int(input('Segundo valor: '))

opcao = 0
while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = pvalor + svalor
        print('A soma dos valores {} + {} '
              '= {}.'.format(pvalor, svalor, soma))
        sleep(1)


