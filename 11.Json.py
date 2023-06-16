#JSON - Java Script object Notation

#JSon is a data exchange format which is similar to XML

#Json is a light weight format compared to XML

# * To create address book and write some records into it
# * Read this address book

book={}
book['tom']={
    'name':'tom',
    'address':'1 Street, NY',
    'phone':'9804857308'

}
book['alex']={
    'name':'alex',
    'address':'Texas',
    'phone':'9806878508'
}
import json
s=json.dumps(book)
print(s)
with open("book.txt","w") as f:
    f.write(s)

