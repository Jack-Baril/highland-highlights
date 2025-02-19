from functools import cache

from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication

from utils.classproperty import classproperty


class Styles:
    # Defaults for layout creation
    LAYOUT_ALIGNMENT = Qt.AlignCenter
    LAYOUT_MARGINS = 0, 0, 0, 0
    LAYOUT_SPACING = 0

    # HEX colors
    BG_COLOR = "background-color: #101010"
    CLOCK_COLOR = "#007c70"
    DOCX_HEADER_COLOR = "#006666"
    SEPARATOR_COLOR = "background-color: #eb8d18"
    TEXT_COLOR = "#cfcfcf"
    TEXT_HEADER_COLOR = "#007c70"

    # Font
    FONT_FAMILY = "Nunito"
    FONT_WEIGHT = "bold"

    # Font sizes in pixels based on the reference screen's dimensions
    BASE_CLOCK_FONT_SIZE = 155
    BASE_DATE_FONT_SIZE = 45
    BASE_TEMPERATURE_FONT_SIZE = 45
    BASE_SCROLLING_TEXT_FONT_SIZE = 30

    # Widget heights and sizes in pixels based on the reference screen's dimensions
    BASE_CLOCK_HEIGHT = 130
    BASE_DATE_HEIGHT = 64
    BASE_TEMPERATURE_HEIGHT = 64
    BASE_SEPARATOR_HEIGHT = 14
    BASE_WEATHER_ICON_SIZE = 64

    # Reference screen's dimensions in pixels for scaling calculations
    REFERENCE_SCREEN_WIDTH = 1440
    REFERENCE_SCREEN_HEIGHT = 900

    @classmethod
    @cache
    def get_scale_factor(cls):
        screen = QGuiApplication.primaryScreen().availableGeometry()
        return min(
            screen.width() / cls.REFERENCE_SCREEN_WIDTH,
            screen.height() / cls.REFERENCE_SCREEN_HEIGHT,
        )

    @classmethod
    def scale_size(cls, base_size):
        return int(base_size * cls.get_scale_factor())

    @classproperty
    def CLOCK_FONT_SIZE(cls):
        return cls.scale_size(cls.BASE_CLOCK_FONT_SIZE)

    @classproperty
    def DATE_FONT_SIZE(cls):
        return cls.scale_size(cls.BASE_DATE_FONT_SIZE)

    @classproperty
    def TEMPERATURE_FONT_SIZE(cls):
        return cls.scale_size(cls.BASE_TEMPERATURE_FONT_SIZE)

    @classproperty
    def SCROLLING_TEXT_FONT_SIZE(cls):
        return cls.scale_size(cls.BASE_SCROLLING_TEXT_FONT_SIZE)

    @classproperty
    def CLOCK_HEIGHT(cls):
        return cls.scale_size(cls.BASE_CLOCK_HEIGHT)

    @classproperty
    def DATE_HEIGHT(cls):
        return cls.scale_size(cls.BASE_DATE_HEIGHT)

    @classproperty
    def TEMPERATURE_HEIGHT(cls):
        return cls.scale_size(cls.BASE_TEMPERATURE_HEIGHT)

    @classproperty
    def SEPARATOR_HEIGHT(cls):
        return cls.scale_size(cls.BASE_SEPARATOR_HEIGHT)

    @classproperty
    def WEATHER_ICON_SIZE(cls):
        return cls.scale_size(cls.BASE_WEATHER_ICON_SIZE)

    @staticmethod
    def apply_stylesheet(
        font_size,
        font_weight=FONT_WEIGHT,
        font_family=FONT_FAMILY,
        color=TEXT_COLOR,
    ):
        return f"font-size: {font_size}px; font-weight: {font_weight}; font-family: {font_family}; color: {color}"
