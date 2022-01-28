import random

import matplotlib.pyplot as plt


def function_to_optimize(num):
    return num * 2 + num ** 2


population = 180
mutation_rate = 0.01

total_mutation = 0
maximum_extensionmutation = 0
best_list = []


def get_fitness(generation):
    global best
    global best_list
    value_list = [function_to_optimize(generation[x]) for x in range(len(generation))]
    fitness_list = [(max(value_list) - value_list[x]) ** 2 for x in range(len(generation))]

    if best is not None and min(value_list) <= best[1]:
        best = [generation[value_list.index(min(value_list))], min(value_list)]

    best_list.append(best[0])

    return fitness_list


def select_individuals(generation, fitness_list):
    selected_individuals = []
    prob_list = [(fitness_list[x]) / sum(fitness_list) for x in range(len(fitness_list))]

    for x in range(0, len(fitness_list) * 2):
        target = random.random()
        accumulation = 0
        i = 0
        while i < len(fitness_list) and accumulation <= target:
            accumulation += prob_list[i]
            i += 1
        index = i - 1
        selected_individuals.append(generation[index])
    return selected_individuals


def generate_new_generation(selected_individuals):
    mylist = [bin(int(selected_individuals[x] * 1000)) for x in range(len(selected_individuals))]
    newgeneration = []

    for x in range(population):
        global mutation_record
        global total_mutation
        global maximum_extensionmutation
        ab_list = []
        a_list = list(mylist[2 * x])
        b_list = list(mylist[2 * x + 1])

        insert_plus_if_minus(a_list)
        insert_plus_if_minus(b_list)

        insert_0_if_longer(a_list, b_list, abs(len(a_list) - len(b_list)))
        insert_0_if_longer(b_list, a_list, abs(len(a_list) - len(b_list)))

        for x in range(len(a_list)):

            if x >= 3 and mutation_rate > random.uniform(0, 1):
                ab_list.append(str(random.choice([0, 1])))
                total_mutation += 1
                mutation_record += 1
            else:
                ab_list.append(random.choice([a_list[x], b_list[x]]))

        extensionmutation = 0

        while x >= 3 and mutation_rate > random.uniform(0, 1):
            ab_list.append(str(random.choice([0, 1])))
            total_mutation += 1
            mutation_record += 1
            extensionmutation += 1
            maximum_extensionmutation = max(maximum_extensionmutation, extensionmutation)
        newgeneration.append(int(''.join(ab_list), 2) / 1000)
    return newgeneration


def insert_0_if_longer(a_list, b_list, dif):
    if len(a_list) > len(b_list):
        for x in range(dif):
            b_list.insert(3, '0')


def insert_plus_if_minus(a_list):
    if a_list[0] != '-':
        a_list.insert(0, '+')

# Init vales
generation = [round(random.uniform(-8, 8), 3) for i in range(population)]
best = [generation[0], function_to_optimize(generation[0])]
fitness = get_fitness(generation)
average_list = [sum(generation) / len(generation)]

# GA
for x in range(1, 10):
    mutation_record = 0
    nextgeneration = generate_new_generation(select_individuals(generation, fitness))[:]
    fitness = get_fitness(nextgeneration)
    generation = nextgeneration[:]
    average = sum(nextgeneration) / len(nextgeneration)
    average_list.append(average)
    # print("generation", x)
    # print(nextgeneration)
    # print('   fitness =', fitness)
    # print('    average value =', average)
    # print('    local mutaton', mutation_record)

# print("\ntotal mutation= ", total_mutation)
# print("maximum extension mutation", maximum_extensionmutation)
# print("best number found = ", best)

plt.plot(average_list, '-')
plt.plot(best_list, '-')
plt.show()
# https://github.com/wbh123456/Find_Min_with_GA/blob/master/find_minimum.py
