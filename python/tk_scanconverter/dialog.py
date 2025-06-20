import sgtk
import os
import sys
import threading

# from sgtk.platform.qt import QtCore, QtGui
from sgtk.platform.qt import QtGui

from .ui.ui_dialog import Ui_Dialog

# from .event_handler import EventHandler


# standard toolkit logger
logger = sgtk.platform.get_logger(__name__)


def show_dialog(app_instance):
    app_instance.engine.show_dialog(
        "Scan Converter", app_instance, ScanConverterDialog
    )  # SGtk Header Dialog


class ScanConverterDialog(QtGui.QWidget):
    """
    Controller : Scan Converter Dialog
    """

    def __init__(self):
        super().__init__()

        # Instance 변수 설정

        # PathManager 초기화 (show_root 는 Path 객체로 관리)
        # show_root = Path("/show")
        # self.path_mgr = PathManager(show_root)

        # self.event_handler = EventHandler(
        #     self.path_mgr,
        # )

        self.ui = Ui_Dialog()  # UI Builder
        self.ui.setupUi(self)

        # most of the useful accessors are available through the Application class instance
        # it is often handy to keep a reference to this. You can get it via the following method:
        self._app = sgtk.platform.current_bundle()

        # print(f"self.app.context : {self._app.context}")
        # self.app.context : {Project Castle}

        # print(f"self.app.context.project : {self._app.context.project}")
        # self.app.context.project : {'type': 'Project', 'id': 231, 'name': 'Castle'}

        # logging happens via a standard toolkit logger
        logger.info("Launching Scan Converter...")
