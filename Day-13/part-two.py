def main():
    with open('day-13\input.txt', 'r') as f:
        data = f.read().split('\n\n')
        data = [eval(y) for x in data for y in x.splitlines() ]

    sum_below_two = 1
    sum_below_six = 2
    for _, x in enumerate(data):
        if is_ordered(x, [[2]]) > 0:
            sum_below_two += 1
        if is_ordered(x, [[6]]) > 0:
            sum_below_six += 1
            print(x)

    print(sum_below_two * sum_below_six)

def is_ordered(l, r):
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

if __name__ == "__main__":
    main()