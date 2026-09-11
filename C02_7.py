s= input("emter a string: ")
if s[-3:] == "ing":
    print(s[:-3] + "ly")
else:
    print(s + "ing")