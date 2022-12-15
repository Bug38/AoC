from typing import List, Tuple
from dataclasses import dataclass
import re

input = open("15/15.txt").readlines()

@dataclass
class Sensor:
    x: int
    y: int
    radius: int

example = [
    "Sensor at x=2, y=18: closest beacon is at x=-2, y=15",
    "Sensor at x=9, y=16: closest beacon is at x=10, y=16",
    "Sensor at x=13, y=2: closest beacon is at x=15, y=3",
    "Sensor at x=12, y=14: closest beacon is at x=10, y=16",
    "Sensor at x=10, y=20: closest beacon is at x=10, y=16",
    "Sensor at x=14, y=17: closest beacon is at x=10, y=16",
    "Sensor at x=8, y=7: closest beacon is at x=2, y=10",
    "Sensor at x=2, y=0: closest beacon is at x=2, y=10",
    "Sensor at x=0, y=11: closest beacon is at x=2, y=10",
    "Sensor at x=20, y=14: closest beacon is at x=25, y=17",
    "Sensor at x=17, y=20: closest beacon is at x=21, y=22",
    "Sensor at x=16, y=7: closest beacon is at x=15, y=3",
    "Sensor at x=14, y=3: closest beacon is at x=15, y=3",
    "Sensor at x=20, y=1: closest beacon is at x=15, y=3",
]

def runPart1(sensors: List[Sensor], beacons: List[Tuple[int, int]], y_level: int):
    x_min = min([s.x - s.radius for s in sensors])
    x_max = max([s.x + s.radius for s in sensors if 0 <= s.y <= 4000000])
    part1 = set()
    for s in sensors:
        if abs(s.y - y_level) > s.radius:
            continue
        for x in range(s.x - s.radius, s.x + s.radius + 1):
            if not x_min <= x <= x_max:
                continue
            if (x, y_level) in beacons:
                continue
            if abs(s.x - x) + abs(s.y - y_level) <= s.radius:
                part1.add((x, y_level))
                continue
    return len(part1)

def runPart2(sensors: List[Sensor], beacons: List[Tuple[int, int]], xy_limit: int):
    """ Scan each point just outside of each sensor range """
    def getPoints(sensors: List[Sensor], xy_limit):
        for s in sensors:
            for x_rel in range(-(s.radius + 1), s.radius + 2):
                x = s.x + x_rel
                if not 0 <= x <= xy_limit:
                    continue
                y1 = s.y + s.radius + 1 - x_rel
                if not 0 <= y1 <= xy_limit:
                    continue
                y2 = s.y - (s.radius + 1 - x_rel)
                if not 0 <= y2 <= xy_limit:
                    continue
                yield (x, y1)
                yield (x, y2)
    for point in getPoints(sensors, xy_limit):
        scanned = False
        for s in sensors:
            if abs(s.x - point[0]) + abs(s.y - point[1]) <= s.radius:
                scanned = True
                break
        if not scanned:
            return point[0] * 4_000_000 + point[1]

def puzzle(input: List[str], y_level_part1: int, xy_limit_part2: int):
    for i in range(len(input)):
        input[i] = input[i].strip()

    sensors: List[Sensor] = []
    beacons: List[Tuple[int, int]] = []
    for line in input:
        sx, sy, bx, by = [int(n) for n in re.findall(r'-*[0-9]+', line)]
        sensors.append(Sensor(sx, sy, abs(sx-bx) + abs(sy-by)))
        beacons.append((bx, by))

    part1 = runPart1(sensors, beacons, y_level_part1)
    part2 = runPart2(sensors, beacons, xy_limit_part2)
    
    return (part1, part2)


try:
    assert(puzzle(example, 10, 20) == (26, 56000011))
except AssertionError as e:
    print(f"Error in examples, got {puzzle(example, 10, 20)}")
    exit()

part1, part2 = puzzle(input, 2_000_000, 4_000_000)
print(f'{part1=}')
print(f'{part2=}')
print()
