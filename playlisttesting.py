import json
import os
from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC


class StuffThing:
    songList = []

    fileName = input("Attach JSON File here: ")
    if fileName is not None:
        with open(fileName) as data_file:
            playlist = data_file.read()
            data = json.loads(playlist)
            for song in data:
                song_element = song["Song"].encode("cp1252")
                songList.append(song_element)
                print(songList)
                songPath = str(song_element)
                # songInfoElement = QFileInfo(songPath).fileName() intended to be used with qt to get the file info for playlist box
                # self.ui.playlistView.addItem(songInfoElement) intended to be used with qt to add a playlist box

            # the following code here gets the file extension for the specific file and use a different mutagen system, i'm just adding the loading file thingie because it automatically gives an error.
            # the first element of songList has the thing
            ext = os.path.splitext(songList[0])[1]
            if ext == ".flac":
                audioFile = FLAC(songList[0])  # will probably give the error
            else:
                audioFile = EasyID3(songList[0]) # if is MP3, also will give the error
        data_file.close()


if __name__ == "__main__":
    StuffThing()
