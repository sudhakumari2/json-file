import json
filename = 'my_file.txt'
dict1 = {}
with open(filename) as fh:
    for line in fh:
        command, description = line.strip().split(None,1)
        dict1[command] = description.strip()
out_file = open("q7.json", "w")
json.dump(dict1, out_file, indent = 4)
out_file.close()