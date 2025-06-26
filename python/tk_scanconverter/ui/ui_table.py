from tank.platform.qt import QtGui

for name, cls in QtGui.__dict__.items():
    if isinstance(cls, type):
        globals()[name] = cls


class Ui_Table(QtGui.QTableWidget):
    """Viewer : Table Widget"""

    def __init__(self):
        super().__init__()

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

        size_rate = 1.8

        self.scan_list = []  # User가 선택한 Meta Data

        self.column_setting(headers)

        self.row_setting(30, self.scan_list)

        self.set_size(size_rate)

    def set_size(self, size_rate):
        """Table Size Setting"""
        default_row_height = 90 * size_rate

        self.verticalHeader().setVisible(False)
        self.verticalHeader().setDefaultSectionSize(default_row_height)

        self.horizontalHeader().setSectionResizeMode(
            1, QHeaderView.Fixed
        )  # Thumbnail 셀

        # Thumbnail 셀의 크기 설정 (row height에 비례)
        self.setColumnWidth(1, 210 * size_rate)

        self.horizontalHeader().setSectionResizeMode(
            0, QHeaderView.ResizeToContents
        )  # 체크박스 셀

    def column_setting(self, headers=list):
        self.setColumnCount(len(headers))
        self.setHorizontalHeaderLabels(headers)

        # 나머지 텍스트 열은 화면 꽉 채우기
        for col in range(2, len(headers)):
            self.horizontalHeader().setSectionResizeMode(col, QHeaderView.Stretch)

    def row_setting(self, row, scan_list):
        """Row Setting"""
        # 초반 설정
        self.setRowCount(row)

        for row in range(row):
            self.build_table_checkbox(row)

        # Load Metadata btn으로 scan_list를 구성
        scan_list = []  # User가 선택한 Meta Data

        for meta_data in scan_list:
            row = scan_list.index(meta_data)
            self.setRowCount(row + 1)
            self.build_table_checkbox(row)
            # self.build_table_thumbnail(row, scan_data["thumbnail"])

        # return self

    def build_table_thumbnail(self, row: int, thumbnail_path: str):
        """idx : 1번째 row에 Thumbnail 추가"""
        label = QLabel()
        pixmap = QPixmap(thumbnail_path).scaled(80, 80, Qt.KeepAspectRatio)
        label.setPixmap(pixmap)
        self.setCellWidget(row, 1, label)

    def build_table_checkbox(self, row: int):
        checkbox = QCheckBox()

        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.addWidget(checkbox)
        layout.setAlignment(QtGui.Qt.AlignCenter)  # Qt? QtGui.Qt?
        layout.setContentsMargins(0, 0, 0, 0)
        self.setCellWidget(row, 0, widget)
