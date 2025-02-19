from PySide6.QtCore import QTimer


class Timer:
    @staticmethod
    def start(parent, interval, callback):
        timer = QTimer(parent)
        timer.setInterval(interval)
        timer.timeout.connect(callback)
        timer.start()
        return timer
