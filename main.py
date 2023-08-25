#Início da função cachorro_peso()
def cachorro_peso():
    valorBase = 0
    while True:
        try:
            peso = int(input('\nDigite o peso do seu cachorro (Kg): '))
            if peso >= 50: #checagem de peso máximo do cachorro (tem que ter menos que 50kg)
                print('Desculpe, não aceitamos cachorros com 50Kgs ou mais.')
                continue
            elif peso <= 0: 
                print('Cachorro não pode pesar zero ou menos.')
                continue
            else:
                if (peso > 0) and (peso < 3):
                    valorBase = 40
                    return valorBase
                elif (peso >= 3) and (peso < 10):
                    valorBase = 50
                    return valorBase
                elif (peso >= 10) and (peso < 30):
                    valorBase = 60
                    return valorBase
                elif (peso >= 30) and (peso < 50):
                    valorBase = 70
                    return valorBase
        except ValueError:  #caso o usuário digite um valor não numérico, ou um número não inteiro
            print('Valor informado não é válido. Informe um número inteiro por favor.')
#fim da função cachorro_peso()


#início da função cachorro_pelo()
def cachorro_pelo():
    valorPelo = 0
    while True:
        tipoPelo = input(
            'Qual o tipo de pelo do seu cachorro? Digite:\nc- pelo CURTO\nm- pelo MÉDIO\nl- pelo LONGO\n')
        if (tipoPelo != 'c') and (tipoPelo != 'm') and (tipoPelo != 'l'):
            print('"{}" não é um valor válido. Escolha um dos tipos de pelo por favor'.format(tipoPelo))
            continue
        else:
            if tipoPelo == 'c':
                valorPelo = 1
                return valorPelo
            elif tipoPelo == 'm':
                valorPelo = 1.5
                return valorPelo
            elif tipoPelo == 'l':
                valorPelo = 2
                return valorPelo
#fim da função cachorro_pelo()


#início da função cachorro_extra()
def cachorro_extra():
    valorExtra = 0
    while True:
        try:
            adicional = int(input('Deseja algum serviço adicional? Digite o número da opção desejada:\n1- Corte de unhas - R$ 10,00\n2- Escovar os dentes - R$ 12,00\n3- Limpeza de orelhas - R$ 15,00\n0- Finalizar e consultar o preço total\n'))
            if (adicional != 1) and (adicional != 2) and (adicional != 3) and (adicional != 0):
                print('"{}" não é uma opção válida. Digite novamente.'.format(adicional))
                continue
            if adicional == 0:
                break
            else:
                if adicional == 1:
                    valorExtra += 10
                elif adicional == 2:
                    valorExtra += 12
                elif adicional == 3:
                    valorExtra += 15
        except ValueError:
            print('Digite apenas números inteiros por favor.')
            continue
    return valorExtra
#fim da função cachorro_extra()

#início do programa principal
print('Bem-vindo(a) ao petshop')
precoBase = cachorro_peso()
precoPelo = cachorro_pelo()
precoAdicional = cachorro_extra()

precoTotal = precoBase * precoPelo + precoAdicional #cálculo do preço total
print('Total a pagar: R$ {} (preço por peso: {}, preço por tipo de pelo: * R${}, preço adicional(is): R${}).'.format(precoTotal, precoBase, precoPelo, precoAdicional))
#fim do programa principal