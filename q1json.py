import json
dict={"Name":"Ram", 
     "Class":"IV", 
     "Age":9 }
with open("jsonq1.json","w")as a:
    json.dump(dict,a,indent=6)
with open("jsonq1.json","r")as a:
    b=json.load(a)
    print(b)
