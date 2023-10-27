# Tipo inteiro  ->  int
idade = 23
print(type(idade))

# Tipo decimal  ->  float
nota = 8.5
print(type(nota))

# Tipo texto  ->  str
texto = 'Hoje amanheceu 4:30'
print(type(texto))

# Tipo lógico  ->  bool
feriado_hoje = False
print(type(feriado_hoje))


# camelCase
hojeETerca = True
# PascalCase
HojeETerca = True
# snake_case
hoje_e_sabado = False


soma = 1 + 1
print('1 + 1 =', soma)

subtracao = 5 - 4
print('5 - 4 =', subtracao)

multiplicacao = 3 * 7
print('3 * 7 =', multiplicacao)

divisao = 9/6
print('9/6 =', divisao)

divisao_inteira = 9//6
print('9//6 =', divisao_inteira)

resto = 9 % 6    # dividendo - (divisao_inteira * divisor)
print('9 % 6 =', resto)  # 3

exponencial = 5**3
print('5**3 =', exponencial)


# Formatação de texto  -> f string
numero = 2
outro_numero = 7

concatenando1 = str(numero) + str(outro_numero)
concatenando2 = f'{numero}{outro_numero}'

print(concatenando1, concatenando2)

               aula 2

numero = int(input('digite un numero'))

if numero > 0:
    print('e maior numero positivo')

elif numero < 0:
    print('e menor negativo')

else:
    print('eneutro')


ano = int(input("Digite o ano que você nasceu: "))


if ano <= 2005:
    print("é maior de idade")
else:
    print("é menor de idade")


VERSÃO 2:
ano = int(input("Digite o ano que você nasceu: "))

idade = 2023 - ano

if idade >= 18:
    print(f"Você tem {idade} anos, então é maior de idade")
else:
    print(f"Você tem {idade} anos, então é menor de idade")


VERSÃO AVANÇADA APENAS PARA DEIXAR REGISTRADO:

import datetime

ano = int(input("Digite o ano que você nasceu: "))

ano_atual = datetime.datetime.now().year

idade = ano_atual - ano

if idade >= 18:
    print(f"Você tem {idade} anos, então é maior de idade")
else:
    print(f"Você tem {idade} anos, então é menor de idade")

numero = int(input("Digite o numero"))

if numero % 2 == 0:
    print('numero e par')

else:     
    print("numero nao e par")

if numero % 2 == 0:
    print(f'o numero {numero} e par')

else:     
    print("numero nao e par")

              and or

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))


if numero1 > numero2 and numero1 > numero3:
    print(f"O {numero1} é o maior")
elif numero2 > numero1 and numero2 > numero3:
    print(f"O {numero2} é o maior")
elif numero3 > numero2 and numero3 > numero1:
    print(f"O {numero3} é o maior")
else:
    print("Os números são iguais")


letra = str(input("Digite uma letra: "))

if letra == "a" or letra == "b":
    print("Qualquer coisa")

semaforo = str(input("Digite uma cor do sinal de trânsito: "))

if semaforo == 'vermelho':
    print("Pare")
elif semaforo == "amarelo":
    print("Atenção")
elif semaforo == "verde":
    print("Siga")
else:
    print("Inválido")

semaforo = str(input("Digite uma cor do sinal de trânsito: "))

match semaforo:
    case "vermelho":
        print("Pare")
    case "amarelo":
        print("Atenção")
    case "verde":
        print("Siga")
    case _:
        print("Inválido")

ejemplos hechos por mim

numero1 = int(input("digite o numero"))
numero2 = int(input("digite o numero"))

if numero1 > numero2:
    print('numero 1 e menor')

if numero2 > numero1:
    print('numero 2 e maior') 

else:
    print('iguais')   

    
letra = str(input("Digite uma letra: "))
 
if letra == 'f':
    print('femenino')

if letra == 'm':
    print('masculino')

else:
    print("sexo invalido")

QUESTÃO 3:
sexo = str(input("""
Digite o seu sexo: 
F - Feminino
M - Masculino
""")).upper().strip()

if sexo == 'F' or sexo == 'FEMININO':
    print("F - Feminino")
elif sexo == "M" or sexo == 'MASCULINO':
    print("M - Masculino")
else:
    print("Alternativa inválida")


letra = str(input("Digite uma letra: "))
 
if letra == 'a' or letra =='e'or letra== 'i' or letra == '0' or letra == 'u':
    print('e vogal')
else:
    print('e consonate')

QUESTÃO 4:
letra = str(input("Digite uma letra: ")).lower().strip()

if len(letra) == 1:
    if letra in 'aeiou':
        print("é uma vogal")
    elif letra in 'bcdfghjklmnpqrstvxywz':
        print("é uma consoante")
    else:
        print("Caracter inválido, digite uma LETRA meu fi, alfabeto ta ligado?")
else:
    print("Digite apenas UMA letra")

QUESTÃO 5:
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7 and media < 10:
    print("Aprovado")
elif media < 7 and media >= 0:
    print("Reprovado")
elif media == 10:
    print("Aprovado com distinção")
else:
    print("Notas inválidas")

