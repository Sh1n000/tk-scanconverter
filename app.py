import sgtk
import os
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
        # append rez packages
        self.set_rez(["nuke", "conda"])

        # Loading
        tk_scanconverter_app = self.import_module("tk_scanconverter")
        menu_callback = lambda: tk_scanconverter_app.dialog.show_dialog(self)
        self.engine.register_command("Scan Converter", menu_callback)

    def set_rez(self, rez_pkgs):
        # 사용할 Rez 패키지 리스트
        # ResolvedContext 인스턴스 생성 및 적용
        rez_ctx = ResolvedContext(rez_pkgs)
        rez_ctx.apply()

        # Rez 환경 변수 가져오기
        env = rez_ctx.get_environ()
        # print(f"Using Rez environment: {env}")

        nuke_path = env["NUKE_PATH"]
        print(f"NUKE_PATH: {nuke_path}")
        conda_path = env["REZ_CONDA_ROOT"]
        print(f"REZ_CONDA_ROOT: {conda_path}")

        n_py_path = env["NUKE_PYTHON_PATH"]
        print(f"NUKE_PYTHON_PATH: {n_py_path}")
        c_py_path = env["CONDA_PYTHON_PATH"]
        print(f"CONDA_PYTHON_PATH: {c_py_path}")

        if not nuke_path:
            raise ValueError("NUKE_PATH 환경변수를 찾을 수 없습니다.")

        if not conda_path:
            raise ValueError("REZ_CONDA_ROOT 환경변수를 찾을 수 없습니다.")

        if not n_py_path:
            raise ValueError("NUKE_PYTHON_PATH 환경변수를 찾을 수 없습니다.")

        if not c_py_path:
            raise ValueError("CONDA_PYTHON_PATH 환경변수를 찾을 수 없습니다.")

        # 환경 변수 설정
        os.environ["NUKE"] = nuke_path
        os.environ["CONDA"] = conda_path
