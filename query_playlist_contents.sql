SELECT * 
FROM tracks
INNER JOIN playlisttracks
ON tracks.Id = playlisttracks.IdTrack
WHERE IdPlaylist = "chosenPlaylistID"