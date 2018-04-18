class Movie():
    """A class for all the information we need about movies"""
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """
        Parameters needed to contruct the class:

        :parm movie_title: string
        :parm movie_storyline: string
        :parm poster_image: string
        :parm trailer_youtube: string
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
