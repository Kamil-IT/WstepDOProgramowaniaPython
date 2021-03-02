from Levenshtein import distance


def LCS(text1, text2):
    db = [[0 for b in range(len(text2) + 1)] for a in range(len(text1) + 1)]
    for a in range(len(text1)):
        prev_row = db[a]
        curr_row = db[a + 1]
        a_char = text1[a]
        for b in range(len(text2)):
            b_char = text2[b]
            if a_char == b_char:
                curr_row[b + 1] = prev_row[b] + 1
                continue
            curr_row[b + 1] = max(curr_row[b], prev_row[b + 1])
    a = len(text1)
    b = len(text2)
    scope = []
    while a > 0 and b > 0:
        a_char = text1[a - 1]
        b_char = text2[b - 1]
        if a_char == b_char:
            a -= 1
            b -= 1
            scope.append(a_char)
            continue
        if db[a - 1][b] > db[a][b - 1]:
            a -= 1
            continue
        b -= 1
    return len(scope)


def LCS_pause(text1, text2):
    max = 0
    actual = 0
    for i in range(len(text1)):
        for j in range(len(text2)):
            if (i + j) >= len(text1):
                if max < actual:
                    max = actual
                actual = 0
                break
            if text1[i + j] == text2[j]:
                actual += 1
            else:
                if max < actual:
                    max = actual
                actual = 0
    return max


# ex3 a
print("ex3 a")
print(LCS_pause("konwalia", "zawalina"))

# ex3 b
print("ex3 b")
print(LCS("ApqBCrDsEF", "tABuCvDEwxFyz"))

# ex3 d
print("ex3 d")
print(distance("marka", "ariada"))
print(
    "Wynosi 4, ponieważ potrzeba co najmniej czterech działań, np.: usunięcia litery m, zamiany k na i oraz dodania d i a.")

