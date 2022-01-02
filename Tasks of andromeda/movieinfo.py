#import our library that we are going to use fro the project
import imdb
#create the variable that defines the utilitie of the library in our project
hr = imdb.IMDb()
#ask the user to enter the name of the movie, in order to offer the description of the input name
movie_name = input("enter the movie name:  ")
#search the movide name in the database
movies = hr.search_movie(str(movie_name))
#create the index that holds the list of items, such as the title, year of realese and the full cast. Extracting the first result of the index
index = movies[0].getID()
#getting the movide with the index help
movie = hr.get_movie(index)
#we extract the data from the search and index results. This specifies each process.
title = movie['title']
year = movie ['year']
cast = movie ['cast']
#structuring the results
list_of_cast = ','.join(map(str,cast))
#print the results
print("title: ", title)
print("year of release: ", year)
print("full cast : ", list_of_cast)