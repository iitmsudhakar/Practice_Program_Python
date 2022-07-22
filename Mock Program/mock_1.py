class Triangle:
    def __init__(self, a, b, c):
        self.a = a;
        self.b = b;
        self.c = c
        if self.a + self.b > self.c and self.a + self.c > self.b and self.c + self.b > self.a:
            self.valid = True
        else:
            self.valid = False

    def is_equilateral(self):
        if self.a == self.b == self.c:
            return True
        else:
            return False

    def is_isosceles(self):
        if self.a == self.b:
            if self.a != self.c:
                return True

        if self.b == self.c:
            if self.b != self.a:
                return True

        if self.a == self.c:
            if self.a != self.b:
                return True
        return False

    def is_scalene(self):
        if self.a != self.b != self.c:
            return True
        else:
            return False
