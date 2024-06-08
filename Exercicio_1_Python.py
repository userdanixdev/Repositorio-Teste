# Exercícios:
# Fazer um programa em que deve perguntar o nome, idade e criar uma mensagem dizendo em qual 
# ano irá se aposentar. A idade para aposentar é 65 anos.

nome = input('Me diga seu nome: ')
idade = int(input('Me diga sua idade: '))
ano = str(2024-idade+65)
print('Olá'+ nome + 'Você irá se aposentar em '+ ano + '.')
