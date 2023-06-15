#Write a program that asks user to enter dish name and it should print which cuisine is that disk

indian=["samsosa","daal","naan"]
chinese=["stick roll","fried rice","momo"]
italian=["pizza","pasta","risotto"]

dish=input("Enter a dish name:")

if dish in indian:
    print("It's Indian dish bro")

elif dish in chinese:
    print("It's chinese dish bro")
elif dish in italian:
    print("It's Itailian dish bro")
else: print("Based on little knowledge i cant say which dish is it sorry")
