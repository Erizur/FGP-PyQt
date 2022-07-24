# This Python file uses the following encoding: utf-8
import json
import random
import sys

import mutagen
import argparse
import darkdetect
import miniaudio
from PySide6.QtCore import QUrl, QSettings, QFileInfo, QSize
from PySide6.QtGui import QImage, QPixmap, QIcon
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog, QStyleFactory
from mutagen import MutagenError
from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC
from pypresence import Presence

from ui_musicplayer import Ui_MusicPlayer
from ui_settings import Ui_Dialog


class MusicPlayer(QMainWindow):

    def __init__(self):
        super(MusicPlayer, self).__init__()
        self.mPlayer = QMediaPlayer(None)
        self.outputDevice = QAudioOutput(None)
        self.filePath = ""
        self.fileExt = QFileInfo()
        self.songList = []
        self.songIndex = 0
        self.previousVol = 0
        self.rpcMetadata = ""
        self.isPlaylist = False
        self.settingsMenu = SettingsMenu()
        self.ui = Ui_MusicPlayer()
        self.ui.setupUi(self)
        self.checkWhiteButtons()
        self.connectUiSetup()
        self.checkIfArgFile()

    def connectUiSetup(self):
        aOpenSong = self.ui.actionOpen_Song
        aOpenSong.triggered.connect(self.openSong_action)
        aOpenPlaylist = self.ui.actionOpen_Playlist
        aOpenPlaylist.triggered.connect(self.openPlaylist_action)
        bPlay = self.ui.playButton
        bPlay.clicked.connect(self.playButton_Action)
        bStop = self.ui.stopButton
        bStop.clicked.connect(self.stopButton_Action)
        bFoward = self.ui.fowardButton
        bFoward.clicked.connect(self.fowardButton_Action)
        bRewind = self.ui.rewindButton
        bRewind.clicked.connect(self.rewindButton_Action)
        bVolume = self.ui.playButton_2
        bVolume.clicked.connect(self.volumeButton_Action)
        vSlider = self.ui.horizontalSlider
        vSlider.sliderReleased.connect(self.changeVolume)
        vSlider.valueChanged.connect(self.changeVolume)
        vSlider.sliderMoved.connect(self.changeVolume)
        try:
            vSlider.setValue(appSettings.value("Volume"))
        except TypeError:
            vSlider.setValue(100)
            appSettings.setValue("Volume", 100)
        self.ui.actionShuffle.setChecked(bool(appSettings.value("ShuffleOn")))
        self.ui.actionLoop.setChecked(bool(appSettings.value("LoopOn")))
        sSlider = self.ui.songTrackbar
        sSlider.sliderReleased.connect(self.setSliderPos)
        sSlider.sliderMoved.connect(self.onSliderMove)
        sSlider.sliderPressed.connect(self.onSliderPress)
        self.ui.actionLoop.checkableChanged.connect(self.saveLoopValue)
        self.ui.actionShuffle.checkableChanged.connect(self.saveShuffleValue)
        self.ui.actionSettings.triggered.connect(self.openSettings_Action)
        if darkdetect.isDark():
            appSettings.setValue("useWhiteButtons", "true")
            self.checkWhiteButtons()
        else:
            appSettings.setValue("useWhiteButtons", "false")
            self.checkWhiteButtons()
        self.settingsMenu.ui.themeComboBox.currentIndexChanged.connect(self.checkWhiteButtons)

    def checkWhiteButtons(self):
        # also define sizes
        useWhiteButtons = str(appSettings.value("useWhiteButtons"))
        if useWhiteButtons == "true":
            playicon = QIcon(":/images/buttonPlayDark.png")
            pause = QIcon(":/images/buttonPauseDark.png")
            stop = QIcon(":/images/buttonStopDark.png")
            fowIcon = QIcon(":/images/buttonFowardDark.png")
            rewIcon = QIcon(":/images/buttonRewindDark.png")
            volIcon = QIcon(":/images/volumeDownlDark.png")
            volUpIcon = QIcon(":/images/volumeLevelDark.png")
        else:
            playicon = QIcon(":/images/buttonPlayLight.png")
            pause = QIcon(":/images/buttonPauseLight.png")
            stop = QIcon(":/images/buttonStopLight.png")
            fowIcon = QIcon(":/images/buttonFowardLight.png")
            rewIcon = QIcon(":/images/buttonRewindLight.png")
            volIcon = QIcon(":/images/volumeDownLight.png")
            volUpIcon = QIcon(":/images/volumeLevelLight.png")

        self.ui.stopButton.setIcon(stop)
        self.ui.fowardButton.setIcon(fowIcon)
        self.ui.rewindButton.setIcon(rewIcon)
        if self.ui.horizontalSlider.value() == 0:
            self.ui.playButton_2.setIcon(volIcon)
        else:
            self.ui.playButton_2.setIcon(volUpIcon)
        if self.mPlayer.playbackState() == self.mPlayer.StoppedState or self.mPlayer.playbackState() == self.mPlayer.PausedState:
            self.ui.playButton.setIcon(playicon)
        else:
            self.ui.playButton.setIcon(pause)
        self.ui.playButton.setMinimumSize(QSize(45, 25))
        self.ui.playButton.setMaximumSize(QSize(45, 25))
        self.ui.playButton.setBaseSize(QSize(45, 25))
        self.ui.stopButton.setMinimumSize(QSize(45, 25))
        self.ui.stopButton.setMaximumSize(QSize(45, 25))
        self.ui.stopButton.setBaseSize(QSize(45, 25))
        self.ui.rewindButton.setMinimumSize(QSize(45, 25))
        self.ui.rewindButton.setMaximumSize(QSize(45, 25))
        self.ui.rewindButton.setBaseSize(QSize(45, 25))
        self.ui.fowardButton.setMinimumSize(QSize(45, 25))
        self.ui.fowardButton.setMaximumSize(QSize(45, 25))
        self.ui.fowardButton.setBaseSize(QSize(45, 25))
        self.ui.playButton_2.setMinimumSize(QSize(25, 25))
        self.ui.playButton_2.setMaximumSize(QSize(25, 25))
        self.ui.playButton_2.setBaseSize(QSize(25, 25))

    def getSongMetadata(self):
        try:
            if self.fileExt == "flac":
                audio = FLAC(self.filePath)
                songInfo = []

                def getArtist():
                    try:
                        if audio["artist"] in audio.values():
                            artist = "".join(audio["artist"])
                            return artist
                        elif not audio["artist"] in audio.values():
                            noArtist = "Unknown Artist"
                            return noArtist
                    except KeyError:
                        noArtist = "Unknown Artist"
                        return noArtist

                def getTitle():
                    try:
                        if audio["title"] in audio.values():
                            title = "".join(audio["title"])
                            return title
                        elif not audio["title"] in audio.values():
                            noTitle = "Unknown Song"
                            return noTitle
                    except KeyError:
                        noTitle = "Unknown Song"
                        return noTitle

                def getCover():
                    try:
                        pic = audio.pictures[0].data
                        if pic is None:
                            return None
                        else:
                            return pic
                    except IndexError:
                        noCover = QImage(":/images/noCover.png")
                        return noCover

                songInfo.append(getArtist())
                songInfo.append(getTitle())
                self.rpcMetadata = ' - '.join([str(i) for i in songInfo])
                songMetadata = ' - '.join([str(i) for i in songInfo])
                coverThing = getCover()
                if coverThing is not QImage:
                    try:
                        coverPic = QImage.fromData(coverThing)
                        self.ui.coverImage.setPixmap(QPixmap.fromImage(coverPic))
                    except TypeError:
                        self.ui.coverImage.setPixmap(QPixmap.fromImage(coverThing))

                else:
                    self.ui.coverImage.setPixmap(QPixmap.fromImage(coverThing))

                self.ui.label.setText(songMetadata)
            elif self.fileExt == "mp3":
                audio = EasyID3(self.filePath)
                audioID = mutagen.File(self.filePath)
                songInfo = []

                def getArtist():
                    try:
                        if audio["artist"] in audio.values():
                            artist = "".join(audio["artist"])
                            return artist
                        elif not audio["artist"] in audio.values():
                            noArtist = "Unknown Artist"
                            return noArtist
                    except KeyError:
                        noArtist = "Unknown Artist"
                        return noArtist

                def getTitle():
                    try:
                        if audio["title"] in audio.values():
                            title = "".join(audio["title"])
                            return title
                        elif not audio["title"] in audio.values():
                            noTitle = "Unknown Song"
                            return noTitle
                    except KeyError:
                        noTitle = "Unknown Song"
                        return noTitle

                def getCover():
                    try:
                        pixmap = QPixmap()
                        for tag in audioID.tags.values():
                            if tag.FrameID == "APIC":
                                pixmap.loadFromData(tag.data)
                                break
                        return pixmap
                    except IndexError:
                        noCover = QPixmap(":/images/noCover.png")
                        return noCover

                songInfo.append(getArtist())
                songInfo.append(getTitle())
                self.rpcMetadata = ' - '.join([str(i) for i in songInfo])
                songMetadata = ' - '.join([str(i) for i in songInfo])
                coverThing = getCover()
                if coverThing is not QPixmap:
                    try:
                        self.ui.coverImage.setPixmap(QPixmap(coverThing))
                    except TypeError:
                        self.ui.coverImage.setPixmap(QPixmap(coverThing))

                else:
                    self.ui.coverImage.setPixmap(QPixmap(coverThing))

                self.ui.label.setText(songMetadata)
        except MutagenError:
            print("Loading failed :(")
            print(MutagenError)
        except KeyError:
            print("Loading failed :(")

    def saveShuffleValue(self):
        appSettings.setValue("ShuffleOn", self.ui.actionShuffle.isChecked)

    def saveLoopValue(self):
        appSettings.setValue("LoopOn", self.ui.actionLoop.isChecked)

    def checkIfArgFile(self):
        if song_args != "" or song_args is not None:
            fileName = QFileInfo(str(song_args))
            if fileName.exists():
                self.filePath = fileName.absoluteFilePath()
                self.outputDevice.setVolume(float(self.ui.horizontalSlider.value()) / 100)
                self.mPlayer.setAudioOutput(self.outputDevice)
                self.mPlayer.setSource(QUrl.fromLocalFile(self.filePath))
                self.fileExt = QFileInfo(self.filePath).completeSuffix()
                self.mPlayer.play()

    def updateUiText(self):
        if self.mPlayer.playbackState() == self.mPlayer.StoppedState or self.mPlayer.playbackState() == self.mPlayer.PausedState:
            useWhiteButtons = str(appSettings.value("useWhiteButtons"))
            if useWhiteButtons == "true":
                playicon = QIcon(":/images/buttonPlayDark.png")
            else:
                playicon = QIcon(":/images/buttonPlayLight.png")
            self.ui.playButton.setIcon(playicon)
            RPC.update(state="Currently Idle", details=f"{self.rpcMetadata}",
                       large_image="fgplogo", large_text="v1.0 - Qt Rewrite")
        elif self.mPlayer.playbackState() == self.mPlayer.PlayingState:
            useWhiteButtons = str(appSettings.value("useWhiteButtons"))
            if useWhiteButtons == "true":
                pause = QIcon(":/images/buttonPauseDark.png")
            else:
                pause = QIcon(":/images/buttonPauseLight.png")
            self.ui.playButton.setIcon(pause)
            RPC.update(state="Currently Playing", details=f"{self.rpcMetadata}",
                       large_image="fgplogo", large_text="v1.0 - Qt Rewrite")

    def openSong_action(self):
        fileName = QFileDialog.getOpenFileName(self, "Open Song", "", "Audio Files (*.mp3 *.wav *.flac)")
        if fileName:
            self.filePath = fileName[0]
            self.outputDevice.setVolume(float(self.ui.horizontalSlider.value()) / 100)
            self.mPlayer.setAudioOutput(self.outputDevice)
            self.mPlayer.setSource(QUrl.fromLocalFile(self.filePath))
            self.fileExt = QFileInfo(self.filePath).completeSuffix()

    def openPlaylist_action(self):
        if self.isPlaylist is True:
            self.songList.clear()
            self.ui.playlistView.clear()
            self.mPlayer.stop()
        fileName = QFileDialog.getOpenFileName(self, "Open Playlist", "", "Playlist Files (*.json)")
        if fileName is not None:
            playlistPath = fileName[0]
            with open(playlistPath) as data_file:
                playlist = data_file.read()
                data = json.loads(playlist)
                for song in data:
                    song_element = song["Song"].encode("cp1252").decode("utf-8")
                    self.songList.append(song_element)
                    print(self.songList)
                    songPath = str(song_element)
                    songInfoElement = QFileInfo(songPath).fileName()
                    self.ui.playlistView.addItem(songInfoElement)

                self.songIndex = 0
                self.ui.playlistView.setCurrentRow(self.songIndex)
                self.outputDevice.setVolume(float(self.ui.horizontalSlider.value()) / 100)
                self.mPlayer.setAudioOutput(self.outputDevice)
                self.mPlayer.setSource(QUrl.fromLocalFile(self.songList[self.songIndex]))
                self.filePath = self.songList[self.songIndex]
                self.fileExt = QFileInfo(self.filePath).completeSuffix()
                self.isPlaylist = True
            data_file.close()

    def playButton_Action(self):
        if self.mPlayer.mediaStatus() != self.mPlayer.NoMedia:
            if self.mPlayer.playbackState() == self.mPlayer.StoppedState or self.mPlayer.playbackState() == self.mPlayer.PausedState:
                self.mPlayer.play()
                useWhiteButtons = str(appSettings.value("useWhiteButtons"))
                if useWhiteButtons == "true":
                    pause = QIcon(":/images/buttonPauseDark.png")
                else:
                    pause = QIcon(":/images/buttonPauseLight.png")
                self.ui.playButton.setIcon(pause)
            elif self.mPlayer.playbackState() == self.mPlayer.PlayingState:
                self.mPlayer.pause()
                useWhiteButtons = str(appSettings.value("useWhiteButtons"))
                if useWhiteButtons == "true":
                    playicon = QIcon(":/images/buttonPlayDark.png")
                else:
                    playicon = QIcon(":/images/buttonPlayLight.png")
                self.ui.playButton.setIcon(playicon)

    def nextSong_Action(self):
        try:
            if self.isPlaylist is True and self.mPlayer.mediaStatus() == self.mPlayer.EndOfMedia:
                indexMax = len(self.songList)

                if self.songIndex < indexMax - 1:
                    self.mPlayer.stop()
                    if self.ui.actionShuffle.isChecked():
                        self.songIndex = random.randrange(0, indexMax - 1)
                    else:
                        self.songIndex = self.songIndex + 1
                    self.ui.playlistView.setCurrentRow(self.songIndex)
                    self.mPlayer.setAudioOutput(self.outputDevice)
                    self.outputDevice.setVolume(float(self.ui.horizontalSlider.value()) / 100)
                    self.filePath = self.songList[self.songIndex]
                    self.mPlayer.setSource(QUrl.fromLocalFile(self.filePath))
                    self.fileExt = QFileInfo(self.filePath).completeSuffix()
                    self.mPlayer.play()
                elif self.ui.actionLoop.isChecked():
                    if self.songIndex >= indexMax - 1:
                        self.songIndex = 0
                        self.ui.playlistView.setCurrentRow(self.songIndex)
                        self.mPlayer.setAudioOutput(self.outputDevice)
                        self.outputDevice.setVolume(float(self.ui.horizontalSlider.value()) / 100)
                        self.filePath = self.songList[self.songIndex]
                        self.mPlayer.setSource(QUrl.fromLocalFile(self.filePath))
                        self.fileExt = QFileInfo(self.filePath).completeSuffix()
                        self.mPlayer.play()
                else:
                    self.mPlayer.stop()
            if self.mPlayer.mediaStatus() == self.mPlayer.EndOfMedia and self.ui.actionLoop.isChecked() and self.isPlaylist is False:
                self.mPlayer.setAudioOutput(self.outputDevice)
                self.outputDevice.setVolume(float(self.ui.horizontalSlider.value()) / 100)
                self.filePath = self.mPlayer.source()
                self.mPlayer.setSource(QUrl.fromLocalFile(self.filePath))
                self.fileExt = QFileInfo(self.filePath).completeSuffix()
                self.mPlayer.play()

        except IndexError:
            return

    def fowardButton_Action(self):
        try:
            if self.isPlaylist is True:
                indexMax = len(self.songList)

                if self.songIndex < indexMax - 1:
                    self.mPlayer.stop()
                    if self.ui.actionShuffle.isChecked():
                        self.songIndex = random.randrange(0, indexMax)
                        self.filePath = self.songList[self.songIndex]
                    else:
                        self.songIndex = self.songIndex + 1
                        self.filePath = self.songList[self.songIndex]

                    self.ui.playlistView.setCurrentRow(self.songIndex)
                    self.mPlayer.setAudioOutput(self.outputDevice)
                    self.outputDevice.setVolume(float(self.ui.horizontalSlider.value()) / 100)
                    self.mPlayer.setSource(QUrl.fromLocalFile(self.filePath))
                    self.fileExt = QFileInfo(self.filePath).completeSuffix()
                    self.mPlayer.play()
                elif self.songIndex >= indexMax - 1 and self.ui.actionLoop.isChecked():
                    self.songIndex = 0
                    self.ui.playlistView.setCurrentRow(self.songIndex)
                    self.mPlayer.setAudioOutput(self.outputDevice)
                    self.outputDevice.setVolume(float(self.ui.horizontalSlider.value()) / 100)
                    self.filePath = self.songList[self.songIndex]
                    self.mPlayer.setSource(QUrl.fromLocalFile(self.filePath))
                    self.fileExt = QFileInfo(self.filePath).completeSuffix()
                    self.mPlayer.play()
                else:
                    self.mPlayer.stop()
        except IndexError:
            self.mPlayer.stop()

    def rewindButton_Action(self):
        if self.isPlaylist is True:

            if self.songIndex > 0:
                self.mPlayer.stop()
                self.songIndex -= 1
                self.ui.playlistView.setCurrentRow(self.songIndex)
                self.outputDevice.setVolume(float(self.ui.horizontalSlider.value()) / 100)
                self.mPlayer.setSource(QUrl.fromLocalFile(self.songList[self.songIndex]))
                print(self.mPlayer.source())
                self.filePath = self.songList[self.songIndex]
                self.fileExt = QFileInfo(self.filePath).completeSuffix()
                self.mPlayer.play()
            else:
                return

    def volumeButton_Action(self):
        if self.ui.horizontalSlider.value() == 0:
            useWhiteButtons = str(appSettings.value("useWhiteButtons"))
            if useWhiteButtons == "true":
                volIcon = QIcon(":/images/volumeLevelDark.png")
            else:
                volIcon = QIcon(":/images/volumeLevelLight.png")
            self.ui.playButton_2.setIcon(volIcon)
            self.ui.horizontalSlider.setValue(self.previousVol)
            self.outputDevice.setVolume(float(self.ui.horizontalSlider.value()) / 100)
            appSettings.setValue("Volume", self.ui.horizontalSlider.value())
        else:
            self.previousVol = self.ui.horizontalSlider.value()
            self.ui.horizontalSlider.setValue(0)
            useWhiteButtons = str(appSettings.value("useWhiteButtons"))
            if useWhiteButtons == "true":
                volIcon = QIcon(":/images/volumeDownlDark.png")
            else:
                volIcon = QIcon(":/images/volumeDownLight.png")
            self.ui.playButton_2.setIcon(volIcon)
            self.outputDevice.setVolume(float(self.ui.horizontalSlider.value()) / 100)
            appSettings.setValue("Volume", self.ui.horizontalSlider.value())

    def stopButton_Action(self):
        self.mPlayer.stop()

    def updateMaxSlider(self):
        self.ui.songTrackbar.setMaximum(self.mPlayer.duration())

    def updateSlider(self):
        self.ui.songTrackbar.setValue(self.mPlayer.position())

    def onSliderPress(self):
        self.mPlayer.pause()
        self.outputDevice.setVolume(0)

    def onSliderMove(self):
        self.mPlayer.setPosition(self.ui.songTrackbar.value())

    def setSliderPos(self):
        self.mPlayer.play()
        self.outputDevice.setVolume(float(self.ui.horizontalSlider.value()) / 100)

    def openSettings_Action(self):
        self.settingsMenu.show()

    def changeVolume(self):
        if self.ui.horizontalSlider.value() == 0:
            useWhiteButtons = str(appSettings.value("useWhiteButtons"))
            if useWhiteButtons == "true":
                volIcon = QIcon(":/images/volumeDownlDark.png")
            else:
                volIcon = QIcon(":/images/volumeDownLight.png")
            self.ui.playButton_2.setIcon(volIcon)
            self.outputDevice.setVolume(float(self.ui.horizontalSlider.value()) / 100)
            appSettings.setValue("Volume", self.ui.horizontalSlider.value())
        else:
            useWhiteButtons = str(appSettings.value("useWhiteButtons"))
            if useWhiteButtons == "true":
                volIcon = QIcon(":/images/volumeLevelDark.png")
            else:
                volIcon = QIcon(":/images/volumeLevelLight.png")
            self.ui.playButton_2.setIcon(volIcon)
            self.previousVol = self.ui.horizontalSlider.value()
            self.outputDevice.setVolume(float(self.ui.horizontalSlider.value()) / 100)
            appSettings.setValue("Volume", self.ui.horizontalSlider.value())


class SettingsMenu(QDialog):
    def __init__(self):
        super(SettingsMenu, self).__init__()
        self.themesFolder = "themes/"
        self.themesJson = "themes/themes.json"
        self.themes = None
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.readThemes()
        self.setPreviousTheme()
        self.connectUi()

    def setPreviousTheme(self):
        # print(self.ui.themeComboBox.currentIndex())
        # print(appSettings.value("curStyle"))
        self.ui.themeComboBox.setCurrentIndex(appSettings.value("curIndexStyle"))
        curIndex = int(self.ui.themeComboBox.currentIndex())
        selectedThemePath = app.applicationDirPath().replace("\\", "/") + "/themes" + self.themes["themes"][int(curIndex)]["file_location"]
        appSettings.setValue("curStyle", selectedThemePath)
        appSettings.sync()

    def connectUi(self):
        self.ui.themeComboBox.currentIndexChanged.connect(self.defineNewTheme)

    def defineNewTheme(self):
        try:
            # print(self.ui.themeComboBox.currentIndex())
            # print(appSettings.value("curStyle"))
            curIndex = int(self.ui.themeComboBox.currentIndex())
            selectedThemePath = app.applicationDirPath().replace("\\", "/") + "/themes" + self.themes["themes"][int(curIndex)]["file_location"]
            useWhiteButtons = self.themes["themes"][int(curIndex)]["useWhiteButtons"]
            decorStyle = self.themes["themes"][int(curIndex)]["decorationStyle"]
            appSettings.setValue("curStyle", selectedThemePath)
            appSettings.setValue("curIndexStyle", self.ui.themeComboBox.currentIndex())
            appSettings.setValue("useWhiteButtons", useWhiteButtons)
            appSettings.setValue("decorationStyle", decorStyle)
            appSettings.sync()
            print(str(appSettings.value("useWhiteButtons")))
            app.setStyle(QStyleFactory.create(decorStyle))
            with open(selectedThemePath) as theme_data:
                style_sheet = theme_data.read()
                app.setStyleSheet(style_sheet)
        except FileNotFoundError:

            return None

    def readThemes(self):
        with open(self.themesJson) as json_file:
            self.themes = json.load(json_file)
            for i in self.themes['themes']:
                self.ui.themeComboBox.addItem(i["theme_name"])


if __name__ == "__main__":
    appSettings = QSettings("AM_Erizur", "FrutaGroove Player")
    app = QApplication([])
    try:
        style_loc = appSettings.value("curStyle")
        decorationStyle = appSettings.value("decorationStyle")
        app.setStyle(QStyleFactory.create(decorationStyle))
        with open(style_loc) as file:
            styleSheet = file.read()
            app.setStyleSheet(styleSheet)
    except FileNotFoundError:
        app.setStyleSheet(None)
    except TypeError:
        app.setStyleSheet(None)
        appSettings.setValue("curStyle", "")
        appSettings.setValue("curIndexStyle", 0)
        appSettings.setValue("decorationStyle", "")
    parser = argparse.ArgumentParser(description='Simple Music Player.')
    parser.add_argument("song_path", metavar='song_path', type=str, nargs='?',
                        help="Runs the music player with a specified file.", default="")
    args = parser.parse_args()
    song_args = args.song_path
    print(song_args)
    widget = MusicPlayer()
    widget.show()
    client_id = "901120248227442728"  # Enter your Application ID here.
    RPC = Presence(client_id=client_id)
    RPC.connect()
    sys.exit(app.exec())
