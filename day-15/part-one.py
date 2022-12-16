import re

def main():
    with open('day-15\input.txt', 'r') as f:
        data = f.read().splitlines()
    
    y = 2000000
    yx = set()

    sensors = []
    beacons = []

    [(sensors.append([int(item[1]), int(item[3])]), beacons.append([int(item[5]), int(item[7])])) for item in [re.split('=|,|:', line) for line in data]]

    for sensor, beacon in zip(sensors, beacons):
        if (dist := get_distance(sensor, beacon) - abs(sensor[1] - y)) >= 0:
            x = sensor[0]
            [yx.add(i) for i in range(x-dist , x+dist, 1)]
    
    print(len(yx))

def get_distance(s, b):
    return abs(s[0] - b[0]) + abs(s[1] - b[1])

if __name__ == "__main__":
    main()