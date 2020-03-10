import numpy as np


def check_is_integer(x):
    return x - int(x) == 0


def is_recipe_correct(receipt, article_details):
    for col in range(0, len(receipt)):
        for article in range(0, len(article_details)):
            if receipt[col][1] == article_details[article][0]:
                if article_details[article][0] == 1 and check_is_integer(receipt[col][2]):
                    return False
                break
            elif len(article_details) == article + 1:
                return False
    return True


def whole_price(receipt, article_details, client_id):
    price = 0.0
    for col in range(0, len(receipt)):
        for article in range(0, len(article_details)):
            if receipt[col][1] == article_details[article][0] and receipt[col][0] == client_id:
                price += article_details[article][1] * receipt[col][2]
    return price


receipt = np.array(
    [
        # nr client, nr article, count or weight
        [123, 1234, 10],
        [321, 2000, 5],
        [222, 3000, 10],
        [111, 4444, 0.5],
        [111, 4444, 1]
    ])

article_details = np.array(
    [
        # nr article, price, count or weight(0-count, 1-weight)
        [2000, 10.5, 1],
        [1234, 20, 0],
        [3000, 15, 10],
        [4444, 18, 0]
    ])

# ex1
print(is_recipe_correct(receipt, article_details))

# ex2
print(whole_price(receipt, article_details, 123))