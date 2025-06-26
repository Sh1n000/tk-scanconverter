# from dataclasses import dataclass
# # from typing import Optional

# import sys

# import rez

# from rez.resolved_context import ResolvedContext


# @dataclass
# class SysPathAppender:
#     """ShotGrid Toolkit에서 사용하는 경로 설정"""

#     rez_site_pkg: str
#     nuke_plugin_path: str
#     rez_pkg_list: list

#     # def __post_init__(self):
#     #     """초기화 후 경로 추가"""
#     #     self.append_rez_pkgs()
#     #     self.append_nuke_plugin_path()
#     #     self.activate_rez_env(self.rez_pkg_list)

#     def append_rez_pkgs(self):
#         """Python import 경로에 Rez 패키지 경로 추가"""
#         sys.path.append(self.rez_pkg)
#         print(f"Adding Rez package path: {self.rez_pkg}")

#     def append_nuke_plugin_path(self):
#         """Nuke 플러그인 경로를 Nuke와 Python 경로에 추가"""
#         import nuke

#         print("append ############ impport nuke")
#         nuke.pluginAppendPath(self.nuke_plugin_path, addToSysPath=True)
#         print(f"Adding Nuke plugin path: {self.nuke_plugin_path}")

#     def activate_rez_env(self, rez_pkg_list) -> None:
#         """Rez 환경 활성화"""
#         print("activate_rez_env     rez_pkg_list:", rez_pkg_list)
#         rez_context = ResolvedContext(rez_pkg_list)
#         env = rez_context.get_environ()

#         nuke_path = env["NUKE_PATH"]

#         if nuke_path:
#             raise ValueError("Nuke 못찾음")

#         sys.path.append(nuke_path)

#         rez_context.apply()
