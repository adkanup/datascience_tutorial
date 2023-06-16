# Reading and writing file

#create a new file and write into it
# Reading file line by line
# file open modes
# with statement

f=open("funnny.txt","w")
f.write("I love python")
f.close()

#for append
f=open("funnny.txt","a")
f.write(" \n I love C++")
f.close()

#reading line by line from the line funny.txt
