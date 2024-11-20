"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

cpf = "52692382846"
cpf_digitos = []

retira_ponto = "-. "
contador = 0

for digito in cpf:
    if contador < 9 and digito not in retira_ponto:
        cpf_digitos.append(digito)
        contador += 1
    else:
        del digito
        continue

contador = 0

while contador < 2:
    qtd_digito_lista_cpf = len(cpf_digitos) + 1
    indice = 0
    digito = 0
    for valores in range(qtd_digito_lista_cpf,1,-1):
        digito += int(cpf_digitos[indice]) * valores
        indice += 1
    
    digito = (digito * 10) % 11


    if digito > 9:
        cpf_digitos.append("0")
    else:
        cpf_digitos.append(str(digito))
    
    contador += 1


cpf_valido = ""

for digito in cpf_digitos:
    cpf_valido += digito

if cpf_valido == cpf:
    print("VALIDO!!!!!")
else:
    print("No validooo")
