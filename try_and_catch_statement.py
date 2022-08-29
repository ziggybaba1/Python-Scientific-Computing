movie_title = "Salsa dance"
try:
    movie_title = input("Please add movie part: ")
    #purposely wants to test for error
    movie_title = int(movie_title)  
except:
    movie_title = -1
if movie_title != -1:
     print("Movie part is: ",movie_title)
else:
     print("Movie part is", "Input error, it should be a number")