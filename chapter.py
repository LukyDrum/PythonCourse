from os import getcwd


class Chapter:
    def __init__(self, id: int, isFirst: bool, isLast: bool) -> None:
        self.id: int = id
        self.isFirst: bool = isFirst
        self.isLast: bool = isLast

        appPath = getcwd()
        path: str = f"{appPath}/resources/chapters/chapter{id}.txt"
        content: list[str] = []
        with open(path, "r") as f:
            content = [l.strip("\n") for l in f.readlines()]

        self.title: str = content.pop(0)
        self.trinket: str = content.pop(0)

        self.hasTrinket: bool = (self.trinket != "X")

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


