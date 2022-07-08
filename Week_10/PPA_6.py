class Country:
    def __init__(self):
        self.name = None
        self.capital = None

    def set_name(self, name):
        self.name = name

    def set_capital(self, capital):
        self.capital = capital

    def display(self):
        print(f'{self.capital} is the capital of {self.name}')


n = int(input())
countries = []
for i in range(n):
    name = input()
    capital = input()
    cnt = Country()
    cnt.set_name(name)
    cnt.set_capital(capital)
    countries.append(cnt)
