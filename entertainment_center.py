import media
import fresh_tomatoes

# create the following objects
avator = media.Movie(
    "Avatar",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
)
fast_and_furious_8 = media.Movie(
    "Fast & Furious 8",
    "https://upload.wikimedia.org/wikipedia/en/2/2d/The_Fate_of_The_Furious_Theatrical_Poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=uisBaTkQAEs"
)
logan = media.Movie(
    "Logan",
    "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
    "https://www.youtube.com/watch?v=Div0iP65aZo"
)
wonder_woman = media.Movie(
    "Wonder Woman",
    "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",  # noqa
    "https://www.youtube.com/watch?v=VSB4wGIdDwo"
)
wolf_warrior_2 = media.Movie(
    "Wolf Warrior 2",
    "https://upload.wikimedia.org/wikipedia/en/1/11/Wolf_Warriors_poster.jpg",
    "https://www.youtube.com/watch?v=fkqGiPB2D8M"
)

# add all movies above into a list named movies
movies = [avator, fast_and_furious_8, logan, wonder_woman, wolf_warrior_2]

# call the function "open_movies_page" defined in fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)
