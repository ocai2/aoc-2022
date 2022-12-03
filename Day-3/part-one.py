def main():
    with open('day-3\input.txt', 'r') as f:
        data = f.read().splitlines()

    result = list(map(find_repeat, data))

    for x in result:
        print(x)

    print(sum(result))

def find_repeat(s):
    c1 = s[:len(s)//2]
    c2 = s[len(s)//2:]

    return get_priority(''.join(set(c1).intersection(c2)))

def get_priority(c):
    a = ord(c)
    if a <= 90:
        return a - 38
    else:
        return a - 96

if __name__ == "__main__":
    main()