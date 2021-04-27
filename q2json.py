import json
dic={"name":"sudha","age":20,"city":"bihar"}
out_file = open("q2.json", "w")
json.dump(dic, out_file, indent = 6)
out_file.close() 