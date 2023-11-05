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


def create(username, password, grade, subject): # add a username and associated password
    login = db["login"]
    user = login.find_one({"username": username})
    
    if user is not None:
        print("A user with that username has already been found")
        return False
    elif username == "" or password == "":
        print("Please enter a username and password")
        return False
    else:
        login.insert_one({"username": username, "password": password, "grade": grade, "subject": subject})
        return True

pdfs = []

def insert_pdf(file_name, file_path, grade, title, subject):
    pdfs = db["pdfs"]
    with open(file_path, 'rb') as f:
        a = fs.put(f)
        pdfs.insert_one({
                "file_name": file_name,
                "grade": grade,
                "title": title,
                "rating": 0,
                "number_of_ratings": 0,
                "ref": a,
                "subject": subject
            })
    

def read_and_save_pdf(file_name, ref):
    with open(file_name, "wb") as f:
        try:
            page = fs.get(ref).read()
            try:
                f.write(page)
            except:
                print("writing to page failed")
        except:
            print("getting page from fs failed")

def validate_user(username, password):
    login = db["login"]

    user = login.find_one({"username": username, "password": password})
    if user is None:
        print("User not found")
        return False
    else:
        print("User found")
        return True

def search_for_pdf(subject, grade):
    pdfs = db["pdfs"]    
    results = pdfs.find({"subject": subject, "grade": grade})
    return results

def add_rating(ref, rating):
    pdfs = db["pdfs"]
    result = pdfs.find_one({"ref": ref})
    if result is None:
        print("Error leaving rating")
        return False
    else:
        pdfs.update_one({"ref": ref}, {"$set": {
                "rating": result["rating"] + rating,
                "number_of_ratings": result["number_of_ratings"] + 1
            } 
        })
        print("Updating ratings successfully")
        return True
