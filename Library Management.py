#JEPHIN JOHN
#LIBRARY MANAGEMENT USING MONGODB

#importing dependancies

import pymongo as pm
from pymongo import MongoClient

#importing client
print("Connecting to Client...")
jephin_client = MongoClient("localhost",27017)
db = jephin_client["library"]
collection = db["library"]
print("Client, Database Connection Successfully Established. \n")

#function definitions
def search(book_name : str):
    results=collection.find({"book_name": book_name})
    for result in results:
        print("Book Name: ", result["book_name"], "Author: ", result["author"], "Count: ", result["count"])

def insert(book_name : str, author : str,count : int):
    post={"book_name" : book_name, "author" : author, "count" : count}
    collection.insert_one(post)

def update(book_name : str):
    results=collection.find({"book_name" : book_name})
    for result in results:
        x : int = result["count"]
        if(x>=1):
            print("Updating...",book_name,"\n")
            collection.update({"book_name": book_name}, {"$inc": {"count": -1}})
        else:
            print("Not Enough Copies!!! \n")

def delete(book_name : str):
    results = collection.find({"book_name" : book_name})
    for result in results:
        collection.delete_one(result)

#Library Management MENU

while(True):
    x=int(input("\nEnter the choice\n1:-Search\n2:-Insert\n3:-Update\n4:-Delete\n5:Exit\n"))
    if(x==1):
        book_name= str(input("Enter book name : "))
        search(book_name)
    elif(x==2):
        book_name= str(input("Enter book name : "))
        author = str(input("Enter author name : "))
        count = int(input("Enter count : "))
        insert(book_name,author,count)
    elif(x==3):
        book_name = str(input("Enter book name : "))
        update(book_name)
    elif(x==4):
        book_name = str(input("Enter book name : "))
        delete(book_name)
    elif(x==5):
        print("PROGRAM TERMINATED.")
        exit()