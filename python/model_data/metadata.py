from dataclasses import dataclass, field


@dataclass
class MetaData:
    key: str
    type: str
    value: any


# @dataclass
# class UI_Header:
#     check : bool
#     thumbnail : str # 썸네일 경로
#     seq_name : str
#     shot_name : str
#     version : int
#     type : str
#     scan_path : str
#     resolution : str
