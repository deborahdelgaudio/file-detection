import os

from src.json_adapter import read_input, write_output


def test_write_output(tmp_path):
    test_file_path = tmp_path / "output.json"
    data = {"file_hash": "test123", "last_analysis_stats": {}}
    write_output(test_file_path, data)
    assert os.path.exists(test_file_path)


def test_read_input(tmp_path):
    test_file_path = tmp_path / "input.json"
    content = b'{"hashes": ["test123"]}'
    test_file_path.write_bytes(content)
    data = read_input(test_file_path)
    assert isinstance(data, dict)
