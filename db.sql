DROP DATABASE IF EXISTS playnaliticsDB;
CREATE DATABASE IF NOT EXISTS playnaliticsDB;
USE playnaliticsDB;

CREATE TABLE playlists (
    Id VARCHAR() NOT NULL PRIMARY KEY
    userId VARCHAR() NOT NULL
    title VARCHAR(100) NOT NULL
    loaded BOOLEAN NOT NULL
);

CREATE TABLE tracks (
    Id VARCHAR() NOT NULL PRIMARY KEY
    title VARCHAR(100) NOT NULL
    artist VARCHAR(50) NOT NULL
    acusticness FLOAT(10) NOT NULL
    danceability FLOAT(10) NOT NULL
    energy FLOAT(10) NOT NULL
    valence FLOAT(10) NOT NULL
    loudness FLOAT(10) NOT NULL
);

CREATE TABLE playlisttracks(
    IdTrack VARCHAR() NOT NULL
    IdPlaylist VARCHAR() NOT NULL
    FOREIGN KEY (IdTrack) REFERENCES tracks(Id)
    FOREIGN KEY (IdPlaylist) REFERENCES playlists(Id)
    PRIMARY KEY(IdTrack, IdPlaylist)
)