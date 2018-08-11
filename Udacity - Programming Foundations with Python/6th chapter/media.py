import webbrowser
class Movies():
    def __init__(self, m_title, m_storyline, poster_image, youtube_trailer):
        self.title = m_title
        self.storyline = m_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer
        
    def show_trailer(self):
        webbrowser.open(self.trailer_url)