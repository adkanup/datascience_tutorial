#Dictionaries allows you to store key,value pairs.

#They are also known as Maps,hashtables,Associate Arrays

d={"tom":9801234567890,"alex":9800234567890,"william":9800034567890}
print("The Telephone number of user's are:",d) #print
# to access the specific person

display=d["tom"]
print("The number of tom is:",display)

#To add trump
d["trump"]=9801020304
print(d)

#to delete trump
del d["trump"]
print(d)

#for display key and values

for key in d:
    print("key:",key,"values:",d[key])

#To perform operation in python

print("alex" in d)
print("john" in d)

# to clear dictionary
d.clear()
print(d)