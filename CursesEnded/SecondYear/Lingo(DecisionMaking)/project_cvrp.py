# 15
import json


class Driver:
    efficiency = 0
    salary = 0
    # Not bigger than 10
    warehouse = list()


# 50
# demand = 480
class Warehouse:
    x = 0
    y = 0
    demand = 0

    def __init__(self, x, y, demand):
        self.x = x
        self.y = y
        self.demand = demand

    def to_map(self):
        return {
            "x": self.x,
            "y": self.y,
            "demand": self.demand,
        }


def save_warehouse(warehouses):
    f = open("warehouse.json", "w")
    f.write(json.dumps([warehouse.to_map() for warehouse in warehouses]))
    f.close()


def read_warehouse():
    f = open("warehouse.json", "r")
    data = f.read().replace('\n', '')
    robots = []
    for el in json.loads(data):
        robots.append(convert_json_el_to_warehouses(el))
    return robots


def convert_json_el_to_warehouses(json):
    return Warehouse(
        int(json["x"]),
        int(json["y"]),
        int(json["demand"]),
    )


def distance(warehouse, warehouse2):
    return ((warehouse.x - warehouse2.x) ** 2 + (warehouse.y - warehouse2.y) ** 2) ** (1 / 2)
