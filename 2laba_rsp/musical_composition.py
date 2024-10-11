class MusicalComposition:
    def __init__(self, title, duration, style):
        self.title = title
        self.duration = duration  # В минутах
        self.style = style

    def __str__(self):
        return f"'{self.title}', {self.duration} min, style: {self.style}"

class Track(MusicalComposition):
    def __init__(self, title, duration, style, artist):
        super().__init__(title, duration, style)
        self.artist = artist

    def __str__(self):
        return f"Track: {super().__str__()}, artist: {self.artist}"
