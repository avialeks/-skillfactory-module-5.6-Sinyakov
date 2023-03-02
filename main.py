field = [['-']*3 for i in range(3)]

def show_field(f):
    print('  0 1 2')
    for i in range(len(field)):
        print(f"{str(i)} {' '.join(field[i])}")


def players_input(f):
    while True:
        while True:
            try:
                x = int(input('Введите цифру от 0 до 2 по горизонтали: '))
            except ValueError:
                print('Вы ввели не цифру')
                continue
            if x < 0 and x > 2:
                print('Вы вышли из диапазона')
                continue
            break
        while True:
            try:
                y = int(input('Введите цифру от 0 до 2 по вертикали: '))
            except ValueError:
                print('Вы ввели не цифру')
                continue
            if y < 0 and y > 2:
                print('Вы вышли из диапазона')
                continue
            break
        if f[y][x] != '-':
            print('Клетка занята')
            continue
        break
    return x, y


def victory(f, chip):
    def check_line(a1, a2, a3, chip):
        if a1 == chip and a2 == chip and a3 == chip:
            return True

    for i in range(3):
        if check_line(f[i][0], f[i][1], f[i][2], chip) or \
                check_line(f[0][i], f[1][i], f[2][i], chip) or \
                check_line(f[0][0], f[1][1], f[2][2], chip) or \
                check_line(f[2][0], f[1][1], f[0][2], chip):
            return True
    return False


# field = [['-'] * 3 for i in range(3)]

count = 0
while True:
    if count % 2 == 0:
        chip = 'x'
    else:
        chip = 'o'
    print()
    show_field(field)
    print()
    y, x = players_input(field)
    field[x][y] = chip
    if count == 9:
        print('Ничья')
    if victory(field, chip):
        print()
        show_field(field)
        print()
        print(f'Поздравляю!!! Победил |{chip}|')
        break
    count += 1
