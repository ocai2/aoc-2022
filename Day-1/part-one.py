def main():
    with open('day-1\input.txt', 'r') as f:
        data = f.read().splitlines()
    
    max_calories = 0
    calories = 0

    for x in data:
        if x == '':
            max_calories = max(max_calories, calories)
            calories = 0
        else:
            calories += int(x)

    print(max_calories)
    

if __name__ == "__main__":
    main()