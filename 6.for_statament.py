exp=[2340,3500,3600,3100,2950]
total=0
for item in exp:
    total=total+item
    print(total)

#use range () function 1 to 10 print
for i in range(1,11):
    print(i*i)

for i in range(1,11):
    print(i*2)


# In our monthly expenses example,print monthly number and expenses with total

expenses=[2500,1200,3600,2800]
total = 0
for i in range(len(expenses)):

    print(i+1,expenses[i])
    total=total+expenses[i]
print("total",total)