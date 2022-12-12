class node:
    def __init__(self, x, y, distance):
        self.x = x
        self.y = y
        self.distance = distance

def main():
    with open('day-12\input.txt', 'r') as f:
        data = f.read().splitlines()

    start_spots = []
    height_map =  []
    for i, x in enumerate(data):
        found = x.find("S")
        if found > -1:
            x = x.replace("S", "a")

        found = x.find("E")
        if found > -1:
            end = [i, found]
            x = x.replace("E", "z")
        
        start_spots.extend([[i, j] for j, letter in enumerate(x) if letter == 'a'])
        
        height_map.append([ord(y) for y in x])

    flood_fill = [[10000 for _ in range(len(height_map[0]))] for _ in range(len(height_map))]

    q = [node(end[0], end[1], 0)]
    flood_fill[end[0]][end[1]] = 0

    while(len(q) > 0):
        n = q.pop()
        neighbours = find_neighbours(height_map, flood_fill, n)
        for ne in neighbours:
            q.append(ne)

    min_distance = 10000000
    for start in start_spots:
        if flood_fill[start[0]][start[1]] < min_distance:
            min_distance = flood_fill[start[0]][start[1]]

    print(min_distance)

def find_neighbours(m, f, n):
    neighbours = []
    # left
    if n.x > 0:
        if f[n.x-1][n.y] > n.distance + 1 and m[n.x-1][n.y] >= m[n.x][n.y] - 1:
            f[n.x-1][n.y] = n.distance + 1
            neighbours.append(node(n.x-1, n.y, n.distance + 1))
    # right
    if n.x < len(m) - 1:
        if f[n.x+1][n.y] > n.distance + 1 and m[n.x+1][n.y] >= m[n.x][n.y] - 1:
            f[n.x+1][n.y] = n.distance + 1
            neighbours.append(node(n.x+1, n.y, n.distance + 1))
    # top
    if n.y > 0:
        if f[n.x][n.y-1] > n.distance + 1 and m[n.x][n.y-1] >= m[n.x][n.y] - 1:
            f[n.x][n.y-1] = n.distance + 1
            neighbours.append(node(n.x, n.y-1, n.distance + 1))
    # left
    if n.y < len(m[0]) - 1:
        if f[n.x][n.y+1] > n.distance + 1 and m[n.x][n.y+1] >= m[n.x][n.y] - 1:
            f[n.x][n.y+1] = n.distance + 1
            neighbours.append(node(n.x, n.y+1, n.distance + 1))

    return neighbours

if __name__ == "__main__":
    main()