import fresh_tomatoes as ft
from media import Movie

scott_pilgram = Movie("Scott Pilgrim vs The World",
    "Scott Pilgrim must defeat his new girlfriend's seven evil exes in order to win her heart",
    "https://images-na.ssl-images-amazon.com/images/I/51oQ%2B6P1vuL.jpg", 
    "https://www.youtube.com/watch?v=7wd5KEaOtm4")

thor = Movie("Thor",
    "The powerful, but arrogant god Thor, is cast out of Asgard to live amongst humans in Midgard (Earth), where he soon becomes one of their finest defenders",
    "https://vignette.wikia.nocookie.net/marvelmovies/images/6/61/Thor_poster_red.jpg/revision/latest?cb=20140218060252",
    "https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&cad=rja&uact=8&ved=0ahUKEwjwu72kjsHaAhWKwI8KHairC4wQtwIILDAB&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DJOddp-nlNvQ&usg=AOvVaw1TAo0LF67gfJvvJAWu7_6D")

law_abiding_citizen = Movie("Law Abiding Citizen",
    "A frustrated man decides to take justice into his own hands after a plea bargain sets one of his family's killers free. He targets not only the killer but also the district attorney and others involved in the deal.", 
    "http://cdn.collider.com/wp-content/image-base/Movies/L/Law_Abiding_Citizen/Posters/law_abiding_citizen_gerard_butler_movie_poster_01.jpg", 
    "https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwiDi5v0jsHaAhWMQ48KHa-SCokQyCkIJzAA&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DLX6kVRsdXW4&usg=AOvVaw1cfS7nud1sUCW58pzmkMy7")

movies = [scott_pilgram, thor, law_abiding_citizen]

ft.open_movies_page(movies)