class Question:
    def __init__(self, statement, marks):
        self.statement = statement
        self.marks = marks

    def print_question(self):
        print(self.statement)

    def update_marks(self, marks):
        self.marks = marks


class MCQ(Question):
    def __init__(self, statement, marks, ops, c_ops):
        super().__init__(statement, marks)
        self.ops = list(ops)
        self.c_ops = list(c_ops)

    def print_question(self):
        super().print_question()
        for i in self.ops:
            print(self.ops)
