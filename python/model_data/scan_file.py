from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, Union


@dataclass
class ScanFile:
    file_name: str
    dir_path: str
    file_type: str  # exr_seq, mov


@dataclass
class ExrSequenceInfo:
    file_name: str
    dir_path: str
    start_frame: int
    end_frame: int
    frame_count: int
    meta_data: dict


@dataclass
class MovInfo:
    """Mov 1개내에서 여러개의 Shot이 존재"""

    scene_count: int
    scene_duration_list: list  # [1001-1200, 1201-1350, start-end, ...]
    meta_data: dict
