import webbrowser


class Movie(object):
    " Class for movie trailer "
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_release_date):
        """ Class describing the movie
        Args:
        title (str)= movie's title
        storyline (str)= what the movie is about
        poster_image_url (str)= URL to a poster image
        trailer_youtube_url (str)= youtube video of the movie's trailer
        release_date (str)= date the movie was release
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = movie_release_date

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
