print('Добро пожаловать в числовую угадайку!')


import random
print('Введите правую границу, до которой будем играть:')
x = int(input())
num = random.randint(1, x)



def is_valid(n):
    if 0 <= n <= x:
        return True
    else:
        return False

print('Введите число:')

count = 0
while True:
    n = int(input())
    
    if is_valid(n):
        if n < num:
            print('Ваше число меньше загаданного, попробуйте еще разок:')

        if n > num:
            print('Ваше число больше загаданного, пропробуйте еще раз:')

        count += 1
        if n == num:
            print('Вы угадали за', count, 'попыток, поздравляем!')
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break
    
    else:
        print('А может быть все-таки введем целое число в указанном интервале?')



