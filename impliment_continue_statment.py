a = ["shirt", "sock", "pants", "sock", "towel"]
b=[]
for i in a:
    # print(i)
    if i == "sock":
        continue
    else:
        print(f"washing {i}")
b.append(i)    
print(b)