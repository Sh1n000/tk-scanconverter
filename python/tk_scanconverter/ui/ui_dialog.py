# ui_dialog.py  [old app : Ui_Builder]


from tank.platform.qt import QtCore

for name, cls in QtCore.__dict__.items():
    if isinstance(cls, type):
        globals()[name] = cls

from tank.platform.qt import QtGui

for name, cls in QtGui.__dict__.items():
    if isinstance(cls, type):
        globals()[name] = cls


from .ui_table import Ui_Table


class Ui_Dialog(object):
    """Viewer : Main Window UI Builder"""

    def setupUi(self, MainWindow):
        # Main Window
        if not MainWindow.objectName():
            MainWindow.setObjectName("Scan Converter")
        MainWindow.resize(1200, 800)

        main_win_layout = QtGui.QVBoxLayout(MainWindow)

        self.table = Ui_Table()

        # 레이아웃 구성
        main_win_layout.addLayout(self.build_header_layout1())
        main_win_layout.addLayout(self.build_header_layout2())
        main_win_layout.addWidget(self.table)
        main_win_layout.addLayout(self.build_bottom_layout())

        # load StyleSheet css
        self.load_style_css(MainWindow)

        # Test Button
        main_win_layout.addWidget(self.test_button())

    def test_button(self):
        """Test Button"""
        self.btn_test = QPushButton("Test")
        self.btn_test.setObjectName("btn_test")
        self.btn_test.setFixedSize(100, 30)
        return self.btn_test

    def load_style_css(self, MainWindow):
        # 스타일시트 메인윈도우로 연결
        from pathlib import Path

        app_p = Path(__file__).parents[3]
        qss_path = Path(app_p, "style.css")

        resource_path = Path(app_p, "resources", "Red Check.png").as_posix()

        with open(qss_path, "r") as f:
            style = f.read()

        # 이미지 경로 치환
        style = style.replace("{{CHECK_IMAGE}}", resource_path)

        MainWindow.setStyleSheet(style)

    def build_header_layout1(self):
        layout = QHBoxLayout()
        # Path Label
        path_label = QLabel("Path :")
        path_label.setObjectName("path_label")
        layout.addWidget(path_label)

        # Path Line Edit
        self.path_line_edit = QLineEdit()
        self.path_line_edit.setObjectName("path_line_edit")
        layout.addWidget(self.path_line_edit, 2)

        return layout

    def build_header_layout2(self):
        layout = QHBoxLayout()
        check_layout = self.build_check_layout()
        check_layout.setSizeConstraint(QHBoxLayout.SetFixedSize)

        layout.addLayout(check_layout)

        layout.addStretch()

        # Select Button
        self.btn_select = QPushButton("Select to Convert")
        self.btn_select.setObjectName("btn_select")
        layout.addWidget(self.btn_select)

        # Load Button
        self.btn_load = QPushButton("Load Metadata")
        self.btn_load.setObjectName("btn_load")
        layout.addWidget(self.btn_load)

        return layout

    def build_bottom_layout(self):
        layout = QHBoxLayout()
        """Excel Layout"""
        excel_layout = self.build_excel_layout()
        layout.addLayout(excel_layout)

        """Action Layout"""
        action_layout = self.build_action_layout()
        layout.addLayout(action_layout)

        return layout

    def build_check_layout(self):
        """Check All, Uncheck All"""
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)

        # Check All 버튼
        self.btn_check_all = QPushButton("Check All")
        self.btn_check_all.setObjectName("btn_check_all")

        # Uncheck All 버튼
        self.btn_uncheck_all = QPushButton("Uncheck All")
        self.btn_uncheck_all.setObjectName("btn_uncheck_all")

        self.btn_check_all.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.btn_uncheck_all.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.btn_check_all.setFixedSize(80, 30)
        self.btn_uncheck_all.setFixedSize(80, 30)

        layout.addWidget(self.btn_check_all)
        layout.addWidget(self.btn_uncheck_all)
        return layout

    def build_excel_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Excel"))
        # Edit
        btn_excel_edit = QPushButton("Edit")
        btn_excel_edit.setObjectName("btn_excel_edit")
        # Save
        btn_excel_save = QPushButton("Save")
        btn_excel_save.setObjectName("btn_excel_save")

        layout.addWidget(btn_excel_edit)
        layout.addWidget(btn_excel_save)
        return layout

    def build_action_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Action"))
        # Collect
        btn_collect = QPushButton("Collect")
        btn_collect.setObjectName("btn_collect")
        # Publish
        btn_publish = QPushButton("Publish")
        btn_publish.setObjectName("btn_publish")

        layout.addWidget(btn_collect)
        layout.addWidget(btn_publish)

        return layout
