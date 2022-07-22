class Student:
    count = 0

    def __init__(self, name, roll, maths, physics, chemistry):
        Student.count += 1
        self.roll = roll
        self.name = name
        self.maths = maths
        self.physics = physics
        self.chemistry = chemistry


class Group:
    def __init__(self):
        self.members = []

    def add(self, student):
        self.members.append(student)

    def print_members(self):
        for student in self.members:
            print(student.name)


def remove(self, roll):
    if roll in self.members:
        self.members.remove(roll)
    else:
        print('Student not found')


study_group = Group()
study_group.add(Student('Lathika', 1, 100, 90, 80))
study_group.add(Student('Keerthana', 2, 80, 70, 60))
study_group.add(Student('Sourabh', 3, 100, 50, 60))


student = Student('Anish')



