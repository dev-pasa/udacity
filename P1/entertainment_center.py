import fresh_tomatoes # only work if fresh_tomatoes.py file in the same folder with media.py and entertainment_center.py
import media # Use functions from media.py
# You can replace the following instances with your favorite movie
# movie_name = media.Movie("Name", "Storyline", "Poster URL (you can get from wikipiedia)", "movie trailier URL from youtube"


toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=4KPTXpQehio")

avatar = media.Movie("Avatar", "A marine on an alien planet", "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

interstellar = media.Movie("Interstellar", "A science finction epic film", "http://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg", "https://www.youtube.com/watch?v=2LqzF5WauAw")

transcendence = media.Movie("Transcendence", "A science fiction film directed by cinematographer Wally Pfister", "http://upload.wikimedia.org/wikipedia/en/e/ef/Transcendence2014Poster.jpg", "https://www.youtube.com/watch?v=VCTen3-B8GU")

the_lego_movie = media.Movie("The Lego Movie", "A 2014 computer animated adventure comedy film", "http://upload.wikimedia.org/wikipedia/en/1/10/The_Lego_Movie_poster.jpg", "https://www.youtube.com/watch?v=fZ_JOBCLF-I")

big_hero_6 = media.Movie("Big Hero 6", "a 2014 American 3D computer-animated superhero action comedy film", "http://upload.wikimedia.org/wikipedia/en/4/4b/Big_Hero_6_%28film%29_poster.jpg", "https://www.youtube.com/watch?v=z3biFxZIJOQ")

movies = [toy_story, avatar, interstellar, transcendence, the_lego_movie, big_hero_6]
# Once you finished updating with your own movie, do not forget to update the list

fresh_tomatoes.open_movies_page(movies) # use fresh_tomatoes.py to call the function open_movie_page 