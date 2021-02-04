from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QHBoxLayout,QVBoxLayout,QLabel,QSlider,QStyle,QSizePolicy,QFileDialog
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtMultimedia import QMediaPlayer,QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Media player")
        self.setGeometry(150,50,1080,630)
        self.setWindowIcon(QtGui.QIcon("play.ico"))
        self.media_palyer()
        self.show()

    def media_palyer(self):
        self.mediaPlayer = QMediaPlayer(self,QMediaPlayer.VideoSurface)
        videowidget = QVideoWidget()

        # Open Video Button
        openbtn = QPushButton("Open Video")
        openbtn.clicked.connect(self.openVideo)

        # Play Button
        self.playbtn = QPushButton()
        self.playbtn.setEnabled(False)
        self.playbtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playbtn.clicked.connect(self.play_video)

        # Create Slider
        self.slider = QSlider(QtCore.Qt.Horizontal)
        self.slider.setRange(0,0)

        # Create Label
        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Maximum)

        # Create HBox Layout
        hbox = QHBoxLayout()
        hbox.setContentsMargins(0,0,0,0)
        hbox.addWidget(openbtn)
        hbox.addWidget(self.playbtn)
        hbox.addWidget(self.slider)

        # Create VBox Layout
        vbox = QVBoxLayout()
        vbox.addWidget(videowidget)
        vbox.addLayout(hbox)
        vbox.addWidget(self.label)
        self.setLayout(vbox)

        # Create palette
        palete = self.palette()
        palete.setColor(QtGui.QPalette.Window,QtCore.Qt.black)
        self.setPalette(palete)
        self.mediaPlayer.setVideoOutput(videowidget)

    def openVideo(self):
        filename, _ = QFileDialog.getOpenFileName(self,"Open Video")
        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QtCore.QUrl.fromLocalFile(filename)))
            self.playbtn.setEnabled(True)
        
    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playbtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()
            self.playbtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    
if __name__ == "__main__":
    App = QApplication(sys.argv)
    Window = Window()
    sys.exit(App.exec())