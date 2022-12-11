def main():
    with open('day-9\input.txt', 'r') as f:
        data = f.read().splitlines()

    direction_dict = {
        "U": [0, 1],
        "D": [0, -1],
        "L": [-1, 0],
        "R": [1, 0],
    } # x, y

    knot_positions = [[0, 0] for _ in range(10)]

    visited = set()
    visited.add(tuple(knot_positions[9]))

    for _, x in enumerate(data):
        step_direction = direction_dict[x[0]]
        distance = get_distance(x)
        for _ in range(distance):
            knot_positions[0][0] += step_direction[0]
            knot_positions[0][1] += step_direction[1]

            for i in range(1, 10, 1):
                if is_touching(knot_positions[i], knot_positions[i-1]):
                    break

                knot_positions[i][0] += ((knot_positions[i-1][0] > knot_positions[i][0]) - (knot_positions[i-1][0] < knot_positions[i][0]))
                knot_positions[i][1] += ((knot_positions[i-1][1] > knot_positions[i][1]) - (knot_positions[i-1][1] < knot_positions[i][1]))

                if i == 9 and tuple(knot_positions[9]) not in visited:
                    visited.add(tuple(knot_positions[9]))

    print(len(visited))

def get_distance(s):
    line = s.split()
    return int(line[1])

def is_touching(h, t):
    if abs(h[0] - t[0]) > 1:
        return False
    if abs(h[1] - t[1]) > 1:
        return False
    return True

if __name__ == "__main__":
    main()