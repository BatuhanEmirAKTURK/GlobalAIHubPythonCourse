mylist = [1,2,3,4,5,6,7,8,9]

print("The first version of the list\n",mylist)

a = mylist[:4]
b = mylist[4:]

a , b = mylist[4:] , mylist[:4]

print("\nPerforming swap operation ... Please wait ...")

print("\nLatest version of the list\n",a + b)
