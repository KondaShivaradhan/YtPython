
from firebase_admin import credentials, initialize_app, firestore, storage
import firebase_admin
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['YtMusic']
collection = db["allSongs"]

# initialize_app()
cred = credentials.Certificate('serviceAccountKey.json')
initialize_app(cred)
db = firestore.client()
bucket = storage.bucket(name='check')
# bucket = storage.bucket()
# blob = bucket.blob("path/to/your/file.m4a")
# blob.upload_from_filename("path/to/local/file.m4a")
def upload_file(file_path, destination):
    blob = bucket.blob(destination)
    blob.upload_from_filename(file_path)
    return blob.public_url

def add_song(data):
    print(data)
    songpath = './downloads/AbaAxgufFA8.m4a'
    upload_file(songpath,'/songs')
    doc_ref = db.collection('allSongs').document(data['vid'])
    doc_ref.set({
        'vid':data['vid'],
        'title': data['title'],
        'thumb': data['thumb'],
        'url': data['url'],
        'duration':data['duration']
    })
    print('dont adding to firebase')
    # Mongo DB
    result = collection.find_one({"vid": data['vid']})
    if result is None:
        collection.insert_one(data)
        print('inserting new one')
    else:
        print('updating exsisting one')
        
        collection.update_one({"vid": data['vid']},{"$set": data})
    client.close()
    
    collection = db['allSongs']
    filter_query = {'vid': data['vid']}
    update_query = {
        '$set': {
            'vid': data['vid'],
            'title': data['title'],
            'thumb': data['thumb'],
            'url': data['url']
        }
    }

    collection.update_one(filter_query, update_query, upsert=True)

