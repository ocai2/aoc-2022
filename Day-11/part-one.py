import math

class monkey:
    def __init__(self, number):
        self.number = number
        self.items = []
        self.operator = ""
        self.value = ""
        self.divisor = 0
        self.true_monkey_num = None
        self.false_monkey_num = None
        self.inspect_count = 0

def main():
    with open('day-11\input.txt', 'r') as f:
        data = f.read().split('\n\n')

    # read monkeys
    monkey_list = []
    for i, x in enumerate(data):
        monkey_list.append(monkey(i))

        lines = x.splitlines()

        line_one = lines[1].split()
        starting_items = [int(s.strip(',')) for s in line_one[2:]]
        monkey_list[i].items = starting_items

        line_two = lines[2].split()
        operator = line_two[4]
        value = line_two[5]
        monkey_list[i].operator = operator
        monkey_list[i].value = value

        line_three = lines[3].split()
        divisor = int(line_three[3])
        monkey_list[i].divisor = divisor

        true_monkey = int(lines[4][-1])
        false_monkey = int(lines[5][-1])
        monkey_list[i].true_monkey_num = true_monkey
        monkey_list[i].false_monkey_num = false_monkey

    # for x in monkey_list:
    #     print()
    #     print(f'monkey = {x.number}')
    #     print(f'items = {x.items}')
    #     print(f'operator = {x.operator}')
    #     print(f'value = {x.value}')
    #     print(f'divisor = {x.divisor}')
    #     print(f'true = {x.true_monkey_num}')
    #     print(f'false = {x.false_monkey_num}')

    n_monkeys = len(data)
    current_monkey = 0
    for i in range(20 * n_monkeys):
        for item in monkey_list[current_monkey].items:
            item = get_operated_item(item, monkey_list[current_monkey].operator, monkey_list[current_monkey].value)
            if throw_item(item, monkey_list[current_monkey].divisor):
                monkey_list[monkey_list[current_monkey].true_monkey_num].items.append(item)
            else:
                monkey_list[monkey_list[current_monkey].false_monkey_num].items.append(item)
            monkey_list[current_monkey].inspect_count += 1
        monkey_list[current_monkey].items.clear()
        
        current_monkey += 1
        if current_monkey == n_monkeys:
            current_monkey = 0
    
    monkey_list.sort(key = lambda x: x.inspect_count, reverse=True)
    for x in monkey_list:
        print()
        print(f'monkey = {x.number}')
        print(f'items = {x.items}')
        print(f'operator = {x.operator}')
        print(f'value = {x.value}')
        print(f'divisor = {x.divisor}')
        print(f'true = {x.true_monkey_num}')
        print(f'false = {x.false_monkey_num}')
        print(f'count = {x.inspect_count}')
    
    print(monkey_list[0].inspect_count * monkey_list[1].inspect_count)

def throw_item(item, divisor):
    return item % divisor == 0

def get_operated_item(item, operator, value):
    if value == "old":
        value = item
    else:
        value = int(value)
    
    if operator == "+":
        return math.floor((item + value) / 3)
    if operator == "-":
        return math.floor((item - value) / 3)
    if operator == "*":
        return math.floor((item * value) / 3)
    if operator == "/":
        return math.floor((item / value) / 3)
        
if __name__ == "__main__":
    main()