import random


def check_limitations(products, solution):
    create = 0
    packing = 0
    for index in range(len(products)):
        create += products[index][0] * solution[index]
        packing += products[index][1] * solution[index]
    if create > total_create_time or packing > total_pack_time:
        return False
    return True


def next_neighborhood(products, current_neighborhood, tabu_list):
    new_solution = current_neighborhood.copy()

    for i in range(5):
        product_to_change = random.randint(0, len(products) - 1)

        new_solution[product_to_change] = new_solution[product_to_change] + 1

        if new_solution not in tabu_list:
            if check_limitations(products, new_solution):
                return new_solution
        else:
            new_solution[product_to_change] = new_solution[product_to_change] - 1
            product_to_change = product_to_change == 0 if 1 else 0
            new_solution[product_to_change] = new_solution[product_to_change] + 1
            if new_solution not in tabu_list:
                if check_limitations(products, new_solution):
                    return new_solution
        new_solution[product_to_change] = new_solution[product_to_change] - 1
        if new_solution not in tabu_list:
            if check_limitations(products, new_solution):
                return new_solution
    for i in range(5):
        new_solution = [random.randint(0, max_chair), random.randint(0, max_table)]
        if new_solution not in tabu_list:
            if check_limitations(products, new_solution):
                return new_solution


def function_value(products, solution):
    value = 0
    for index in range(len(products)):
        value += products[index][2] * solution[index]
    return value


def tabu_search(products):
    tabu_list = []

    neighborhood = [0, 0]
    best_solution = -1
    count_product = neighborhood

    for i in range(1000):
        print(f'Step {i}')
        print(f'Function value: {function_value(products, neighborhood)}, neighborhood: {neighborhood}')
        if function_value(products, neighborhood) > best_solution:
            best_solution = function_value(products, neighborhood)
            count_product = neighborhood
            tabu_list.append(neighborhood)
            print(f'New best value')
        else:
            print(f'New in tabu list')
            tabu_list.append(neighborhood)

        for i in range(5):
            new_neighborhood = next_neighborhood(products, neighborhood, tabu_list)
            if new_neighborhood is not None:
                neighborhood = new_neighborhood
                break
        if new_neighborhood is None:
            return best_solution, count_product
    return best_solution, count_product


chair_create_time = 3
chair_pack_time = 6
chair_profit = 20

table_create_time = 4
table_pack_time = 2
table_profit = 24

total_create_time = 60
total_pack_time = 32

max_chair = 5
max_table = 15

chairs_details = [chair_create_time, chair_pack_time, chair_profit]
tables_details = [table_create_time, table_pack_time, table_profit]

solution = tabu_search([chairs_details, tables_details])
print(f'Solution: Fx value: {solution[0]}, chairs: {solution[1][0]}, tables: {solution[1][1]}')
