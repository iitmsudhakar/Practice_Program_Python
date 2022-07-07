class Student:
    def __init__(self, name, marks):
        self.name = str(name)
        self.marks = int(marks)

    def print_info(self):
        print(f'{self.name};{self.marks}')
