# -*- coding utf-8 -*-

from src import playlist
from src.database import trackdb, coverdb
import os

folder = u'D:/Drive E/Vietnam'
songs = [folder + '/' + song for song in os.listdir(folder)]
trackdata = trackdb.TrackDB('D:/Cloud/Dropbox/Programming/Code/py/Miusik/test/data/trackdb')
coverdata = coverdb.CoverDB('D:/Cloud/Dropbox/Programming/Code/py/Miusik/test/data/coverdb')


def test1():
    # trackdata = trackdb.TrackDB('D:/Cloud/Dropbox/Programming/Code/py/Miusik/test/data/trackdb')
    # coverdata = coverdb.CoverDB('D:/Cloud/Dropbox/Programming/Code/py/Miusik/test/data/coverdb')
    # print len(trackdata), trackdata.get_songs()
    # print len(coverdata), coverdata.get_covers_keys()
    my_playlist = playlist.Playlist('Playlist 1')
    playlist_loc = "D:/Cloud/Dropbox/Programming/Code/py/Miusik/test/data/Playlist 1.db"
    my_playlist.set_loc(playlist_loc)
    for song in songs:
        # print song
        my_playlist.add_track(song, trackdata, coverdata)

    print my_playlist.get_loc_list()

    my_playlist.save_self()
    trackdata.save_db()
    coverdata.save_db()
