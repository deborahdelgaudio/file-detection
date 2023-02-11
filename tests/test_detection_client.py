from typing import Mapping

import pytest

from detection_client import VTDetectionClient


@pytest.fixture
def test_client():
    client = VTDetectionClient(api_key="test-apikey-123")
    return client


@pytest.fixture
def mocked_response():
    class Mocked:
        last_analysis_stats = {
            "harmless": 0,
            "type-unsupported": 5,
            "malicious": 44,
            "undetected": 26,
        }

    return Mocked


def test_set_client(test_client):
    test_client.set_client()
    assert hasattr(test_client, "vtclient")


def test_get_file_analysis(test_client, mocker, mocked_response):
    test_client.set_client()
    mocker.patch("detection_client.vt.Client.get_object", return_value=mocked_response)
    response = test_client.get_file_analysis(file_hash="test-1234")
    assert isinstance(response, Mapping)
