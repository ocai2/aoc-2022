def main():
    with open('day-6\input.txt', 'r') as f:
        data = f.read()
    
    result = 0
    s = data
    for i, _ in enumerate(s):
        if len(set(s[i:i+4])) == 4:
            print(i, set(s[i:i+4]), s[i:i+4])
            result = i + 4
            break
    
    print(result)

if __name__ == "__main__":
    main()