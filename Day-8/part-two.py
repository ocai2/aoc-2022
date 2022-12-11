def main():
    with open('day-8\input.txt', 'r') as f:
        data = f.read().splitlines()

    tree_array = [[int(y) for y in x] for x in data]
    m, n = len(tree_array), len(tree_array[0])

    max_distance = 0
    for i in range(m):
        for j in range(n):
            cell_distance = get_paths(tree_array[i][j], tree_array, i, j)
            if cell_distance > max_distance:
                max_distance = cell_distance

    print(max_distance)

def get_paths(c, t, i, j):
    left = list(reversed(t[i][:j]))
    right = t[i][j+1:]

    t_t = list(map(list, zip(*t)))
    up = list(reversed(t_t[j][:i]))
    down = t_t[j][i+1:]

    return get_tree_value(c, up, down, left, right)

def get_tree_value(c, up, down, left, right):
    d_up = distance_to_tree(c, up)
    d_down = distance_to_tree(c, down)
    d_left = distance_to_tree(c, left)
    d_right = distance_to_tree(c, right)

    return d_up * d_down * d_left * d_right

def distance_to_tree(c, trees):
    if not trees:
        return 0
    for i, x in enumerate(trees):
        if x >= c:
            return i + 1
    return len(trees)

if __name__ == "__main__":
    main()