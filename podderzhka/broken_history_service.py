class BrokenHistoryService:
    def __init__(self):
        self._history = []

    def save_record(self, operation: str, result: int) -> None:
        raise Exception("Database error")

    def get_history(self) -> list:
        return self._history.copy()