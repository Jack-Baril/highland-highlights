from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication, QImage, QPixmap
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

import fitz

from config import Config
from theme.styles import Styles
from utils.file_watcher import FileWatcher
from utils.timer import Timer


class Slideshow(QWidget):
    def __init__(self):
        super().__init__()
        self.file_watcher = FileWatcher(
            Config.FILE_UPLOAD_DIRECTORY, "*.pdf", self.reload_pages
        )
        self.current_page = 0
        self.pixmap_cache = []
        self.create_layout()
        self.reload_pages()
        self.timer = Timer.start(
            self, Config.SLIDESHOW_CYCLE_INTERVAL, self.cycle_pages
        )

    def create_layout(self):
        self.label = QLabel()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(*Styles.LAYOUT_MARGINS)
        layout.setAlignment(Styles.LAYOUT_ALIGNMENT)
        layout.addWidget(self.label)

    def reload_pages(self):
        latest_pdf = self.file_watcher.get_latest_file()
        if latest_pdf:
            self.load_pages(latest_pdf)
        self.current_page = 0
        self.update_slideshow()

    def load_pages(self, pdf_path):
        self.pixmap_cache = []
        with fitz.open(pdf_path) as pdf:
            for page_num in range(len(pdf)):
                page = pdf.load_page(page_num)
                pixmap = page.get_pixmap(alpha=False)
                image = QImage(
                    pixmap.samples,
                    pixmap.width,
                    pixmap.height,
                    pixmap.stride,
                    QImage.Format_RGB888,
                )
                pixmap = QPixmap.fromImage(image)
                scaled_pixmap = self.scale_pixmap(pixmap)
                self.pixmap_cache.append(scaled_pixmap)

    def scale_pixmap(self, pixmap):
        return pixmap.scaled(
            QGuiApplication.primaryScreen().availableGeometry().size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation,
        )

    def update_slideshow(self):
        if not self.pixmap_cache:
            self.label.setVisible(False)
            return None
        self.label.setVisible(True)
        self.label.setPixmap(self.pixmap_cache[self.current_page])

    def cycle_pages(self):
        if self.pixmap_cache:
            self.current_page = (self.current_page + 1) % len(self.pixmap_cache)
            self.update_slideshow()
