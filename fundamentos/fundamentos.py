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
