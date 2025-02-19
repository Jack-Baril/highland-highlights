import sys
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from config import Config
from theme.layouts import Layouts


class Main(Layouts):
    def __init__(self):
        super().__init__()
        self.file_upload_directory = Path(Config.FILE_UPLOAD_DIRECTORY)
        self.file_upload_directory.mkdir(parents=True, exist_ok=True)
        self.setWindowTitle(Config.APP_NAME)
        self.setWindowIcon(QIcon(Config.APP_ICON_PATH))
        self.setCursor(Qt.BlankCursor)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape and self.isFullScreen():
            self.setWindowState(self.windowState() & ~Qt.WindowFullScreen)
        if event.key() == Qt.Key_F11:
            self.setWindowState(self.windowState() ^ Qt.WindowFullScreen)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.showFullScreen()
    sys.exit(app.exec())
