import sgtk
import sys

rez_site_pkg = "/home/rapa/resetting/rez_install/lib/python3.9/site-packages"

# Nuke Python Version 3.11 과 맞춘 Conda 환경 경로 및 pyseq parent dir
nuke_plugin_path = "/home/rapa/anaconda3/envs/nuke_pyseq/lib/python3.11/site-packages"

sys.path.append(rez_site_pkg)
sys.path.append(nuke_plugin_path)


from sgtk.platform import Application

from rez.resolved_context import ResolvedContext

try:
    from rez.resolved_context import ResolvedContext
except ImportError:
    ResolvedContext = None


class SgtkScanConverterApp(Application):
    """
    Scan Converter App 진입점 Class
    """

    def init_app(self):
        # 사용할 Rez 패키지 리스트
        rez_pkg_list = ["nuke", "conda"]
        # ResolvedContext 인스턴스 생성 및 적용
        rez_ctx = ResolvedContext(rez_pkg_list)
        rez_ctx.apply()

        # Rez 환경 변수 가져오기
        env = rez_ctx.get_environ()
        print(f"Using Rez environment: {env}")

        nuke_path = env.get("REZ_NUKE_ROOT")
        if not nuke_path:
            raise ValueError("NUKE_PATH 환경변수를 찾을 수 없습니다.")
        sys.path.append(nuke_path)
        print(f"Added REZ_NUKE_PATH : {nuke_path}")

        # Loading
        tk_scanconverter_app = self.import_module("tk_scanconverter")
        menu_callback = lambda: tk_scanconverter_app.dialog.show_dialog(self)
        self.engine.register_command("Scan Converter", menu_callback)
