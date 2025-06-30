from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import List, Dict, Any
from pathlib import Path

# from ..model_data import select_file


@dataclass
class ScanFile:
    selected_dir: str
    ext: str  # exr, mov
    file_list: List[Path]


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
