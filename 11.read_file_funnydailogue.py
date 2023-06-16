#reading file from the text funnydai
f=open("funnydai","r")
# print(f.read())
for line in f:
    print(line)
    token=line.split(' ') #split
    print(str(token))
    print(len(token))
f.close()



