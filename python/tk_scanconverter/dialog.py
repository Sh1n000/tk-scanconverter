import sgtk
import tank
import os
import sys
import threading

# from sgtk.platform.qt import QtCore, QtGui
from sgtk.platform.qt import QtGui

from .ui.ui_dialog import Ui_Dialog

from .event_handler import EventHandler


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

        self.ui = Ui_Dialog()  # UI Builder
        self.ui.setupUi(self)

        self._app = sgtk.platform.current_bundle()

        # Shotgrid Linked Project Path
        self.project_path = self._app.sgtk.roots.get("primary")

        # 이벤트 핸들러 연결
        self.event_handler = EventHandler(self.ui, self.project_path)

        # logging happens via a standard toolkit logger
        logger.info("Launching Scan Converter...")
