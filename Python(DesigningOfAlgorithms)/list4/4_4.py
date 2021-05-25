import robot4_0


def binary_search_id(robots, search_values):
    if type(search_values) is not list:
        search_values = [search_values]

    for search_value in search_values:
        low = 0
        high = len(robots) - 1
        while low <= high:
            mid = (high + low) // 2

            if robots[mid]._id < search_value:
                low = mid + 1
            elif robots[mid]._id > search_value:
                high = mid - 1
            else:
                return robots[mid]._id
    return None


def binary_search_robot_index_min_max(array, search_values):
    if type(search_values) is not list:
        search_values = [search_values]
    robots = array.copy()
    contains_robots = []
    for search_value in search_values:
        low = 0
        high = len(robots) - 1
        while low <= high:
            mid = (high + low) // 2

            if robots[mid]._mass < search_value:
                low = mid + 1
            elif robots[mid]._mass > search_value:
                high = mid - 1
            else:
                contains_robots.append(robots[mid])
                robots.remove(robots[mid])
                low = 0
                high = len(robots) -1
    if len(contains_robots) == 0:
        return None, None
    elif len(contains_robots) == 1:
        return contains_robots[0]._id, contains_robots[0]._id
    contains_robots.sort(key=lambda robot: robot._id)
    return binary_search_id(contains_robots, min(contains_robots, key=lambda robot: robot._id)._id), \
           binary_search_id(contains_robots, max(contains_robots, key=lambda robot: robot._id)._id),


def binary_search_robot_indexs(robots, search_values):
    if type(search_values) is not list:
        search_values = [search_values]

    contains_ids = []
    for search_value in search_values:
        low = 0
        high = len(robots) - 1
        while low <= high:
            mid = (high + low) // 2

            if robots[mid]._mass < search_value:
                low = mid + 1
            elif robots[mid]._mass > search_value:
                high = mid - 1
            else:
                contains_ids.append(robots[mid]._id)
                robots.remove(robots[mid])
                low = 0
                high = len(robots) -1
    return contains_ids


# Prepare to search
robots = robot4_0.generate_random_robots(10)
robots.quick_sort(key=lambda robot: robot._mass)
robot4_0.print_all_robots(robots)

# Search id max
min_id, max_id = binary_search_robot_index_min_max(robots, [50, 200])
print(min_id, max_id)

# Search ids range
ids_range = binary_search_robot_indexs(robots, [50, 200])
print(ids_range)
