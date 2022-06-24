#importing dependancies

from flask import Flask
from pymongo import *
import json
from bson import json_util

print("Connecting to MongoClient")
jephin_client = MongoClient("localhost",27017)
db=jephin_client["library"]
collections=db["library"]
print("Connection Successfully Establised to LocalHost, Port:27017 to Local Database: Library ")

lib_flask=Flask("__name__")

@lib_flask.route("/books", methods=['GET'])
def root():
    book_data = list(collections.find({}))
    return json.dumps(book_data,default=json_util.default)

if __name__ == "__main__":
    lib_flask.run(debug=True)