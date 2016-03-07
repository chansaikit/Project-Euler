import csv, string

with open("../data/p022_names.txt", "rb") as f: 
    for row in csv.reader(f, delimiter =',')  : 
        data = sorted(row, key=str.lower)
        print sum((sum([string.lowercase.index(a)+1 for a in data[x].lower()]) * (x+1)) for x in range(len(data))) 