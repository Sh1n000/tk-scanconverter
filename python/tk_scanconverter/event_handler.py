import os
import subprocess

from pathlib import Path

import sgtk
from sgtk.platform.qt import QtGui
from sgtk.platform.qt import QtCore


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

        # self.file_manager = file_manager

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

        nuke = os.environ.get("NUKE")

        cmd = f"{nuke}"

        result = subprocess.run(cmd, shell=True)

        return result

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
        1. org Dir, jpg Dir 생성
        2. event json 생성
        3. jpg ffmpeg Converting
        4. 원본 파일 이동 (org)
        """

        self.select_dir()  # 폴더만 선택가능

        selected_p = self.ui.path_line_edit.text()
        selected_path = Path(selected_p)
        print(f"Selected Path: {selected_path}")

        # selected_fm = FileManager(selected_path)

        # # Converting 폴더 체크
        # if not (selected_fm.is_exr_sequence() or selected_fm.is_mov()):
        #     QtGui.QMessageBox.information(None, "알림", "변환 대상 파일이 없습니다.")
        #     return

        # """경로 지정"""
        # org_path = selected_path / "org"
        # jpg_path = selected_path / "jpg"
        # meta_path = selected_path / "metadata"
        # # filmstrip_path = selected_path / "filmstrip"
        # # montage_path = selected_path / "montage"
        # # mp4_path = selected_path / "mp4"

        # # select_event.json 생성
        # selected_fm.save_select_event_json()

        # # Convert Config 생성
        # selected_cfg_factory = ConvertConfigFactory(selected_fm)

        # if selected_fm.is_exr_sequence():
        #     """Scan Data = EXR Sequence"""
        #     try:
        #         exr_to_jpg = selected_cfg_factory.get("exr_to_jpg")
        #         jpg_mc = MediaConverter(exr_to_jpg)
        #         jpg_mc.convert()
        #         print("EXR to JPG Complete")

        #         # jpg_to_webm = selected_cfg_factory.get("jpg_seq_to_webm")
        #         # webm_mc = MediaConverter(jpg_to_webm)
        #         # webm_mc.convert()

        #         # jpg_to_mp4 = selected_cfg_factory.get("jpg_seq_to_mp4")
        #         # mp4_mc = MediaConverter(jpg_to_mp4)
        #         # mp4_mc.convert()

        #         """
        #         Meta Data 생성 (JSON & 엑셀)
        #         """
        #         # # 1) EXR 파일 리스트 수집
        #         # exr_dict = selected_fm.collect_by_extension()
        #         # exr_files = exr_dict[".exr"]

        #         # # 2) ExifManager로 메타데이터 추출
        #         # exif_mgr = ExifManager()
        #         # raw_meta_list = exif_mgr.extract_metadata(exr_files)
        #         # # print(f"Raw Meta List: {raw_meta_list}")

        #         # # 3) MetadataManager에 맵핑 & 저장
        #         # meta_mgr = MetadataManager()
        #         # for path, meta in zip(exr_files, raw_meta_list):
        #         #     meta_mgr.add_record(path, meta)

        #         # # 4) JSON 또는 Excel로 출력
        #         # meta_mgr.save_json(selected_path)

        #         # meta_mgr.save_excel(selected_path, "metadata.xlsx")

        #     except Exception as e:
        #         err_box = QMessageBox()
        #         err_box.setIcon(QMessageBox.Critical)
        #         err_box.setWindowTitle("오류 발생")
        #         err_box.setText("변환 중 오류가 발생했습니다.")
        #         err_box.setInformativeText(str(e))
        #         err_box.exec()
        #         return

        #     print("@" * 80)
        #     print("EXR to JPG , Metadata 완료")
        #     print("@" * 80)

        #     """Original exr 파일 이동"""
        #     for exr in selected_fm.file_dict[".exr"]:
        #         dm.move_file(exr, org_path / exr.name)

        #     print("@" * 80)
        #     print("JPG to Media Start ")
        #     print("@" * 80)

        #     """jpg -> media Converting"""

        #     # WEBM
        #     jpg_to_webm = selected_cfg_factory.get("jpg_to_webm")
        #     webm_mc = MediaConverter(jpg_to_webm)
        #     webm_mc.convert()
        #     print("JPG to WEBM Complete")

        #     """JPG to MP4 (Rez 환경 x264, ffmpeg,  Python 스크립트)"""

        #     jpg_to_mp4 = selected_cfg_factory.get("jpg_to_mp4")
        #     print("jpg_to_MP4 Config: ", jpg_to_mp4)
        #     mp4_mc = MP4Converter(jpg_to_mp4)
        #     mp4_mc.convert()
        #     print("JPG to MP4 Complete (rez-env)")

        #     """Org to MP4 (Rez 환경 x264, ffmpeg,  Python 스크립트)"""

        #     org_to_mp4 = selected_cfg_factory.get("org_to_mp4")
        #     print("org_to_MP4 Config: ", org_to_mp4)
        #     mp4_mc = MP4Converter(org_to_mp4)
        #     mp4_mc.convert()
        #     print("Org to MP4 Complete (rez-env)")

        #     # jpg_to_montage = selected_cfg_factory.get("jpg_seq_to_tile_montage")
        #     # montage_mc = MediaConverter(jpg_to_montage)
        #     # montage_mc.convert()
        #     # print("EXR to tile Montage Complete")

        #     # # Filmstrip 만들기
        #     # film_cfg = selected_cfg_factory.get("jpg_seq_to_filmstrip", columns=5)
        #     # film_mc = MediaConverter(film_cfg)
        #     # film_mc.convert()
        #     # print("EXR to Filmstrip Complete")

        #     """완료 메세지박스 """
        #     QMessageBox.information(
        #         None,
        #         "Converting 완료",
        #         f"Selected Path: {selected_path} \n 1. org 파일이동 : Select Path / org \n 2. jpg Converting : Select Path /jpg \n 3. Meta Data : Select Path /metadata \n 4. webm, mp4 생성완료",
        #         QMessageBox.Ok,
        #     )

        # elif selected_fm.is_mov():  # mov
        #     """MOV는 보류"""
        #     pass
        #     # mov 파일 이동
        #     for mov in selected_fm.file_dict[".mov"]:
        #         dm.move_file(mov, org_path / mov.name)

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

    def collect_to_shot(self):
        """
        1. Seq / Shot Name이 지정된 경로 생성
        2. Seq / Shot Name 지정된 경로로 Data 이동
        3.
        """
        pass

    def nuke_set_slate_info(self):
        """
        ShotGrid 연결 +  Publish 까지 구현되면
        Publish할 Slate 썸네일

        Nuke의 Group Node로 Slate 정보 Setting
        1. Date   2. Project 3. FrameRate
        4.seq/shot 5. [value firtst_frame]_[value last_frame]([value frame])

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
