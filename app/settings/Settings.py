import argparse
from typing import List

class Settings:
    def __init__(self):
        pass


    def parse(self, args: List[str]):
        args = self._createParser().parse_args(args)
        self.param1 : str = args.param_1
        self.param2 : int = args.param_2

    def _createParser(self) -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(description='')
        parser.add_argument('--param-1' , type=str , default="a")
        parser.add_argument('--param-2' , type=int,  default=5)

        return parser
