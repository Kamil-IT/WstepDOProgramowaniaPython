import robot4_0


def identify_robot_with_resolution(robots, resolutions):
    sorted_robots = []
    for resolution in resolutions:
        for robot in robots:
            if robot._resolution == resolution:
                sorted_robots.append(robot)
    return sorted_robots


def quick_sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return array


def bubble_sort(array):
    n = len(array)
    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False

        if already_sorted:
            break
    return array


robots = robot4_0.generate_random_robots(9)
data = [robot._resolution for robot in robots]
sort_data_quick = quick_sort(data)
sort_data_bubble = quick_sort(data)

sorted_robots_quick = identify_robot_with_resolution(robots, sort_data_quick)
sorted_robots_bubble = identify_robot_with_resolution(robots, sort_data_bubble)

robot4_0.print_all_robots(sorted_robots_quick)
robot4_0.print_all_robots(sorted_robots_bubble)
