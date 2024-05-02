import random


def greetings(settings):
    print('Добро пожаловать в игру Крестики-Нолики')
    print('Правила:')
    print('1. Игровое поле 3х3')
    print('2. Играют 2-а игрока')
    print('3. В рамках одной игры каждый игрок играет либо Крестиком, либо Ноликом')
    print("Побеждает тот, кто первым собрал вертикальную, горизонтальную или диагональную линию")
    print()
    print('Первый ход назначается случайным образом')
    print('Ход осуществляется путем ввода двух цифр через пробел (номер строки и номер столбца')
    print()
    print(f'Первым ходит: {settings[0][0]}, играет "{settings[0][1]}"')


def show_field(data):
    print('| |1|2|3|')
    print(f'|1|{data[0][0]}|{data[0][1]}|{data[0][2]}|')
    print(f'|2|{data[1][0]}|{data[1][1]}|{data[1][2]}|')
    print(f'|3|{data[2][0]}|{data[2][1]}|{data[2][2]}|')
    pass


def get_players_settings(pl1, pl2):
    first_player = random.randint(1, 2)
    if first_player == 1:
        return [(pl1, 'x'), (pl2, 'o')]
    return [(pl2, 'o'), (pl1, 'x')]


def get_step_data(field):
    x, y = 0, 0
    while True:

        step_player = input(f'{current_step[0]}, ваш ход:').split(' ')
        try:
            x, y = int(step_player[0]), int(step_player[1])
            x, y = x - 1, y - 1

            if 0 <= x < 3 and 0 <= y < 3 and field[x][y] == ' ':
                break
            else:
                print('Неправильный ввод, попробуйте еще раз')
        except ValueError:
            print('Неправильный ввод, попробуйте еще раз')

    return x, y


def check_win(field):
    win = False

    # диагонали
    if field[0][0] == field[1][1] and field[1][1] == field[2][2] and field[2][2] != ' ':
        win = True

    if field[0][2] == field[1][1] and field[1][1] == field[2][0] and field[2][0] != ' ':
        win = True

    # строки
    if field[0][0] == field[0][1] and field[0][1] == field[0][2] and field[0][2] != ' ':
        win = True

    if field[1][0] == field[1][1] and field[1][1] == field[1][2] and field[1][2] != ' ':
        win = True

    if field[2][0] == field[2][1] and field[2][1] == field[2][2] and field[2][2] != ' ':
        win = True

    # колонки
    if field[0][0] == field[1][0] and field[1][0] == field[2][0] and field[2][0] != ' ':
        win = True

    if field[0][1] == field[1][1] and field[1][1] == field[2][1] and field[2][1] != ' ':
        win = True

    if field[0][2] == field[1][2] and field[1][2] == field[2][2] and field[2][2] != ' ':
        win = True

    return win


if __name__ == '__main__':
    data_fields = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    player1 = 'Игрок 1'
    player2 = 'Игрок 2'

    players_settings = get_players_settings(player1, player2)
    greetings(players_settings)
    show_field(data_fields)

    current_step = players_settings[0]

    for step in range(1, 10):
        # ход игрока
        step_data = get_step_data(data_fields)
        x, y = step_data[0], step_data[1]

        # установка значений
        data_fields[x][y] = current_step[1]
        show_field(data_fields)

        # проверка выигрыша
        # возможно окончание игры
        win = check_win(data_fields)

        if win == True:
            print(f'{current_step[0]} выиграл игру')
            break

        # передача хода
        if current_step == players_settings[0]:
            current_step = players_settings[1]
        else:
            current_step = players_settings[0]

    print('Боевая ничья')