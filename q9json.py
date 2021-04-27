import json
dic={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        }  
}
for j in dic.values():
    for i in j:
        print(i)
    item=input("enter which} item would you like to buy=")
    if  item in j:
        no_of_item=int(input("enter no of item"))
        for k in j.values():
            k=int(k)
            if no_of_item<=k:
                a=k-no_of_item
                a=str(a)
                dic["shopping_list"][item]=a
                break   
            elif no_of_item>k:
                k=int(k)
                a=no_of_item-k
                a=a+k
                c=a-a
                c=str(c)
                dic["shopping_list"][item]=c
                break
    else:
        break
my_file=open("q91.json","w")
json.dump(dic,my_file ,indent=4)
my_file.close()
            