def main():
    with open('day-13\input.txt', 'r') as f:
        data = f.read().split('\n\n')

    sum_of_the_indices_of_the_good_pairs = 0
    for i, x in enumerate(data):
        left_raw, right_raw = x.splitlines()
        left = parse_line(left_raw)
        right = parse_line(right_raw)

        print(left)
        print(right)
        result = is_ordered(left, right) 
        print(result)
        print()
        if result > 0:
            sum_of_the_indices_of_the_good_pairs += i + 1

    print(sum_of_the_indices_of_the_good_pairs)

def is_ordered(l, r):
    # looked this up
    match l, r:
        case int(), int():
            return (l<r)-(l>r)
        case list(), list():
            for ln, rn in zip(l, r):
                if result := is_ordered(ln, rn):
                    return result
            return is_ordered(len(l), len(r))
        case int(), list():
            return is_ordered([l], r)
        case list(), int():
            return is_ordered(l, [r])

def parse_line(s):
    # use eval next time
    current_list = root = []
    stack = []
    r = ''

    for _, c in enumerate(s):
        if c == '[':
            temp = []
            current_list.append(temp)
            stack.append(current_list)
            current_list = temp
        elif c == ']':
            if r != '':
                current_list.append(int(r))
                r = ''
            current_list = stack.pop()
        elif c == ',':
            if r != '':
                current_list.append(int(r))
            r = ''
        else:
            r += c

    return root[0]

if __name__ == "__main__":
    main()