#Defining function

#Named and positional Argument
total=0
def sum(a,b):
    #Document strings this function takes two arguments which are integers numbers and it will return sum of them as output

    '''

    :param a:
    :param b:
    :return:
    '''
    print("The value of a is:",a)
    print("The value of b is",b)
    total=a+b
    print("Inside argument",total) #local variable
    return total

n=sum(b=5,a=6)
print("Inside argument:",total)#Gobal variable


total=0
def subtract(a,b=0):
    print("The value of a is:",a)
    print("The value of b is",b)
    total=a-b
    print("The value of total inside is :",total)
    return total


n=subtract(5)
print("The subtract of value is:",total)

