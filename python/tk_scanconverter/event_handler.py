import os
import sys
import subprocess
import json


from pathlib import Path
from dataclasses import asdict
from typing import List, Dict, Any

import sgtk
from sgtk.platform.qt import QtCore, QtGui


from ..model_data import select_file

# from .data.select_scan_to_convert import FileManager

# from .model_data import metadata
# from .model_data import scan_file


class EventHandler(object):
    """UI Event 관리 Class"""

    def __init__(self, ui, project_path):
        super().__init__()

        self.ui = ui  # UI Builder
        self.project_path = project_path
        self.table = self.ui.table  # Ui_Table()

        self.current_p = Path(__file__).parent

        # Line Edit Scan Path
        self.default_scan_p = Path(self.project_path) / "product" / "scan"
        default_str_p = str(self.default_scan_p)
        self.ui.path_line_edit.setText(default_str_p)

        self._connect_signals()

    @staticmethod
    def _error(comment: str, error: Exception):
        error_box = QtGui.QMessageBox()
        error_box.setIcon(QtGui.QMessageBox.Critical)
        error_box.setWindowTitle("Error")
        error_box.setText(comment)
        error_box.setInformativeText(str(error))
        error_box.exec()

    def _connect_signals(self):
        # 버튼 클릭 이벤트 연결
        self.ui.btn_select.clicked.connect(self.selected_to_convert)

        self.ui.btn_check_all.clicked.connect(self.check_all)
        self.ui.btn_uncheck_all.clicked.connect(self.uncheck_all)

        self.ui.btn_test.clicked.connect(self.test_button_clicked)

    def test_button_clicked(self):
        """Test Button Clicked Event"""
        print("Test Button Clicked")

        # Nuke 환경변수
        nuke_path = os.environ.get("NUKE")

        # # Nuke Plugin Setting  # Nuke Plugin Path Append를 시도 했으나 RLM라이선스 필요
        # cmd = f"python {p / 'nuke_setup.py'}"
        # nuke_setup = subprocess.run(cmd, shell=True)

        # Run Nuke
        nuke_cmd = f"{nuke_path} -ix {self.current_p / 'nuke_test.py'}"

        run_nuke = subprocess.run(nuke_cmd, shell=True)

        return run_nuke

    def update_path_line_edit(self, path: Path):
        """Path Line Edit에 경로를 문자열로 설정"""
        self.ui.path_line_edit.setText(str(path))

    def select_dir(self):
        """폴더만 선택가능"""
        options = QtGui.QFileDialog.Options()
        options |= QtGui.QFileDialog.ShowDirsOnly

        scan_dir_path = QtGui.QFileDialog.getExistingDirectory(
            None,
            "Select Folder",
            self.ui.path_line_edit.text(),
            options=options,
        )
        if scan_dir_path:
            self.ui.path_line_edit.setText(scan_dir_path)

    def selected_to_convert(self):
        """
        Convert 버튼 클릭 시
        1. 확장자 인식
        2.
        3.
        4.
        """

        self.select_dir()  # 폴더만 선택가능

        selected_p = self.ui.path_line_edit.text()

        # Str -> Path 객체
        selected_path = Path(selected_p)
        print(f"Selected Path: {selected_path}")

        # 확장자 인식
        for f in selected_path.iterdir():
            if f.is_file():
                ext = f.suffix.lower().strip(".")

                file = [str(p) for p in selected_path.glob(f"*.{ext}")]

        print(f"Ext: {ext}")  # exr, mov
        print(f"Selected File: {file}")

        # selected_sf = select_file.ScanFile(selected_p, ext, file)
        # selected_data = asdict(selected_sf)
        # print(selected_data)
        # print(selected_data["selected_dir"])
        # print(selected_data["ext"])
        # print(selected_data['file_list'])

        selected_data = {
            "selected_dir": selected_path,
            "ext": ext,
            "file_list": file,
        }

        """cmd를 List로 바꿔서 시도"""
        # File Manager로 전달
        cmd = f"python {self.current_p}/file_manager.py -- {selected_data}"  # Dict가 List Class로 바뀌는 문제
        # cmd = f"python {self.current_p / 'file_manager.py'} -- {data_json}"

        result = subprocess.run(cmd, shell=True, capture_output=True)

        if result.returncode != 0:
            # 에러 로그 출력
            print("▶ file_manager 에러:", result.stderr)
        else:
            print("▶ file_manager 결과:", result.stdout)

        return result

    def load_metadata(self):
        """
        - select_to_convert 버튼으로 생성된 엑셀파일 불러오기
        -  Metadata (엑셀파일)를 Table Wiget의 scan_list에 추가

        scan_list = [
            {
            "file_path :"",
            "thumbnail": thumbnail_path,
            }
            ]
        - 썸네일 UI와 연결
        """
        # Scanlsit 경로 생성
        pass

    def edit_metadata(self):
        """Check Box에 체크되어있는 Metadata를 수정할 수 있도록 엑셀파일 관련 프로그램 실행"""
        pass

    def save_metadata(self):
        """
        1. Seq / Shot Name이 있는지 없는지 체크  ( Validate )
        2. 수정된 엑셀파일 저장
        3. Seq / Shot Name이 지정된 경로 생성
        4. Seq / Shot Name 지정된 경로로 Data 이동
        """
        pass

    def check_all(self):
        """모든 행의 체크박스를 체크 상태로 변경"""
        for row in range(self.table.rowCount()):
            cell_widget = self.table.cellWidget(row, 0)
            if cell_widget:
                checkbox = cell_widget.findChild(QtGui.QCheckBox)
                if checkbox:
                    checkbox.setChecked(True)
        print("check_all")

    def uncheck_all(self):
        """모든 행의 체크박스를 언체크 상태로 변경"""
        for row in range(self.table.rowCount()):
            cell_widget = self.table.cellWidget(row, 0)
            if cell_widget:
                checkbox = cell_widget.findChild(QtGui.QCheckBox)
                if checkbox:
                    checkbox.setChecked(False)
        print("uncheck_all")
