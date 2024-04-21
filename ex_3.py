import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def set_x(self, x):
        self.x = x
    
    def set_y(self, y):
        self.y = y
    
    def distance_to(self, other_point):
        return math.sqrt((self.x - other_point.get_x())**2 + (self.y - other_point.get_y())**2)

# Пример использования класса
point1 = Point(1, 2)
point2 = Point(4, 6)

print("Координаты точки 1:", point1.get_x(), ",", point1.get_y())
print("Координаты точки 2:", point2.get_x(), ",", point2.get_y())

print("Расстояние между точками:", point1.distance_to(point2))
