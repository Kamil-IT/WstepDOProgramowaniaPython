import numpy as np
import random


# Min mark = 2,0
# Max mark = 5,5
# Step = 0,5
def create_random_matrix_marks(stud_quantity, sub_quantity):
    return np.random.choice(np.arange(2., 6., 0.5), size=(stud_quantity, sub_quantity))


def count_stud_not_pass(matrix_indexes, number_subjects):
    list_indexes = matrix_indexes.tolist()
    stud_not_pass = 0
    for index in list_indexes:
        if index.count(2.0) >= number_subjects:
            stud_not_pass += 1
    return stud_not_pass


# Return to lists(protection for to same avg)
def marks_min_max_avg(matrix_indexes):
    list_indexes = stud_indexes.tolist()
    avg_marks = []
    for index in list_indexes:
        avg_marks.append(sum(index))

    max_avg = max(avg_marks)
    min_avg = min(avg_marks)

    min_marks = []
    max_marks = []

    for index in list_indexes:
        avg = sum(index)
        if max_avg == avg:
            max_marks.append(index)
        elif min_avg == avg:
            min_marks.append(index)
    return min_marks, max_marks


def stud_with_avg_4_and_more(matrix_indexes):
    list_indexes = matrix_indexes.tolist()
    list = []
    for index in list_indexes:
        if sum(index) / len(index) >= 4.0:
            list.append(index)
    return list

def stud_max_of_max_marks(matrix_indexes):
    max_marks = []
    list_indexes = matrix_indexes.tolist()
    for mark in np.arange(5.5, 1.5, -0.5):
        for index in list_indexes:
            max_marks.append(index.count(mark))

        count_max_mark = max(max_marks)
        if max_marks.count(count_max_mark) > 1:
            if mark == 2.0:
                return list_indexes
            else:
                for i in range(len(max_marks) - 1, -1, -1):
                    if max_marks[i] != count_max_mark and count_max_mark != 0:
                        list_indexes.pop(i)
        else:
            index_max = max_marks.index(count_max_mark)
            return list_indexes[index_max:index_max + 1]
        max_marks.clear()


def marks_histogerms(matrix):
    histograms = []
    trans_matrix = np.transpose(stud_indexes).tolist()
    for marks in trans_matrix:
        histograms.append(histograms.append(np.histogram(marks, bins=[2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5])))
    return histograms


stud_indexes = create_random_matrix_marks(3, 3)
print("Base matrix")
print(stud_indexes)
print()

# ex1
print("ex1")
print(count_stud_not_pass(stud_indexes, 2))

# ex2
print("ex2")
min_marks, max_marks = marks_min_max_avg(stud_indexes)
print("Oceny studentów z najniższą średnią:")
print(min_marks)

print("Oceny studentów z najwyższą średnią: ")
print(max_marks)

# ex3
print("ex3")
print(stud_max_of_max_marks(stud_indexes))

# ex4
print("ex4")
print(marks_histogerms(stud_indexes))

# ex5
print("ex5")
print(stud_with_avg_4_and_more(stud_indexes))
