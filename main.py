from imdb import IMDb

# create an instance of the IMDb class
ia = IMDb()

# get a movie
advTime = ia.get_movie('1305826')

# print the names of the directors of the movie
print('Directors:')
for director in advTime['directors']:
    print(director['name'])

# print the genres of the movie
print('Genres:')
for genre in advTime['genres']:
    print(genre)

# search for a person name
people = ia.search_person('Mel Gibson')
for person in people:
   print(person.personID, person['name'])