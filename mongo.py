import pymongo
import dns
import sys
import base64, os
import gridfs


try:
  client = pymongo.MongoClient("mongodb+srv://sawyer:sawyer@hth.lu1wsfd.mongodb.net/?retryWrites=true&w=majority")
  
# return a friendly error if a URI error is thrown 
except pymongo.errors.ConfigurationError:
  print("An Invalid URI host error was received. Is your Atlas host name correct in your connection string?")
  sys.exit(1)

db = client.hth
fs = gridfs.GridFS(db)


def create(username, password): # add a username and associated password
    login = db["login"]
    user = login.find_one({"username": username})

    if user is not None:
        print("A user with that username has already been found")
        return False
    else:
        login.insert_one({"username": username, "password": password})
        return True

pdfs = []

def insert_pdf(file_name, file_path):
    with open(file_path, 'rb') as f:
        a = fs.put(f)
        pdfs.append(a)
        #string = base64.b64encode(f.read())
        #pdf.insert_one({"file_name": file_name, "pdf_data": string})
    

def read_and_save_pdf(file_name):
    with open("out.pdf", "wb") as f:
        f.write(fs.get(pdfs[-1]).read())


insert_pdf("HW6", "HW6.pdf")
read_and_save_pdf("HW6")
