def main():
    with open('day-5\input.txt', 'r') as f:
        data = f.read().splitlines()

    big_list = []
    for i in range(1,37,4):
        sub_list = [x[i] for x in list(reversed(data[:8])) if x[i] != ' ']
        big_list.append(sub_list)

    l = len(data)
    for i in range(10, l, 1):
        operation = parse_operation_string(data[i])
        execute_crane_operation(operation, big_list)
    
    for x in big_list:
        print(x)

    print()
    s = ''.join(x[-1] for x in big_list)
    print(s)

def execute_crane_operation(o, l):
    # print(f'moving {o[0]} from {o[1]} to {o[2]}:')
    # print(f'{o[1]} = {l[o[1] - 1]}')
    # print(f'{o[2]} = {l[o[2] - 1]}')
    l[o[2] - 1].extend(l[o[1] - 1][-o[0]:])
    del l[o[1] - 1][-o[0]:]
    # print('done: ')
    # print(f'{o[1]} = {l[o[1] - 1]}')
    # print(f'{o[2]} = {l[o[2] - 1]}')
    # print()
        
def parse_operation_string(s):
    l = s.split()
    return [int(l[i]) for i in range(1, 6, 2)]

if __name__ == "__main__":
    main()