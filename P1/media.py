import webbrowser #import module to open webbrowser

class Movie():
    """ This class provides a way to store movie related information"""
    
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube): #class constructor to definite variables from data source
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    
    def show_trailer(self): #method: open browser and play a trailer of a movie
        webbrowser.open(self.trailer_youtube_url)