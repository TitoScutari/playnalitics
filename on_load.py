from playlist_list import PlaylistList
from spotify_user import SpotifyUser
from playnaliticsDB import playnaliticsDB

def main():
    user = SpotifyUser(current=True)
    user.get_data()

    db = playnaliticsDB()
    db.connect()
    db.clean()
    db.commit()

    db.insert_user(user)
    db.close(commit=True)

    playlist_list = PlaylistList()
    playlist_list.load_list(user.id)
    playlist_list.write_json("current_user_playlists.json")

if __name__ == "__main__":
    main()

