
"""
Задание №5 
📌Дорабатываем класс прямоугольник из прошлого семинара. 
📌Добавьте возможность сложения и вычитания. 
📌При этом должен создаваться новый экземпляр прямоугольника. 
📌Складываем и вычитаем периметры, а не длинну и ширину. 
📌При вычитании не допускайте отрицательных значений.
Задание №6 
📌Доработайте прошлую задачу. 
📌Добавьте сравнение прямоугольников по площади 
📌Должны работать все шесть операций сравнения
"""

class Rectangle:
    '''Класс прямоугольник, с методами расчета периметра и площади фигуры.'''

    def __init__(self, a: int, b: int = None):
        '''Метод инициализации прямоугольника со сторонами a и b.'''
        self.a = a
        self.b = b if b is not None else a

    def perimeter(self):
        '''Метод расчета периметра прямоугольника.'''
        return 2 * (self.a + self.b)

    def __add__(self, other):
        '''Переопределенный дандер метод сложения двух прямоугольников.'''
        new_perimeter = self.perimeter() + other.perimeter()
        new_a = max(self.a, self.b, other.a, other.b)
        new_b = new_perimeter/2 - new_a
        
        return Rectangle(new_a, new_b)

    def __sub__(self, other):
        '''Переопределенный дандер метод вычитания двух прямоугольников.'''
        new_perimeter = max((self.a+self.b)*2, (other.a +other.b)*2) - min((self.a+self.b)*2, (other.a +other.b)*2)
        new_a = min(self.a, self.b, other.a, other.b)
        new_b = new_perimeter/2 - new_a

        return Rectangle(new_a, new_b)

    def __str__(self):
        '''Переопределенный дандер метод строчного выведения экземпляра класса'''
        return f'Прямоугольник {self.a} x {self.b}'

    def area(self):
        '''Метод расчета площади прямоугольника.'''
        return self.a * self.b

    def __eq__(self, other):
        '''Переопределенный дандер метод сравнения на равенство по площади.'''
        return self.area() == other.area()

    def __ne__(self, other):
        '''Переопределенный дандер метод сравнения на неравенство по площади.'''
        return self.area() != other.area()

    def __lt__(self, other):
        '''Переопределенный дандер метод сравнения на меньше по площади.'''
        return self.area() < other.area()

    def __le__(self, other):
        '''Переопределенный дандер метод сравнения на меньше или равно по площади.'''
        return self.area() <= other.area()

    def __gt__(self, other):
        '''Переопределенный дандер метод сравнения на больше по площади.'''
        return self.area() > other.area()

    def __ge__(self, other):
        '''Переопределенный дандер метод сравнения на больше или равно по площади.'''
        return self.area() >= other.area()


if __name__ == '__main__':
    rect_1 = Rectangle(5, 7)
    rect_2 = Rectangle(11, 2)
    rect_3 = Rectangle(3, 4)

    # Проверка сложения прямоугольников
    sum_rect = rect_1 + rect_2
    print(sum_rect)  

    # Проверка вычитания прямоугольников
    sub_rect = rect_2 - rect_3
    print(sub_rect)  

    # Проверка сравнения прямоугольников по площади
    print(rect_1 == rect_2)  
    print(rect_1 != rect_2)  
    print(rect_1 < rect_2)   
    print(rect_1 <= rect_2)  
    print(rect_1 > rect_2)   
    print(rect_1 >= rect_2)  

