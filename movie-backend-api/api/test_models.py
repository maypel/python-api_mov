# %%
from database import SessionLocal
from models import Movie, Rating, Tag, Link

db = SessionLocal()

# %% 
# Tester la récupération de quelques films
movies = db.query(Movie).limit(20).all()

if movies:
    for movie in movies:
        print(f"ID : {movie.movieId}, Titre : {movie.title}, Genres : {movie.genres}")
else:
    print("No movies found.")

# %%
#  Récupérer les films du genre Romance
romance_movies = db.query(Movie).filter(Movie.genres.like("%Romance%")).limit(10).all()

if romance_movies:
    for movie in romance_movies:
        print(f"ID : {movie.movieId}, Titre : {movie.title}, Genres : {movie.genres}")
else:
    print("No romance movies found.")

# %%
# Tester la récupération de quelques évaluations (ratings)
Ratings = db.query(Rating).limit(5).all()

for rating in Ratings:
    print(f"User ID : {rating.userId}, Movie ID : {rating.movieId}, Rating : {rating.rating}, Timestamp : {rating.timestamp}")
# %%
# Films avec une note supérieure ou égale à 4
high_rated_movies = db.query(Movie).join(Rating).filter(Rating.rating >= 4).limit(5).all()

for title, rating in high_rated_movies:
    print(title, rating)
    
# %%
hight_rated_movies = (
    db.query(Movie.title, Rating.rating)
    .join(Rating)
    .filter(Rating.rating >= 4)
    .limit(5)
    .all()
    
)
print(hight_rated_movies)

for title, rating in hight_rated_movies:
    print(title, rating)


# %%
hight_rated_movies = (
    db.query(Movie.title, Rating.rating)
    .join(Rating)
    .filter(Rating.rating >= 4, Movie.movieId == Rating.movieId)
    .limit(5)
    .all()
    
)
print(hight_rated_movies)

for title, rating in hight_rated_movies:
    print(title, rating)

# %%
# Récupération des tags associés aux films
tags = db.query(Tag).limit(5).all()

for tag in tags:  
    print(f"User ID : {tag.userId}, Movie ID : {tag.movieId}, Tag : {tag.tag}, Timestamp : {tag.timestamp}")

# %%
# Tester la classe Link
links = db.query(Link).limit(5).all()

for link in links:
    print(f"Movie ID : {link.movieId}, IMDB ID : {link.imdbId}, TMDB ID : {link.tmdbId}")
# %%
# fermer la Session
db.close()
# %%
