from dataclasses import dataclass
from typing import Optional, Union


@dataclass
class NukeReadNode:
    """Nuke Read Node 정보"""

    file_path: str
    first_frame: int
    last_frame: int
    frame_count: int
    file_type: str  # exr_seq, mov


@dataclass
class NukeWriteNode:
    """Nuke Write Node 정보"""

    output_path: str
