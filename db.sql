DROP DATABASE IF EXISTS playnaliticsDB;
CREATE DATABASE playnaliticsDB;
USE playnaliticsDB;

CREATE TABLE playlists (
    Id VARCHAR(22) NOT NULL PRIMARY KEY,
    userId VARCHAR(10) NOT NULL,
    title VARCHAR(100) NOT NULL
);

CREATE TABLE tracks (
    Id VARCHAR(22) NOT NULL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    artist VARCHAR(50) NOT NULL,
    acusticness FLOAT(10) NOT NULL,
    danceability FLOAT(10) NOT NULL,
    energy FLOAT(10) NOT NULL,
    valence FLOAT(10) NOT NULL,
    loudness FLOAT(10) NOT NULL,
    musicKey INT,
    bpm FLOAT(10) 
);

CREATE TABLE playlisttracks(
    IdPlaylist VARCHAR(22) NOT NULL,
    IdTrack VARCHAR(22) NOT NULL,
    FOREIGN KEY (IdTrack) REFERENCES tracks(Id),
    FOREIGN KEY (IdPlaylist) REFERENCES playlists(Id),
    PRIMARY KEY(IdTrack, IdPlaylist)
)