import sgtk
import tank
import threading

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
        project_path = self._app.sgtk.roots.get("primary")

        #  Link Controller : Event Handler
        self.event_handler = EventHandler(self.ui, project_path)

        # logging happens via a standard toolkit logger
        logger.info("Launching Scan Converter...")
