import sgtk
import os
import sys

rez_site_pkg = "/home/rapa/resetting/rez_install/lib/python3.9/site-packages"
sys.path.append(rez_site_pkg)


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
        # append rez packages
        self.set_rez(["nuke", "pyseq"])

        # Loading
        tk_scanconverter_app = self.import_module("tk_scanconverter")
        menu_callback = lambda: tk_scanconverter_app.dialog.show_dialog(self)
        self.engine.register_command("Scan Converter", menu_callback)

    def set_rez(self, rez_pkgs=list):
        # 사용할 Rez 패키지 리스트
        # ResolvedContext 인스턴스 생성 및 적용
        rez_ctx = ResolvedContext(rez_pkgs)
        rez_ctx.apply()

        """Rez 환경 변수 가져오기"""
        env = rez_ctx.get_environ()
        print(f"Using Rez environment: {env}")

        nuke = env["NUKE"]  # Run Nuke Path

        if not nuke:
            raise ValueError("NUKE 환경변수를 찾을 수 없습니다.")

        sys.path.append(nuke)

        # 환경변수 지정
        os.environ["NUKE"] = nuke

        os.environ["REZ_PYSEQ"] = env["REZ_PYSEQ"]

        # """Nuke 에 플러그인 추가시 conda_py311 사용"""
        # pyseq = env["REZ_PYSEQ"] # Conda py311
        # conda_py311 = env["CONDA_PY311"]  # "/home/rapa/anaconda3/envs/py311/lib/python3.11/site-packages"

        # if not conda_py311:
        #     raise ValueError("PYTHONPATH 환경변수를 찾을 수 없습니다.")

        # sys.path.append(conda_py311)

        # os.environ["CONDA_PY311"] = conda_py311
