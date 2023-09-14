# Tipos Básicos

print(True)  # -> Booleano
print(False)  # -> Booleano
print(1.2 + 1)  # -> Float
print('Aqui eu falo na minha lingua')  # -> String
print('também funciona')  # -> String
print('você é ' + 3 * 'muito ' + 'legal')  # -> String
# print(3 + 'a') -> Ambiguidade
print([1, 2, 3])  # -> Lista
print({'nome': 'Fernando', 'idade': 30, 'salário': 20000.00})  # -> Dicionário
print(None)  # -> Nulo

# Tipos Variáveis

a = 10
b = 5.2
print(a + b)

a = 'agora sou uma string'
print(a)

# print(a + b)

# Comentários de Código

# Minhas variáveis
salario = 3450.45
despesas = 2456.20

"""
A ideia é calcular o quanto
vai sobrar no final do mês

"""
print(salario - despesas)

# print('Fim')
print('Fim de verdade')  # comentário aqui também vale

#  Operadors Aritméticos
# Operadores Binários
print(2 + 3)  # -> Soma
print(4 - 7)  # -> Subtracao
print(2 * 5.3)  # -> Multiplicação
print(9.4 / 3)  # -> Divisão
print(9.4 // 3)  # -> Divisão Inteira
print(5 ** 8)  # -> Potenciacao
print(10 % 3)  # -> Resto

y = 5
# Unário operador pré fixado
print(++y)  # -> Soma
# Unário operador pós fixado
x = 5
# print(x--)    # -> Subtracao


# Desafio 1 Operadores Aritméticos
# Minhas variáveis
salario = 3450.45
despesas = 2456.20

# Resposta
percentual_comprometido = despesas / salario * 100
print(percentual_comprometido)

# Operadores Relacionais

3 > 4  # -> Maior que
4 >= 3  # -> Maior ou igual
1 < 2  # -> Menor que
3 <= 1  # -> Menor ou igual
3 != 2  # -> Diferente
3 == 3  # -> Igual
print(2 == '2')  # -> Igual

# Operadores de Atribuição

a = 3
a = a + 7  # -> Atribuição de Variável

a += 5  # a = a + 5
print(a)

a -= 3  # a = a - 3
print(a)

a *= 2  # a = a * 2
print(a)

a /= 4  # a = a / 4
print(a)

a %= 4  # a = a % 4
print(a)

a **= 8  # a = a ** 8
print(a)

a //= 256  # a = a //
