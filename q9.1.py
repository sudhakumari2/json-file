import json
dict={
    "shopping_list":
        { 
            "chaco":15,
            "Biscuits":50,
            "Diary_milk":30,
            "ice_cream":20,
        } 
}
item=input("enter which item would you like to buy=")
no_of_item=int(input("PLEASE enter How many item would you like to buy="))
for key in dict:
    for i in dict[key]:
        if i == item:
            dict[key][i]=(dict[key][i]-no_of_item)
print(json.dumps(dict, indent=4))
my_file=open("q9.json","w")
json.dump(dict,my_file,indent=4)
my_file.close()