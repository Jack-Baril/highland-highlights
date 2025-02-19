from pathlib import Path

from PySide6.QtCore import QFileSystemWatcher


class FileWatcher:
    def __init__(
        self,
        watch_directory,
        file_extension_filter,
        on_directory_update,
        on_new_file_detected=None,
    ):
        self.watch_directory = Path(watch_directory)
        self.file_extension_filter = file_extension_filter
        self.on_directory_update = on_directory_update
        self.on_new_file_detected = on_new_file_detected
        self.file_watcher = QFileSystemWatcher()
        self.file_watcher.addPath(str(self.watch_directory))
        self.file_watcher.directoryChanged.connect(on_directory_update)

    def get_latest_file(self):
        files = list(self.watch_directory.glob(self.file_extension_filter))
        if not files:
            return None
        latest_file = max(files, key=lambda f: f.stat().st_mtime)
        return (
            self.on_new_file_detected(latest_file)
            if self.on_new_file_detected
            else latest_file
        )
