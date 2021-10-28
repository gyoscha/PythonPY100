EMPTY_CEIL = '-'


def init_field(size: int = 3):   # можно в дальнейшем поменять поле
    return [
        [EMPTY_CEIL for _ in range(size)]
        for _ in range(size)
    ]


def player_step(x: int, y: int, symbol: str, field: list):
    set_ceil(field, x, y, symbol)


def enemy_step(x: int, y: int, symbol: str, field: list):
    player_step(x, y, symbol, field)


def get_ceil(field: list, x, y):   # получить одну ячейку
    return field[x][y]


def set_ceil(field: list, x, y, symbol) -> None:
    field[x][y] = symbol


def is_empty_ceil(field: list, x: int, y: int) -> bool:   # проверяем ячейка пустая или нет
    current_ceil = field[x][y]
    # if current_ceil == EMPTY_CEIL:
    #    return True
    # else:
    #    return False

    return True if current_ceil == EMPTY_CEIL else False


def is_win(field: list, symbol: str) -> bool:
    win_combinations = [
        [(1, 1), (1, 2), (1, 3)],   # строки
        [(2, 1), (2, 2), (2, 3)],
        [(3, 1), (3, 2), (3, 3)],

        [(1, 1), (2, 1), (3, 1)],   # столбцы
        [(1, 2), (2, 2), (3, 2)],
        [(1, 3), (2, 3), (3, 3)],

        [(1, 1), (2, 2), (3, 3)],   # диагонали
        [(1, 3), (2, 2), (3, 1)],
    ]

    for win_comb in win_combinations:
        ceil_1 = get_ceil(field, x=win_comb[0][0]-1, y=win_comb[0][1]-1)   # вторая [] отвечает за место x и y в кортеже, который стоит на каком-то месте
        ceil_2 = get_ceil(field, x=win_comb[1][0]-1, y=win_comb[1][1]-1)   # -1 используем для того чтобы x and y были в индексах от 0
        ceil_3 = get_ceil(field, x=win_comb[2][0]-1, y=win_comb[2][1]-1)
        if ceil_1 == ceil_2 == ceil_3 == symbol:
            return True

    return False


def is_available_ceil(field):
    for row in field:
        for ceil in row:
            if ceil == EMPTY_CEIL:
                return True
    return False


if __name__ == '__main__':
    main_field = init_field()
    for row in main_field:
        for ceil in row:
            print(ceil, end=' ')
    print()

