def main():
    with open('day-6\input.txt', 'r') as f:
        data = f.read()
    
    result = 0
    s = data
    for i, _ in enumerate(s):
        if len(set(s[i:i+14])) == 14:
            print(i, set(s[i:i+14]), s[i:i+14])
            result = i + 14
            break
    
    print(result)

if __name__ == "__main__":
    main()