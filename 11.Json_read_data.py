f=open("book.txt","r") #your file direction
s=f.read()
print(s)

import json
book=json.loads(s)
book

#to know the type of data
print(type(book))

#to read tom data
print(book['tom'])

#to read tom address
for person in book:
    print(book[person])


