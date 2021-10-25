# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSlider,
    QStatusBar, QWidget)

class Ui_MusicPlayer(object):
    def setupUi(self, MusicPlayer):
        if not MusicPlayer.objectName():
            MusicPlayer.setObjectName(u"MusicPlayer")
        MusicPlayer.resize(350, 350)
        MusicPlayer.setMinimumSize(QSize(350, 350))
        MusicPlayer.setMaximumSize(QSize(350, 350))
        MusicPlayer.setBaseSize(QSize(350, 350))
        icon = QIcon()
        iconThemeName = u"MainTheme"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u":/images/fgpNewLogo.png", QSize(), QIcon.Normal, QIcon.Off)
        
        MusicPlayer.setWindowIcon(icon)
        self.actionOpen_Song = QAction(MusicPlayer)
        self.actionOpen_Song.setObjectName(u"actionOpen_Song")
        self.actionOpen_Playlist = QAction(MusicPlayer)
        self.actionOpen_Playlist.setObjectName(u"actionOpen_Playlist")
        self.actionSettings = QAction(MusicPlayer)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionShuffle = QAction(MusicPlayer)
        self.actionShuffle.setObjectName(u"actionShuffle")
        self.actionShuffle.setCheckable(True)
        self.actionShuffle.setChecked(False)
        self.actionLoop = QAction(MusicPlayer)
        self.actionLoop.setObjectName(u"actionLoop")
        self.actionLoop.setCheckable(True)
        self.actionLoop.setChecked(False)
        self.actionPlaylists_Editor = QAction(MusicPlayer)
        self.actionPlaylists_Editor.setObjectName(u"actionPlaylists_Editor")
        self.actionReport_an_Issue = QAction(MusicPlayer)
        self.actionReport_an_Issue.setObjectName(u"actionReport_an_Issue")
        self.actionGitHub = QAction(MusicPlayer)
        self.actionGitHub.setObjectName(u"actionGitHub")
        self.actionAbout_FGP = QAction(MusicPlayer)
        self.actionAbout_FGP.setObjectName(u"actionAbout_FGP")
        self.actionCheck_for_Updates = QAction(MusicPlayer)
        self.actionCheck_for_Updates.setObjectName(u"actionCheck_for_Updates")
        self.centralwidget = QWidget(MusicPlayer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(11, 11, 334, 291))
        self.gridLayout_3 = QGridLayout(self.layoutWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.infoLayout = QGridLayout()
        self.infoLayout.setObjectName(u"infoLayout")
        self.coverImage = QLabel(self.layoutWidget)
        self.coverImage.setObjectName(u"coverImage")
        self.coverImage.setMinimumSize(QSize(200, 200))
        self.coverImage.setMaximumSize(QSize(200, 200))
        self.coverImage.setBaseSize(QSize(200, 200))
        self.coverImage.setFrameShape(QFrame.NoFrame)
        self.coverImage.setPixmap(QPixmap(u":/images/noCover.png"))
        self.coverImage.setScaledContents(True)
        self.coverImage.setAlignment(Qt.AlignCenter)

        self.infoLayout.addWidget(self.coverImage, 0, 0, 1, 1)

        self.playlistView = QListWidget(self.layoutWidget)
        self.playlistView.setObjectName(u"playlistView")
        self.playlistView.setMinimumSize(QSize(120, 200))
        self.playlistView.setMaximumSize(QSize(120, 200))
        self.playlistView.setBaseSize(QSize(120, 200))

        self.infoLayout.addWidget(self.playlistView, 0, 1, 1, 1)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(330, 20))
        self.label.setMaximumSize(QSize(330, 20))
        self.label.setBaseSize(QSize(330, 20))
        self.label.setAlignment(Qt.AlignCenter)

        self.infoLayout.addWidget(self.label, 1, 0, 1, 2)


        self.gridLayout_3.addLayout(self.infoLayout, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.songTrackbar = QSlider(self.layoutWidget)
        self.songTrackbar.setObjectName(u"songTrackbar")
        self.songTrackbar.setMinimumSize(QSize(330, 20))
        self.songTrackbar.setMaximumSize(QSize(330, 20))
        self.songTrackbar.setBaseSize(QSize(330, 20))
        self.songTrackbar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.songTrackbar, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.rewindButton = QPushButton(self.layoutWidget)
        self.rewindButton.setObjectName(u"rewindButton")
        self.rewindButton.setMinimumSize(QSize(45, 25))
        self.rewindButton.setMaximumSize(QSize(45, 25))
        self.rewindButton.setBaseSize(QSize(55, 25))
        self.rewindButton.setAutoFillBackground(False)
        icon1 = QIcon()
        icon1.addFile(u":/images/buttonRewindLight.png", QSize(), QIcon.Normal, QIcon.Off)
        self.rewindButton.setIcon(icon1)
        self.rewindButton.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.rewindButton, 0, 0, 1, 1)

        self.playButton = QPushButton(self.layoutWidget)
        self.playButton.setObjectName(u"playButton")
        self.playButton.setMinimumSize(QSize(45, 25))
        self.playButton.setMaximumSize(QSize(45, 25))
        self.playButton.setBaseSize(QSize(55, 25))
        icon2 = QIcon()
        icon2.addFile(u":/images/buttonPlayLight.png", QSize(), QIcon.Normal, QIcon.Off)
        self.playButton.setIcon(icon2)
        self.playButton.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.playButton, 0, 1, 1, 1)

        self.stopButton = QPushButton(self.layoutWidget)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setMinimumSize(QSize(45, 25))
        self.stopButton.setMaximumSize(QSize(45, 25))
        self.stopButton.setBaseSize(QSize(55, 25))
        icon3 = QIcon()
        icon3.addFile(u":/images/buttonStopLight.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stopButton.setIcon(icon3)
        self.stopButton.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.stopButton, 0, 2, 1, 1)

        self.fowardButton = QPushButton(self.layoutWidget)
        self.fowardButton.setObjectName(u"fowardButton")
        self.fowardButton.setMinimumSize(QSize(45, 25))
        self.fowardButton.setMaximumSize(QSize(45, 25))
        self.fowardButton.setBaseSize(QSize(55, 25))
        icon4 = QIcon()
        icon4.addFile(u":/images/buttonFowardLight.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fowardButton.setIcon(icon4)
        self.fowardButton.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.fowardButton, 0, 3, 1, 1)

        self.playButton_2 = QPushButton(self.layoutWidget)
        self.playButton_2.setObjectName(u"playButton_2")
        self.playButton_2.setMinimumSize(QSize(25, 25))
        self.playButton_2.setMaximumSize(QSize(25, 25))
        self.playButton_2.setBaseSize(QSize(55, 25))
        icon5 = QIcon()
        icon5.addFile(u":/images/volumeLevelLight.png", QSize(), QIcon.Normal, QIcon.Off)
        self.playButton_2.setIcon(icon5)
        self.playButton_2.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.playButton_2, 0, 4, 1, 1)

        self.horizontalSlider = QSlider(self.layoutWidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMinimumSize(QSize(80, 20))
        self.horizontalSlider.setMaximumSize(QSize(80, 20))
        self.horizontalSlider.setBaseSize(QSize(80, 20))
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setValue(100)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.horizontalSlider, 0, 5, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        MusicPlayer.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MusicPlayer)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 350, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuPlaylist = QMenu(self.menubar)
        self.menuPlaylist.setObjectName(u"menuPlaylist")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MusicPlayer.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MusicPlayer)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setSizeGripEnabled(False)
        MusicPlayer.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuPlaylist.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOpen_Song)
        self.menuFile.addAction(self.actionOpen_Playlist)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuPlaylist.addAction(self.actionShuffle)
        self.menuPlaylist.addAction(self.actionLoop)
        self.menuPlaylist.addSeparator()
        self.menuPlaylist.addAction(self.actionPlaylists_Editor)
        self.menuHelp.addAction(self.actionReport_an_Issue)
        self.menuHelp.addAction(self.actionGitHub)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout_FGP)
        self.menuHelp.addAction(self.actionCheck_for_Updates)

        self.retranslateUi(MusicPlayer)

        QMetaObject.connectSlotsByName(MusicPlayer)
    # setupUi

    def retranslateUi(self, MusicPlayer):
        MusicPlayer.setWindowTitle(QCoreApplication.translate("MusicPlayer", u"FrutaGroove Player", None))
        self.actionOpen_Song.setText(QCoreApplication.translate("MusicPlayer", u"Open Song", None))
        self.actionOpen_Playlist.setText(QCoreApplication.translate("MusicPlayer", u"Open Playlist", None))
        self.actionSettings.setText(QCoreApplication.translate("MusicPlayer", u"Settings", None))
        self.actionShuffle.setText(QCoreApplication.translate("MusicPlayer", u"Shuffle", None))
        self.actionLoop.setText(QCoreApplication.translate("MusicPlayer", u"Loop", None))
        self.actionPlaylists_Editor.setText(QCoreApplication.translate("MusicPlayer", u"Playlists Editor", None))
        self.actionReport_an_Issue.setText(QCoreApplication.translate("MusicPlayer", u"Report an Issue", None))
        self.actionGitHub.setText(QCoreApplication.translate("MusicPlayer", u"GitHub Page", None))
        self.actionAbout_FGP.setText(QCoreApplication.translate("MusicPlayer", u"About FGP", None))
        self.actionCheck_for_Updates.setText(QCoreApplication.translate("MusicPlayer", u"Check for Updates", None))
        self.coverImage.setText("")
        self.label.setText(QCoreApplication.translate("MusicPlayer", u"No Song Information", None))
        self.rewindButton.setText("")
        self.playButton.setText("")
        self.stopButton.setText("")
        self.fowardButton.setText("")
        self.playButton_2.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MusicPlayer", u"File", None))
        self.menuPlaylist.setTitle(QCoreApplication.translate("MusicPlayer", u"Playlist", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MusicPlayer", u"Help", None))
    # retranslateUi

