'''
Multiple Select Questions (MSQ) could have more than one correct answers. The marks scored by a student in a 
MSQ will be determined by the following conditions:

(1) If the question has cc correct options, each individual correct option carries \cfrac{n}{c} 
c
n
​
  marks
(2) If a student selects any of the wrong options, the marks awarded for the question will be 0.

Calculate the marks obtained by the student and print this as float value.

The input contains four lines.

(1) First line is the number of marks for the question.

(2) Second line contains the number of options for the question.

(3) Third line is a comma-separated sequence of correct options for this question.

(4) Fourth line is a comma-separated sequence of options given by the student.

Write a program to print the number of marks scored by a student.

'''

marks = int(input())
correct_option_count = int(input())
options = input()
C_option = options.split(',')
leng = int(len(C_option))
#print(C_option)
entered_option = input()
E_option = entered_option.split(',')
#print(E_option)

def mark(marks,leng):
    individual_mark = marks/leng
    return individual_mark

def _calculation(E_option,C_option):
    for x in E_option:
        sum = 0
        if x not in C_option:
            return 0.0
        elif x in C_option:
            sum += mark(marks,leng)
    return sum
    
