class Album:
    def __init__(self, title):
        self.title = title
        self.tracks = []

    def add_track(self, track):
        self.tracks.append(track)

    def remove_track(self, track_title):
        self.tracks = [track for track in self.tracks if track.title != track_title]

    def total_duration(self):
        return sum(track.duration for track in self.tracks)

    def sort_tracks_by_style(self):
        self.tracks.sort(key=lambda track: track.style)

    def find_track_by_duration_range(self, min_duration, max_duration):
        return [track for track in self.tracks if min_duration <= track.duration <= max_duration]

    def __str__(self):
        return f"Album: {self.title}, Tracks: {len(self.tracks)}"
