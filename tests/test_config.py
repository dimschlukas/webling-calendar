from webling_calendar.config import Config
import pytest
import os


def test_config_file_creation(tmp_path):
    file_path = os.path.join(tmp_path, "testdir/.testenv")
    assert os.path.isfile(file_path) == False
    Config(file_path)
    assert os.path.isfile(file_path) == True


def test_load_config(tmp_path):
    file_path = os.path.join(tmp_path, "testdir/.testenv")
    c = Config(file_path)
    assert c.webling_api_key == ""
    assert c.webling_endpoint_url == ""


def test_set_enpoint_url(tmp_path):
    file_path = os.path.join(tmp_path, "testdir/.testenv")
    c = Config(file_path)
    c.set_enpoint_url("https://testwebsite.com")
    assert c.webling_endpoint_url == "https://testwebsite.com"
    assert os.getenv("WEBLING_ENDPOINT_URL") == "https://testwebsite.com"


def test_set_api_key(tmp_path):
    file_path = os.path.join(tmp_path, "testdir/.testenv")
    c = Config(file_path)
    c.set_api_key("testAPIkey")
    assert c.webling_api_key == "testAPIkey"
    assert os.getenv("WEBLING_API_KEY") == "testAPIkey"


def test_check_config_empty(tmp_path):
    file_path = os.path.join(tmp_path, "testdir/.testenv")
    c = Config(file_path)

    with pytest.raises(
        Exception,
        match="WEBLING_API_KEY, WEBLING_ENDPOINT_URL is not set in configuration.",
    ) as e_info:
        c.check_configuration()
