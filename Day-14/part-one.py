def main():
    with open('day-14\input.txt', 'r') as f:
        data = f.read().splitlines()

    map_array = [['.' for _ in range(120)] for _ in range(200)]


    for line in data:
        corners = [[int(i) for i in j.split(',')] for j in line.split(' -> ')]
        add_rocks_to_map(map_array, corners)
        add_rocks_to_map(map_array, get_points_between(corners))

    n_sands = 0
    while True:
        if sim_sand(map_array):
            break
        else:
            n_sands += 1

    print(n_sands)
    print()

    # printing
    print('   ',end='')
    for _ in range(12):
        for _ in range(9):
            print('.',end='')
        print('|',end='')
    print()

    for i, x in enumerate(map_array):
        print(i, end='')
        if i < 10:
            print(' ',end='')
        if i < 100:
            print(' ',end='')
        for c in x:
            print(c, end='')
        print()

def sim_sand(m):
    x = 0
    y = 60
    while True:
        if x == len(m) -1:
            return True
        if m[x+1][y] == '.':
            x += 1
        elif m[x+1][y-1] == '.':
            x += 1
            y -= 1
        elif m[x+1][y+1] == '.':
            x += 1
            y += 1
        else:
            m[x][y] = 'o'
            return False

def add_rocks_to_map(m, p):
    for point in p:
        # print(point[0]-440)
        m[point[1]][point[0]-440] = '#'

def get_points_between(a):
    points = []
    for i in range(0, len(a) - 1, 1):
        if a[i][0] == a[i+1][0]:
            if a[i][1] > a[i+1][1]:
                points.extend([[a[i][0], j] for j in range(a[i+1][1] + 1, a[i][1], 1)])
            else:
                points.extend([[a[i][0], j] for j in range(a[i][1] + 1, a[i+1][1], 1)])
        else:
            if a[i][0] > a[i+1][0]:
                points.extend([[j, a[i][1]] for j in range(a[i+1][0] + 1, a[i][0], 1)])
            else:
                points.extend([[j, a[i][1]] for j in range(a[i][0] + 1, a[i+1][0], 1)])
    return points

if __name__ == "__main__":
    main()