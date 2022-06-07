def _check1(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False

def _check2(year):
    if year % 100 != 0:
        if year % 4 == 0:
            return True
        else:
            return False




def check_leap_year(year):
    if _check1(year) or _check2(year):
        return True
    else:
        return False


print(check_leap_year(2020))