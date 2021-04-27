import json
a={"a":  1,"a":  2,"a":  3, "a": 4,   "b": 1, "b": 2}
my_file = open("q6.json", "w")
json.dump(a, my_file, indent = 3)
my_file.close() 
