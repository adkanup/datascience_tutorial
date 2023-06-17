x=int(input("Enter a First Number:")) #1
y=int(input("Enter a Second Number:")) #0
try:
    z= x/y
except Exception as e:

    print('exception occured',e)
    z= None
print("division is :",z)
