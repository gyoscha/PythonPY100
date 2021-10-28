if __name__ == "__main__":

    count_row = 10
    count_col = 10
    matrix = [
        [i * j for j in range(1, count_col)]  # i - строка, j - столбец
        for i in range(1, count_row)
    ]

    for row in range(len(matrix)):   # строки в матрице (получаем идекс строки)
        for col in range(len(matrix[0])):   # столбцы. Всегда сначала идут строки
            print(f'{matrix[row][col]:2}', end=" ")
        print()
