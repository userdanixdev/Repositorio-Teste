# Exercício 2: Dissecando uma variável
# Faça um programa que leia alguma coisa pelo teclado e mostre na tela seu tipo primitivo 
# e todas as informações possíveis:

a=input('Digite algo: ')  # 'a' variável que irá receber algum digito do teclado pelo usuário
print('O tipo primitivo desse valor é: ',type(a))   # Qual é a classe da entrada do usuário
print('Possui espaços? ',a.isspace())
print('É um número? ',a.isnumeric())
print('É alfabético? ',a.isalpha())
print('É alfanumérico? ',a.isalnum())
print('É maiúscula? ',a.isupper())
print('É Minúscula? ',a.islower())
print('Estpa capitalizada? ',a.istitle())


