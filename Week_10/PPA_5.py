class Vector:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.s = 0

    def print_info(self):
        print(f'({self.x},{self.y})')

    def scale(self, s):
        self.s = int(s)
        self.x = self.x * self.s
        self.y = self.y * self.s

    def reflect_about_X(self):
        self.x = self.x
        self.y = -self.y

    def reflect_about_Y(self):
        self.x = -self.x
        self.y = self.y

    def add(self, V):
        v = Vector(0, 0)
        v.x = self.x + V.x
        v.y = self.y + V.y
        return v
