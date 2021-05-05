def get_len_of_biggest_number(numbers):
    max_len = 0
    for number in numbers:
        if len(number) > max_len:
            max_len = len(number)
    return max_len


def sort(numbers, sorted_numbers, possition_number, max_index_number):
    max_number = []
    if possition_number == get_len_of_biggest_number(numbers) - 1:
        for number in numbers:
            sorted_numbers.append(number)
            numbers.remove(number)
    else:
        while len(numbers) != 0:
            biggest_number = get_len_of_biggest_number(numbers)
            for i in range(9, 0, -1):
                numbers_to_remove = []
                for number in numbers:
                    if len(number) >= biggest_number and str(number[possition_number]) == str(i):
                        max_number.append(number)
                        numbers_to_remove.append(number)
                for e in numbers_to_remove:
                    numbers.remove(e)
                if len(max_number) == 1:
                    sorted_numbers.append(max_number[0])
                    max_number.clear()
                elif len(max_number) != 0:
                    sort(max_number, sorted_numbers, possition_number + 1, max_index_number)


def sort_numbers(numbers):
    str_numbers = []
    for number in numbers:
        str_numbers.append(str(number))

    sorted_numbers = []
    sort(str_numbers, sorted_numbers, 0, get_len_of_biggest_number(str_numbers))
    return sorted_numbers


numbers = [1234, 22220, 1123, 2321, 1234, 53255]

print(sort_numbers(numbers))
