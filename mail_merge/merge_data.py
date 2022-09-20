class MergeData:

    path: str
    data: list[str]

    def __init__(self, path: str) -> None:
        self.path = path
        self._load()

    def _load(self) -> None:
        with open(self.path) as file:
            self.data = file.read().split("\n")
