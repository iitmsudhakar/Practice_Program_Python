class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def distance(self):
        d = (self.x ** 2) + (self.y ** 2)
        d = d ** 0.5
        return d

    def is_origin(self):
        if self.x == 0 and self.y == 0:
            return True
        else:
            return False

    def on_xaxis(self):
        if self.x != 0 and self.y == 0:
            return True
        else:
            return False

    def on_yaxis(self):
        if self.y != 0 and self.x == 0:
            return True
        else:
            return False

    def quadrant(self):
        if self.on_xaxis and self.on_yaxis:
            if self.x > 0 and self.y > 0:
                return "first"
            elif self.x < 0 and self.y > 0:
                return "second"
            elif self.x < 0 and self.y < 0:
                return "third"
            else:
                return "fourth"

    def slope(self):
        if not self.on_yaxis():
            p = self.y / self.x
            return p
