def main():
    with open('day-9\input.txt', 'r') as f:
        data = f.read().splitlines()

    direction_dict = {
        "U": [0, 1],
        "D": [0, -1],
        "L": [-1, 0],
        "R": [1, 0],
    } # x, y

    head_position = [0, 0]
    tail_position = [0, 0]

    visited = set()
    visited.add(tuple(tail_position))

    for _, x in enumerate(data):
        step_direction = direction_dict[x[0]]
        distance = get_distance(x)
        for _ in range(distance):
            head_position[0] += step_direction[0]
            head_position[1] += step_direction[1]
            if not is_touching(head_position, tail_position):
                tail_position[0] = (head_position[0] > tail_position[0]) - (head_position[0] < tail_position[0])
                tail_position[1] = (head_position[1] > tail_position[1]) - (head_position[1] < tail_position[1])
                if tuple(tail_position) not in visited:
                    visited.add(tuple(tail_position))

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