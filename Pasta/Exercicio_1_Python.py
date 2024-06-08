# Exercícios:
# Fazer um programa em que deve perguntar o nome, idade e criar uma mensagem dizendo em qual 
# ano irá se aposentar. A idade para aposentar é 65 anos.

nome = input('Me diga seu nome: ') # Variável esperando entrada do usuário em modo string (str)
idade = int(input('Me diga sua idade: '))  # Variável que recebe entrada do usuário com tipo inteiro
ano = str(2024-idade+65)    # variável que recebe str, tipo string com calculos dentro
print('Olá '+ nome + 'Você irá se aposentar em '+ ano + '.')    # Interpolação de variável dentro da função print
# Obs: Sem nomear o tipo da variável ano como str não é possível fazer interpolação.
