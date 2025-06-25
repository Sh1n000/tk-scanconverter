# ui_dialog.py  [old app : Ui_Builder]


from tank.platform.qt import QtCore

for name, cls in QtCore.__dict__.items():
    if isinstance(cls, type):
        globals()[name] = cls

from tank.platform.qt import QtGui

for name, cls in QtGui.__dict__.items():
    if isinstance(cls, type):
        globals()[name] = cls


class Ui_Dialog(object):
    """
    Viewer
    UI Builder -> Ui_Dialog

    To DO List
    1. Table Class로 분리
    2.  Event 연결
    """

    def setupUi(self, MainWindow):
        # Main Window
        if not MainWindow.objectName():
            MainWindow.setObjectName("Scan Converter")
        MainWindow.resize(1200, 800)

        main_layout = QtGui.QVBoxLayout(MainWindow)

        # 레이아웃 구성
        main_layout.addLayout(self.build_header_layout1())
        main_layout.addLayout(self.build_header_layout2())
        # main_layout.addLayout(self.build_header_layout3())
        main_layout.addWidget(self.build_main_table())  # Table Class로 불러올 예정
        main_layout.addLayout(self.build_bottom_layout())

        # load StyleSheet css
        self.load_style_css(MainWindow)

        # # Test CheckBox [ Link css & Image ]
        # test_checkbox = QtGui.QCheckBox("✔ Red Check Test")
        # test_checkbox.setChecked(True)
        # main_layout.addWidget(test_checkbox)

    def load_style_css(self, MainWindow):
        # 스타일시트 메인윈도우로 연결
        from pathlib import Path

        app_p = Path(__file__).parents[3]
        qss_path = Path(app_p, "style.css")

        resource_path = Path(app_p, "resources", "Red Check.png").as_posix()

        with open(qss_path, "r") as f:
            # MainWindow.setStyleSheet(f.read())
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

        # date_lay = self.build_date_layout()
        # layout.addLayout(date_lay)

        # # Select Button
        # self.btn_select = QPushButton("Select to Convert")
        # self.btn_select.setObjectName("btn_select")
        # layout.addWidget(self.btn_select)

        # # Load Button
        # self.btn_load = QPushButton("Load Metadata")
        # self.btn_load.setObjectName("btn_load")
        # layout.addWidget(self.btn_load)
        return layout

    def build_header_layout2(self):
        layout = QHBoxLayout()
        check_layout = self.build_check_layout()
        check_layout.setSizeConstraint(QHBoxLayout.SetFixedSize)

        layout.addLayout(check_layout)

        layout.addStretch()

        # date_lay = self.build_date_layout()
        # layout.addLayout(date_lay)

        # Select Button
        self.btn_select = QPushButton("Select to Convert")
        self.btn_select.setObjectName("btn_select")
        layout.addWidget(self.btn_select)

        # Load Button
        self.btn_load = QPushButton("Load Metadata")
        self.btn_load.setObjectName("btn_load")
        layout.addWidget(self.btn_load)

        return layout

    # def build_header_layout3(self):
    #     layout = QHBoxLayout()
    #     pass
    #     return layout

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

    def build_table_checkbox(self, row: int):
        checkbox = QCheckBox()

        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.addWidget(checkbox)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)
        self.table.setCellWidget(row, 0, widget)

    def build_main_table(self):
        """
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        Table관련부분은 Class로 분리할 것
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        """

        self.table = QTableWidget()
        # widget_dict 에 'table' 키로 등록
        """Column Header Setting"""
        headers = [
            "check",
            "thumbnail",
            "seq_name",
            "shot_name",
            "version",
            "type",
            "scan_path",
            "resoliution",
        ]
        self.table.setColumnCount(len(headers))
        self.table.setHorizontalHeaderLabels(headers)
        self.table.verticalHeader().setVisible(False)

        self.table.horizontalHeader().setSectionResizeMode(
            0, QHeaderView.ResizeToContents
        )  # 체크박스 셀
        """Table Size Setting"""
        size_rate = 1.3
        default_row_height = 90 * size_rate
        self.table.verticalHeader().setDefaultSectionSize(default_row_height)

        self.table.horizontalHeader().setSectionResizeMode(
            1, QHeaderView.Fixed
        )  # Thumbnail 셀
        self.table.setColumnWidth(1, 160 * size_rate)
        # 나머지 텍스트 열은 화면 꽉 채우기
        for col in range(2, len(headers)):
            self.table.horizontalHeader().setSectionResizeMode(col, QHeaderView.Stretch)

        """Row Setting"""
        # 초반 설정
        initial_rows = 30
        self.table.setRowCount(initial_rows)

        for row in range(initial_rows):
            self.build_table_checkbox(row)

        # Load Metadata btn으로 scan_list를 구성
        scan_list = []  # User가 선택한 Meta Data

        for meta_data in scan_list:
            row = scan_list.index(meta_data)
            self.table.setRowCount(row + 1)
            self.build_table_check(row)
            # self.build_table_thumbnail(row, scan_data["thumbnail"])

        return self.table

    def build_table_thumbnail(self, row: int, thumbnail_path: str):
        """idx : 1번째 row에 Thumbnail 추가"""
        label = QLabel()
        pixmap = QPixmap(thumbnail_path).scaled(80, 80, Qt.KeepAspectRatio)
        label.setPixmap(pixmap)
        self.table.setCellWidget(row, 1, label)

    def build_excel_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Excel"))
        # Edit
        btn_excel_edit = QPushButton(" Edit")
        btn_excel_edit.setObjectName("btn_excel_edit")
        # Save
        btn_excel_save = QPushButton(" Save")
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

    # def build_date_layout(self):
    #     date_lay = QHBoxLayout()
    #     date_lay.setContentsMargins(0, 0, 0, 0)
    #     date_lay.setSpacing(2)

    #     date_lbl = QLabel("Date :")
    #     date_lbl.setObjectName("date_label")
    #     date_lbl.setFixedWidth(40)
    #     date_lbl.setMargin(0)

    #     self.date_combo_box = QComboBox()
    #     self.date_combo_box.setObjectName("date_combo_box")
    #     self.date_combo_box.setFixedWidth(150)

    #     date_lay.addWidget(date_lbl)
    #     date_lay.addWidget(self.date_combo_box)
    #     return date_lay
