# ui_dialog.py  [old app : Ui_Builder]


from tank.platform.qt import QtCore

for name, cls in QtCore.__dict__.items():
    if isinstance(cls, type):
        globals()[name] = cls

from tank.platform.qt import QtGui

for name, cls in QtGui.__dict__.items():
    if isinstance(cls, type):
        globals()[name] = cls

# from . import resources_rc


class Ui_Dialog(object):
    """
    Viewer
    UI Builder -> Ui_Dialog

    To DO List
    1. Table Class로 분리
    2. Project Combobox 제거 -> Context로 Project 관리
    3. Date Combobox 제거
    4. Event 연결
    """

    def setupUi(self, MainWindow):
        # Main Window
        if not MainWindow.objectName():
            MainWindow.setObjectName("Scan Converter")
        MainWindow.resize(1200, 800)

        main_layout = QtGui.QVBoxLayout(MainWindow)

        # Test Context
        self.context = self.test_context_setup(MainWindow)

        # 레이아웃 구성
        main_layout.addLayout(self.build_header_layout1())
        main_layout.addLayout(self.build_header_layout2())
        main_layout.addLayout(self.build_header_layout3())
        main_layout.addWidget(self.build_main_table())  # Table Class로 불러올 예정
        main_layout.addLayout(self.build_bottom_layout())

        # # Test CheckBox [ Link css & Image ]
        # test_checkbox = QtGui.QCheckBox("✔ Red Check Test")
        # test_checkbox.setChecked(True)
        # main_layout.addWidget(test_checkbox)

        # load StyleSheet css
        self.load_style_css(MainWindow)

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

    def test_context_setup(self, input_widget):
        """Input Widget : Dialog or MainWindow"""
        context = QLabel(input_widget)
        context.setObjectName("context")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(context.sizePolicy().hasHeightForWidth())
        context.setSizePolicy(sizePolicy)
        context.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        return context

    def build_header_layout1(self):
        layout = QHBoxLayout()
        # Path Label
        path_label = QLabel("Path :")
        path_label.setObjectName("path_label")
        layout.addWidget(path_label)

        # Path Line Edit
        path_line_edit = QLineEdit()
        path_line_edit.setObjectName("path_line_edit")
        layout.addWidget(path_line_edit, 3)

        # Select Button
        btn_select = QPushButton("Select to Convert")
        btn_select.setObjectName("btn_select")
        layout.addWidget(btn_select)

        # Load Button
        btn_load = QPushButton("Load Metadata")
        btn_load.setObjectName("btn_load")
        layout.addWidget(btn_load)
        return layout

    def build_header_layout2(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)  # Project와 Date 블록 사이만 띄우기

        project_lay = self.build_project_layout()
        layout.addLayout(project_lay)

        date_lay = self.build_date_layout()
        layout.addLayout(date_lay)

        layout.addStretch()  # 공간 채우기

        return layout

    def build_header_layout3(self):
        layout = QHBoxLayout()
        check_layout = self.build_check_layout()
        check_layout.setSizeConstraint(QHBoxLayout.SetFixedSize)

        layout.addLayout(check_layout)

        layout.addStretch()

        # project_lay = self.build_project_layout()
        # layout.addLayout(project_lay)

        # date_lay = self.build_date_layout()
        # layout.addLayout(date_lay)

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
        btn_all = QPushButton("Check All")
        btn_all.setObjectName("btn_check_all")

        # Uncheck All 버튼
        btn_none = QPushButton("Uncheck All")
        btn_none.setObjectName("btn_uncheck_all")

        btn_all.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        btn_none.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        btn_all.setFixedSize(80, 30)
        btn_none.setFixedSize(80, 30)

        layout.addWidget(btn_all)
        layout.addWidget(btn_none)
        return layout

    def build_table_checkbox(self, row: int):
        checkbox = QCheckBox()

        # # 스타일시트  qss 연결실패
        # from pathlib import Path
        # app_p = Path(__file__).parents[3]
        # print(app_p)
        # self.qss_path = Path(app_p, "style.qss")
        # with open(self.qss_path, "r") as f:
        #     checkbox.setStyleSheet(f.read())

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

        table = QTableWidget()
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
        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)
        table.verticalHeader().setVisible(False)

        table.horizontalHeader().setSectionResizeMode(
            0, QHeaderView.ResizeToContents
        )  # 체크박스 셀
        """Table Size Setting"""
        size_rate = 1.3
        default_row_height = 90 * size_rate
        table.verticalHeader().setDefaultSectionSize(default_row_height)

        table.horizontalHeader().setSectionResizeMode(
            1, QHeaderView.Fixed
        )  # Thumbnail 셀
        table.setColumnWidth(1, 160 * size_rate)
        # 나머지 텍스트 열은 화면 꽉 채우기
        for col in range(2, len(headers)):
            table.horizontalHeader().setSectionResizeMode(col, QHeaderView.Stretch)

        """Row Setting"""
        # 초반 설정
        initial_rows = 30
        table.setRowCount(initial_rows)

        self.table = table
        for row in range(initial_rows):
            self.build_table_checkbox(row)

        # Load Metadata btn으로 scan_list를 구성
        scan_list = []  # User가 선택한 Meta Data

        for meta_data in scan_list:
            row = scan_list.index(meta_data)
            table.setRowCount(row + 1)
            self.build_table_check(row)
            # self.build_table_thumbnail(row, scan_data["thumbnail"])

        return table

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

    def build_project_layout(self):
        """
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        Context로 받아서 콤보박스 제거할 것
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        """
        project_lay = QHBoxLayout()
        project_lay.setContentsMargins(0, 0, 0, 0)
        project_lay.setSpacing(2)

        # Project 라벨
        pro_lbel = QLabel("Project :")
        pro_lbel.setObjectName("project_label")
        pro_lbel.setFixedWidth(60)
        pro_lbel.setMargin(0)

        # Project 콤보박스
        pro_cmb = QComboBox()
        pro_cmb.setObjectName("project_combo_box")
        pro_cmb.setFixedWidth(150)
        pro_cmb.setStyleSheet("padding:0px; margin:0px;")  # 내부 여백 최소화

        project_lay.addWidget(pro_lbel)
        project_lay.addWidget(pro_cmb)

        return project_lay

    def build_date_layout(self):
        date_lay = QHBoxLayout()
        date_lay.setContentsMargins(0, 0, 0, 0)
        date_lay.setSpacing(2)

        # Date 라벨
        date_lbl = QLabel("Date :")
        date_lbl.setObjectName("date_label")
        date_lbl.setFixedWidth(40)
        date_lbl.setMargin(0)

        # Date 콤보박스
        date_cmb = QComboBox()
        date_cmb.setObjectName("date_combo_box")
        date_cmb.setFixedWidth(150)
        date_cmb.setStyleSheet("padding:0px; margin:0px;")

        date_lay.addWidget(date_lbl)
        date_lay.addWidget(date_cmb)
        return date_lay
