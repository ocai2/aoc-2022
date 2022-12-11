# this solution sucks dont look

def main():
    with open('day-8\input.txt', 'r') as f:
        data = f.read().splitlines()

    tree_array = [[int(y) for y in x] for x in data]
    m, n = len(tree_array), len(tree_array[0])
    vision_array_horizontal = [n * [0] for i in range(m)]

    for i, row in enumerate(tree_array):
        parse_row(row, vision_array_horizontal[i])

    t_tree_array = list(map(list, zip(*tree_array)))
    temp_vision_array = [n * [0] for _ in range(m)]

    for i, row in enumerate(t_tree_array):
        parse_row(row, temp_vision_array[i])

    vision_array_vertical = list(map(list, zip(*temp_vision_array)))
    vision_array_combined = [[x | y for x, y in zip(l1, l2)] for l1, l2 in zip(vision_array_horizontal, vision_array_vertical)]
    sum_visible = 0

    for x in vision_array_combined:
        sum_visible += sum(x)
        print(x)

    print(sum_visible)

def parse_row(t, v):
    curr_tallest = -1
    for i, cell in enumerate(t):
        if cell > curr_tallest:
            curr_tallest = cell
            v[i] = 1

    curr_tallest = -1
    for i, cell in reversed(list(enumerate(t))):
        if cell > curr_tallest:
            curr_tallest = cell
            v[i] = 1

if __name__ == "__main__":
    main()