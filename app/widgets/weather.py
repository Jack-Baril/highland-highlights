import requests

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QHBoxLayout, QLabel, QWidget

from config import Config
from theme.styles import Styles
from utils.timer import Timer


class Weather(QWidget):
    def __init__(self):
        super().__init__()
        self.create_layout()
        self.timer = Timer.start(
            self, Config.WEATHER_UPDATE_INTERVAL, self.fetch_weather
        )
        self.fetch_weather()

    def create_layout(self):
        self.icon_label = QLabel(self)
        self.temperature_label = QLabel(self)
        layout = QHBoxLayout(self)
        layout.addWidget(self.icon_label)
        layout.addWidget(self.temperature_label)
        self.setLayout(layout)

    def fetch_weather(self):
        response = requests.get(Config.WEATHER_API_URL)
        temperature = response.json()
        weather_icon = requests.get(
            f"https:{temperature['current']['condition']['icon']}"
        ).content
        self.update_weather(temperature, weather_icon)

    def update_weather(self, temperature, weather_icon):
        self.temperature_label.setText(
            f"{temperature['current']['temp_f']:.0f}°"
        )
        pixmap = QPixmap()
        pixmap.loadFromData(weather_icon)
        scaled_pixmap = self.scale_weather_icon(pixmap)
        self.icon_label.setPixmap(scaled_pixmap)

    def scale_weather_icon(self, pixmap):
        scaled_size = Styles.WEATHER_ICON_SIZE
        return pixmap.scaled(
            scaled_size,
            scaled_size,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation,
        )
