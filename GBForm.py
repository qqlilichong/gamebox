
#####################################################################

import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

#####################################################################


class MainApp(QApplication):
    def __init__(self, corex):
        super().__init__(sys.argv)
        self.form = MainForm(corex)

    def showform(self):
        self.form.show()

    def waitexit(self):
        sys.exit(self.exec_())


#####################################################################


class MainForm(QWidget):
    def __init__(self, corex):
        super().__init__()
        self.resize(640, 480)
        self.setWindowTitle('GBox')
        self.setStyleSheet('font-family:微软雅黑;')

        self.corex = corex
        self.c_cores = QComboBox(self)
        self.c_games = QListWidget(self)
        self.c_game_preview = QLabel(self)
        self.c_game_comment = QLabel(self)
        c_laymy = QHBoxLayout(self)
        c_laylt = QVBoxLayout(self)
        c_layrt = QVBoxLayout(self)
        c_laylt.addWidget(self.c_cores)
        c_laylt.addWidget(self.c_games)
        c_layrt.addWidget(self.c_game_preview)
        c_layrt.addWidget(self.c_game_comment)
        c_laymy.addLayout(c_laylt)
        c_laymy.addLayout(c_layrt)
        self.setLayout(c_laymy)
        self.c_game_preview.setFixedSize(320, 320)
        self.c_game_preview.setStyleSheet('border:2px solid lightgray;')
        self.c_game_comment.setStyleSheet('border:2px solid gray;')
        self.c_game_comment.setFixedSize(self.c_game_preview.width(), self.height() - self.c_game_preview.height())
        self.c_game_comment.setAlignment(Qt.AlignLeft)

        self.c_cores.currentIndexChanged.connect(self.slot_core_changed)
        self.c_games.itemClicked.connect(self.slot_game_selected)
        self.c_games.itemDoubleClicked.connect(self.slot_game_run)

        for key, core in self.corex.cores.items():
            self.c_cores.addItem(core.comment, key)

    def slot_clear(self):
        self.c_game_preview.clear()
        self.c_game_comment.clear()

    def slot_core_changed(self, idx):
        self.c_games.clear()
        self.slot_clear()

        key = self.c_cores.itemData(idx)
        for configer in self.corex.games:
            if configer.corename != key:
                continue
            item = QListWidgetItem()
            item.setText(configer.comment)
            item.setData(Qt.UserRole, configer)
            self.c_games.addItem(item)

    def slot_game_selected(self, item):
        self.slot_clear()
        configer = item.data(Qt.UserRole)
        if not configer:
            return

        img = os.path.join(configer.dir, configer.preview)
        self.c_game_preview.setPixmap(QPixmap(img))
        self.c_game_comment.setText(configer.desc)

    def slot_game_run(self, item):
        configer = item.data(Qt.UserRole)
        if not configer:
            return

        if self and configer.coreref:
            self.setHidden(True)
            configer.coreref.run(configer)
            self.setHidden(False)


#####################################################################
