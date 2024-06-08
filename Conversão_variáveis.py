# Exercício: Convertente tipos primitivos
# Obs: Dados de entrada sem conversão são todos strings:

aluno=input('Digite seu nome: ')
periodo_corrente=input('Digite o período corrente: ')
ira=input('Digite seu índice de rendimento acadêmico: ')
laurea=input('informe se vc é laureado da turma: ')
print(type(aluno))
print(type(periodo_corrente))
print(type(ira))
print(type(laurea))

# Segue abaixo com conversão de tipos:

aluno=input('Digite seu nome: ')
periodo_corrente=int(input('Digite o período corrente: '))
ira=float(input('Digite seu índice de rendimento acadêmico: '))
laurea=bool(input(' Informe se vc é laureado da turma: '))
print(type(aluno))
print(type(periodo_corrente))
print(type(ira))
print(type(laurea))

