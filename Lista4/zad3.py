def is_palindrome(word):
    if len(word) == 0:
        return True
    if len(word) == 1:
        return True

    if word[len(word)-1] == word[0]:
        return is_palindrome(word[1:-1])
    else:
        return False


print(is_palindrome("abcba"))
