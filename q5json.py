import json
dict={"Name":"sudha","Age":20,"Num":[1,2,3,4],"Bool":True}
data=json.dumps(dict)
print(data)
my_file=open("q5.json","w")
json.dump(dict,my_file,indent=4)
my_file.close()
# complex data type