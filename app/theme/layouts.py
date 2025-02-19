from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

from theme.styles import Styles
from widgets.clock import Clock
from widgets.date import Date
from widgets.scrolling_text import ScrollingText
from widgets.slideshow import Slideshow
from widgets.weather import Weather


class Layouts(QMainWindow):
    def __init__(self):
        super().__init__()
        central_widget = self.create_central_widget()
        self.setCentralWidget(central_widget)

    def create_central_widget(self):
        central_widget = QWidget(self)
        central_widget.setLayout(self.create_main_layout())
        self.setStyleSheet(Styles.BG_COLOR)
        return central_widget

    def create_main_layout(self):
        main_layout = self.create_layout(QVBoxLayout)
        main_layout.addLayout(self.create_top_layout())
        main_layout.addWidget(self.create_separator())
        main_layout.addLayout(self.create_slide_show_layout())
        return main_layout

    def create_top_layout(self):
        top_layout = self.create_layout(QHBoxLayout)
        clock_date_weather_layout = self.create_clock_date_weather_layout()
        scrolling_text_widget = self.create_scrolling_text_widget()
        top_layout.addLayout(clock_date_weather_layout, stretch=1)
        top_layout.addWidget(scrolling_text_widget, stretch=1)
        return top_layout

    def create_slide_show_layout(self):
        slide_show_layout = self.create_layout(QVBoxLayout)
        slideshow_widget = Slideshow()
        slide_show_layout.addWidget(slideshow_widget)
        return slide_show_layout

    def create_date_weather_layout(self):
        date_weather_layout = self.create_layout(QHBoxLayout)
        date_weather_layout.addWidget(self.create_date_widget())
        date_weather_layout.addWidget(self.create_weather_widget())
        return date_weather_layout

    def create_clock_date_weather_layout(self):
        clock_date_weather_layout = self.create_layout(
            QVBoxLayout, Qt.AlignTop | Qt.AlignCenter
        )
        clock_widget = self.create_clock_widget()
        clock_date_weather_layout.addWidget(clock_widget)
        clock_date_weather_layout.addLayout(self.create_date_weather_layout())
        return clock_date_weather_layout

    def create_clock_widget(self):
        clock = Clock()
        clock.setStyleSheet(
            Styles.apply_stylesheet(
                font_size=Styles.CLOCK_FONT_SIZE,
                color=Styles.CLOCK_COLOR,
            )
        )
        clock.setFixedHeight(Styles.CLOCK_HEIGHT)
        return clock

    def create_scrolling_text_widget(self):
        scrolling_text_widget = ScrollingText()
        scrolling_text_widget.setStyleSheet(
            Styles.apply_stylesheet(font_size=Styles.SCROLLING_TEXT_FONT_SIZE)
        )
        return scrolling_text_widget

    def create_date_widget(self):
        date = Date()
        date.setStyleSheet(
            Styles.apply_stylesheet(font_size=Styles.DATE_FONT_SIZE)
        )
        date.setFixedHeight(Styles.DATE_HEIGHT)
        return date

    def create_weather_widget(self):
        weather = Weather()
        weather.setStyleSheet(
            Styles.apply_stylesheet(font_size=Styles.TEMPERATURE_FONT_SIZE)
        )
        weather.setFixedHeight(Styles.TEMPERATURE_HEIGHT)
        return weather

    def create_separator(self):
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFixedHeight(Styles.SEPARATOR_HEIGHT)
        separator.setStyleSheet(f"{Styles.SEPARATOR_COLOR}; border: none")
        return separator

    @staticmethod
    def create_layout(
        layout_name,
        alignment=Styles.LAYOUT_ALIGNMENT,
        margins=Styles.LAYOUT_MARGINS,
        spacing=Styles.LAYOUT_SPACING,
    ):
        layout = layout_name()
        layout.setContentsMargins(*margins)
        layout.setAlignment(alignment)
        layout.setSpacing(spacing)
        return layout
