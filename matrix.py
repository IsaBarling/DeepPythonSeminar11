# Решить задачи, которые не успели решить на семинаре.
# Добавьте ко всем задачам с семинара строки документации и методы вывода
# информации на печать.
# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц


class Matrix:
    """
    Класс Матрица, представляющий матрицу и включающий методы для работы с матрицами.
    """

    def __init__(self, list_of_lists: list[list[int]]):
        """
        Инициализация матрицы с помощью списка списков, где каждый внутренний список представляет строку матрицы.
        :param list_of_lists: Список списков, представляющий матрицу.
        """
        self.list_of_lists = list_of_lists

    def __str__(self):
        """
        Метод для строкового представления матрицы.
        :return: Строковое представление матрицы.
        """
        result = ''
        for row in self.list_of_lists:
            for elem in row:
                result += ''.join(f'{elem}\t')
            result += ''.join('\n')
        return result

    def __eq__(self, other):
        """
        Переопределенный метод сравнения матриц на равенство.
        :param other: Другой объект матрицы для сравнения.
        :return: True, если матрицы равны, иначе False.
        """
        return True if self.list_of_lists == other.list_of_lists else False

    def __add__(self, other):
        """
        Переопределенный метод сложения матриц.
        :param other: Другой объект матрицы для сложения.
        :return: Новая матрица, полученная путем поэлементного сложения текущей и другой матрицы.
        """
        result = []
        row = []
        for i in range(len(self.list_of_lists)):
            for j in range(len(self.list_of_lists[0])):
                row.append(self.list_of_lists[i][j] + other.list_of_lists[i][j])
            result.append(row)
            row = []
        return Matrix(result)

    def __mul__(self, other):
        """
        Переопределенный метод умножения матриц.
        :param other: Другой объект матрицы для умножения.
        :return: Новая матрица, полученная путем умножения текущей и другой матрицы.
        """
        m = len(self.list_of_lists)
        n = len(other.list_of_lists)
        k = len(other.list_of_lists[0])
        result = [[0 for _ in range(k)] for _ in range(m)]
        for i in range(m):
            for j in range(k):
                result[i][j] = sum(self.list_of_lists[i][k] * other.list_of_lists[k][j] for k in range(n))
        return Matrix(result)


if __name__ == '__main__':
    matrix_1 = Matrix([[3, 3, 3], [3, 3, 3], [3, 3, 3]])
    matrix_2 = Matrix([[3, 3, 3], [3, 3, 3], [3, 3, 3]])

    # Сложение матриц
    matrix_sum = matrix_1 + matrix_2
    print(matrix_sum)

    # Умножение матриц
    matrix_mul = matrix_1 * matrix_2
    print(matrix_mul)

    # Сравнение матриц
    if matrix_1 == matrix_2:
        print('Матрицы равны')
    else:
        print('Матрицы не равны')

