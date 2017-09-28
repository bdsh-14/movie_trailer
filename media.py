import webbrowser

class Movie():
    def __init__(self, movie_name, movie_storyline, movie_poster_image, movie_trailer_youtube):
        self.title = movie_name
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image
        self.trailer = movie_trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer)


    def show_storyline(self):
        print(self.storyline)