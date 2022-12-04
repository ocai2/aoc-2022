def main():
    with open('day-4\input.txt', 'r') as f:
        data = f.read().splitlines()

    result = 0
    for x in data:
        four_nums = get_nums(x)
        result += is_covered(four_nums)
        
    print(result)

def is_covered(n):
    if n[0] <= n[2] and n[1] >= n[3]:
        return 1
    elif n[0] >= n[2] and n[1] <= n[3]:
        return 1
    else:
        return 0

def get_nums(s):
    c = s.replace('-',',').split(',')
    return list(map(int, c))

if __name__ == "__main__":
    main()