account=("test","test1","test2","password")
username=input("enter username")
password=input("enter password"+username+":")
if (account.get(username)==password):
    print("login sucessfull")
    test=input(".")
else:
    print("login failed")