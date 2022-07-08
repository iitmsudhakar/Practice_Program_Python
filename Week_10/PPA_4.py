class Signal:
    def __init__(self, T):
        self.state = 'red'
        self.v = 0
        self.T = int(T)

    def sense(self, nv):
        self.v = int(nv)

    def update(self):
        if self.state == "red":
            if self.v < self.T:
                self.state = "red"
            if self.v >= self.T:
                self.state = "green"
        elif self.state == "green":
            if self.v < self.T:
                self.state = "red"
            if self.v >= self.T:
                self.state = "green"
