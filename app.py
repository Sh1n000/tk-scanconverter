import sgtk

from sgtk.platform import Application


class SgtkScanConverterApp(Application):
    """
    Scan Converter App 진입점 Class
    이 클래스는 앱 초기화, 종료, 메뉴 등록 등의 역할을 담당합니다.
    """

    def init_app(self):
        # 앱 패키지로부터 dialog 모듈을 가져옵니다.
        app_payload = self.import_module("tk_scanconverter")

        # Scan Converter 대화상자(Dialog)를 보여주는 명령을 등록합니다.
        menu_callback = lambda: app_payload.dialog.show_dialog(self)
        self.engine.register_command("Scan Converter", menu_callback)
