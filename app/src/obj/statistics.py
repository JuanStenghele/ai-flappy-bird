class Statistics:
    def __init__(self) -> None:
        self.score = 0

    def increase_score(self) -> None:
        self.score += 1

    def get_score(self) -> int:
        return self.score

    def reset(self) -> None:
        self.score = 0