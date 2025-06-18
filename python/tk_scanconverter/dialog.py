import sgtk
import os
import sys
import threading

# from sgtk.platform.qt import QtCore, QtGui
from sgtk.platform.qt import QtGui

from .ui.ui_dialog import Ui_Dialog

# from ui.ui_event_handler import IOManagerEventHandler


# standard toolkit logger
logger = sgtk.platform.get_logger(__name__)


def show_dialog(app_instance):
    app_instance.engine.show_dialog(
        "Scan Converter...", app_instance, ScanConverterDialog
    )


class ScanConverterDialog(QtGui.QWidget):
    """
    Controller : Scan Converter Dialog
    """

    def __init__(self):
        super().__init__()

        # Instance 변수 설정

        # self.event_handler =IOManagerEventHandler(
        #     self.ui.widget_dict,
        #     self.path_mgr,
        # )

        self.ui = Ui_Dialog()  # UI Builder
        self.ui.setupUi(self)

        # most of the useful accessors are available through the Application class instance
        # it is often handy to keep a reference to this. You can get it via the following method:
        self._app = sgtk.platform.current_bundle()

        """Starter App 템플릿"""
        # set up our very basic UI
        self.ui.context.setText("Current Context: %s" % self._app.context)

        # logging happens via a standard toolkit logger
        logger.info("Launching Scan Converter...")
