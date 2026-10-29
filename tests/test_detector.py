from src.detector import *
from src.loader import load_logins
import pytest

def test_is_suspicious():
    assert is_suspicious(5,3) is True

def test_is_not_suspicious():
    assert is_suspicious(2,3) is False

def test_is_suspicious_on_limit():
    assert is_suspicious(3,3) is True


def test_find_suspicious_ips():
    failed_counts = {
        "192.168.1.10": 5,
        "192.168.1.20": 1,
        "192.168.1.30": 4
    }
    assert find_suspicious_ips(failed_counts) == ["192.168.1.10", "192.168.1.30"]

def test_find_no_suspicious_ips():
    failed_counts = {
            "192.168.1.10": 2,
            "192.168.1.20": 2,
            "192.168.1.30": 2
        }
    assert find_suspicious_ips(failed_counts) == []

def test_find_suspicious_ips_custom_limit():
    failed_counts = {
                "192.168.1.10": 5,
                "192.168.1.20": 3,
                "192.168.1.30": 7
            }
    assert find_suspicious_ips(failed_counts, 4) == ["192.168.1.10", "192.168.1.30"]

def test_detect_suspicious_logins():
    logins_list = [
        {"ip":"192.168.1.10", "status" : "Failed"},
        {"ip":"192.168.1.10", "status" : "Failed"},
        {"ip":"192.168.1.10", "status" : "Failed"},
        {"ip":"192.168.1.10", "status" : "Success"},
        {"ip":"192.168.1.10", "status" : "Success"},
        {"ip":"192.168.1.10", "status" : "Success"},
        {"ip":"192.168.1.10", "status" : "Success"},
        {"ip":"192.168.1.20", "status" : "Failed"},
        {"ip":"192.168.1.20", "status" : "Success"},
        {"ip":"192.168.1.20", "status" : "Success"},
        {"ip":"192.168.1.20", "status" : "Success"},
        {"ip":"192.168.1.30", "status" : "Failed"},
        {"ip":"192.168.1.30", "status" : "Failed"},
        {"ip":"192.168.1.30", "status" : "Success"},
        {"ip":"192.168.1.30", "status" : "Success"},
        {"ip":"192.168.1.30", "status" : "Success"},
        {"ip":"192.168.1.30", "status" : "Success"}
    ]

    assert detect_suspicious_logins(logins_list) == ["192.168.1.10"]


def test_detect_suspicious_logins_missing_status():
    logins_list = [
    {"ip": "192.168.1.10"}
    ]
    with pytest.raises(KeyError):
        detect_suspicious_logins(logins_list)