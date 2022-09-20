class Template:

    path: str
    data: str

    def __init__(self, path: str) -> None:
        self.path = path
        self._load()

    def _load(self) -> None:
        """Loads the template file into memory"""
        with open(self.path) as file:
            self.data = file.read()

    def merge(self, token: str, value: str) -> str:
        return self.data.replace(token, value)
