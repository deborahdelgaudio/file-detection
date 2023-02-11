import json
from typing import Mapping


def write_output(file_path: str, data: Mapping):
    with open(file_path, "w") as f:
        json.dump(data, f)


def read_input(file_path: str) -> Mapping:
    with open(file_path, "r") as f:
        data = json.load(f)
    return data
