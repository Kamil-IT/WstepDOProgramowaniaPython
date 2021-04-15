import json
import random

import numpy as np


class Robot:
    _id = None
    _type = None
    _mass = None
    _range = None
    _resolution = None

    def __init__(self, id, type, mass, range, resolution):
        self._id = id
        self._type = type
        self._mass = mass
        self._range = range
        self._resolution = resolution

    def to_map(self):
        return {
            "id": self._id,
            "type": self._type,
            "mass": self._mass,
            "range": self._range,
            "resolution": self._resolution,
        }


def to_string_all_element_robots(robots):
    robots_string = []
    for robot in robots:
        robots_string.append(
            [format_string_4_el(str(robot._id)),
             format_string_4_el(str(robot._type)),
             format_string_4_el(str(robot._mass)),
             format_string_4_el(str(robot._range)),
             format_string_4_el(str(robot._resolution))])
    return robots_string


def generate_random_robot(id_start):
    robot = Robot(id_start,
                  random.choice(['AUV', 'AFV', 'AGV']),
                  random.randint(50, 2000),
                  random.randint(1, 1000),
                  random.randint(1, 30))
    id_start += 1
    return robot


def generate_random_robots(n, id_start=1):
    generated_robots = []
    for i in range(id_start, n):
        generated_robots.append(generate_random_robot(i))
    return generated_robots


def format_string_4_el(string):
    if len(string) == 1:
        return "   " + string
    elif len(string) == 2:
        return "  " + string
    elif len(string) == 3:
        return " " + string
    return string


def print_all_robots(robots):
    print(np.array([["  id", "type", "mass", " ran", " res"]]))
    print(np.array(to_string_all_element_robots(robots)))


def save_robots(robots):
    f = open("robots.json", "w")
    f.write(json.dumps([robot.to_map() for robot in robots]))
    f.close()


def read_robots():
    f = open("robots.json", "r")
    data = f.read().replace('\n', '')
    robots = []
    for el in json.loads(data):
        robots.append(convert_json_el_to_robot(el))
    return robots


def convert_json_el_to_robot(json):
    return Robot(
        int(json["id"]),
        str(json["type"]),
        int(json["mass"]),
        int(json["range"]),
        int(json["resolution"]),
    )



robots = generate_random_robots(5)
print_all_robots(robots)
save_robots(robots)
print_all_robots(read_robots())
