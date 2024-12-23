n = int(input('Введите число от 3 до 20: '))

def get_password(namber):
    password = ''
    for i in range(1, namber):
        for j in range(2, namber):
            if j <= i:
                continue
            if namber % (i + j) == 0:
                password += str(i) + str(j)
    return password


result = get_password(n)
print('Пароль: ', result)