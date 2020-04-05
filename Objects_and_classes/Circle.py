class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = self.diameter/2

    def calculate_circumference(self):
        circumference = self.__pi * self.diameter
        return circumference

    def calculate_area(self):
        area = self.radius * self.radius * self.__pi
        return area

    def calculate_area_of_sector(self, angle):
        sector_area = self.calculate_area() * angle/360
        return sector_area


circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
