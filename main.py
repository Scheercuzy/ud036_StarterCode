import fresh_tomatoes as ft
from media import Movie

# Making instances
scott_pilgram = Movie(
	"Scott Pilgrim vs The World",
	"Scott Pilgrim must defeat his new girlfriend's seven evil exes in order "
	"to win her heart",
	"https://images-na.ssl-images-amazon.com/images/I/51oQ%2B6P1vuL.jpg",
	"https://www.youtube.com/watch?v=7wd5KEaOtm4")

thor = Movie(
	"Thor",
	"The powerful, but arrogant god Thor, is cast out of Asgard to live "
	"amongst humans in Midgard (Earth), where he soon becomes one of their "
	"finest defenders",
	"https://vignette.wikia.nocookie.net/marvelmovies/images/6/61/Thor_poster_red.jpg/revision/latest?cb=20140218060252", # NOQA
	"https://www.youtube.com/watch?v=JOddp-nlNvQ")

law_abiding_citizen = Movie(
	"Law Abiding Citizen",
	"A frustrated man decides to take justice into his own hands after a plea "
	"bargain sets one of his family's killers free. He targets not only the "
	"killer but also the district attorney and others involved in the deal.",
	"http://cdn.collider.com/wp-content/image-base/Movies/L/Law_Abiding_Citizen/Posters/law_abiding_citizen_gerard_butler_movie_poster_01.jpg", # NOQA
	"https://www.youtube.com/watch?v=LX6kVRsdXW4")

# Listing instances
movies = [scott_pilgram, thor, law_abiding_citizen]

# Generating Website
ft.open_movies_page(movies)
