s= input("enter a string: ")
length = len(s)
if length > 2 and s[-3:] == "ing":
    print(s + "ly")
else:
    print(s + "ing")