from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QScrollArea, QVBoxLayout, QWidget

from config import Config
from theme.styles import Styles
from utils.docx_html_converter import DocxHtmlConverter
from utils.file_watcher import FileWatcher
from utils.timer import Timer


class ScrollingText(QWidget):
    def __init__(self):
        super().__init__()
        self.file_watcher = FileWatcher(
            Config.FILE_UPLOAD_DIRECTORY,
            "*.docx",
            self.update_text,
            DocxHtmlConverter.parse_docx,
        )
        self.text = self.file_watcher.get_latest_file()
        self.labels = self.create_labels(self.text)
        self.create_scroll_area()
        self.create_layout()
        self.timer = Timer.start(
            self, Config.TEXT_SCROLL_INTERVAL, self.scroll_labels
        )

    def create_scroll_area(self):
        self.scroll_area = QScrollArea(self)
        self.scroll_widget = QWidget(self)
        self.scroll_area.setWidget(self.scroll_widget)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("border: none")
        self.scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.scroll_area.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.scroll_area.setEnabled(False)

    def create_layout(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(*Styles.LAYOUT_MARGINS)
        scroll_layout = QVBoxLayout(self.scroll_widget)
        for label in self.labels:
            scroll_layout.addWidget(label)
        layout.addWidget(self.scroll_area)

    def create_labels(self, text):
        return [self.setup_label(text) for _ in range(2)]

    def setup_label(self, text):
        label = QLabel(self)
        label.setText(text)
        label.setWordWrap(True)
        return label

    def set_text(self, text):
        self.text = text
        for label in self.labels:
            label.setText(self.text)

    def update_text(self):
        latest_text = self.file_watcher.get_latest_file()
        if latest_text:
            self.set_text(latest_text)

    def scroll_labels(self):
        for i, label in enumerate(self.labels):
            label.move(0, label.y() - 1)
            next_label = self.labels[(i + 1) % len(self.labels)]
            if label.y() + label.height() <= 0:
                label.move(0, next_label.y() + next_label.height())
