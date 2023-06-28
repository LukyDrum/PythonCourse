from os import path


class Challenge:
    def __init__(self, id: int) -> None:
        self.id: int = id

        appPath = path.dirname(path.abspath(__file__))
        resPath: str = f"{appPath}/resources/challenges/challenge{id}.txt"
        content: list[str] = []
        with open(resPath, "r") as f:
            content = [l.strip("\n") for l in f.readlines()]

        self.title: str = content.pop(0)
        self.answer: int = int(content.pop(0))

        self.codeSource: str = f"challenge{self.id}.py"
        self.hasCode: bool = path.exists(f"{appPath}/static/{self.codeSource}")

        self.bodyContent: list[str] = []

        for l in content:
                self.bodyContent.append(l)

