"""
Recebendo dados do usuário

input() -> todo dado recebido via input é do tipo String

Em python, string é tudo que estiver entre:
- Aspas simples:
- Aspas duplas:
- Aspas simples triplas:
- Aspas duplas triplas:

Exemplos:
- Aspas simples -> 'Gabriel Vieira'
- Aspas duplas -> "Gabriel Vieira"
- Aspas simples triplas -> '''Gabriel Vieira'''
"""
# - Aspas duplas triplas -> """Gabriel Vieira"""

#  Entrada de dados
# print ("Qual seu nome? ")
# nome = input() # Input -> Entrada

nome = input("Qual seu nome? ")

# Exemplo de print 'antigo' 2.x
# print('Seja bem-vindo(a) %s' % nome)

# Exemplo de print 'moderno' 3.x
# print('Seja bem-vindo(a) {0}'.format{nome})

# Exemplo de print 'mais atual' 3.7
print(f'Seja bem-vindo(a) {nome}')

# print(Qual sua idade? )
# idade = input()

idade = int(input('Qual sua idade? '))

# Processamento

# Saida
# Exemplo de print 'antigo' 2.x
# print('O %s tem %s anos' % (nome, idade))

# Exemplo de print 'moderno' 3.x
# print('O {0} tem {1} anos'.format(nome, idade))

# Exemplo de print 'mais atual' 3.7
print(f'O {nome} tem {idade} anos')

"""
# int(idae) => cast

Cast é a 'conversão' de um tipo de dado para outro.
"""
print(f'O {nome} nasceu em {2020 - idade}')
