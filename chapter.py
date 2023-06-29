from os import path


class Chapter:
    def __init__(self, id: int, isFirst: bool, isLast: bool) -> None:
        self.id: int = id
        self.isFirst: bool = isFirst
        self.isLast: bool = isLast
        self.name: str = f"chapter{self.id}"

        appPath = path.dirname(path.abspath(__file__))
        resPath: str = f"{appPath}/resources/chapters/chapter{id}.txt"
        content: list[str] = []
        with open(resPath, "r") as f:
            content = [l.strip("\n") for l in f.readlines()]

        self.title: str = content.pop(0)
        self.codeSource: str = f"chapter{self.id}.py"
        self.hasCode: bool = path.exists(f"{appPath}/static/chaptersCode/{self.codeSource}")

        if self.hasCode:
            with open(f"{appPath}/static/chaptersCode/{self.codeSource}", "r") as src:
                self.defaultCode = src.read()
        else:
            self.defaultCode = ""

        self.bodyContent: list[str] = []
        self.endContent: list[str] = []

        isBody: bool = True
        for l in content:
            if l == "END":
                isBody = False
            elif isBody:
                self.bodyContent.append(l)
            else:
                self.endContent.append(l)


