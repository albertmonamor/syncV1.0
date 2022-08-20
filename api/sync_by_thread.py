from PyQt5.QtCore import QThread, pyqtSignal

from api.SyncFolder import SyncFolders


class SyncThread(QThread):

    emitStatus = pyqtSignal(int)

    def __init__(self, src, dst, parent=None):
        super(SyncThread, self).__init__(parent)

        self.s_path = src
        self.d_path = dst
        self.synchron = SyncFolders()

    # noinspection PyUnresolvedReferences
    def run(self) -> None:
        self.emitStatus.emit(1)
        self.synchron.sync(self.synchron.getFolders(self.s_path, self.d_path))
        self.emitStatus.emit(0)


