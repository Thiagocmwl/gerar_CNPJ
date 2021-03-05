from random import randint

cnpj = str(randint(100000000000, 999999999999))

# Primeiro dígito
i = 5
soma = 0
for x in cnpj:
    soma += int(x) * i
    i -= 1
    if i == 1:
        i = 9

primeiro_digito = 11 - (soma % 11) if 11 - (soma % 11) <= 9 else 0
cnpj += str(primeiro_digito)

# Segundo dígito
i = 6
soma = 0
for x in cnpj:
    soma += int(x) * i
    i -= 1
    if i == 1:
        i = 9

segundo_digito = 11 - (soma % 11) if 11 - (soma % 11) <= 9 else 0
cnpj += str(segundo_digito)

# Conclusão
cnpj_formatado = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}'

print(f'CNPJ: {cnpj}')
print(f'CNPJ formatado: {cnpj_formatado}')



