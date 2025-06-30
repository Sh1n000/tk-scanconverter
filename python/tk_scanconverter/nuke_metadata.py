import nuke
import os

selected_dir = "/home/rapa/share_storage/show/castle/product/scan/20241226_2/001_C014C018_230920_RO8N"

selected_f = os.listdir(selected_dir)
print(selected_dir)


for image in selected_f:
    read_node = nuke.createNode("Read")
    write_node = nuke.createNode("Write")
    read_node["file"].setValue(f"{selected_dir}/{image}")


def read_node_from_path(path, first_frame=None, last_frame=None):
    """
    param path: 파일 경로 (EXR 시퀀스 혹은 MOV 파일)
    return: Nuke Read Node
    """
    # 확장자 검사
    ext = os.path.splitext(path)[1].lower()
    if ext not in (".exr", ".mov"):
        raise ValueError("Check Filr Path : Scan Path ext는 .exr, .mov 이어야 합니다.")

    if ext == ".mov":
        # MOV 파일의 경우 PySceneDetect를 사용하여 씬을 분리하고 메타데이터를 추출

        # Nuke Read Node 생성
        read_node = nuke.nodes.Read(file=path)
        pass

    elif ext == ".exr":
        read_node = nuke.nodes.Read()
        read_node["file"].setValue(path)
        read_node["first"].setValue(first_frame)
        read_node["last"].setValue(last_frame)
        return read_node


def extract_metadata(read_node, frame=None):
    """
    param read_node: Nuke Read Node
    return: 메타데이터 딕셔너리
    """

    if not isinstance(read_node, nuke.ReadNode):
        raise TypeError("Check Read Node")

    meta = nuke.metadata(read_node)
    return meta


def print_metadata(meta):
    print("=== Metadata ===")
    for k, v in meta.items():
        print(f"{k}: {v}")


def main():
    if len(sys.argv) < 2:
        print("Usage: nuke -ix script.py <input_path>")
        sys.exit(1)

    path = sys.argv[1]

    # EXR 시퀀스 파싱
    start_frame, end_frame = parse_exr_sequence(path)
    print(f"Start Frame: {start_frame}, End Frame: {end_frame}")

    # Nuke Read Node 생성
    read_node = read_node_from_path(
        exr_sequence_path, first_frame=start_frame, last_frame=end_frame
    )

    # 메타데이터 추출
    metadata = extract_metadata(read_node)

    # 메타데이터 출력
    print_metadata(metadata)


if __name__ == "__main__":
    main()
