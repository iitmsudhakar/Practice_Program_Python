def check_palindrome(word):
    if len(word) < 1:
        return True
    else:
        if word[0] == word[-1]:
            return check_palindrome(word[1:-1])
        else:
            return False

print(check_palindrome('madamq'))