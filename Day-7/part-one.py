class directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.size = 0
        self.children = []

def main():
    with open('day-7\input.txt', 'r') as f:
        data = f.read().splitlines()

    root = directory('/', None)
    current_directory = root
    
    for i in range(1, len(data), 1):
        line = data[i].split()
        if line[0] == "$":
            # cd
            if len(line) > 2:
                if line[2] == "..":
                    current_directory = current_directory.parent
                else:
                    current_directory = next(d for d in current_directory.children if d.name == line[2])
            # ls
            else:
                i += 1
                size = 0
                while data[i][0] != "$":
                    line = data[i].split()
                    if line[0] == "dir":
                        current_directory.children.append(directory(line[1], current_directory))
                    else:
                        size += int(line[0])
                    i += 1
                    if i >= len(data):
                        break
                current_directory.size += size
                add_to_parent(current_directory, size)
    
    q = [root]
    total_sum = 0
    while len(q) > 0:
        d = q.pop()
        if d.size <= 100000:
            total_sum += d.size
        for c in d.children:
            q.append(c)
    
    print(total_sum)
            
def add_to_parent(x, n):
    while x.parent != None:
        x = x.parent
        x.size += n

if __name__ == "__main__":
    main()