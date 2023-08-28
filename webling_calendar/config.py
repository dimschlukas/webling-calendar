import os
from typing import Optional
from dotenv import load_dotenv, set_key


class Config:
    webling_api_key: Optional[str] = None
    webling_endpoint_url: Optional[str] = None

    def __init__(self, config_file_path=None):
        self.config_file_path = config_file_path
        if self.config_file_path is None:
            self.config_file_path = os.path.join(
                os.path.expanduser("~"), ".config", "webling-calendar", ".env"
            )

        if not os.path.isfile(self.config_file_path):
            print("config does not exist")
            print("creating config files now")
            self.create_config_file()
            self.set_api_key("")
            self.set_enpoint_url("")

        self.load_config()

    def load_config(self):
        load_dotenv(self.config_file_path, override=True)
        self.webling_api_key = os.getenv("WEBLING_API_KEY")
        self.webling_endpoint_url = os.getenv("WEBLING_ENDPOINT_URL")

    def set_api_key(self, newKey):
        self.webling_api_key = newKey
        set_key(self.config_file_path, "WEBLING_API_KEY", newKey)
        self.load_config()

    def set_enpoint_url(self, newUrl):
        self.webling_endpoint_url = newUrl
        set_key(self.config_file_path, "WEBLING_ENDPOINT_URL", newUrl)
        self.load_config()

    def create_config_file(self):
        config_folder_path = os.path.dirname(self.config_file_path)
        if not os.path.exists(config_folder_path):
            os.makedirs(os.path.dirname(self.config_file_path))
        open(self.config_file_path, "x").close()

    def check_configuration(self):
        missing = []
        if self.webling_api_key is None or self.webling_api_key == "":
            missing.append("WEBLING_API_KEY")

        if (
            self.webling_endpoint_url is None
            or self.webling_endpoint_url == ""
        ):
            missing.append("WEBLING_ENDPOINT_URL")

        if len(missing) > 0:
            raise Exception(
                f"{', '.join(missing)} is not set in configuration."
            )
