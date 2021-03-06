# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Cloud\Dropbox\Programming\Code\py\Miusik\src\ui\mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from src.widgets import playlistview

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class VolumeButton(QtGui.QToolButton):
    mouse_enter = QtCore.pyqtSignal()

    def __init__(self, parent):
        super(self.__class__, self).__init__(parent)
        self.clicked.connect(self.stop_show_slider)

    def enterEvent(self, event):
        self.hide_slider = QtCore.QTimer()
        self.hide_slider.setSingleShot(True)
        self.hide_slider.timeout.connect(self.parent().parent().volume_slider.hide)
        self.show_slider = QtCore.QTimer()
        self.show_slider.timeout.connect(self.showing_slider)
        self.show_slider.setSingleShot(True)
        self.show_slider.start(500)

    def leaveEvent(self, event):
        self.hide_slider.start(1500)

    def stop_show_slider(self):
        self.show_slider.stop()

    @QtCore.pyqtSlot()
    def showing_slider(self):
        vol_btn_pos = self.parent().parent().volume_button.pos()
        self.parent().parent().volume_slider.move(vol_btn_pos.x()+25, vol_btn_pos.y()+1)
        self.parent().parent().volume_slider.show()
        # raise the slider to avoid the layout break mouse enter event
        self.parent().parent().volume_slider.raise_()


class VolumeSilder(QtGui.QFrame):
    """docstring for VolumeSilder"""
    mouse_over = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(VolumeSilder, self).__init__(parent)
        self.setLineWidth(1)
        self.setMidLineWidth(0)
        self.setFrameShape(QtGui.QFrame.Box | QtGui.QFrame.Raised)
        self.slider = QtGui.QSlider()
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.setFixedSize(100, 23)
        self.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        self.setMouseTracking(True)
        hbox = QtGui.QHBoxLayout(self)
        hbox.setMargin(2)
        hbox.setSpacing(0)
        hbox.addWidget(self.slider)
        self.setLayout(hbox)

    def enterEvent(self, event):
        self.parent().parent().volume_button.hide_slider.stop()
        self.parent().parent().volume_button.hide_slider.deleteLater()

    def leaveEvent(self, event):
        QtCore.QTimer.singleShot(200, self.hide)


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName(_fromUtf8("main_window"))
        # main_window.resize(580, 520)
        main_window.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        main_window.setAnimated(True)
        main_window.setTabShape(QtGui.QTabWidget.Triangular)
        self.centralwidget = QtGui.QWidget(main_window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 6, 0, 6)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))

        ###########
        # main menu
        ###########
        self.main_menu = QtGui.QHBoxLayout()
        self.main_menu.setObjectName(_fromUtf8("main_menu"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.main_menu.addItem(spacerItem)
        self.music_menu_button = QtGui.QPushButton(self.centralwidget)
        self.music_menu_button.setEnabled(True)
        self.music_menu_button.setFlat(False)
        self.music_menu_button.setObjectName(_fromUtf8("music_menu_button"))
        self.main_menu.addWidget(self.music_menu_button)
        self.radio_menu_button = QtGui.QPushButton(self.centralwidget)
        self.radio_menu_button.setObjectName(_fromUtf8("radio_menu_button"))
        self.main_menu.addWidget(self.radio_menu_button)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.main_menu.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.main_menu)
        self.lineUnderMainMenu = QtGui.QFrame(self.centralwidget)
        self.lineUnderMainMenu.setFrameShape(QtGui.QFrame.HLine)
        self.lineUnderMainMenu.setFrameShadow(QtGui.QFrame.Sunken)
        self.lineUnderMainMenu.setObjectName(_fromUtf8("lineUnderMainMenu"))
        self.verticalLayout_2.addWidget(self.lineUnderMainMenu)

        #########
        # toolbar
        #########
        self.toolbar = QtGui.QHBoxLayout()
        self.toolbar.setObjectName(_fromUtf8("toolbar"))
        spacerItem2 = QtGui.QSpacerItem(5, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.toolbar.addItem(spacerItem2)
        self.open_folder_button = QtGui.QToolButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/open_folder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_folder_button.setIcon(icon)
        self.open_folder_button.setObjectName(_fromUtf8("open_folder_button"))
        self.toolbar.addWidget(self.open_folder_button)
        self.add_file_button = QtGui.QToolButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/add_file.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_file_button.setIcon(icon1)
        self.add_file_button.setObjectName(_fromUtf8("add_file_button"))
        self.toolbar.addWidget(self.add_file_button)
        self.save_playlist_button = QtGui.QToolButton(self.centralwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_playlist_button.setIcon(icon2)
        self.save_playlist_button.setObjectName(_fromUtf8("save_playlist_button"))
        self.toolbar.addWidget(self.save_playlist_button)
        self.load_playlist_button = QtGui.QToolButton(self.centralwidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/load.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.load_playlist_button.setIcon(icon3)
        self.load_playlist_button.setObjectName(_fromUtf8("load_playlist_button"))
        self.toolbar.addWidget(self.load_playlist_button)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.toolbar.addItem(spacerItem3)
        self.app_setting_button = QtGui.QToolButton(self.centralwidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/setting.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.app_setting_button.setIcon(icon4)
        self.app_setting_button.setObjectName(_fromUtf8("app_setting_button"))
        self.toolbar.addWidget(self.app_setting_button)
        self.app_info_button = QtGui.QToolButton(self.centralwidget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/info.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.app_info_button.setIcon(icon5)
        self.app_info_button.setObjectName(_fromUtf8("app_info_button"))
        self.toolbar.addWidget(self.app_info_button)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.toolbar.addItem(spacerItem4)
        self.search_box = QtGui.QLineEdit(self.centralwidget)
        self.search_box.setMinimumSize(QtCore.QSize(150, 0))
        self.search_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.search_box.setText(_fromUtf8(""))
        self.search_box.setObjectName(_fromUtf8("search_box"))
        self.toolbar.addWidget(self.search_box)
        spacerItem5 = QtGui.QSpacerItem(5, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.toolbar.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.toolbar)


        ###########
        # main area
        ###########
        self.main_area = QtGui.QVBoxLayout()
        self.main_area.setObjectName(_fromUtf8("main_area"))

        # main content
        self.main_content = QtGui.QHBoxLayout()
        self.main_content.setObjectName(_fromUtf8("main_content"))

        # playlist frame
        self.playlists_frame = QtGui.QFrame(self.centralwidget)
        self.playlists_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.playlists_frame.setFrameShadow(QtGui.QFrame.Plain)
        self.playlists_frame.setLineWidth(0)
        self.playlists_frame.setMidLineWidth(0)
        self.playlists_frame.setObjectName(_fromUtf8("playlists_frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.playlists_frame)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.main_content.addWidget(self.playlists_frame)
        self.main_area.addLayout(self.main_content)

        # choose layout buttons
        self.choose_layout_buttons = QtGui.QHBoxLayout()
        self.choose_layout_buttons.setObjectName(_fromUtf8("choose_layout_buttons"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.choose_layout_buttons.addItem(spacerItem6)
        self.playlist_button = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playlist_button.sizePolicy().hasHeightForWidth())
        self.playlist_button.setSizePolicy(sizePolicy)
        self.playlist_button.setMinimumSize(QtCore.QSize(30, 25))
        self.playlist_button.setMaximumSize(QtCore.QSize(30, 25))
        self.playlist_button.setToolTip(_fromUtf8(""))
        self.playlist_button.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/playlist.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playlist_button.setIcon(icon6)
        self.playlist_button.setDefault(True)
        self.playlist_button.setFlat(False)
        self.playlist_button.setObjectName(_fromUtf8("playlist_button"))
        self.choose_layout_buttons.addWidget(self.playlist_button)
        self.lyrics_button = QtGui.QPushButton(self.centralwidget)
        self.lyrics_button.setMinimumSize(QtCore.QSize(30, 25))
        self.lyrics_button.setMaximumSize(QtCore.QSize(30, 25))
        self.lyrics_button.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/lyrics.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lyrics_button.setIcon(icon7)
        self.lyrics_button.setObjectName(_fromUtf8("lyrics_button"))
        self.choose_layout_buttons.addWidget(self.lyrics_button)
        self.artist_info_button = QtGui.QPushButton(self.centralwidget)
        self.artist_info_button.setMinimumSize(QtCore.QSize(30, 25))
        self.artist_info_button.setMaximumSize(QtCore.QSize(30, 25))
        self.artist_info_button.setText(_fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/artistinfo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.artist_info_button.setIcon(icon8)
        self.artist_info_button.setObjectName(_fromUtf8("artist_info_button"))
        self.choose_layout_buttons.addWidget(self.artist_info_button)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.choose_layout_buttons.addItem(spacerItem7)
        self.main_area.addLayout(self.choose_layout_buttons)
        self.verticalLayout_2.addLayout(self.main_area)
        self.lineUnderMainArea = QtGui.QFrame(self.centralwidget)
        self.lineUnderMainArea.setFrameShape(QtGui.QFrame.HLine)
        self.lineUnderMainArea.setFrameShadow(QtGui.QFrame.Sunken)
        self.lineUnderMainArea.setObjectName(_fromUtf8("lineUnderMainArea"))
        self.verticalLayout_2.addWidget(self.lineUnderMainArea)

        ##############
        # control area
        ##############
        self.control_area = QtGui.QHBoxLayout()
        self.control_area.setSpacing(0)
        self.control_area.setObjectName(_fromUtf8("control_area"))
        spacerItem8 = QtGui.QSpacerItem(12, 5, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.control_area.addItem(spacerItem8)
        self.main_control = QtGui.QVBoxLayout()
        self.main_control.setSpacing(0)
        self.main_control.setObjectName(_fromUtf8("main_control"))

        # controler
        self.controler = QtGui.QHBoxLayout()
        self.controler.setObjectName(_fromUtf8("controler"))
        self.controler_buttons = QtGui.QVBoxLayout()
        self.controler_buttons.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.controler_buttons.setSpacing(4)
        self.controler_buttons.setObjectName(_fromUtf8("controler_buttons"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.previous_button = QtGui.QToolButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previous_button.sizePolicy().hasHeightForWidth())
        self.previous_button.setSizePolicy(sizePolicy)
        self.previous_button.setMinimumSize(QtCore.QSize(40, 40))
        self.previous_button.setMaximumSize(QtCore.QSize(40, 40))
        self.previous_button.setText(_fromUtf8(""))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/previous.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previous_button.setIcon(icon9)
        self.previous_button.setObjectName(_fromUtf8("previous_button"))
        self.horizontalLayout_2.addWidget(self.previous_button, QtCore.Qt.AlignVCenter)
        self.play_pause_button = QtGui.QToolButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.play_pause_button.sizePolicy().hasHeightForWidth())
        self.play_pause_button.setSizePolicy(sizePolicy)
        self.play_pause_button.setMinimumSize(QtCore.QSize(50, 50))
        self.play_pause_button.setMaximumSize(QtCore.QSize(50, 50))
        self.play_pause_button.setText(_fromUtf8(""))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/play.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_pause_button.setIcon(icon10)
        self.play_pause_button.setIconSize(QtCore.QSize(32, 32))
        self.play_pause_button.setObjectName(_fromUtf8("play_pause_button"))
        self.horizontalLayout_2.addWidget(self.play_pause_button, QtCore.Qt.AlignVCenter)
        self.next_button = QtGui.QToolButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next_button.sizePolicy().hasHeightForWidth())
        self.next_button.setSizePolicy(sizePolicy)
        self.next_button.setMinimumSize(QtCore.QSize(40, 40))
        self.next_button.setMaximumSize(QtCore.QSize(40, 40))
        self.next_button.setStyleSheet(_fromUtf8(""))
        self.next_button.setText(_fromUtf8(""))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/next.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_button.setIcon(icon11)
        self.next_button.setObjectName(_fromUtf8("next_button"))
        self.horizontalLayout_2.addWidget(self.next_button, QtCore.Qt.AlignVCenter)
        self.controler_buttons.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))

        # shuffle button
        self.shuffle_button = QtGui.QToolButton(self.centralwidget)
        self.shuffle_button.setMinimumSize(QtCore.QSize(24, 24))
        self.shuffle_button.setMaximumSize(QtCore.QSize(24, 24))
        self.shuffle_button.setText(_fromUtf8(""))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/shuffle.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shuffle_button.setIcon(icon12)
        self.shuffle_button.setObjectName(_fromUtf8("shuffle_button"))
        self.horizontalLayout_4.addWidget(self.shuffle_button, QtCore.Qt.AlignVCenter)
        shuffle_button_menu = QtGui.QMenu()
        ag = QtGui.QActionGroup(shuffle_button_menu, exclusive=True)
        for mode in ("Off", "On"):
            act = ag.addAction(QtGui.QAction(mode, shuffle_button_menu, checkable=True))
            shuffle_button_menu.addAction(act)
        self.shuffle_button.setMenu(shuffle_button_menu)
        self.shuffle_button.setPopupMode(2)

        # repeat button
        self.repeat_button = QtGui.QToolButton(self.centralwidget)
        self.repeat_button.setMinimumSize(QtCore.QSize(24, 24))
        self.repeat_button.setMaximumSize(QtCore.QSize(24, 24))
        self.repeat_button.setText(_fromUtf8(""))
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/repeat.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.repeat_button.setIcon(icon13)
        self.repeat_button.setObjectName(_fromUtf8("repeat_button"))
        self.horizontalLayout_4.addWidget(self.repeat_button, QtCore.Qt.AlignVCenter)
        repeat_button_menu = QtGui.QMenu()
        ag = QtGui.QActionGroup(repeat_button_menu, exclusive=True)
        for mode in ("Off", "Song", "Album", "Playlist"):
            act = ag.addAction(QtGui.QAction(mode, repeat_button_menu, checkable=True))
            repeat_button_menu.addAction(act)
        self.repeat_button.setMenu(repeat_button_menu)
        self.repeat_button.setPopupMode(2)

        # volume slider
        self.volume_slider = VolumeSilder(self.centralwidget)
        self.volume_slider.slider.setRange(0, 100)
        self.volume_slider.hide()
        # volume button
        self.volume_button = VolumeButton(self.centralwidget)
        self.volume_button.setMinimumSize(QtCore.QSize(24, 24))
        self.volume_button.setMaximumSize(QtCore.QSize(24, 24))
        self.volume_button.setText(_fromUtf8(""))
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/volume-full.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.volume_button.setIcon(icon14)
        self.volume_button.setObjectName(_fromUtf8("volume_button"))
        self.horizontalLayout_4.addWidget(self.volume_button, QtCore.Qt.AlignVCenter)
        self.controler_buttons.addLayout(self.horizontalLayout_4)
        self.controler.addLayout(self.controler_buttons)
        spacerItem9 = QtGui.QSpacerItem(25, 5, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.controler.addItem(spacerItem9)

        # playing song info
        self.playing_song_info = QtGui.QVBoxLayout()
        self.playing_song_info.setSpacing(0)
        self.playing_song_info.setObjectName(_fromUtf8("playing_song_info"))
        self.playing_song = QtGui.QLabel(self.centralwidget)
        self.playing_song.setMaximumSize(QtCore.QSize(16777215, 35))
        self.playing_song.setSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Fixed)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.playing_song.setFont(font)
        self.playing_song.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.playing_song.setObjectName(_fromUtf8("playing_song"))
        self.playing_song_info.addWidget(self.playing_song, QtCore.Qt.AlignRight)
        self.artist = QtGui.QLabel(self.centralwidget)
        self.artist.setMaximumSize(QtCore.QSize(16777215, 25))
        self.artist.setSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Fixed)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        self.artist.setFont(font)
        self.artist.setObjectName(_fromUtf8("artist"))
        self.artist.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.playing_song_info.addWidget(self.artist, QtCore.Qt.AlignRight)
        self.controler.addLayout(self.playing_song_info)
        self.main_control.addLayout(self.controler)

        # slider
        self.slider_area = QtGui.QHBoxLayout()
        self.slider_area.setSpacing(4)
        self.slider_area.setObjectName(_fromUtf8("slider_area"))
        self.position = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.position.sizePolicy().hasHeightForWidth())
        self.position.setSizePolicy(sizePolicy)
        self.position.setMinimumSize(QtCore.QSize(35, 20))
        self.position.setMaximumSize(QtCore.QSize(50, 20))
        self.position.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.position.setLineWidth(0)
        self.position.setText(_fromUtf8("00:00"))
        self.position.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.position.setObjectName(_fromUtf8("position"))
        self.slider_area.addWidget(self.position)
        self.seek_slider = QtGui.QSlider()
        self.seek_slider.setOrientation(QtCore.Qt.Horizontal)
        self.seek_slider.setSingleStep(1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.seek_slider.sizePolicy().hasHeightForWidth())
        self.seek_slider.setSizePolicy(sizePolicy)
        self.seek_slider.setMinimumSize(QtCore.QSize(200, 20))
        self.seek_slider.setMaximumSize(QtCore.QSize(16777215, 20))
        self.seek_slider.setObjectName(_fromUtf8("seek_slider"))
        self.slider_area.addWidget(self.seek_slider)
        self.duration = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.duration.sizePolicy().hasHeightForWidth())
        self.duration.setSizePolicy(sizePolicy)
        self.duration.setMinimumSize(QtCore.QSize(35, 20))
        self.duration.setMaximumSize(QtCore.QSize(50, 20))
        self.duration.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.duration.setLineWidth(0)
        self.duration.setText(_fromUtf8("00:00"))
        self.duration.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.duration.setObjectName(_fromUtf8("duration"))
        self.slider_area.addWidget(self.duration)
        self.main_control.addLayout(self.slider_area)
        self.control_area.addLayout(self.main_control)
        spacerItem10 = QtGui.QSpacerItem(20, 5, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.control_area.addItem(spacerItem10)

        # cover
        self.cover = QtGui.QLabel(self.centralwidget)
        self.cover.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cover.sizePolicy().hasHeightForWidth())
        self.cover.setSizePolicy(sizePolicy)
        self.cover.setMinimumSize(QtCore.QSize(150, 150))
        self.cover.setMaximumSize(QtCore.QSize(150, 150))
        self.cover.setText(_fromUtf8(""))
        # self.cover.setPixmap(QtGui.QPixmap(_fromUtf8("../../album_art_example/take_me_to_your_heart.jpg")))
        self.cover.setScaledContents(True)
        self.cover.setAlignment(QtCore.Qt.AlignCenter)
        self.cover.setObjectName(_fromUtf8("cover"))
        self.control_area.addWidget(self.cover)
        spacerItem11 = QtGui.QSpacerItem(12, 5, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.control_area.addItem(spacerItem11)
        self.verticalLayout_2.addLayout(self.control_area)
        main_window.setCentralWidget(self.centralwidget)

        self.setup_playlist_view(main_window)
        self.retranslateUi(main_window)
        # self.pl_tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        # main_window.setWindowTitle(_translate("main_window", "Miusik", None))
        self.music_menu_button.setText(_translate("main_window", "MUSIC", None))
        self.radio_menu_button.setText(_translate("main_window", "RADIO", None))
        self.open_folder_button.setText(_translate("main_window", "Open Folder", None))
        self.add_file_button.setText(_translate("main_window", "Open Files", None))
        self.save_playlist_button.setText(_translate("main_window", "Save Playlist", None))
        self.load_playlist_button.setText(_translate("main_window", "Load Playlist", None))
        self.app_setting_button.setText(_translate("main_window", "Setting", None))
        self.app_info_button.setText(_translate("main_window", "...", None))
        self.search_box.setPlaceholderText(_translate("main_window", "Search", None))

    def setup_playlist_view(self, main_window):
        # playlistview.CustomTabWidget.__init__(self, main_window)
        self.pl_tabs = playlistview.CustomTabWidget(self.playlists_frame)
        self.horizontalLayout.addWidget(self.pl_tabs)



from PyQt4 import phonon
import resources_rc

def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
