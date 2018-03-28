import pymongo

client = pymongo.MongoClient(host='localhost')
collection = client.lianxi.sutdents

student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}

result = collection.insert_many([student1, student2])
condition1 = {'id':'20170202'}
condition2 = {'id':{'$gt':2}}
print( collection.find_one(condition1))
result = collection.find_one(condition1)
result['gender'] = 'female'
result = collection.update_one(condition1, {'$set':result})
print(result.matched_count, result.modified_count)
print(collection.find_one(condition1))
