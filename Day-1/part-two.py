import itertools

def main():
    with open('day-1\input.txt', 'r') as f:
        data = f.read().splitlines()
    
    int_list = list(map(convert_to_int, data))
    delimiter = ''
    split_list = [list(y) for x, y in itertools.groupby(int_list, lambda z: z == delimiter) if not x]
    sum_list = list(map(sum, split_list))
    top_three = sorted(sum_list, reverse=True)[:3]

    for x in top_three:
        print(x)
    
    print(sum(top_three))

def convert_to_int(s):
    if not s:
        return s
    try:
        return int(s)
    except ValueError:
        return s

if __name__ == "__main__":
    main()