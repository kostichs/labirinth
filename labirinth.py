import csv


DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left
MY_PATH = '.'
START_POINT = 'o'
EXIT_POINT = 'X'


def walk(row: int, col: int) -> bool:  
    '''
    Эта функция начинает выполнение с указанных параметров row и col и 
    продолжает выполнение до тех пор, пока не найдет последний элемент, обозначенный символом {EXIT_POINT}. 
    Вокруг текущего элемента матрицы проверяются ячейки, чтобы определить, свободна ли ячейка сверху, справА, 
    снизу или слева. Эти возможные пути добавляются в список pathes, и следующая ячейка(ячейки) проверяются рекурсивно. 
    Если существует несколько направлений, то все возможные варианты также добавляются в этот список.
    Если на каком-то вызове функции список pathes оказывается пустым, значит, на этом направлении тупик. Тогда
    функция начинает возвращаться к предыдущим элементам списка pathes, откуда были другие возможные пути (перекрестки).
    Функция помечает каждую новую ячейку при вызове функции символом {START_POINT}, чтобы отслеживать выбранный путь
    и избежать петляния по уже пройденным ходам. 
    Когда найдена конечная точка, рекурсивная функция завершается и каждая ячейка вдоль правильного пути 
    помечается символом {MY_PATH}.

    Параметры:
        row (int): Начальный индекс строки.
        col (int): Начальный индекс столбца.
    
    Возвращает:
        bool: True, если достигнута конечная точка {EXIT_POINT}, в противном случае - False.
    '''
    pathes = []
    for dir in DIRECTIONS:
        if matrix[row + dir[0]][col + dir[1]] == EXIT_POINT or matrix[row + dir[0]][col + dir[1]] == MY_PATH:
            return True
        else:
            matrix[row][col] = START_POINT

    for dir in DIRECTIONS:
        if matrix[row + dir[0]][col + dir[1]] == ' ':
            pathes.append((row + dir[0], col + dir[1]))
    if len(pathes) > 0:
        for i in range(len(pathes)):
            if walk(pathes[i][0], pathes[i][1]):
                matrix[pathes[i][0]][pathes[i][1]] = MY_PATH
                return True
            else: 
                # Убери эту строку, если нужно увидеть,
                # какие тупики попали в обход лабиринта.
                matrix[pathes[i][0]][pathes[i][1]] = ' '


if __name__ == '__main__':
    # Есть два сгенерированных лабиринта.
    maze1 = 'maze-1.csv'
    maze = 'maze.csv'
    # Перевод csv файла в матрицу.
    with open(maze, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        matrix = []
        for row in reader:
            matrix.append(row) 

    # Очистка лабиринта от нулей, чтобы лучше отображались проходы.
    matrix = [[' ' if element == '0' else element for element in row] for row in matrix]
    # По условию, искомая цель всегда находится в предпоследнем ряду в предпоследнем столбце матрицы.
    end = (len(matrix) - 2, len(matrix) - 2)
    matrix[end[0]][end[1]] = EXIT_POINT
    # Запуск рекурсивной функции.
    walk(1, 1)
    # Вывод найденного пути.
    for row in matrix:
        print(' '.join(row))