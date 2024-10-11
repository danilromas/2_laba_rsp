from musical_composition import Track
from album import Album
from file_manager import load_album_data, save_album_data

def display_menu():
    print("\n--- Music Collection Menu ---")
    print("1. Add track")
    print("2. Remove track")
    print("3. Display album")
    print("4. Total album duration")
    print("5. Sort tracks by style")
    print("6. Find track by duration range")
    print("7. Save and exit")
    print("----------------------------")

def add_track(album):
    title = input("Enter track title: ")
    artist = input("Enter artist: ")
    duration = float(input("Enter track duration (in minutes): "))
    style = input("Enter music style: ")
    track = Track(title, duration, style, artist)
    album.add_track(track)
    print(f"Track '{title}' added.")

def remove_track(album):
    title = input("Enter the title of the track to remove: ")
    album.remove_track(title)
    print(f"Track '{title}' removed.")

def display_album(album):
    print(f"\nAlbum: {album.title}")
    for track in album.tracks:
        print(track)

def total_album_duration(album):
    duration = album.total_duration()
    print(f"\nTotal album duration: {duration} minutes")

def sort_tracks_by_style(album):
    album.sort_tracks_by_style()
    print("\nTracks sorted by style.")

def find_track_by_duration_range(album):
    min_duration = float(input("Enter minimum duration: "))
    max_duration = float(input("Enter maximum duration: "))
    found_tracks = album.find_track_by_duration_range(min_duration, max_duration)
    if found_tracks:
        print("\nTracks found:")
        for track in found_tracks:
            print(track)
    else:
        print("No tracks found in the given duration range.")

def main():
    album = load_album_data('data.json')
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_track(album)
        elif choice == '2':
            remove_track(album)
        elif choice == '3':
            display_album(album)
        elif choice == '4':
            total_album_duration(album)
        elif choice == '5':
            sort_tracks_by_style(album)
        elif choice == '6':
            find_track_by_duration_range(album)
        elif choice == '7':
            save_album_data(album, 'data.json')
            print("Album saved. Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
