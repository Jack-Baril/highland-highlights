from PySide6.QtCore import QTime
from PySide6.QtWidgets import QLabel

from utils.timer import Timer


class Clock(QLabel):
    def __init__(self):
        super().__init__()
        self.timer = Timer.start(self, 1000, self.update_time)
        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime()
        hour = current_time.hour() % 12 or 12
        time_string = (
            f"{hour:02}:{current_time.minute():02}:{current_time.second():02}"
        )
        self.setText(time_string)
