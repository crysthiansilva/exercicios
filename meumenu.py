import random
import time


def menu():
    print('-' * 65)
    print('MENU GERAL DE EXERCÍCIOS - Desenvolvido por Crysthian M. Silva')
    print('-' * 65)
    print('[ 001 ] - \033[1;32mVARIÁVEL + INPUT\033[m')
    print('[ 002 ] - \033[1;32mINPUT + UPPER.\033[m')
    print('[ 003 ] - \033[1;32mOPERAÇÕES ARITMETICAS.\033[m')
    print('[ 004 ] - \033[1;32mDISSECANDO UMA VARIÁVEL.\033[m')
    print('[ 005 ] - \033[1;32mANTECESSOR E SUCESSOR.\033[m')
    print('[ 006 ] - \033[1;32mDOBRO - TRIPLO - RAÍZ QUADRADA.\033[m')
    print('[ 007 ] - \033[1;32mMÉDIA ESCOLAR.\033[m')
    print('[ 008 ] - \033[1;32mCONVERSOR DE MEDIDAS.\033[m')
    print('[ 009 ] - \033[1;32mMAIOR E MENOR IDADE.\033[m')
    print('[ 010 ] - \033[1;32mCONVERSOR DE MOEDAS.\033[m')
    print('[ 011 ] - \033[1;32mTABUADAS.\033[m')
    print('[ 012 ] - \033[1;32mCALCULAR PINTURA.\033[m')
    print('[ 013 ] - \033[1;32mCALCULAR DESCONTO.\033[m')
    print('[ 014 ] - \033[1;32mREAJUSTE SALARIAL.\033[m')
    print('[ 015 ] - \033[1;32mCONVERSOR DE TEMPERATURA C X F.\033[m')
    print('[ 016 ] - \033[1;32mALUGUEL DE CARRO.\033[m')
    print('[ 017 ] - \033[1;32mSORTEIO.\033[m')
    print('[ 018 ] - \033[1;32mANALIZE DE TEXTO.\033[m')
    print('[ 019 ] - \033[1;32mSEPARANDO DÍGITOS DE UM NÚMERO.\033[m')
    print('[ 020 ] - \033[1;32mMANIPULANDO STRINGS.\033[m')
    print('[ 021 ] - \033[1;32mPRIMEIRO E ULTIMO NOME\033[m')
    print('[ 022 ] - \033[1;32mJOGO ADIVINHE O NÚMERO ENTRE 0 E 5.\033[m')
    print('[ 023 ] - \033[1;32mVELOCIDADE MAXIMA PERMITIDA.\033[m')
    print('[ 024 ] - \033[1;32mJOGO DO PAR OU IMPAR.\033[m')
    print('[ 025 ] - \033[1;32mCALCULAR UMA VIAJEM.\033[m')
    print('[ 026 ] - \033[1;32mSABER SE O ANO É BISSEXTO.\033[m')
    print('[ 027 ] - \033[1;32mIDENTIFICAR MENOR E MAIOR NÚMERO.\033[m')
    print('[ 028 ] - \033[1;32mAUMENTO SALARIAL.\033[m')
    print('[ 029 ] - \033[1;32mCONVERSOR DE BASES NUMÉRICAS.\033[m')
    print('[ 030 ] - \033[1;32mALISTAMENTO MILITAR.\033[m')
    print('[ 031 ] - \033[1;32mMEDIA ESCOLAR.\033[m')
    print('[ 032 ] - \033[1;32mCLASSIFICAÇÃO DE ATLETAS.\033[m')
    print('[ 033 ] - \033[1;32mSIMULADOR PAGAMENTO LOJA.\033[m')
    print('[ 034 ] - \033[1;32mJOGO PEDRA, PAPEL OU TESOURA.\033[m')
    print('-' * 65)
    print('ESCOLHA SUA OPÇÃO DE EXERCÍCIO ENTRE 001 A 100')
    print('-' * 65)




resp = 1
while resp != 99:
    menu()
    op = int(input('Digite o número do exercício: '))
    match (op):
        case 1:
            print('\033[1;32mTITULO: Variável + input.\033[m\n')
            print(f'----------- EXERCÍCIO Nº {op} ---------')
            frase = input('Digite uma frase qualquer:\n ')
            print('Resposta: ')
            print(frase)
            print('-' * 15, ' FIM DO EXERCIIO ', '-' * 15)
        case 2:
            print('\033[1;32mTITULO: Comando input + upper.\033[m\n')
            print(f'--------------- EXERCÍCIO Nº {op} ---------------')
            nome = input('Digite seu nome: ')
            print('\n\033[1;45m RESUMO:\033[m\n')
            print(f'Olá \033[1;35m{nome.upper()}\033[m, Bons estudos em Python !')
            print('-' * 15, ' FIM DO EXERCIIO ', '-' * 15)
        case 3:
            print(f'--------------- EXERCÍCIO Nº {op} ---------------')
            print('\033[1;32mTITULO: OPERAÇÕES ARITMETICAS\033[m\n')
            n1 = int(input('Digite o primeiro número: '))
            n2 = int(input('Digite o segundo número: '))
            soma = n1 + n2
            sub = n2 - n1
            mult = n1 * n2
            div = n1 / n2
            print('\n\033[1;45m RESUMO:\033[m\n')
            print(f'PRIMEIRO NÚMERO: {n1}')
            print(f'SEGUNDO NÚMERO: {n2}')
            print(f'SOMA: {n1} + {n2} = {soma}')
            print(f'SUBTRAÇÃO: {n2} - {n1} = {sub}')
            print(f'MULTIPLICAÇÃO: {n1} * {n2} = {mult}')
            print(f'DIVISÃO: {n1} / {n2} = {div}')
            print('-' * 15, ' FIM DO EXERCIIO ', '-' * 15)
        case 4:
            print('\033[1;32mTITULO: Dissecando uma Variável.\033[m\n')
            print(f'--------------- EXERCÍCIO Nº {op} ---------------')
            texto = input('Digite algo: ')

            print('\n\033[1;45m RESUMO:\033[m\n')
            print(f'TIPO PRIMITIVO: {type(texto)}')
            print(f'SÓ TEM ESPAÇOS?: {texto.isspace()}')
            print(f'É UM NÚMERO: {texto.isnumeric()}')
            print(f'É ALFABÉTICO: {texto.isalpha()}')
            print(f'É ALFA NUMÉRICO? {texto.isalnum()}')
            print(f'ESTÁ EM MAIÚSCULO? {texto.isupper()}')
            print(f'ESTÁ EM MINÚSCULO? {texto.islower()}')
            print(f'ESTÁ EM CAPITALISE? {texto.capitalize()}')

            print('-' * 15, ' FIM DO EXERCIIO ', '-' * 15)
        case 5:
            print('\033[1;32mTITULO: Antecessor e Sucessor\033[m\n')
            print(f'--------------- EXERCÍCIO Nº {op} ---------------')
            num = int(input('Digite um número: '))
            a = num - 1
            s = num + 1
            print('\n\033[1;45m RESUMO:\033[m\n')
            print(f'ANTECESSOR: {a}')
            print(f'NÚMERO DIGITADO: {num}')
            print(f'SUCESSOR: {s}')
            print(f'{a} --> \033[1;32m{num}\033[m --> {s}')
            pausa = int(input('Para continuar digite 1 a 98 - SAIR 99: '))

            print('-' * 15, ' FIM DO EXERCIIO ', '-' * 15)
        case 6:
            print('\033[1;32mTITULO: Dobro, Triplo e Raiz Quadrada\033[m\n')
            for c in range(1, 4):
                print(f'--------------- EXERCÍCIO Nº {op} ---------------')
                num = int(input('Digite um número: '))
                print('\n\033[1;45m RESUMO:\033[m\n')
                print(f'NÚMERO ESCOLHIDO: {num}')
                print(f'DOBRO: {num * 2}')
                print(f'TRIPLO: {num * 3}')
                print(f'RAIZ QUADRADA: {pow(num, (1 / 2)): .2f}')
            print('-' * 15, ' FIM DO EXERCIIO ', '-' * 15)

        case 7:
            print('\033[1;32mTITULO: Média Escolar\033[m\n')
            for c in range(1, 4):
                print(f'--------------- EXERCÍCIO Nº {op} ---------------')
                nome = input(f'Digite o Nome do {c}º aluno: ')
                n1 = float(input(f'Digite a 1ª nota: '))
                n2 = float(input(f'Digite a 2ª nota: '))
                soma = n1 + n2
                media = soma / 2
                print('\n\033[1;45m RESUMO:\033[m\n')
                print(f'NOME DO ALUNO: {nome.upper()}')
                print(f'1ª NOTA: {n1}')
                print(f'2ª NOTA: {n2}')
                print(f'MÉDIA: {media}')
                if media > 7.0:
                    print(f'MÉDIA {media}, parabéns {nome}, você foi \033[1;32mAPROVADO.\033[m')
                elif media >= 5.0 and media < 7.0:
                    print(f'MÉDIA {media}, {nome}, você ficou em \033[1;33mRECUPERAÇÃO.\033[m')
                else:
                    print(f'MÉDIA {media}, {nome}, você está \033[1;31mREPROVADO.\033[m')
            print('-' * 15, ' FIM DO EXERCIIO ', '-' * 15)

        case 8:
            print('\033[1;32mTITULO: Conversor de Medidas\033[m\n')

            for c in range(1, 4):
                print(f'--------------- EXERCÍCIO Nº {op} ---------------')

                medida = float(input('Digite uma medida em Metros: '))
                km = medida / 1000
                hec = medida / 100
                deca = medida / 10
                metro = medida
                dec = medida * 10
                cm = medida * 100
                mm = medida * 1000
                print('\n\033[1;45m RESUMO:\033[m\n')
                print(f'{medida} metros equivalem a: ')
                print(f'{km} Kilômetros')
                print(f'{hec} Hectômetros')
                print(f'{deca} Decâmetros')
                print(f'\033[1;32m{metro}\033[m Metros')
                print(f'{dec} Decímetros')
                print(f'{cm} Centìmetros')
                print(f'{mm} Milímetros')
            print('-' * 15, ' FIM DO EXERCIIO ', '-' * 15)
        case 9:
            print('\033[1;32mTITULO: Maior e Menor idade\033[m\n')
            totmenor = 0
            totmaior = 0
            for c in range(1, 6):
                print(f'--------------- EXERCÍCIO Nº {op} ---------------')

                atual = int(input('Digite o ano atual: '))
                nasc = int(input('Digite o ano de seu nascimento: '))
                idade = atual - nasc

                if idade >= 18:
                   totmaior = totmaior + 1
                   print(f'TOTAL DE PESSOAS MAIOR DE IDADE: {totmaior} ')
                elif idade < 18:
                   totmenor = totmenor + 1
                   print(f'TOTAL DE PESSOAS MENOR DE IDADE: {totmenor} ')
                else:
                    print('Você digitou dados inválidos.')
            print('\n\033[1;45m RESUMO:\033[m\n')
            print(f'TOTAL DE PESSOAS MAIOR DE IDADE: {totmaior} ')
            print(f'TOTAL DE PESSOAS MENOR DE IDADE: {totmenor} ')
            print('-' * 15, ' FIM DO EXERCIIO ', '-' * 15)
        case 10:
            print('\033[1;32mTITULO: Conversor de Moedas\033[\n')
            for c in range(1, 3):
                print(f'--------------- EXERCÍCIO Nº {op} ---------------')
                din = float(input('Digite o valor em Real R$: '))
                dh = float(input('Digite o valor do Dolar hoje S$: '))
                ien = float(input('Digite o valor do ien hoje: Y$: '))
                d = din / dh
                y = din / ien
                print('\n\033[1;45m RESUMO:\033[m\n')
                print(f'R$ {din: .2f} = S$ \033[1;34m{d: .2f} dolares\033[m e Y$ \033[1;35m{y: .2f}\033[m iens hoje.')
                print('-' * 15, ' FIM DO EXERCIIO ', '-' * 15)
        case 11:
            print('\033[1;32mTITULO: Tabuada\033[m\n')
            print(f'--------------- EXERCÍCIO Nº {op} ---------------')
            cont = 1

            num = int(input('Digite a tabuada desejada: '))
            print('\n\033[1;45m RESUMO:\033[m\n')
            for c in range(1, 11):
                resu = num * c
                print(f'{num} X {c} = {resu}')
            print('-' * 15, ' FIM DO EXERCIIO ', '-' * 15)

        case 12:
            print('\033[1;32mTITULO: Calcular Pintura\033[m\n')
            print(f'--------------- EXERCÍCIO Nº {op} ---------------')
            l = float(input('Digite a largura da parede: '))
            a = float(input('Digite altura da parede: '))
            area = l * a
            print('\n\033[1;45m RESUMO:\033[m\n')
            print(f'LARGURA DA PAREDE: {l} METROS.')
            print(f'ALTURA DA PAREDE: {a} METROS.')
            print(f'ÁREA TOTAL: {area: .2f} M²')
            print(f'Será necessário \033[1;32m{area / 2}\033[m litros de Tinta para pintar a parede.')
            print('-' * 15, ' FIM DO EXERCIIO ', '-' * 15)

        case 13:
            print('\033[1;32mTITULO: Calcular Desconto\033[1;32m\n')
            print(f'--------------- EXERCÍCIO Nº {op} ---------------')
            for c in range(1, 3):
                v = float(input('Digite o valor bruto: R$ '))
                pdesc = float(input('Digite o percentual de desconto: '))
                pdesc = v * pdesc / 100
                vl = v - pdesc
                print('\n\033[1;45m RESUMO:\033[m\n')
                print(f'VALOR BRUTO: R$ {v} REAIS.')
                print(f'PERCENTUAL DE DESCONTO: {pdesc} %')
                print(f'TOTAL LIQUIDO: R$ {vl} REAIS.')
                print('-' * 15, ' FIM DO EXERCIIO ', '-' * 15)

        case 14:
            print('\033[1;32mTITULO: Reajuste Salarial\033[m\n')
            print(f'--------------- EXERCÍCIO Nº {op} ---------------')
            for c in range(1, 3):
                nome = input('Digite o nome do Funcionário: ')
                sal = float(input(f'Digite o salário do funcionário: {nome.strip().upper()} '))
                aum = float(input('Digite a porcentagem de aumento: '))
                tot = sal + (sal * aum / 100)
                print('\n\033[1;45m RESUMO:\033[m\n')
                print(f'NOME DO FUNCIONÁRIO: \033[1;33m{nome.strip().upper()}\033[m')
                print(f'SALÁRIO ANTERIOR: \033[1;33mR$ {sal: .2f}\033[m Reais')
                print(f'PORCENTAGEM DE AUMENTO: \033[1;33m{aum} %\033[m')
                print(f'SALÁRIO NOVO: \033[1;33mR$ {tot: .2f}\033[m Reais.')
                print('-' * 15, ' FIM DO EXERCIIO ', '-' * 15)
        case 15:
            print('\033[1;32mTITULO: Conversor de temperatura.\033[m\n')
            print(f'--------------- EXERCÍCIO Nº {op} ---------------')

            for cont in range(1, 3):

                temp = input('Escolha o tipo de conversão (C x F) ou (F x C): ')
                if temp == 'c':
                    graus = float(input('Digite a temperatura em graus Cº : '))
                    fa = (graus * 1.8) + 32
                    print('\n\033[1;45m RESUMO:\033[m\n')
                    print(f'\033[1;33m{graus}º\033[m graus Celsios = \033[1;33m{fa: .2f}º\033[m graus Fahrenheit')

                elif temp == 'f':
                    graus = float(input('Digite a temperatura em graus Fº : '))
                    fa = (graus - 32) / 1.8
                    print('\n\033[1;45m RESUMO:\033[m\n')
                    print(f'\033[1;33m{graus}º\033[m graus Fahrenheit = \033[1;33m{fa: .2f}º\033[m graus Celsos')

                else:
                    print('Você digitou errado, opções válidas c ou f')
            print('-' * 15, ' FIM DO EXERCIIO ', '-' * 15)
        case 16:
            print('\033[1;32mTITULO: Aluguel de carro\033[m\n')
            print(f'--------------- EXERCÍCIO Nº {op} ---------------')
            for c in range(1, 3):
                km = float(input('Qual a distância percorrida em km ? '))
                dias = int(input('Quantos dias de aluguel ? '))
                totpagar = (dias * 60) + (km * 0.15)

                print('\n\033[1;45m RESUMO:\033[m\n')
                print(f'DISTÂNCIA PERCORRIDA: {km} Km ')
                print(f'DIAS DE ALUGUEL: {dias} Dias ')
                print('CUSTO DIÁRIA: R$ 60,00 Reais')
                print('CUSTO KM RODADO R$: 0.15 Centavos')
                print(f'TOTAL A PAGAR R$: {totpagar} Reais')
                print('-' * 15, ' FIM DO EXERCIIO ', '-' * 15)
        case 17:
            print('\033[1;32mTITULO: Sorteio\033[m\n')
            print(f'--------------- EXERCÍCIO Nº {op} ---------------')
            lista = []
            for c in range(1, 5):
                nome = input(f'Digite o {c}º Nome: ')
                lista.append(nome.upper())

                print(lista)
                escolha = random.choice(lista)
            print('\n\033[1;45m RESUMO:\033[m\n')
            print(f'O escolhido foi: {escolha}')
            print('-' * 15, ' FIM DO EXERCIIO ', '-' * 15)
        case 18:
            print('\033[1;32mTÍTULO: Analize de texto\033[m\n')
            for c in range(1, 4):
                frase = input('Digite uma frase: ').strip()
                print('\n\033[1;45m RESUMO:\033[m\n')
                print(f'FRASE EM MAIÚSCULO: {frase.upper()}')
                print(f'FRASE EM MINÚSCULO: {frase.lower()}')
                print(f'TOTAL DE LETRAS NA FRASE: {len(frase) - frase.count(" ")}')
            print('-' * 15, ' FIM DO EXERCIIO ', '-' * 15)
        case 19:
            print('\033[1;32mTÍTULO: SEPARANDO DÍGITOS DE UM NÚMERO.\033[m\n')
            for c in range(1, 5):
                num = int(input(f'Digite o {c}º número: '))
                u = num // 1 % 10
                d = num // 10 % 10
                ce = num // 100 % 10
                m = num // 1000 % 10
                print(f'UNIDADE: {u}')
                print(f'DEZENA: {d}')
                print(f'CENTENA: {ce}')
                print(f'MILHAR: {m}')
            print('-' * 15, ' FIM DO EXERCIIO ', '-' * 15)
        case 20:
            print('\033[1;32mTÍTULO: Manipulando strings\033[m\n')
            for c in range(1, 4):
                frase = str(input('Digite uma frase: ')).strip().upper()
                print('\n\033[1;45m RESUMO:\033[m\n')
                print(f'LETRA A APARECE {frase.count("A")}')
                print(f'LETRA E APARECE {frase.count("E")}')
                print(f'LETRA I APARECE {frase.count("I")}')
                print(f'LETRA O APARECE {frase.count("O")}')
                print(f'LETRA U APARECE {frase.count("U")}')
                print(f'LETRA A APARECE NA 1ª VEZ NA POSIÇÃO {frase.find("A") + 1}')
                print(f'LETRA E APARECE NA 1ª VEZ NA POSIÇÃO {frase.find("E") + 1}')
                print(f'LETRA I APARECE NA 1ª VEZ NA POSIÇÃO {frase.find("I") + 1}')
                print(f'LETRA O APARECE NA 1ª VEZ NA POSIÇÃO {frase.find("O") + 1}')
                print(f'LETRA U APARECE NA 1ª VEZ NA POSIÇÃO {frase.find("U") + 1}')
                print(f'LETRA A APARECE NA ULTIMA VEZ NA POSIÇÃO {frase.rfind("A") + 1}')
                print(f'LETRA E APARECE NA ULTIMA VEZ NA POSIÇÃO {frase.rfind("E") + 1}')
                print(f'LETRA I APARECE NA ULTIMA VEZ NA POSIÇÃO {frase.rfind("I") + 1}')
                print(f'LETRA O APARECE NA ULTIMA VEZ NA POSIÇÃO {frase.rfind("O") + 1}')
                print(f'LETRA U APARECE NA ULTIMA VEZ NA POSIÇÃO {frase.rfind("U") + 1}')
            print('-' * 15, ' FIM DO EXERCIIO ', '-' * 15)
        case 21:
            print('\033[1;32mTÍTULO: PRIMEIRO E ULTIMO NOME\033[m\n')
            for c in range(1, 4):
                nome = str(input('Digite seu nome completo: ')).strip().upper()
                n = nome.split()
                print('\n\033[1;45m RESUMO:\033[m\n')
                print(f'PRIMEIRO NOME: {n[0]}')
                print(f'ULTIMO NOME: {n[len(n)-1]}')
            print('-' * 15, ' FIM DO EXERCIIO ', '-' * 15)
        case 22:
            from random import randint
            print('\033[1;32mTITULO: JOGO ADIVINHE O NÚMERO ENTRE 0 E 5.\033[m\n')
            for c in range(1, 4):
                computador = randint(0, 5)
                print(computador)
                print('\n\033[1;45m RESUMO:\033[m\n')
                num = int(input('Meu número escolhido é: '))
                print('Processando...')
                time.sleep(2)
                #print(computador)
                if num == computador:
                    print('Parabens, você acertou o meu número.')
                    o = str(input('Vamos jogar de novo?')).strip().lower()
                    if o == 's':
                        resp = int(input(f'Deseja continuar? \033[1;31;40m99\033[m Para finalizar. --> '))
                    else:
                        print('Digite 99 no menu principal para sair!')


                else:
                    print(f'Você errou {c} de 3 tentativas!')
                    if c == 3:
                        print('Fim de jogo, você errou as 3 tentativas.')
            print('-' * 15, ' FIM DO EXERCIIO ', '-' * 15)
        case 23:
            print('\033[1;32mTITULO: VELOCIDADE MAXIMA PERMITIDA\033[m\n')
            for c in range(1, 4):
                vel = float(input('Digite a velocidade do veículo:'))
                vlm = 80.00
                multa = 7.00
                va = vel - vlm
                if vel <= 80.00:
                    print('\n\033[1;45m RESUMO:\033[m\n')
                    print(f'VELOCIDADE ATUAL: {vel: .2f} Km/h')
                    print(f'VELOCIDADE MÁXIMA PERMITIDA: {vlm: .2f} Km/h')
                    print('\033[1;35;40mVocê está dentro da lei, Boa viajem!\033[m')
                elif vel > 80.00:
                    print('\n\033[1;45m RESUMO:\033[m\n')
                    print(f'VELOCIDADE ATUAL: {vel: .2f} Km/h')
                    print(f'VELOCIDADE MÁXIMA PERMITIDA: {vlm: .2f} Km/h')
                    print(f'Você está {va: .2f} Km/h ACIMA DO PERMITIDO. ')
                    print(f'\033[1;35;40mVOCÊ FOI MULTADO EM R$ {va * multa: .2f} Reais\033[m')
                else:
                    print("Você Digitou dados errados.")
            print('-' * 15, ' FIM DO EXERCIIO ', '-' * 15)
        case 24:
            print('\033[1;32mTITULO: JOGO DO PAR OU IMPAR\033[m\n')
            from random import randint
            comp = randint(1, 10)

            for c in range(1, 4):
                num = int(input('Escolha seu número, PAR ou IMPAR ? '))
                tot = comp + num
                if tot % 2 == 0:
                    print('Deu PAR')
                    if comp % 2 == 0 and num % 2 == 1:
                        print('O seu Adversário Ganhou !')
                    else:
                        print(f'{tot} é PAR - VOCÊ GANHOU !!!')
                elif tot % 2 == 1:
                    print('Deu IMPAR')
                    if comp % 2 == 1 and num % 2 == 0:
                        print('O seu Adversário Ganhou !')
                    if comp % 2 == 0 and num % 2 == 1:
                        print(f'{tot} é PAR - VOCÊ GANHOU !!!')

                else:
                    print('Deu EMPATE - Joguem novamente.')

            print('-' * 15, ' FIM DO EXERCIIO ', '-' * 15)
        case 25:
            print('\033[1;32mTITULO: CALCULAR UMA VIAJEM\033[m\n')
            pp = 0.00
            for c in range(1, 4):
                d = float(input('Qual a distancia da viajem? :'))
                if d <= 200:
                    pp = 0.50
                    print('\n\033[1;45m RESUMO:\033[m\n')
                    print(f'DISTANCIA PERCORRIDA: {d} Km')
                    print(f'VALOR POR KM PERCORRIDO: R$ {pp: .2f} CENTAVOS.')
                    print(f'\033[1;33;40mVALOR DA VIAJEM R$ {pp * d: .2f} REAIS\033[m')
                elif d > 200:
                    pp = 0.45
                    print('\n\033[1;45m RESUMO:\033[m\n')
                    print(f'DISTANCIA PERCORRIDA: {d} Km')
                    print(f'VALOR POR KM PERCORRIDO: R$ {pp: .2f} CENTAVOS.')
                    print(f'\033[1;33;40mVALOR DA VIAJEM R$ {pp * d: .2f} REAIS\033[m')
            print('-' * 15, ' FIM DO EXERCIIO ', '-' * 15)
        case 26:
            print('\033[1;32mTITULO: SABER SE O ANO É BISSEXTO.\033[m\n')

            for c in range(1, 4):
                from datetime import date

                ano = int(input('Digite o ano desejado: '))
                if ano == 0:
                    ano = date.today().year

                if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
                    print('\n\033[1;45m RESUMO:\033[m\n')
                    print(f'\033[1;33;40mO ANO {ano} É BISSEXTO.\033[m')
                else:
                    print('\n\033[1;45m RESUMO:\033[m\n')
                    print(f'\033[1;33;40mO ANO {ano} NÃO É BISSEXTO.\033[m')
                print('-' * 15, ' FIM DO EXERCIIO ', '-' * 15)
        case 27:
            print('\033[1;32mTITULO: IDENTIFICAR MENOR E MAIOR NÚMERO.\033[m\n')

            for c in range(1, 4):
                n1 = int(input(f'Digite o 1º número: '))
                n2 = int(input(f'Digite o 2º número: '))
                n3 = int(input(f'Digite o 3º número: '))
                lista = [n1, n2, n3]
                lista2 = sorted(lista)
                print('\n\033[1;45m RESUMO:\033[m\n')
                print(f'\033[1;33mMENOR NÚMERO = {lista2[0]}\033[m')
                print(f'\033[1;33mNÚMERO INTERMEDIÁRIO = {lista2[1]}\033[m')
                print(f'\033[1;33mMAIOR NÚMERO = {lista2[-1]}\033[m ')
            print('-' * 15, ' FIM DO EXERCIIO ', '-' * 15)

        case 28:
            print('\033[1;32mTITULO: AUMENTO SALARIAL.\033[m\n')

            for c in range(1, 4):
                sal = float(input('Digite o salário do funcionário: '))

                print('\n\033[1;45m RESUMO:\033[m\n')
                if sal >= 5000.00:
                    aum1 = sal * 10 / 100
                    print(f'SALARIO ANTERIOR R$ {sal: .2f} REAIS')
                    print(f'AUMENTO DE 10% = R$ {aum1: .2f} REAIS')
                    print(f'SALARIO ATUALIZADO R$ {sal + aum1: .2f} REAIS')
                elif sal < 5000.00:
                    aum1 = sal * 15 / 100
                    print(f'SALARIO ANTERIOR R$ {sal: .2f} REAIS')
                    print(f'AUMENTO DE 15% = R$ {aum1: .2f} REAIS')
                    print(f'SALARIO ATUALIZADO R$ {sal + aum1: .2f} REAIS')
                else:
                    print('Você digitou algum valor errado !')
            print('-' * 15, ' FIM DO EXERCIIO ', '-' * 15)
        case 29:
            print('\033[1;32mTITULO: CONVERSOR DE BASES NUMÉRICAS.\033[m\n')
            for c in range(1, 4):
                num = int(input('Digite um número inteiro qualquer: '))
                print('''ESCOLHA A BASE DESEJADA: 
                [ 1 ] BINÁRIA
                [ 2 ] OCTODECIMAL
                [ 3 ] HEXADECIMAL''')
                op = int(input('\nDigite sua opção: '))
                print('\n\033[1;45m RESUMO:\033[m\n')
                if op == 1:
                    print(f'{num} EM BASE BINÁRIA = {bin(num)[2:]}')
                elif op == 2:
                    print(f'{num} EM BASE OCTADECIMAL = {oct(num)[2:]}')
                elif op == 3:
                    print(f'{num} EM BASE HEXADECIMAL = {hex(num)[2:]}')
                else:
                    print('Você digitou algo errado.')
            print('-' * 15, ' FIM DO EXERCIIO ', '-' * 15)
        case 30:
            print('\033[1;32mTITULO: ALISTAMENTO MILITAR.\033[m\n')
            for c in range(1, 4):
                from datetime import date
                atual = date.today().year
                nome = str(input('Digite seu nome completo: '))
                nasc = int(input('Digite o ano de seu nascimento: '))
                idade = atual - nasc
                alis = nasc + 18
                print('\n\033[1;45m RESUMO:\033[m\n')
                if idade < 18:
                    print(f'NOME: {nome}')
                    print(f'ANO ATUAL: {atual}')
                    print(f'IDADE: {idade}')
                    print(f'ANO DO ALISTAMENTO: {alis}')
                    print(f'FALTAM {18 - idade} ANOS PARA SEU ALISTAMENTO.')
                    print(f'VOLTE NO ANO DE {alis}')
                elif idade > 18:
                    print(f'NOME: {nome}')
                    print(f'ANO ATUAL: {atual}')
                    print(f'IDADE: {idade}')
                    print(f'ANO DO ALISTAMENTO: {alis}')
                    print(f'PASSARAM {alis - nasc} ANOS DO SEU ALISTAMENTO.')
                    print(f'DEVERIA TER SE ALISTADO NO ANO DE {nasc + 18}')
                else:
                    print(print(f'NOME: {nome}'))
                    print(f'VOCÊ NASCEU EM {nasc} - ESTÁ NO ANO DE SEU ALISTAMENTO.')
                print('-' * 15, ' FIM DO EXERCIIO ', '-' * 15)
        case 31:
            from datetime import date

            print('\033[1;32mMEDIA ESCOLAR.\033[m\n')
            for c in range(1, 4):
                atual = date.today().year
                nome = str(input('Digite o nome do aluno: '))
                nasc = int(input('Digite o ano nascimento: '))
                n1 = float(input('Digite a 1ª nota: '))
                n2 = float(input('Digite a 2ª nota: '))
                media = (n1 + n2) / 2
                if media >= 7.00:
                    print('\n\033[1;45m RESUMO:\033[m\n')
                    print(f'NOME DO ALUNO: {nome.strip().upper()}')
                    print(f'ANO DE EXERCICIO: {atual}')
                    print(f'1ª NOTA: {n1}')
                    print(f'2ª NOTA: {n2}')
                    print(f'MÉDIA FINAL: {media: .2f}')
                    print(f'\033[1;33;40m{nome.upper()}, você foi APROVADO, parabens.\033[m')
                elif media >= 5.00 and media < 7.00:
                    print('\n\033[1;45m RESUMO:\033[m\n')
                    print(f'NOME DO ALUNO: {nome.strip().upper()}')
                    print(f'ANO DE EXERCICIO: {atual}')
                    print(f'1ª NOTA: {n1}')
                    print(f'2ª NOTA: {n2}')
                    print(f'MÉDIA FINAL: {media: .2f}')
                    print(f'\033[1;33;40m{nome.upper()}, você está em RECUPERAÇÃO, estude mais.\033[m')
                elif media < 5.00:
                    print('\n\033[1;45m RESUMO:\033[m\n')
                    print(f'NOME DO ALUNO: {nome.strip().upper()}')
                    print(f'ANO DE EXERCICIO: {atual}')
                    print(f'1ª NOTA: {n1}')
                    print(f'2ª NOTA: {n2}')
                    print(f'MÉDIA FINAL: {media: .2f}')
                    print(f'\033[1;33;40m{nome.upper()}, você foi REPROVADO.\033[m')
                else:
                    print('Você digitou algo errado, recomece o exercicio.')
                print('-' * 15, ' FIM DO EXERCIIO ', '-' * 15)
        case 32:
            from datetime import date
            print('\033[1;32mTITULO: CLASSIFICANDO ATLETAS.\033[m\n')
            for c in range(1,4):
                nome = str(input('Digite o nome do atleta: ').strip())
                atual = date.today().year
                nasc = int(input('Digite o ano nascimento do atleta: '))
                idade = atual - nasc
                if idade > 0 and idade <= 7:
                    print('\n\033[1;45m RESUMO:\033[m\n')
                    print(f'NOME DO ATLETA: \033[1;32m{nome.upper()}\033[m')
                    print(f'DATA NASCIMENTO: {nasc} => IDADE: {idade} ANOS')
                    print('CLASSIFICAÇÃO: \033[1;32mMIRIM\033[m')
                elif idade > 7 and idade <= 12:
                    print('\n\033[1;45m RESUMO:\033[m\n')
                    print(f'NOME DO ATLETA: \033[1;32m{nome.upper()}\033[m')
                    print(f'DATA NASCIMENTO: {nasc} => IDADE: {idade} ANOS')
                    print('CLASSIFICAÇÃO: \033[1;32mINFANTIL\033[m')
                elif idade > 12 and idade <= 18:
                    print('\n\033[1;45m RESUMO:\033[m\n')
                    print(f'NOME DO ATLETA: \033[1;32m{nome.upper()}\033[m')
                    print(f'DATA NASCIMENTO: {nasc} => IDADE: {idade} ANOS')
                    print('CLASSIFICAÇÃO: \033[1;32mJUNIOR\033[m')
                elif idade > 18 and idade <= 21:
                    print('\n\033[1;45m RESUMO:\033[m\n')
                    print(f'NOME DO ATLETA: \033[1;32m{nome.upper()}\033[m')
                    print(f'DATA NASCIMENTO: {nasc} => IDADE: {idade} ANOS')
                    print('CLASSIFICAÇÃO: \033[1;32mADULTO\033[m')
                elif idade > 21 and idade <= 35:
                    print('\n\033[1;45m RESUMO:\033[m\n')
                    print(f'NOME DO ATLETA: \033[1;32m{nome.upper()}\033[m')
                    print(f'DATA NASCIMENTO: {nasc} => IDADE: {idade} ANOS')
                    print('CLASSIFICAÇÃO: \033[1;32mSENIOR\033[m')
                elif idade > 35 and idade <= 60:
                    print('\n\033[1;45m RESUMO:\033[m\n')
                    print(f'NOME DO ATLETA: \033[1;32m{nome.upper()}\033[m')
                    print(f'DATA NASCIMENTO: {nasc} => IDADE: {idade} ANOS')
                    print('CLASSIFICAÇÃO: \033[1;32mSENIOR\033[m')
                else:
                    print('Você não tem mais idade para ficar jogando bola, vai ver NETFLIX')
                print('-' * 15, ' FIM DO EXERCIIO ', '-' * 15)
        case 33:
            print('\033[1;32mTITULO: PAGAMENTO EM LOJA.\033[m\n')
            for c in range(1, 4):
                nome = str(input('Digite o nome do cliente: ').strip())
                vl = float(input('Digite o valor da compra R$ '))
                print('===========================================')
                print('[ 1 ] PGTO A VISTA 10% DESCONTO')
                print('[ 2 ] PGTO CARTAO 1X 5% DESCONTO')
                print('[ 3 ] PGTO CARTAO 2X PREÇO NORMAL')
                print('[ 4 ] PGTO CARTAO 3X 20% ACRESCIMO')
                print('===========================================\n')

                esc = int(input('Escolha a forma de pagamento: '))
                vista = vl - vl * (10 / 100)
                cartao1 = vl - vl * (5 / 100)
                cartao2 = vl
                cartao3 = vl + vl * (20/100)
                if esc == 1:
                    print('\n\033[1;45m RESUMO:\033[m\n')
                    print(f'NOME DO CLIENTE: {nome.upper()}')
                    print(f'OPÇÃO DE PAGAMENTO: {esc}')
                    if esc == 1:
                        print('A VISTA')
                    elif esc == 2:
                        print('CARTÃO 1X')
                    elif esc == 3:
                        print('CARTÃO 2X')
                    elif esc == 4:
                        print('CARTÃO 3X')
                    else:
                        print('Você Digitou uma opção errada, verifique.')

                if esc == 2:
                    print('\n\033[1;45m RESUMO:\033[m\n')
                    print(f'NOME DO CLIENTE: {nome.upper()}')

                    if esc == 1:
                        print('OPÇÃO DE PAGAMENTO: A VISTA')
                    elif esc == 2:
                        print('OPÇÃO DE PAGAMENTO: CARTÃO 1X')
                    elif esc == 3:
                        print('OPÇÃO DE PAGAMENTO: CARTÃO 2X')
                    elif esc == 3:
                        print('OPÇÃO DE PAGAMENTO: CARTÃO 3X')
                    else:
                        print('Você Digitou uma opção errada, verifique.')

                if esc == 3:
                    print('\n\033[1;45m RESUMO:\033[m\n')
                    print(f'NOME DO CLIENTE: {nome.upper()}')
                    print(f'OPÇÃO DE PAGAMENTO: {esc}')
                    if esc == 1:
                        print('A VISTA')
                    elif esc == 2:
                        print('CARTÃO 1X')
                    elif esc == 3:
                        print('CARTÃO 2X')
                    elif esc == 3:
                        print('CARTÃO 3X')
                    else:
                        print('Você Digitou uma opção errada, verifique.')

                if esc == 4:
                    print('\n\033[1;45m RESUMO:\033[m\n')
                    print(f'NOME DO CLIENTE: {nome.upper()}')
                    print(f'OPÇÃO DE PAGAMENTO: {esc}')
                    if esc == 1:
                        print('A VISTA')
                    elif esc == 2:
                        print('CARTÃO 1X')
                    elif esc == 3:
                        print('CARTÃO 2X')
                    elif esc == 3:
                        print('CARTÃO 3X')
                    else:
                        print('Você Digitou uma opção errada, verifique.')

            print('-' * 15, ' FIM DO EXERCIIO ', '-' * 15)
        case 34:
            print('\033[1;32mTITULO: JOGO PEDRA, PAPEL OU TESOURA.\033[m\n')
            import random
            for c in range(1, 4):
                print('========================================')
                print(f'{c}ª RODADA!')
                print('[ 1 ] PEDRA')
                print('[ 2 ] PAPEL')
                print('[ 3 ] TESOURA')
                print('========================================')
                lista = [1, 2, 3]
                jogador = int(input('JOGADOR FAÇA SUA ESCOLHA: '.strip()))
                computador = random.choice(lista)
                time.sleep(2)
                print('JÓ')
                time.sleep(2)
                print('KEN')
                time.sleep(2)
                print('PÔ !!!')
                print('\n\033[1;45m RESUMO:\033[m\n')
                if jogador == 1 and computador == 1:
                    print('JOGADOR E COMPUTADOR COLOCARAM PEDRA')
                    print('\033[1;34mRODADA EMPATADA\033[m')
                elif jogador == 2 and computador == 2:
                    print('JOGADOR E COMPUTADOR COLOCARAM PAPEL')
                    print('\033[1;34mRODADA EMPATADA\033[m')
                elif jogador == 3 and computador == 3:
                    print('JOGADOR E COMPUTADOR COLOCARAM TESOURA')
                    print('\033[1;34mRODADA EMPATADA\033[m')
                elif jogador == 1 and computador == 2:
                    print('JOGADOR COLOCOU PEDRA')
                    print('COMPUTADOR COLOCOU PAPEL')
                    print('PAPEL EMBRULHA PEDRA - \033[1;34mCOMPUTADOR GANHOU\033[m')
                elif jogador == 2 and computador == 3:
                    print('JOGADOR COLOCOU PAPEL')
                    print('COMPUTADOR COLOCOU TESOURA')
                    print('TESOURA CORTA O PAPEL - \033[1;34mCOMPUTADOR GANHOU\033[m')
                elif jogador == 3 and computador == 1:
                    print('JOGADOR COLOCOU TESOURA')
                    print('COMPUTADOR COLOCOU PEDRA')
                    print('PEDRA QUEBRA A TESOURA - \033[1;34mCOMPUTADOR GANHOU\033[m')
                    #print('--')
                elif computador == 1 and jogador == 2:
                    print('COMPUTADOR COLOCOU PEDRA')
                    print('JOGADOR COLOCOU PAPEL')
                    print('PAPEL EMBRULHA PEDRA - \033[1;34mJOGADOR GANHOU\033[m')
                elif computador == 2 and jogador == 3:
                    print('COMPUTADOR COLOCOU PAPEL')
                    print('JOGADOR COLOCOU TESOURA')
                    print('TESOURA CORTA O PAPEL - \033[1;34mJOGADOR GANHOU\033[m')
                elif computador == 3 and jogador == 1:
                    print('COMPUTADOR COLOCOU TESOURA')
                    print('JOGADOR COLOCOU PEDRA')
                    print('PEDRA QUEBRA A TESOURA - \033[1;34mJOGADOR GANHOU\033[m')
                else:
                    print('VOCÊ DIGITOU DADOS INVÁLIDOS, RECOMECE !!')
            print('-' * 15, ' FIM DO EXERCIIO ', '-' * 15)


    resp = int(input(f'Deseja continuar? \033[1;31;40m99\033[m Para finalizar. --> '))













