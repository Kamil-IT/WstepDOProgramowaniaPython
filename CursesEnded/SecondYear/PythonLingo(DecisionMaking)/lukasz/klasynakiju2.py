import random


def download_warehouses():
    with open('warehouse_list.txt') as f:
        for lines in f:
            warehouse_vector.append(tuple(lines.split()))
    return warehouse_vector


def download_drivers():
    with open('drivers_list.txt') as f:
        for lines in f:
            driver_vector.append(tuple(lines.split()))
    return driver_vector


def tranform_toint_warehouses(warehouses_list):
    INT_WAREHOUSES = list()
    for el in warehouses_list:
        el0 = int(el[0])
        el1 = int(el[1])
        el2 = int(el[2])
        INT_WAREHOUSES.append((el0, el1, el2))
    return INT_WAREHOUSES


def tranform_toint_drivers(drivers_list):
    INT_DRIVERS = list()
    for el in drivers_list:
        el0 = float(el[0])
        el1 = float(el[1])
        el2 = int(el[2])
        INT_DRIVERS.append((el0, el1, el2))
    return INT_DRIVERS


def distance(warehouse, warehouse2):
    return ((warehouse[0] - warehouse2[0]) ** 2 + (warehouse[1] - warehouse2[1]) ** 2) ** (1 / 2)


def summed_distances(mag_vector):

    if len(mag_vector) == 0:
        return 0
    if len(mag_vector) == 1:
        return distance(WAREHOUSES[mag_vector[0]], WAREHOUSE_BASE) + distance(WAREHOUSES[mag_vector[0]], WAREHOUSE_BASE)
    else:
        first_dist = distance(WAREHOUSES[mag_vector[0]], WAREHOUSE_BASE)
        last_dist = distance(WAREHOUSES[mag_vector[len(mag_vector) - 1]], WAREHOUSE_BASE)
        sum_dist = 0
        for i in range(len(mag_vector) - 1):
            sum_dist += distance(WAREHOUSES[mag_vector[i]], WAREHOUSES[mag_vector[i + 1]])
        return sum_dist + first_dist + last_dist


def main_function(mag_vector, driver_id):
    func = (summed_distances(mag_vector) * (1 / (DRIVERS[driver_id][0] * 70))) * DRIVERS[driver_id][1]
    return func


def hour_limitation(mag_vector, driver_id):
    func = (summed_distances(mag_vector) * (1 / (DRIVERS[driver_id][0] * 80)))
    return func


def is_checked_hour_limitation(mag_vector):
    for key in mag_vector.keys():
        if hour_limitation(mag_vector[key], int(key[6])) > 20:
            return False
    return True


def possible_solutions(drivers_werehouses, warehouse_suplies, drvier_available_demand):
    drivers_werehouses, drvier_available_demand, warehouse_suplies = random_solution(drivers_werehouses,
                                                                                     drvier_available_demand,
                                                                                     warehouse_suplies)
    while not is_checked_hour_limitation(drivers_werehouses):
        drivers_werehouses, drvier_available_demand, warehouse_suplies = random_solution(drivers_werehouses,
                                                                                         drvier_available_demand,
                                                                                         warehouse_suplies)

    print(warehouse_suplies)
    print(drvier_available_demand)
    print(drivers_werehouses)



def random_solution(drivers_werehouses, drvier_available_demand, warehouse_suplies):
    while sum([warehouse_suplies[key] for key in warehouse_suplies.keys()]) != 0:
        wh_index = str(random.randint(0, 29))
        driver_index = random.randint(0, 14)

        if drvier_available_demand[f'demand{driver_index}'] <= warehouse_suplies[f'suply{wh_index}']:
            max_delivery = drvier_available_demand[f'demand{driver_index}']
        else:
            max_delivery = warehouse_suplies[f'suply{wh_index}']

        # It can be random but we will generate a lot of we possible solution
        # Many of them will be shitty
        # rndmd = random.randint(1, max_delivery[0])

        if max_delivery != 0:
            drivers_werehouses[f'driver{driver_index}'].append(int(wh_index))
            drvier_available_demand[f'demand{driver_index}'] = drvier_available_demand[
                                                                   f'demand{driver_index}'] - max_delivery
            warehouse_suplies[f'suply{wh_index}'] = warehouse_suplies[f'suply{wh_index}'] - max_delivery

    return drivers_werehouses, drvier_available_demand, warehouse_suplies


if __name__ == "__main__":
    driver_vector = []
    warehouse_vector = []
    drivers_werehouses = {}
    warehouse_suplies = {}
    drvier_available_demand = {}
    WAREHOUSE_BASE = (150, 150, 0)

    WAREHOUSES = (tranform_toint_warehouses(download_warehouses()))
    DRIVERS = (tranform_toint_drivers(download_drivers()))

    for i in range(15):
        drivers_werehouses['driver' + str(i)] = []

    for i in range(30):
        warehouse_suplies['suply' + str(i)] = WAREHOUSES[i][2]

    for i in range(15):
        drvier_available_demand['demand' + str(i)] = DRIVERS[i][2]

    possible_solutions(drivers_werehouses, warehouse_suplies, drvier_available_demand)
