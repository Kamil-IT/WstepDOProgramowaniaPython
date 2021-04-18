# Prepare robots to search
import robot4_0


def binary_search_robot_indexs(array, search_values):
    if type(search_values) is not list:
        search_values = [search_values]

    robots = array.copy()
    contains_ids = []
    for search_value in search_values:
        low = 0
        high = len(robots) - 1
        while low <= high:
            mid = (high + low) // 2

            if robots[mid][1] < search_value:
                low = mid + 1
            elif robots[mid][1] > search_value:
                high = mid - 1
            else:
                contains_ids.append(robots[mid][0])
                robots.remove(robots[mid])
                low = 0
                high = len(robots) - 1
    print(f'Find {search_values} in {list(map(lambda obj: obj[1], array))} = {contains_ids}')
    return contains_ids


robots = robot4_0.generate_random_robots(10)
robots.sort(key=lambda robot: robot._mass)
robot4_0.print_all_robots(robots)

robots_id_mass = list(map(lambda robot: (robot._id, robot._mass), robots))
robots_id_range = list(map(lambda robot: (robot._id, robot._range), robots))
robots_id_resolution = list(map(lambda robot: (robot._id, robot._resolution), robots))

# Search ids range
ids_range = set(binary_search_robot_indexs(robots_id_mass, [50, 200]))
ids_range.intersection(set(binary_search_robot_indexs(robots_id_range, [50, 200])))
ids_range.intersection(set(binary_search_robot_indexs(robots_id_resolution, [50, 200])))

print(ids_range)
