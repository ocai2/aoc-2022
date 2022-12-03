def main():
    with open('day-3\input.txt', 'r') as f:
        data = f.read().splitlines()

    split_list = list(list_splitter(data, 3))
    results = list(map(find_repeat, split_list))

    for x in results:
        print(x)
        
    print(sum(results))

def list_splitter(list, size):
    for i in range(0, len(list), size):
        yield list[i:i+size]

def find_repeat(s):
    c1 = s[0]
    c2 = s[1]
    c3 = s[2]
    return get_priority(''.join(set(c1).intersection(c2, c3)))

def get_priority(c):
    a = ord(c)
    if a <= 90:
        return a - 38
    else:
        return a - 96

if __name__ == "__main__":
    main()