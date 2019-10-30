def if_palindrome(word):
    if len(word) == 0:
        return True
    if len(word) == 1:
        return True

    if word[len(word)-1] == word[0]:
        return if_palindrome(word[1:-1])
    else:
        return False


print(if_palindrome("abcba"))
