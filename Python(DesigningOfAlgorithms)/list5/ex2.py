import robot4_0


def identify_robot_with_resolution(robots, resolutions):
    sorted_robots = []
    for resolution in resolutions:
        for robot in robots:
            if robot._resolution == resolution:
                sorted_robots.append(robot)
    return sorted_robots


def counting_sort(resolutions):
    max_element = int(max(resolutions))
    min_element = int(min(resolutions))
    range_of_elements = max_element - min_element + 1

    count_arr = [0 for _ in range(range_of_elements)]
    result = [0 for _ in range(len(resolutions))]

    for i in range(0, len(resolutions)):
        count_arr[resolutions[i] - min_element] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    for i in range(len(resolutions) - 1, -1, -1):
        result[count_arr[resolutions[i] - min_element] - 1] = resolutions[i]
        count_arr[resolutions[i] - min_element] -= 1

    for i in range(0, len(resolutions)):
        resolutions[i] = result[i]

    return resolutions


robots = robot4_0.generate_random_robots(10)
data = [robot._resolution for robot in robots]
sort_data = counting_sort(data)

sorted_robots = identify_robot_with_resolution(robots, sort_data)

robot4_0.print_all_robots(sorted_robots)
