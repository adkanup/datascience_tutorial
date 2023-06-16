f=open("funnydai","r")
f_out=open("funny_count.txt","w")
for line in f:
    token=line.split(' ')
    f_out.write(line+"wordcount:"+str(len(token)))
    f.close()
    f_out.close()

