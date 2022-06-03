def _backlog_(n):
    if n > 5:
        return False
    else:
        return True


# function for CGPA check

def _cgpa_(n):
    if n < float(6):
        return False
    else:
        return True


n1 = int(input())
n2 = float(input())



if _backlog_(n1) and _cgpa_(n2):
    print(5 * n2)
else:
    print("Not Selected")
