import abc
from typing import Mapping

import vt


class DetectionClient(metaclass=abc.ABCMeta):
    def set_client(self) -> None:
        raise NotImplementedError

    def get_file_analysis(self, file_hash: str) -> Mapping:
        raise NotImplementedError


class VTDetectionClient(DetectionClient):
    def __init__(self, api_key):
        self.api_key = api_key

    def set_client(self):
        self.vtclient = vt.Client(self.api_key)

    def get_file_analysis(self, file_hash: str) -> Mapping:
        file = self.vtclient.get_object(f"/files/{file_hash}")
        stats = file.last_analysis_stats
        return {"file_hash": file_hash, "last_analysis_stats": stats}
