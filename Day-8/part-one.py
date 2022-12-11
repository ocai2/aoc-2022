def main():
    with open('day-8\input.txt', 'r') as f:
        data = f.read().splitlines()

    tree_array = [[int(y) for y in x] for x in data]
    m, n = len(tree_array), len(tree_array[0])

    visible_array = [n * [0] for i in range(m)]

    # left to right
    for x in range(m):
        tallest_tree = -1
        for y in range(n):
            if tree_array[x][y] > tallest_tree:
                tallest_tree = tree_array[x][y]
                visible_array[x][y] = 1
    
    # right to left
    for x in range(m):
        tallest_tree = -1
        for y in range(n-1, 0, -1):
            if tree_array[x][y] > tallest_tree:
                tallest_tree = tree_array[x][y]
                visible_array[x][y] = 1

    # top to bottom
    for y in range(n):
        tallest_tree = -1
        for x in range(m):
            if tree_array[x][y] > tallest_tree:
                tallest_tree = tree_array[x][y]
                visible_array[x][y] = 1

    # bottom to top
    for y in range(n):
        tallest_tree = -1
        for x in range(m-1, 0, -1):
            if tree_array[x][y] > tallest_tree:
                tallest_tree = tree_array[x][y]
                visible_array[x][y] = 1

    print(sum([sum(x) for x in visible_array]))

if __name__ == "__main__":
    main()