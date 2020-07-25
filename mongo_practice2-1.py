from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

target_movie = db.movies.find_one({'title': '월-E'})
target_rating = target_movie['rating']

movies = list(db.movies.find({'rating': target_rating}))

for movie in movies:
    print(movie['title'])



db.movies.update_many({'rating':target_rating},{ '$set': {'rating':0} })
