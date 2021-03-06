from ast import literal_eval
from src import common
import shelve
import gc


class CoverDB():
    def __init__(self, loc):
        self._loc = loc
        self.__covers = {}
        self.load_db()
        self._added = False
        self._removed = False
        self._unsaved_updated_covers = []

    def __len__(self):
        return len(self.__covers)

    def get_covers_keys(self):
        return self.__covers.keys()

    def add_to_updated_covers(self, covers):
        pass

    def add_cover(self, album, albumartist, cover):
        if (album, albumartist) not in self.get_covers_keys():
            self.__covers[(album, albumartist)] = cover
            self._added = True

    def add_cover_from_track(self, trackobj):
        al_ar = trackobj.get_album_n_albumartist()
        cover = trackobj.get_tag_disk('cover')
        if cover:
            self.add_cover(al_ar[0], al_ar[1], cover)

    def remove_cover(self, album, albumartist):
        try:
            del self.__covers[(album, albumartist)]
            self._removed = True
        except KeyError:
            pass

    def remove_cover_from_track(self, trackobj):
        al_ar = trackobj.get_album_n_albumartist()
        self.remove_cover(al_ar[0], al_ar[1])

    def get_cover(self, album, albumartist):
        self.__covers.get((album, albumartist))

    def load_db(self, loc=None):
        if not loc:
            loc = self._loc

        try:
            coverdata = shelve.open(loc, protocol=2)
            if len(coverdata) == 0:
                coverdata["__dbversion"] = common.COVERDB_VER
            elif coverdata.get("__dbversion") != common.COVERDB_VER:
                raise common.VersionError
        except Exception:
            return
        # convert key in coverdata from string to tuple
        data_keys = [literal_eval(key.decode('utf-8'))
                     for key in coverdata.iterkeys() if key != "__dbversion"]
        diff = set(data_keys) - set(self.__covers)
        for key in diff:
            self.__covers[key] = coverdata[unicode(key).encode('utf-8')]

        coverdata.close()
        print "coverdb load", gc.collect()

    def save_db(self, loc=None):
        if not loc:
            loc = self._loc
        try:
            coverdata = shelve.open(loc, protocol=2)  # highest protocol
            coverdata["__dbversion"] = common.COVERDB_VER
        except Exception:
            return
        data_keys = [literal_eval(key.decode('utf-8'))
                     for key in coverdata.iterkeys() if key != "__dbversion"]

        if self._added or len(self.__covers) > len(data_keys):
            diff_added = set(self.__covers) - set(data_keys)
            diff_added.update(self._unsaved_updated_covers)
            for key in diff_added:
                coverdata[unicode(key).encode('utf-8')] = self.__covers[key]
            self._unsaved_updated_albums = []
            self._added = False

        # if self._removed:
        diff_removed = set(data_keys) - set(self.__covers)
        for key in diff_removed:
            del coverdata[str(key).encode('utf-8')]
        self._removed = False

        coverdata.sync()
        coverdata.close()
        print "coverdb save", gc.collect()

# end class CoverDB
