import os.path
import sys
from PyQt5.Qt import *
from PyQt5.QtWidgets import *

from api.analyze import fixWarpPath
from api.sync_by_thread import SyncThread
from ui.style import Templates as Css
from ui.style import qLabel, QButton


class SyncUI(QWidget):

    def __init__(self, parent=None):
        super(SyncUI, self).__init__(parent)
        # /* var class */
        self.UI = {}
        self.setting = {"s_path": 0,
                        "d_path": 0}

        # /* setting Window * /
        self.setWindowTitle("synchronous folders V1.0")
        self.MainGrid = QGridLayout()
        self.setLayout(self.MainGrid)
        self.setStyleSheet(Css['window'])
        self.setGeometry(100, 100, 700, 400)

        self.UI['title'] = qLabel("Sync between folders ", Css['label'])
        self.UI['title'].setFont(QFont("consolas", 12, QFont.Light))
        self.UI['title'].setAlignment(Qt.AlignCenter)
        self.UI['tsource'] = qLabel("selected: (No selected)", Css['select'])
        self.UI['bsource'] = QButton("+\nsource folder", Css['button'])
        self.UI['bsource'].setMinimumSize(40, 200)
        self.UI['bsource'].clicked.connect(lambda: self.openDirectory("tsource", "s_path"))
        self.UI['tdst'] = qLabel("selected: (No selected)", Css['select'])
        self.UI['bdst'] = QButton("+\ndestination folder", Css['button'])
        self.UI['bdst'].setMinimumSize(40, 200)
        self.UI['bdst'].clicked.connect(lambda: self.openDirectory("tdst", "d_path"))
        self.UI['bstart'] = QButton("Start Synchronous", Css['start'])
        self.UI['bstart'].clicked.connect(self.startSynchronous)
        self.UI['bstart'].setMinimumHeight(40)

        self.MainGrid.addWidget(self.UI['title'], 0, 0, 1, 2)
        self.MainGrid.addWidget(self.UI['tsource'], 1, 0)
        self.MainGrid.addWidget(self.UI['bsource'], 2, 0)
        self.MainGrid.addWidget(self.UI['tdst'], 1, 1)
        self.MainGrid.addWidget(self.UI['bdst'], 2, 1)
        self.MainGrid.addWidget(self.UI['bstart'], 3, 0, 1, 2, Qt.AlignCenter)

    def openDirectory(self, typ, typ_path):
        path = QFileDialog.getExistingDirectory()
        self.setting[typ_path] = path
        if not self.verifySelected():
            QMessageBox(QMessageBox.Critical, "error", f"source path can't be destination path").exec_()
            return

        if path:
            self.UI[typ].setText(f"selected: {fixWarpPath(path)}")

    def verifySelected(self) -> bool:
        return self.setting.get("s_path") != self.setting.get("d_path")

    def startSynchronous(self):
        self.sender().setText("initializing....")
        if not (self.setting.get("s_path") and self.setting.get("d_path")):
            QMessageBox(QMessageBox.Critical, "error", f"`source` path or `destination` path is empty").exec_()

            self.sender().setText("Start Synchronous")
            return

        sync_thread = SyncThread(self.setting['s_path'], self.setting['d_path'], self)
        sync_thread.emitStatus.connect(self.getStatusSync)
        sync_thread.start()

    def getStatusSync(self, stat):
        if stat:
            self.UI['bstart'].setDisabled(True)
            self.UI['bstart'].setText("sync . . .")
        else:
            self.UI['bstart'].setDisabled(False)
            self.UI['bstart'].setText("Start Synchronous")
            QMessageBox(QMessageBox.Information, "status sync",
                        f"Synchronous main folder "
                        f"`{os.path.basename(self.setting['s_path'])}` with `{os.path.basename(self.setting['d_path'])}`"
                        f"\nfinished successfully!").exec_()


# /* run application  */
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SyncUI()
    ex.show()

    sys.exit(app.exec_())
