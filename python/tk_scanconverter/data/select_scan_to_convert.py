# from dataclasses import dataclass
# from pathlib import Path
# from collections import defaultdict
# from typing import List, Dict, Any
# from typing import Optional

# # 외장 module
# import pyseq
# from pyseq import Sequence


# @dataclass
# class FileManager:
#     """
#     선택된 Scan 파일 관리 Class
#     1. EXR시퀀스 인지, Mov인지 확인 후
#     2. Output Path 경로 생성
#     """

#     selected_p: Path  # 선택된 Scan Path
#     output_d_list: Path
#     file_dict: dict

#     def __post_init__(self):
#         self.org_dir = self.selected_p / "org"
#         self.jpg_dir = self.selected_p / "jpg"
#         self.montage_dir = self.selected_p / "montage"
#         # self.meta_dir = self.selected_p / "metadata"

#         output_d_list = [self.org_dir, self.jpg_dir, self.montage_dir]

#         """경로 생성"""
#         for d in output_d_list:
#             if not d.exists():
#                 d.mkdir(parents=True, exist_ok=True)
#                 print(f"FileManager Create Dir: {d}")

#         self.output_d_list = output_d_list

#         self.file_dict: Dict[str, List[Path]] = defaultdict(list)
#         self.collect_by_extension()

#     def collect_by_extension(self) -> Dict[str, List[Path]]:
#         """확장자별로 파일을 수집"""
#         self.file_dict.clear()
#         for f in self.path.iterdir():
#             if f.is_file():
#                 self.file_dict[f.suffix.lower()].append(f)
#         return dict(self.file_dict)

#     def is_exr_sequence(self) -> bool:
#         """폴더 내 EXR 시퀀스 존재 여부 판별"""
#         return len(self.get_exr_sequences()) > 0

#     def is_mov(self) -> bool:
#         """폴더 내 MOV 파일 존재 여부 판별"""
#         return bool(self.file_dict.get(".mov"))

#     def get_exr_sequences(self) -> List[Sequence]:
#         """EXR 파일 중 Sequence 객체로 인식된 것만 필터링"""

#         exr_files = self.file_dict.get(".exr", [])
#         if not exr_files:
#             return []

#         raw = pyseq.get_sequences([str(f) for f in exr_files])
#         # pyseq.get_sequences 결과에 문자열이 섞일 수 있음
#         seqs: List[Sequence] = [s for s in raw if isinstance(s, Sequence)]
#         return seqs

#     # def get_exr_paths(self, seq_name: str) -> list[Path]:
#     #     """시퀀스 이름으로 EXR 파일 리스트 반환"""
#     #     seq_dir = self.scan_root / seq_name
#     #     return sorted(seq_dir.glob("*.exr"))
