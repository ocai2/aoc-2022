def main():
    with open('day-10\input.txt', 'r') as f:
        data = f.read().splitlines()

    cool_cycles = [20, 60, 100, 140, 180, 220]
    signal_strengths = []

    x = 1
    cycle = 0
    for _, line in enumerate(data):
        cycle += 1
        if cycle in cool_cycles:
            signal_strengths.append(x * cycle)

        if line[0] == "n":
            continue
        
        cycle += 1
        if cycle in cool_cycles:
            signal_strengths.append(x * cycle)
        
        _, v = line.split()
        x += int(v)
    
    print(sum(signal_strengths))

if __name__ == "__main__":
    main()