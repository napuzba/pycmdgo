import logging
from typing import List


from .settings import Settings


class App:
    def __init__(self):
        self.settings : Settings = Settings()

    def loadSettings(self, args: List[str] = None):
        self.settings.parse(args)
        self.initLogging()

    def initLogging(self):
        logging.basicConfig(format='%(asctime)s %(message)s')
        logging.root.setLevel(logging.INFO)

    def run(self):
        logging.info("param1 : {}".format(self.settings.param1))
        logging.info("param2 : {}".format(self.settings.param2))
