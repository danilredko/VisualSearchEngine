import json


class Config:
    """
    A class to represent Conf object

    """
    def __init__(self):
        """
        Read config.json file with all needed attributes for the project
        """
        with open("config.json") as f:
            self.config = json.load(f)
