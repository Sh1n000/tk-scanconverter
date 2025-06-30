import sys
import argparse

from typing import List, Dict, Any


import pyseq
from pyseq import Sequence


class FileManager:
    """
    Controller : model_data의 scan_file을 받아 Return
    """

    def __init__(self, data):
        self.data = data

        self.dir = self.data["selected_dir"]
        self.ext = self.data["ext"]
        self.file_list = self.data["file_list"]

    def get_exr_sequences(self) -> List[Sequence]:
        """EXR 파일 중 Sequence 객체로 인식된 것만 필터링"""
        exr_files = self.file_list
        if not exr_files:
            return []

        raw = pyseq.get_sequences([str(f) for f in exr_files])
        # pyseq.get_sequences 결과에 문자열이 섞일 수 있음
        seqs: List[Sequence] = [s for s in raw if isinstance(s, Sequence)]
        return seqs

    def setting_data_sequences(self):
        seqs = self.get_exr_sequences()
        for seq in seqs:
            seq_info = {
                "pattern": seq.format(),
                "start_frame": seq.start(),
                "end_frame": seq.end(),
                "frame_count": len(seq),
            }
        return seq_info


if __name__ == "__main__":
    data = sys.argv
    print(type(data))
    # <class 'list'>

    fm = FileManager(data)

    # if fm.ext == "exr":
    #     print("exr seq")
    #     seq_info = fm.setting_data_sequences()
    #     print(seq_info)

    # elif fm.ext == "mov":
    #     print("mov")

    # else:
    #     print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
