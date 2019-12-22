def is_palindrome(word):
    if len(word) == 0:
        return True
    if len(word) == 1:
        return True

    if word[len(word)-1] == word[0]:
        return is_palindrome(word[1:-1])
    else:
        return False


def is_palindrome_while(word):
    while len(word):
        if len(word) == 0 or len(word) == 1:
            return True
        if word[0] == word[-1]:
            word = word[1:-1]
        else:
            return False



print(is_palindrome("abacba"))
print(is_palindrome_while("abacba"))
