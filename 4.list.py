#list are used to store multiple item in a single variable

items=["butter","fruits","oil","milk"]
print(items)
print(items[0])
print(items[1])
items[0]="pasta"
print(items)
print(items[0:2])
print(items[-1])
items.append("chocolate")
print(items)
items.insert(2,"cheese")
print(items)

bathroom=["soap","shampoo"]
total_item=items+bathroom
print(bathroom)
#to check
print("camera" in total_item)
print(len(total_item))
print("cheese" in total_item)
