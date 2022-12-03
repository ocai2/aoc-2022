"""
A = Rock
B = Paper
C = Scissors

X = Rock
Y = Paper
Z = Scissors

Points:
Rock = 1
Paper = 2
Scissors = 3
+
Win = 6
Draw = 3
Lose = 0

"""

def main():
    with open('day-2\input.txt', 'r') as f:
        data = f.read().splitlines()
    
    results = list(map(result, data))
    for x in results:
        print(x)
    print(sum(results))

def result(s):
    his_move = s[0]
    our_move = s[2]
    if his_move == 'A':
        if our_move == 'X':
            return 3 + 1
        elif our_move == 'Y':
            return 6 + 2
        elif our_move == 'Z':
            return 0 + 3
    elif his_move == 'B':
        if our_move == 'X':
            return 0 + 1
        elif our_move == 'Y':
            return 3 + 2
        elif our_move == 'Z':
            return 6 + 3
    elif his_move == 'C':
        if our_move == 'X':
            return 6 + 1
        elif our_move == 'Y':
            return 0 + 2
        elif our_move == 'Z':
            return 3 + 3

if __name__ == "__main__":
    main()