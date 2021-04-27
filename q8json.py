import json
a=[["neelam","programer","24","2400"],
["komal","trainer","24","20000"],
["anuradha","HR","25","40000"],
["Abhishek","manager","29","63000"] ] 
dic1={}
list3=[]
list1=["name","designation","age","salary"]
list2=["emp1","emp2","emp3","emp4"]
for  i in a:
    j=0
    dict2={}
    while j<len(i):
        dict2[list1[j]]=i[j]
        j+=1
    list3.append(dict2)
for k in list3:
    for j in list2:
        dic1[j]=k
print(dic1)
with open("q8.json","w")as b:
    json.dump(dic1,b,indent=4)
