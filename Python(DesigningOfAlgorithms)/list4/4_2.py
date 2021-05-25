import robot4_0


def binary_search(robots, search_values):
    if type(search_values) is not list:
        search_values = [search_values]

    for search_value in search_values:
        low = 0
        high = len(robots) - 1
        print(f'Set low = 0 and  high = len(robots) - 1')
        while low <= high:
            mid = (high + low) // 2
            print(f'Set mid: mid = (high + low) // 2 = {(high + low) // 2}')

            if robots[mid]._mass < search_value:
                print(f'{robots[mid]._mass}(robots[mid]._mass) < {search_value}(search_value) then low = mid + 1')
                low = mid + 1
            elif robots[mid]._mass > search_value:
                print(f'{robots[mid]._mass}(robots[mid]._mass) > {search_value}(search_value) then high = mid - 1')
                high = mid - 1
            else:
                print(f'robots[mid]._mass == search_value then return robots[mid]')
                return robots[mid]
    return None


# Prepare robots to search
robots = robot4_0.generate_random_robots(10)
robots.quick_sort(key=lambda robot: robot._mass)
robot4_0.print_all_robots(robots)

# Search
find_robot = binary_search(robots, [50, 200])
print(find_robot)
