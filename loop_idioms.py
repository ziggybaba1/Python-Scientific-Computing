movies=[4,5,81,22,100,41]
movie_number=-1
print("Before:",movie_number)
for in_movie in movies:
    if in_movie > movie_number:
        movie_number=in_movie
    print(in_movie,movie_number)
print("highest:",movie_number)
