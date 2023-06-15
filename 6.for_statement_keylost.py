#Search for key in home and when found print key found in a location

key_location="chair"
locations=["garage","Living Room","Kitchen","Sofa","chair"]
for i in locations:
    if i==key_location:
        print("Key Found in",i)
        break
    else:
        print("Key is not found in",i)
