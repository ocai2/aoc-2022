def main():
    with open('day-10\input.txt', 'r') as f:
        data = f.read().splitlines()

    x = 1
    cycle = 0
    print()

    for _, line in enumerate(data):
        cycle = check_cycle(cycle, x)

        if line[0] == "n":
            continue
        
        cycle = check_cycle(cycle, x)
        
        _, v = line.split()
        x += int(v)
    print()

def check_cycle(c, x):
    a = c % 40
    if abs(x - a) < 2:
        print("#", end="")
    else:
        print(" ", end="")

    c += 1
    if c % 40 == 0:
        print()
    return c

if __name__ == "__main__":
    main()