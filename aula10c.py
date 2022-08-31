from random import randint
from time import sleep
computador = randint (0, 5)
print('Adivinhe o número que eu pensei entre 0 e 5 e tente adivinhar...')
num=int(input('Em que número eu pensei? '))
if num == computador:
    print('Processando...')
    sleep(2)
    print('Parabéns, você acertou!')
elif num != computador:
    print('Processando...')
    sleep(2)
    print('Ixi, não foi dessa vez!Eu pensei no número {}'.format(computador))
