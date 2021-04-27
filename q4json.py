
my_dic={'4': 5, '6': 7, '1': 3, '2': 4}
dic={}
a=sorted(my_dic.keys())
for i in a:
    for j in my_dic:
            dic.update({i:my_dic[i]})
print(dic)
import json
with open("q4.json","w") as a:   
    json.dump(dic,a, indent = 4)

